import datetime as dt


def ask_for_year() -> str:
    """Recursively ask user for the year to time travel back to."""

    year = input(
        'Which year do you want to travel to? Type the date in this format YYYY-MM-DD:\n')

    # Date input validation
    date_format = '%Y-%m-%d'  # YYYY-MM-DD
    try:
        dateObject = dt.datetime.strptime(year, date_format)
        # print(dateObject)
        return year
    except ValueError:
        print('Incorrect date format. Should be YYYY-MM-DD')
        ask_for_year()


year = ask_for_year()
