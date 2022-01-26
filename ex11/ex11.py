#################################################################
# FILE : ex11.py
# WRITER : Michael Hasson , mikey641 , 322893892
# EXERCISE : intro2cs2 ex11 2020
# DESCRIPTION: Classes and function for Diagnosing records
#################################################################
from collections import Counter
from itertools import combinations


class Node:
    """
    Class meant to represent Nodes
    """

    def __init__(self, data, positive_child=None, negative_child=None):
        """
        Constructor for a Node object
        :param data:
        :param positive_child:
        :param negative_child:
        """
        self.data = data
        self.positive_child = positive_child
        self.negative_child = negative_child

    def get_data(self):
        """
        :return: Node's data
        """
        return self.data

    def set_data(self, val):
        """
        :param val: New value for Node's data
        """
        self.data = val

    def get_positive_child(self):
        """
        :return: Node's positive_child
        """
        return self.positive_child

    def get_negative_child(self):
        """
        :return: Node's negative_child
        """
        return self.negative_child


class Record:
    """
    Class meant to represent a (medical) Record object,
    """

    def __init__(self, illness, symptoms):
        """
        Constructor for a Record object
        :param illness: illness name
        :param symptoms: list of symptoms of the illness
        """
        self.illness = illness
        self.symptoms = symptoms

    def get_illness(self):
        """
        :return: illness name
        """
        return self.illness

    def get_symptoms(self):
        """
        :return: list object of symptoms
        """
        return self.symptoms


def parse_data(filepath):
    """
    This function creates a list of Record objects from a file
    :param filepath: filepath of a file with data of the records
    :return:
    """
    with open(filepath) as data_file:
        records = []
        for line in data_file:
            words = line.strip().split()
            records.append(Record(words[0], words[1:]))
        return records


class Diagnoser:
    """
    This class represents Diagnoser objects, represented as binary trees
    """

    def __init__(self, root):
        """
        Constructor for a Diagnoser object
        :param root: root of the tree.
        """
        self.root = root

    def get_root(self):
        """
        :return: root of the tree
        """
        return self.root

    def diagnose(self, symptoms):
        """
        This function recieves a list of symptoms and returns an illness diagnosis
        :param symptoms: list object of symptoms
        :return:illness diagnosis (string)
        """
        return self.diagnose_node(symptoms).get_data()

    def diagnose_node(self, symptoms):
        """
        This function recieves a list of symptoms and returns an illness diagnosis
        :param symptoms: list object of symptoms
        :return:illness diagnosis (Node)
        """
        if self.root is None:
            return
        return self.diagnose_helper(symptoms, self.root)

    def diagnose_helper(self, symptoms, cur_question):
        """
        Recursive function that handles function diagnose
        :param symptoms: list object of symptoms
        :param cur_question: current question/Node of the tree we are checking
        :return:
        """
        positive = cur_question.get_positive_child()
        negative = cur_question.get_negative_child()
        if positive is None and negative is None:  # if we have reached a leaf, return it
            return cur_question

        if cur_question.get_data() in symptoms:
            return self.diagnose_helper(symptoms, positive)
        else:
            return self.diagnose_helper(symptoms, negative)

    def calculate_success_rate(self, records):
        """
        This function calculates the success rate of a Diagnosis object.
        :param records: list of Record objects
        :return: success rate
        """
        if len(records) == 0:
            return 0
        success = 0
        for record in records:
            illness = record.get_illness()
            symptoms = record.get_symptoms()
            if self.diagnose(symptoms) == illness:
                success += 1
        return success / len(records)

    def leaf_list(self, cur):
        """
        This recursive function returns the leaves of a diagnosis object
        :param cur: Root of the tree
        :return: List of the data's of the leaves' Nodes
        """
        negative = cur.get_negative_child()
        positive = cur.get_positive_child()
        if negative is None and positive is None:
            if cur.get_data() is not None:
              return [cur.get_data()]
        lst = []
        lst += self.leaf_list(negative)
        lst += self.leaf_list(positive)
        return lst

    def all_illnesses(self):
        """
        This function returns the list of possible illnesses of the Diagnosis object
        :return: list of illnesses, sorted by the number of appearences
        """
        full_illnesses_lst = self.leaf_list(self.root)  # list of leafs with duplicates
        if len(full_illnesses_lst) == 0:
            return []
        sorted_lst = Counter(full_illnesses_lst).most_common()  # removing duplicates and sorting by count
        sorted_lst = [i[0] for i in sorted_lst]
        return sorted_lst

    def paths_to_illness(self, illness):
        """
        This function recieves an illness string and returns a list of possible paths to it.
        :param illness: string illness
        :return: list of paths, each path is a list of boolean values
        """
        return self.paths_to_illness_helper(illness, self.root, [])

    def paths_to_illness_helper(self, illness, cur, lst):
        """
        This recursive function is used in function paths_to_illness. Uses backtracking.
        :param illness: illness to find paths to
        :param cur: current Node we're checking
        :param lst: lst of a possible path, by default it's empty, and is returned when the path reaches a leaf
        :return:
        """
        negative = cur.get_negative_child()
        positive = cur.get_positive_child()
        if negative is None and positive is None:  # if we reach a leaf
            if cur.get_data() == illness:  # if the leaf we've reached is the required illness, we return the path
                return [lst]
            else:
                return []
        path_lst = []  # to this list we will add all possible paths
        lst.append(False)  # trying the path with the next Node as the negative one
        path_lst += self.paths_to_illness_helper(illness, negative, lst[:])
        lst.pop()
        lst.append(True)  # trying the path with the next Node as the positive one
        path_lst += self.paths_to_illness_helper(illness, positive, lst[:])
        return path_lst


