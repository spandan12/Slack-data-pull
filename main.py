import logging
import os
from dotenv import load_dotenv
# Import WebClient from Python SDK (github.com/slackapi/python-slack-sdk)
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError

# WebClient insantiates a client that can call API methods
# When using Bolt, you can use either `app.client` or the `client` passed to listeners.

load_dotenv()

client = WebClient(token=os.environ.get("BOT_USER_OAUTH_TOKEN"))
logger = logging.getLogger(__name__)

# You probably want to use a database to store any conversations information ;)
conversations_store = {}

def fetch_conversations():
    try:
        # Call the conversations.list method using the WebClient
        result = client.conversations_list()
        save_conversations(result["channels"])

    except SlackApiError as e:
        logger.error("Error fetching conversations: {}".format(e))


# Put conversations into the JavaScript object
def save_conversations(conversations):
    conversation_id = ""
    for conversation in conversations:
        # Key conversation info on its unique ID
        conversation_id = conversation["id"]

        # Store the entire conversation object
        # (you may not need all of the info)
        conversations_store[conversation_id] = conversation

fetch_conversations()