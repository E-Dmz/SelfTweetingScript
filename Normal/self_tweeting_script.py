

# [🧡 Code] 🤖 This script is a self-tweeting script:

import twitter
from keys import keys

api = twitter.Api(**keys)

with open('self_tweeting_script.py', 'r') as f:
    api.PostUpdate(f.read())

# @42born2code @ThePSF #Python #twitterapi #100DaysOfCode