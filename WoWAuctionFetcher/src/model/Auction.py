class Auction(object):
	def __init__(self, id, item, owner):
		self.id = id;
		self.item = item;
		self.owner = owner;
		self.ownerRealm = ownerRealm;
		self.bid = bid;
		self.buyout = buyout;
		self.quantity = quantity;
		self.timeLeft = timeLeft;
		#self.bonusLists = None;
		#if bonusLists != None: self.bonusLists = bonusLists

	def getBidPerCount():
		return 1.0 * self.big / self.quantity;

	def getBuyoutPerCount():
		return 1.0 * self.buyout / self.quantity;



