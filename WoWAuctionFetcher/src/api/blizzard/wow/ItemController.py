from HTTPRequestController import HTTPRequestController;
from WoWAuctionFetcher.src.model.Item import Item;

class ItemController(HTTPRequestController):
	def __init__(self, api_key):
		super(ItemController, self).__init__(api_key);
		self.url = self.url + "item/{}?locale={}";

	def request(self, item, locale):
		param = [item, locale]
		response, responseContent = self.sendRequest(self.url, param);
		if response.ok:
			return Item(responseContent);
		return None;


if __name__ == "__main__":

	ic = ItemController("nqc2bm6wcuyv8ux499rcrhrahp952waw");
	item = ic.request("127850", "en_US");
	print(dir(item))
	print(item.id);
	print(item.name);
