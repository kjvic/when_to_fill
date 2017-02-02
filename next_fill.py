from datetime import date
from datetime import timedelta

"""
Command line utility to compute when to fill a medication.
Will compute multiple future dates at a user's option.
"""

def compute_next_fill(last_fill_date, days_per_rx):
    """
    Computes the next day that a medication should be filled, given
    1. The last time that it was filled
    2. How often it should be filled
    """
    return last_fill_date + days_per_rx


if __name__ == "__main__":
    print "When was your last fill?"
    month = int(raw_input("Month (MM): "))
    day = int(raw_input("Day (DD): "))
    year = int(raw_input("Year (YYYY): "))
    last_fill_date = date(year, month, day)

    print "\nHow often do you fill this med?"
    _days_per_rx = int(raw_input("Every ___ days: "))
    days_per_rx = timedelta(_days_per_rx)


    keep_going = True
    while keep_going:
        print "\nNext fill is on/after:",
        next_fill_date = compute_next_fill(last_fill_date, days_per_rx)
        print next_fill_date
        last_fill_date = next_fill_date

        print "\nTo calculate next fill date, just press RETURN"
        print "To quit, type q"
        should_quit = raw_input()
        if should_quit == "q":
            keep_going = False
