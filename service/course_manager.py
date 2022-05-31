"""Course manager for get actual course USD."""
import os

from dotenv import load_dotenv

import requests


load_dotenv()


class CourseUSD:

    @staticmethod
    def get_course_usd():
        """The method get actual course USD."""
        response = requests.get(os.getenv('USD_COURSE_URL')).json()
        usd_course = response['Valute']['USD']['Value']
        print(usd_course)
        return int(usd_course)
