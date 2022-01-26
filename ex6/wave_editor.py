#################################################################
# FILE : wave_editor.py
# WRITER : Michael Hasson , mikey641 , 322893892
# EXERCISE : intro2cs2 ex6 2020
# DESCRIPTION: A wav file editor
#################################################################
import wave_helper
import math

CHANNEL_1 = 0
CHANNEL_2 = 1

REVERSE_SOUND_OPT="1"
NEGATIVE_OPT="2"
ACCELERATE_OPT="3"
SLOW_OPT="4"
INCREASE_VOL_OPT="5"
DECREASE_VOL_OPT="6"
LOW_PASS_OPT="7"
END_MENU_OPT="8"

FILE_ERROR_OUTPUT=-1

CHANGE_WAV_MENU_OPT="1"
COMPOSE_MUSIC_OPT="2"
EXIT_PROGRAM_OPT="3"

INCREASE_VOLUME_SCALAR=1.2 
DECREASE_VOLUME_SCALAR=1.2
    
MAX_VOLUME = 32767
MIN_VOLUME = -32768
DEF_SAMPLE_RATE = 2000
FREQUENCIES = {'A': 440, 'B': 494, 'C': 523, 'D': 587, 'E': 659, 'F': 698, 'G': 784, 'Q': 0}


def reverse_sound(audio_data):
    """
    this function takes a audio_data list and revereses it.
    :param audio_data: a list that contains lists of 2 int objects
    :return: new_lst - a new reversed list
    """
    new_lst = audio_data[:]  # no need to deep copy, we are just changing the indexes not the content.
    new_lst.reverse()
    print("audio data list was reversed")
    return new_lst


def multiply_audio_data_by_scalar(audio_data, scalar):
    """
    this function takes a audio_data list and multiplies it's objects by a scalar
    :param audio_data: a list that contains lists of 2 int objects
    :param scalar: the number to multiply by
    :return: new, multiplied list
    """
    new_lst = []
    index = 0
    for i in audio_data:
        new_lst.append([])
        for num in i:
            if num * scalar < MIN_VOLUME:
                add_val = MIN_VOLUME
            elif num * scalar > MAX_VOLUME:
                add_val = MAX_VOLUME
            else:
                add_val = int(num * scalar)
            new_lst[index].append(add_val)
        index += 1
    return new_lst


def turn_sound_negative(audio_data):
    """
    this function takes a audio_data list and turn it's objects negative
    :param audio_data: a list that contains lists of 2 int objects
    :return: new, negative list
    """
    print("audio data list was turned negative")
    return multiply_audio_data_by_scalar(audio_data, -1)


def accelerate_sound_speed(audio_data):
    """
    this function takes a audio_data list and removes all the objects with a non-even index.
    :param audio_data: a list that contains lists of 2 int objects
    :return: new, faster audio_data list
    """
    fast_lst = []
    index = 0
    for i in audio_data:
        if index % 2 == 0:
            fast_lst.append(i)
        index += 1
    print("audio data list was accelerated")
    return fast_lst

def slow_sound_speed(audio_data):
    """
    this function takes a audio_data list and between every 2 objects, adds a new object that is the mean value of
    these 2 values.
    :param audio_data: a list that contains lists of 2 int objects
    :return: new, slower-speed audio_data list
    """
    if audio_data==[]:
        return []
    slow_lst = []
    i = 0
    while i + 1 < len(audio_data):
        slow_lst.append(audio_data[i])
        additional_value = [int((audio_data[i][CHANNEL_1] + audio_data[i + 1][CHANNEL_1]) / 2),
                            int((audio_data[i][CHANNEL_2] + audio_data[i + 1][CHANNEL_2]) / 2)]
        slow_lst.append(additional_value)
        i += 1
    slow_lst.append(audio_data[i])
    print("audio data list was slowed")
    return slow_lst


def increase_volume(audio_data):
    """
    this function takes a audio_data list and multiplies it's objects by 1.2
    :param audio_data: a list that contains lists of 2 int objects
    :return: new, multiplied list
    """
    print("volume is increased")
    return multiply_audio_data_by_scalar(audio_data, INCREASE_VOLUME_SCALAR)


def decrease_volume(audio_data):
    """
    this function takes a audio_data list and divides it's objects by 1.2
    :param audio_data: a list that contains lists of 2 int objects
    :return: new, divided list
    """
    print("volume is decreased")
    return multiply_audio_data_by_scalar(audio_data, 1 / DECREASE_VOLUME_SCALAR)


def low_pass_filter(audio_data):
    """
    this function takes a audio_data list and replaces each value with the mean value of the
     previous value,the value, and the next value.
     the first value  is replaced with the mean value of itself and the next value.
     the last value  is replaced with the mean value of itself and the previous value.
    :param audio_data: a list that contains lists of 2 int objects
    :return: new, low passed
    """
    if audio_data==[]:
        return []
    new_lst = []
    i = 0
    new_lst.append([int((audio_data[i][CHANNEL_1] + audio_data[i + 1][CHANNEL_1]) / 2),
                    int((audio_data[i][CHANNEL_2] + audio_data[i + 1][CHANNEL_2]) / 2)])
    i += 1
    while i + 1 < len(audio_data):
        new_lst.append(
            [int((audio_data[i - 1][CHANNEL_1] + audio_data[i][CHANNEL_1] + audio_data[i + 1][CHANNEL_1]) / 3),
             int((audio_data[i - 1][CHANNEL_2] + audio_data[i][CHANNEL_2] + audio_data[i + 1][CHANNEL_2]) / 3)])
        i += 1
    new_lst.append([int((audio_data[i - 1][CHANNEL_1] + audio_data[i][CHANNEL_1]) / 2),
                    int((audio_data[i - 1][CHANNEL_2] + audio_data[i][CHANNEL_2]) / 2)])
    print("audio data list was low pass filtered")
    return new_lst

