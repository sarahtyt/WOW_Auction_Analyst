import json;
import os;

def printAucCount(items, fn):
    fname = os.path.join(os.path.dirname(__file__), '../../data/auctions/' + fn);
    file = open(fname);
    data = json.load(file);
    #print(type(data));
    #print(data.keys());
    #print(data["realms"]);
    print("total auctions: ", len(data["auctions"]));
    #print(data["auctions"][0]);
    file.close();
    newitems = 0;
    for auc in data["auctions"]:
        item = auc["item"];
        if item not in items:
            newitems += 1;
            items[item] = 1;
        else:
           items[item] += 1;
    print("new items:", newitems);
    print("auction items:", len(items));

if __name__ == "__main__":

    items = {};
    fn = os.path.join(os.path.dirname(__file__), '../../data/auctions/');
    for filename in os.listdir(fn):
        print(filename);
        printAucCount(items, filename);
    fn = os.path.join(os.path.dirname(__file__), '../../data/items.itms');
    #file = open(fn, 'w+');
    #json.dump(items, file);
    #file.close();
    x = sorted(items, key=items.__getitem__, reverse=True);
    print(x[0:20]);
    for item in x[0:20]:
        print(items[item]);
    #print(items.values().sort().reverse()[0:20]);
