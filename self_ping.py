import time
import requests
import os

def self_ping():
    while True:
        try:
            url = os.getenv('RENDER_EXTERNAL_URL')
            if url:
                requests.get(url)
        except:
            pass
        time.sleep(600)