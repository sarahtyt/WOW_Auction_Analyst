import requests;
import json;
import datetime;
import time;


api_key = "nqc2bm6wcuyv8ux499rcrhrahp952waw";
baseUrl = "https://us.api.battle.net/wow/auction/data";
server = "illidan";
locale = "en_US";

baseDir = "C:/Users/yinzl/Desktop/wowauc"

def makeRequestUrl(server, locale, api_key):
    return baseUrl + "/" + server + "?locale=" + locale + "&apikey=" + api_key;

def getFiles(server, locale, api_key):
    files = [];
    requestUrl = makeRequestUrl(server, locale, api_key);
    print("HTTP Request made for: " + requestUrl);
    r = requests.get(requestUrl);
    if r.ok:
        contents = json.loads(r.content)
        for file in contents["files"]:
            files.append(file["url"]);
    return files;


def retrieve():
    now = datetime.datetime.now()
    aucfiles = getFiles(server, locale, api_key);
    index = 0;
    for aucfile in aucfiles:
        print("HTTP Request made for: " + str(aucfile));
        r = requests.get(aucfile);
        if r.ok:
            print("Auction data retrived for: " + server + "/" + locale);
            dir = str.format("{}/{}-{}-{}-{}.auc", baseDir, now.year, now.month, now.day, now.hour);
            if index > 0:
                dir += "."
                dir += str(index)
            file = open(dir, 'w+');
            contents = json.loads(r.content);
            print("Writing auction date to file: " + dir);
            json.dump(contents, file);
            file.close();
            index += 1;
    return index;


def run():
    while(True):
        print("======================== Retriving WoW Auction ======================")
        print(str.format("Retrieving WoW auction data for time: {}", datetime.datetime.now()));
        retrieve();
        print("======================== Wait for another hour ======================")
        for i in range(0,6):
            print("sleeping........,current time: " + str(datetime.datetime.now()))
            time.sleep(600);

##retrieve();


if __name__ == "__main__":
    print(makeRequestUrl("illidan", "en_US", api_key));
    r = requests.get(makeRequestUrl("illidan", "en_US", api_key));
    print(r.status_code);


