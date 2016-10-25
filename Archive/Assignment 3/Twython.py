from twython import Twython

# Replace the following strings with your own keys and secrets
TOKEN = '1101820572-QNtPCZDrFm0tWn2sVhOT40L86xcLqAgE5W6vaGL'
TOKEN_SECRET = 'IHCdr6VkKbB3jEzn9xG4ZyTVUNXIPPw3SP5KBI4xFKUbZ'
CONSUMER_KEY = 'zLsC7FASDt1zyWiB9mOv8ZDr6'
CONSUMER_SECRET = '80BxvhJ9U7phNaUUONofYUEG4B9GgKvu75XKAse0WIbbcVYrBX'


t = Twython(CONSUMER_KEY, CONSUMER_SECRET,
   TOKEN, TOKEN_SECRET)

data = t.search(q="Donald Trump", count=500)

for status in data['statuses']:
 print(status['text'])
