import os

from dotenv import load_dotenv


class TwitterComplaintBot:
    """
    A class representing a Twitter bot that complains to the user's ISP on
    Twitter if the user's current internet speed doesn't match at least the
    internet speed guaranteed by the ISP.
    """

    def __init__(
            self,
            promised_down,
            promised_up,
            driver_path,
            twitter_email,
            twitter_password
    ):
        """Initialize browser driver."""


if __name__ == '__main__':
    load_dotenv()

    TWITTER_EMAIL = os.getenv('EMAIL')
    TWITTER_PASSWORD = os.getenv('PASSWORD')

    tcp = TwitterComplaintBot
    
    