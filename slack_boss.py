import logging
import os
import csv

from dotenv import load_dotenv

# Import WebClient from Python SDK (github.com/slackapi/python-slack-sdk)
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError

# Load env variables
load_dotenv()

# WebClient instantiates a client that can call API methods
# When using Bolt, you can use either `app.client` or the `client` passed to listeners.
client = WebClient(token=os.environ.get("SLACK_USER_TOKEN"))
logger = logging.getLogger(__name__)

# Load form name(s) from CSV
with open('sample.csv', newline='') as student_names:
    student_reader = csv.reader(student_names)
    channel_names = [
        # Map step
        row[2].lower().replace(' ', '-')
        # Iteration source
        for idx, row in enumerate(student_reader)
        # Filter step
        if idx > 0
    ]

for name in channel_names:
    try:
        # Call the conversations.create method using the WebClient
        # conversations_create requires the channels:manage bot scope
        result = client.conversations_create(
            # The name of the channel (from CSV)
            name=name,
            is_private=True,
        )
        # Log the result which includes information like the ID of the conversation
        logger.info(result)

    except SlackApiError as e:
        logger.error("Error creating conversation: {}".format(e))