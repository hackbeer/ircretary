from plugins.echo import CommandPlugin

import twitter

# Twitter application keys example. Bogus keys, won't work. More info on README
consumer_key = 'fGfWx4aZYb8PiYbBeG7w'
consumer_secret = 'bcDoCgoopCauEGu8ksUqrgDgkMgQ1DnsNWMoMBIYYY'
access_token_key = '125329777-ddddDYJ3lscMvGq5fxeEZ7vMIpOfmycBQ1TMqr6n'
access_token_secret = 'eKBjU7dddgd4caaaaaav4a2czylDeKQEmr5TFniII'

class Tuite(CommandPlugin):

	def __init__(self):
		self.api = twitter.Api(consumer_key=consumer_key,
													 consumer_secret=consumer_secret,
													 access_token_key=access_token_key,
													 access_token_secret=access_token_secret)

	def getCommands(self):
		return ['tuite']

	def tuite(self, data):
		self.api.PostUpdate('<' + data['user'] + '> ' + data['message'])
