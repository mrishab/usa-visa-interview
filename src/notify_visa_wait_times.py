import os
import yaml
from bot import Bot
import get_visa_wait_times_request
from sequential_travel_client import SequentialTravelClient
from slack_client import SlackClient
from slack_message_builder import SlackMessageBuilder
from travel_client import TravelClient

class NotifyVisaWaitTimes:
    def __init__(self, file_name) -> None:
        self.file_name = file_name
        self.get_visa_wait_times_request = None
        self.bot = None

    def load(self):
        slack_token = os.environ['SLACK_TOKEN']
        with open(self.file_name, "r") as file:
            data = yaml.safe_load(file)
            self.get_visa_wait_times_request = get_visa_wait_times_request.from_dict(data)
        travel_client = SequentialTravelClient(travel_client=TravelClient())
        slack_msg_builder = SlackMessageBuilder()
        slack_client = SlackClient(token=slack_token)

        self.bot = Bot(travel_client=travel_client, slack_msg_builder=slack_msg_builder, slack_client=slack_client)


    def run(self):
        self.bot.notify_visa_wait_times(self.get_visa_wait_times_request)
