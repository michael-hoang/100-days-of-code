import gspread
from oauth2client.service_account import ServiceAccountCredentials


class FlightClub:
    """Manages FlightClub admission."""

    def __init__(self):
        """Initialize first name, last name, and email to be processed for admission."""
        self.registration = False
        self.firstName = ''
        self.lastName = ''
        self.email = ''

    def signUp(self):
        """Obtain information for signup."""
        self.registration = True
        print('Welcome to Michael\'s Flight Club.\nWe find the best deals and email you.')
        self.firstName = input('What is your first name?\n')
        self.lastName = input('What is your last name?\n')

        emailValidation = False
        while not emailValidation:
            self.email = input('What is your email?\n')
            if self.email == 'q':
                self.registration = False
                break

            emailConfirm = input('Type your email again.\n')
            if emailConfirm == 'q':
                self.registration = False
                break

            if self.email == emailConfirm:
                print('You\'re in the club!')
                emailValidation = True
            else:
                print('Email did not match. Please try again.\n(To exit, enter \'q\')')

    def updateGoogleSheet(self):
        """Record member registration information into Google Sheet."""
        if self.registration == True:
            scope = ["https://spreadsheets.google.com/feeds", 'https://www.googleapis.com/auth/spreadsheets',
                     "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]

            creds = ServiceAccountCredentials.from_json_keyfile_name(
                filename='../Part 1 - Flight Deal Finder/cred/google_spreadsheet_key.json', scopes=scope)
            client = gspread.authorize(creds)
            userSheet = client.open('Flight Deals').worksheet('users')
            userSheetData = userSheet.get_all_records()
            numUsers = len(userSheetData)
            numFilledRows = numUsers + 1  # add 1 for the header row
            userSheet.update(f'A{numFilledRows + 1}', self.firstName.title())
            userSheet.update(f'B{numFilledRows + 1}', self.lastName.title())
            userSheet.update(f'C{numFilledRows + 1}', self.email)
            self.registration = False


if __name__ == '__main__':
    fc = FlightClub()
    fc.signUp()
    fc.updateGoogleSheet()
