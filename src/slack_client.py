import os
import logging
from slack_sdk import WebClient
from slack_message import SlackMessage


logging.basicConfig(level=logging.ERROR)

class SlackClient:
    def __init__(self, token=os.environ['SLACK_TOKEN']) -> None:
        self.client = WebClient(token=token)

    def post_msg(self, channel: str, msg: SlackMessage) -> None:
        self.client.chat_postMessage(
            channel=channel,
            text=msg.text,
            blocks=msg.blocks
        )
