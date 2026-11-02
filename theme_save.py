import json,os

with open('credits.json','r') as f:
    credit = json.load(f)


ACTIVE_THEME_FILE = credit["theme"]
ACTIVE_APPEARANCE = "dark"

