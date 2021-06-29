# meds calculator

This project helps you plan out prescription refills.

## Usage
Run `python3 next_fill.py`, and follow the interactive prompts.

## Example session
```
$ python3 next_fill.py
When was your last fill?
	Month (MM): 06
	Day (DD): 02
	Year (YYYY): 2021

How often do you fill this med?
	Every ___ days: 30

Next fill date: on/after  2021-07-02
You should have  3 days' supply left (NOT counting today's dose)

To quit, type q
To calculate the next fill date, press RETURN

Next fill date: on/after  2021-08-01

Next fill date: on/after  2021-08-31

Next fill date: on/after  2021-09-30
q
Quitting...
$
```