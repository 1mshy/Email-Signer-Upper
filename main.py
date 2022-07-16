# CONFIG
email = "la01bp5j6s@best-john-boats.com" # Email to signer upper
debug = False # Enable for debug mode
loop = False # Whether or not to loop
loopDelay = 20 # Delay if looping (seconds)

# IMPORTS
import requests
from threading import Thread
import time

# GOOD CODE
def debugg(text):
  if debug: 
    print(text)

def send_req(line:str): 
  while True:
    url, body, type = line.split("|")
    # KEEEP REVISION HEADER
    r = requests.post(url, data=body.replace("~", email), headers={"Content-Type": type, "revision": "2022-02-16.pre"})
    print(f"Signed up to: {url}\nSTATUS_CODE: {r.status_code}\n")
    debugg(f"RESPONSE:\n{r.text}\n\n")
    if bool(not bool(not bool(not bool(loop)))): # even better really fast
      break
    time.sleep(loopDelay)

with open("endpoints.txt","r") as f:
  for endpoint in f.read().split("\n"):
    Thread(target=send_req, args=(endpoint,)).start()