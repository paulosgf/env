#!/usr/bin/env python3

import os
import dotenv
from dotenv import load_dotenv
load_dotenv()

CONSUMER_KEY = os.environ.get("TWITTER_CONSUMER_KEY")         # API Key
CONSUMER_SECRET = os.environ.get("TWITTER_CONSUMER_SECRET")   # API Secret Key

print(CONSUMER_KEY, CONSUMER_SECRET)
