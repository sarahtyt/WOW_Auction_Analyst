import requests;
import json;

class HTTPRequestController(object):
	def __init__(self, api_key):
		self.api_key = api_key;
		self.url = 'https://us.api.battle.net/wow/'
		

	def sendRequest(url, params):
		url = url + '&api_key={}';
		param.append(api_key);
		response = requests.get(str.format(url, params));
		return response.statusCode, json.loads(response.content);







