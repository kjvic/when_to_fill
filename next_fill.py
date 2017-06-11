#!/usr/bin/env python

"""
Command line utility to compute when to fill a medication.
Will compute multiple future dates at a user's option.
"""

from datetime import datetime
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
    # timedelta specifies a number of days when passed an int
    _days_per_rx = int(input("\tEvery ___ days: "))
    if _days_per_rx <= 0:
        raise InputError(
            "Cannot fill every ", _days_per_rx,
            "Fill frequency must be a positive number of days")
    print()
    return timedelta(_days_per_rx)

def loop_template_method(gen, customization_fn=lambda *args: None):
    next_fill_date = next(gen)
    print("Next fill date: on/after ", next_fill_date)
    customization_fn()
    should_quit = input()
    if should_quit == "q":
        print("Quitting...")
        return False
    return True

def get_first_time_fn(days_per_rx, last_fill_date):
    now = datetime.now().date()
    def _first_time_fn():
        num_pills_left = get_num_pills_left(
            days_per_rx, last_fill_date, now)
        print("You should have ",
              num_pills_left,
              "pills left (NOT counting today's dose)"
              "\n\n"
              "To quit, type q"
              "\n"
              "To calculate the next fill date, press RETURN")
    return _first_time_fn

def get_num_pills_left(days_per_rx, last_fill_date, now):
    delta = now - last_fill_date
    days_used_up = delta.days
    return days_per_rx.days - days_used_up

def main():
    last_fill_date = read_last_fill_date()
    days_per_rx = read_days_per_rx()
    gen = next_fill_generator(last_fill_date, days_per_rx)
    first_time_fn = get_first_time_fn(days_per_rx, last_fill_date)
    if not loop_template_method(gen, first_time_fn):
        return
    while loop_template_method(gen):
        pass

if __name__ == "__main__":
    main()