def single_sample(note, sample_rate, index):
    """
    This function recieves a note, the sample rate and the index within the full samples cycle, and returns the sample's
    value.
    :param note: A chosen musical note
    :param sample_rate: the sample rate of the composition
    :param index:index within the full samples cycle
    :return:one sample's value.
    """
    if note =="Q":
        return [0,0]
    frequency = FREQUENCIES.get(note)
    samples_per_cycle = sample_rate / frequency
    number = int(MAX_VOLUME * math.sin(math.pi * 2 * index / samples_per_cycle))
    return [number, number]

def single_note_samples(note, sample_rate, sixteenth_of_second):
    """
    This function recieves a note, the sample rate and the how long it is played in the form of sixteenth of second,
    and returns the full cycle of samples.
    :param note: A chosen musical note
    :param sample_rate: the sample rate of the composition
    :param sixteenth_of_second: how long the note is played in the form of sixteenth of second,
    :return:the whole sample of the note.
    """
    number_of_samples = int((sixteenth_of_second / 16) * sample_rate)
    samples_lst = []
    for i in range(number_of_samples):
        samples_lst.append(single_sample(note, sample_rate, i))
    return samples_lst


def compose_music(notes_file):
    """
    thsi function uses func single_note_samples to write a full audio data according to a file specifing the notes and
    times per note.
    :param notes_file: the note specifing the instructions of the musical composition
    :return: full audio data
    """
    f = open(notes_file, 'r')
    notes=f.read().split()
    i = 0
    music_lst = []
    while i + 2 <= len(notes):
        note = notes[i]
        sixteenth_of_second = int(notes[i + 1])
        music_lst += single_note_samples(note, DEF_SAMPLE_RATE, sixteenth_of_second)
        i += 2
    f.close()
    return music_lst

def change_wav_checks():
    """
    This function checks the values before inserted into func change_wav_menu.
    return: sample rate and audio data.
    """
    filename = input("Please insert filename")
    if wave_helper.load_wave(filename) == FILE_ERROR_OUTPUT:
        print("file is invalid or does not exist")
        change_wav_checks()
    else:
        sample_rate, audio_data = wave_helper.load_wave(filename)
        
    return  sample_rate, audio_data
 
def change_wav_menu(sample_rate=None, audio_data=None):
    """
    this function opens up a menu allowing users to edit an exisitng wav file, or a one created
    through func compose_music
    :param sample_rate: the sample rate, it is None by default. Used when directed by func compose_music or when we
    re-edit a file.
    :param audio_data: the audio data, it is None by default. Used when directed by func compose_music or when we
    re-edit a file.
    :return: None
    """
    if not sample_rate:
        sample_rate, audio_data=change_wav_checks()
    print("Choose one of the following options to edit your file:")
    edit_choice = input("1.reverse sound \n 2.turn sound negative\n 3.accelerate sound speed\n 4.slow sound speed\n "
                        "5.increase volume\n 6.decrease volume\n 7.low pass filter \n 8.go to end menu ")
    if edit_choice == REVERSE_SOUND_OPT:
        audio_data = reverse_sound(audio_data)
    elif edit_choice == NEGATIVE_OPT:
        audio_data = turn_sound_negative(audio_data)
    elif edit_choice == ACCELERATE_OPT:
        audio_data = accelerate_sound_speed(audio_data)
    elif edit_choice == SLOW_OPT:
        audio_data = slow_sound_speed(audio_data)
    elif edit_choice == INCREASE_VOL_OPT:
        audio_data = increase_volume(audio_data)
    elif edit_choice == DECREASE_VOL_OPT:
        audio_data = decrease_volume(audio_data)
    elif edit_choice == LOW_PASS_OPT:
        audio_data = low_pass_filter(audio_data)
    elif edit_choice == END_MENU_OPT:
        filename=input("choose a file name")
        end_menu(filename, sample_rate, audio_data)
        return None
    else:
        print ("incorrect number choice")
    change_wav_menu(sample_rate, audio_data)
    
def end_menu(filename, sample_rate, audio_data):
    """
    this function is the end menu. When users want to exit the code they are directed here where
    :param filename: file name for the new wav file.
    :param sample_rate: The sample rate of the wav file
    :param audio_data: The audio data (list containing 2 index lists) of the wav file.
    :return:None
    """
    a=wave_helper.save_wave(sample_rate, audio_data, filename)
    if a==0:
        print("file was saved")
        main()
    else:
        print("file saving error")

def main():
    """this is the main function directing users to the 2 main functions:change_wav_menu, and compose_music"""
    print("Hello! welcome to the wave file editor. Please choose one of the following options by typing its' number:")
    print("1. Change existing wave file")
    print("2. Composing music in a wave file format")
    print("3. Exit program")
    user_choice = input()
    if user_choice == CHANGE_WAV_MENU_OPT:
        change_wav_menu()
    elif user_choice == COMPOSE_MUSIC_OPT:
        composition_file = input("please insert the composition instructions filename")
        audio_data = compose_music(composition_file)
        change_wav_menu(DEF_SAMPLE_RATE, audio_data)
    elif user_choice == EXIT_PROGRAM_OPT:
        return None
    else:
        print ("incorrect number choice")
        main()


if __name__ == "__main__":
    main()