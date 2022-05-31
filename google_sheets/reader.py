"""Google sheets reader."""

from google_sheets.connector import SPREADSHEET_ID, service


class GoogleSheetsReader:

    @staticmethod
    def get_google_sheets_table():
        """Get information from Google sheets."""
        values = service.spreadsheets().values().get(
            spreadsheetId=SPREADSHEET_ID,
            range='A1:E51',
            majorDimension='ROWS'
        ).execute()
        return values['values'][1:]
