from get_visa_wait_times_request import GetVisaWaitTimesRequest
from sequential_travel_client import SequentialTravelClient
from slack_client import SlackClient
from slack_message_builder import SlackMessageBuilder


class Bot:
    def __init__(self, travel_client: SequentialTravelClient, slack_msg_builder: SlackMessageBuilder, slack_client: SlackClient):
        self.travel_client = travel_client
        self.slack_msg_builder = slack_msg_builder
        self.slack_client = slack_client

    def notify_visa_wait_times(self, req: GetVisaWaitTimesRequest) -> None:
        wait_times = self.travel_client.get_visa_wait_times(req)

        msg = self.slack_msg_builder.build_get_visa_wait_times(wait_times)

        self.slack_client.post_msg(channel="usa-visa-interview", msg=msg)