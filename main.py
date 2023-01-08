import datetime as dt


def ask_for_year() -> str:
    """Ask user for the year to time travel back to."""

    year = input(
        'Which year do you want to travel to? Type the date in this format YYYY-MM-DD:\n')


year = ask_for_year()