def build_tree(records, symptoms):
    """
    This function creates a Diagnosis tree out of a list of records and a list of symptoms
    :param records: list of Record object
    :param symptoms: list of symptoms (string)
    :return: Node of the root the new tree
    """
    tree_result_list = []
    root = create_symptom_nodes(symptoms, tree_result_list)  # creating a diagnosis tree with the leaves set as None
    tree = Diagnoser(root)  # creating a Diagnosis object out of the root
    # Creating an empty list of lists. To the i list we will add all the illneses from the records that match the
    # i leaf.
    tree_result_list_matches = [[] for i in range(len(tree_result_list))]
    for record in records:
        match = tree.diagnose_node(record.get_symptoms())  # matching tree leaf for record
        index = tree_result_list.index(match)  # index of the leaf in the list
        tree_result_list_matches[index].append(record.get_illness())  # adding the illness to the matches list
    # for each leaf, we will check the most common illness that matches it.
    for i in range(len(tree_result_list)):
        if len(tree_result_list_matches[i]) != 0:  # if no illness matches, the leaf will remain None
            sorted_lst = Counter(tree_result_list_matches[i]).most_common()  # sorting by count
            common_illness = sorted_lst[0][0]
            tree_result_list[i].set_data(common_illness)  # setting leaf as the common illness
    return root


def create_symptom_nodes(symptoms, leaf_list):
    """
    This function recieves a list of symptoms and a "leaf_list" and creates a diagnosis tree out of the symptoms.
    The leaves are set as None
    :param symptoms:a list of symptoms
    :param leaf_list:list to which we add the leaf Node object
    :return:root of the tree
    """
    if len(symptoms) == 0:
        illness = Node(None)
        leaf_list.append(illness)
        return illness
    new_symptoms_lst = symptoms[1:]
    new = Node(symptoms[0], create_symptom_nodes(new_symptoms_lst, leaf_list),
               create_symptom_nodes(new_symptoms_lst, leaf_list))
    return new


def optimal_tree(records, symptoms, depth):
    """
    This function creates the optimal diagnosis tree, with "depth" levels.
    :param records: list of Record objects
    :param symptoms: list of symptoms that might be included in the tree
    :param depth: depth of the tree/number of symptoms to include in the tree
    :return:root of the tree with the max success rate
    """
    if depth == 0:
        return build_tree(records, [])  # tree with a leaf as the root
    max = (None, -1)
    for symptom_group in combinations(symptoms, depth):  # trying out all the symptoms sublists in the size depth
        root = build_tree(records, symptom_group)
        tree = Diagnoser(root)
        success_rate = tree.calculate_success_rate(records)
        if success_rate > max[1]:
            max = (tree, success_rate)
    return max[0].get_root()



