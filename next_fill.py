#!/usr/bin/env python

"""
Command line utility to compute when to fill a medication.
Will compute multiple future dates at a user's option.
"""

from datetime import date
from datetime import timedelta

def next_fill_generator(last_fill_date, days_per_rx):
    """
    Computes the next day that a medication should be filled, given
    1. The last time that it was filled
    2. How often it should be filled
    """
    while True:
        yield last_fill_date + days_per_rx
        last_fill_date += days_per_rx

def read_last_fill_date():
    print("When was your last fill?")
    month = int(input("\tMonth (MM): "))
    day = int(input("\tDay (DD): "))
    year = int(input("\tYear (YYYY): "))
    return date(year, month, day)

def read_days_per_rx():
    print("\nHow often do you fill this med?")
    days_per_rx = timedelta(int(input("\tEvery ___ days: ")))
    print()
    return days_per_rx

def loop_template_method(gen, customization_fn=lambda *args: None):
    next_fill_date = next(gen)
    print("Next fill date: on/after ", next_fill_date)
    customization_fn()
    should_quit = input()
    if should_quit == "q":
        print("Quitting...")
        return False
    return True

def first_time_fn():
    print()
    print("To quit, type q")
    print("To calculate the next fill date, press any other key")

def main():
    last_fill_date = read_last_fill_date()
    days_per_rx = read_days_per_rx()
    gen = next_fill_generator(last_fill_date, days_per_rx)
    if not loop_template_method(gen, first_time_fn):
        return
    while loop_template_method(gen):
        pass

if __name__ == "__main__":
    main()
