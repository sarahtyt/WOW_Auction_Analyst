import requests;
import json;

class HTTPRequestController(object):
	def __init__(self, api_key):
		self.api_key = api_key;
		self.url = 'https://us.api.battle.net/wow/'
		

	def sendRequest(self, url, params):
		url = url + '&apikey={}';
		params.append(self.api_key);
		response = requests.get(url.format(*params));
		print(url.format(*params))
		return response, json.loads(response.content);







