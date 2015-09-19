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
		'text': "Are you Jamaican? Because you're Jamaican me crazy!",
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
		'text': "Do you have a bandaid? Because I scraped my knee falling for you.",
		'ups': 0,
		'downs': 0,
		'text_type': 'pickup'
	},
	{
		'id': 3,
		'text': "Are you Jamaican? Because you're Jamaican me crazy!",
		'ups': 0,
		'downs': 0,
		'text_type': 'pickup'
	},
	{
		'id': 4,
		'text': "What do you do with epileptic lettuce? You make a seizure salad!",
		'ups': 0,
		'downs': 0,
		'text_type': 'joke'
	},
]


@app.route(APP_URI + 'random/<text_type>')
def get_random(text_type):
	items = filter(lambda item: item['text_type'] == text_type, texts)
	if items == None:
		return '500'
	else:
		print(items)
		item = random.choice(list(items))
		print(item)
		return jsonify(item)

@app.route(APP_URI + 'random/pickup')
def get_random_pickup():
	items = filter(lambda item: item['text_type'] == 'pickup', texts)
	print(items)
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

@app.route(APP_URI + 'upvote/<int:id>')
def upvote_text(id):
	# Fetch item based on id
	item = None
	# Increment ups
	if item != None:
		item['up'] += 1
	return '200'

def main():
	app.run(host='0.0.0.0')

if __name__ == '__main__':
	main()
