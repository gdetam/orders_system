"""Google sheets connector."""

import os

from dotenv import load_dotenv

import googleapiclient.discovery

import httplib2

from oauth2client.service_account import ServiceAccountCredentials


load_dotenv()

CREDENTIALS_FILE = os.getenv('CREDENTIALS_PATH')
SPREADSHEET_ID = os.getenv('SPREADSHEET_ID')

credentials = ServiceAccountCredentials.from_json_keyfile_name(
    CREDENTIALS_FILE,
    ['https://www.googleapis.com/auth/spreadsheets',
     'https://www.googleapis.com/auth/drive']
)
httpAuth = credentials.authorize(httplib2.Http())
service = googleapiclient.discovery.build('sheets', 'v4', http=httpAuth)
