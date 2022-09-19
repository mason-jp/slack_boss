import logging
import os

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
try:
    # Call the conversations.create method using the WebClient
    # conversations_create requires the channels:manage bot scope
    result = client.conversations_create(
        # The name of the conversation
        name="emoji-enthusiasts"
    )
    # Log the result which includes information like the ID of the conversation
    logger.info(result)

except SlackApiError as e:
    logger.error("Error creating conversation: {}".format(e))