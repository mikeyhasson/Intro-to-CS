# FILE : temperature.py
# WRITER : Michael Hasson , mikey641 , 322893892
# EXERCISE : intro2cs2 ex2 2020
# DESCRIPTION: A simple program that checks if the temperature is high enough. if within 3 continuous days, in at least
# 2 days the temperature was higher than a chosen temperature, program will return True.
#################################################################
def is_it_summer_yet (max_temperature,temperature_day1,temperature_day2,temperature_day3):
    """this function checks if the temperature is higher than a given temperature in at least 2 of 3 days"""
    hot_days_count=0
    if temperature_day1> max_temperature:
        hot_days_count += 1
    if temperature_day2> max_temperature:
        hot_days_count += 1
    if temperature_day3> max_temperature:
        hot_days_count += 1
    if hot_days_count >= 2:
        return True
    else:
        return False

