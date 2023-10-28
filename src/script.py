import json

from recombee_api_client.api_client import RecombeeClient
from recombee_api_client.api_requests import *

client = RecombeeClient(
    'proiect-sac-dev',
    'cIiu5vrFrg7gCOOOkSBlOtbiKvgHMrXeai813tEi6ZFJ6hB1EBXDK0DXKjcj0S1m',
)

client.send(AddItemProperty('name', 'string'))
client.send(AddItemProperty('platform', 'string'))
client.send(AddItemProperty('release_date', 'string'))
client.send(AddItemProperty('summary', 'string'))
client.send(AddItemProperty('meta_score', 'double'))
client.send(AddItemProperty('user_review', 'double'))

with open('./games.json', encoding='utf8') as f:
    games = json.loads(f.read())
    i = 0

    for game in games:
        i = i + 1
        # client.send(DeleteItem(str(i)))
        client.send(AddItem(str(i)))
        client.send(SetItemValues(str(i), game))
