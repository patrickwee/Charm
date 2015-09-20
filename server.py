"""

Charm Server

Written by Joshua Paul A. Chan @ HackTheNorth Fall 2015
"""
import math
import random
from flask import Flask, jsonify

APP_URI = "/"
app = Flask(__name__)
app.debug = True

texts = [
  {
    'id': 0,
    'text': "Are you Jamaican? Because Jamaican me crazy!",
    'ups': 0,
    'downs': 0,
    'text_type': 'pickup'
  },
  {
    'id': 1,
    'text': "Can you tie your shoes? I don't want you falling for anyone else.",
    'ups': 0,
    'downs': 0,
    'text_type': 'pickup'
  },
  {
    'id': 2,
    'text': "Do you have a band-aid? Because I scraped my knee falling for you.",
    'ups': 0,
    'downs': 0,
    'text_type': 'pickup'
  },
  {
    'id': 3,
    'text': "Are you religious? Cause you’re the answer to all my prayers.",
    'ups': 0,
    'downs': 0,
    'text_type': 'pickup'
  },
  {
    'id': 4,
    'text': "You know what material this is? Boyfriend/Girlfriend material.",
    'ups': 0,
    'downs': 0,
    'text_type': 'pickup'
  },
  {
    'id': 5,
    'text': "“If I were a gardener, I’d put your tulips and my tulips together.",
    'ups': 0,
    'downs': 0,
    'text_type': 'pickup'
  },
  {
    'id': 6,
    'text': "Hi, you got raisins? No? Well, how about a date?",
    'ups': 0,
    'downs': 0,
    'text_type': 'pickup'
  },
  {
    'id': 7,
    'text': "Are you a thief? 'Cause you stole my heart!",
    'ups': 0,
    'downs': 0,
    'text_type': 'pickup'
  },
  {
    'id': 8,
    'text': "Are you a cliff? 'Cause I'm falling for you!",
    'ups': 0,
    'downs': 0,
    'text_type': 'pickup'
  },
  {
    'id': 9,
    'text': "I'm not drunk, I'm just intoxicated by you!",
    'ups': 0,
    'downs': 0,
    'text_type': 'pickup'
  },
  {
    'id': 10,
    'text': "Do you like going to the gym? 'Cause you've been running in my mind!",
    'ups': 0,
    'downs': 0,
    'text_type': 'pickup'
  },
  {
    'id': 11,
    'text': "Am I in heaven? Or do you just look like an angel?",
    'ups': 0,
    'downs': 0,
    'text_type': 'pickup'
  },
  {
    'id': 12,
    'text': "Your dad must be a terrorist, ‘coz yoh da bomb!",
    'ups': 0,
    'downs': 0,
    'text_type': 'pickup'
  },
  {
    'id': 13,
    'text': "Was your dad an alien? ‘Coz honey, there’s nothing else like you on planet Earth!",
    'ups': 0,
    'downs': 0,
    'text_type': 'pickup'
  },
  {
    'id': 14,
    'text': "Hi, you must be the devil? ‘Coz you’re hot as hell!",
    'ups': 0,
    'downs': 0,
    'text_type': 'pickup'
  },
  {
    'id': 15,
    'text': "Life without you would be like a broken pencil… pointless.",
    'ups': 0,
    'downs': 0,
    'text_type': 'pickup'
  },
  {
    'id': 16,
    'text': "Hi, I know I’m a guy but I want to be Alice, coz your body’s a Wonderland.",
    'ups': 0,
    'downs': 0,
    'text_type': 'pickup'
  },
  {
    'id': 17,
    'text': "Are you a keyboard? 'Cause you're my type!",
    'ups': 0,
    'downs': 0,
    'text_type': 'pickup'
  },
  {
    'id': 18,
    'text': "Top view, side view, bottom view, whatever view, I love view.",
    'ups': 0,
    'downs': 0,
    'text_type': 'pickup'
  },
  {
    'id': 19,
    'text': "Are you good in algebra? Can you substitute my ‘x’?",
    'ups': 0,
    'downs': 0,
    'text_type': 'pickup'
  },
  {
    'id': 20,
    'text': "Are you pizza? Because I have a ‘crust’ on you.",
    'ups': 0,
    'downs': 0,
    'text_type': 'pickup'
  },
  {
    'id': 21,
    'text': "Can I take your picture? 'Cause I wanna show Santa what I want for Christmas.",
    'ups': 0,
    'downs': 0,
    'text_type': 'pickup'
  },
  {
    'id': 22,
    'text': "Are you a dictionary? Because you give meaning to my life.",
    'ups': 0,
    'downs': 0,
    'text_type': 'pickup'
  },
  {
    'id': 23,
    'text': "You must be in a wrong place - the Miss Universe contest is over there.",
    'ups': 0,
    'downs': 0,
    'text_type': 'pickup'
  },
  {
    'id': 24,
    'text': "You must be a banana because I find you a peeling.",
    'ups': 0,
    'downs': 0,
    'text_type': 'pickup'
  }
]


@app.route(APP_URI + 'random/<text_type>')
def get_random(text_type):
	items = filter(lambda item: item['text_type'] == text_type, texts)
	if items == None:
		return '500'
	else:
		# print(items)
		item = random.choice(list(items))
		print(item)
		return jsonify(item)

@app.route(APP_URI + 'downvote/<int:id>')
def downvote_text(id):
	# Fetch item based on id
	item = None
	# If defined, increment downvote by one
	if item != None:
		item['downs'] += 1
		return '200'
	else:
		return '404'

@app.route(APP_URI + 'upvote/<int:id>')
def upvote_text(id):
	# Fetch item based on id
	item = None
	# Increment ups
	if item != None:
		item['up'] += 1
		return '200'
	else:
		return '404'

def main():
	app.run(host='0.0.0.0')

if __name__ == '__main__':
	main()
