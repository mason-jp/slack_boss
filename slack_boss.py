import logging
import os
import csv

from optparse import OptionParser
from dotenv import load_dotenv

# Import WebClient from Python SDK (github.com/slackapi/python-slack-sdk)
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError

# Load env variables
load_dotenv()

# Configure option parser
parser = OptionParser()

parser.add_option('-v', '--verbose', help='Print a lot of stuff', dest='verbose', action='store_true')
parser.add_option('-p', '--prefix', help="A prefix for channel names")
parser.add_option('-f', '--filename', help="The name of the file to pull names from (extension included).")
parser.add_option('-q', '--preview', help="Preview channel names for a given input", action='store_true')

options, args = parser.parse_args()

if not options.filename:
    print('You must provide a filename.')
    exit(1)

if options.prefix:
    options.prefix = options.prefix + '-'

# WebClient instantiates a client that can call API methods
client = WebClient(token=os.environ.get("SLACK_USER_TOKEN"))
logger = logging.getLogger(__name__)

prefix = options.prefix or ''



# Load form name(s) from CSV
with open(options.filename, newline='') as student_names:
    student_reader = csv.reader(student_names)
    channel_names = [
        # Map step, adding prefix to student name pulled from file
        prefix + row[2].lower().replace(' ', '-')
        # Iteration source
        for idx, row in enumerate(student_reader)
        # Filter step
        if idx > 0
    ]


if options.preview:
    print(channel_names)
    exit(0)

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