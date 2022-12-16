import gspread
from oauth2client.service_account import ServiceAccountCredentials
from pprint import pprint


class DataManager:
    """This class is responsible for talking to the Google Sheet."""

    def __init__(self):
        """Initializes destination data attribute."""
        self.SCOPE = ["https://spreadsheets.google.com/feeds", 'https://www.googleapis.com/auth/spreadsheets',
                      "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]
        self.CREDENTIAL = 'cred/google_spreadsheet_key.json'

        self.sheet = ''
        self.destination_data = {}
        self.memberEmails = []

        self._get_destination_data()
        self._get_member_emails()

    def _get_destination_data(self):
        """
        Retrieves data from Google Sheets containing various destinations and stores
        it in self.destination_data attribute.
        """
        creds = ServiceAccountCredentials.from_json_keyfile_name(
            filename=self.CREDENTIAL, scopes=self.SCOPE)
        client = gspread.authorize(creds)
        self.sheet = client.open('Flight Deals').sheet1
        self.destination_data = self.sheet.get_all_records()  # list of dictionaries

    def _get_member_emails(self):
        """Retrieve member emails from Google Sheets and store it in self.memberEmails."""
        creds = ServiceAccountCredentials.from_json_keyfile_name(
            filename=self.CREDENTIAL, scopes=self.SCOPE)
        client = gspread.authorize(creds)
        userSheet = client.open('Flight Deals').worksheet('users')
        self.memberEmails = userSheet.col_values(col=3)[1:]


if __name__ == '__main__':
    dm = DataManager()
    pprint(dm.destination_data)
    print(len(dm.destination_data))
    print(dm.memberEmails)
