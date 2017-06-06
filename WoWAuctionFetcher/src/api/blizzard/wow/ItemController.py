class ItemController(HTTPRequestController):

	def __init__(self, api_key):
		super(ItemController, self).__init__(api_key);
		self.url = self.url + "item/{}?locale={}";

	def request(item, locale):
		param = [item, locale]
		return sendRequest(self.url, param);