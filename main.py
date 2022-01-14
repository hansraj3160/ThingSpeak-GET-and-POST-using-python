import urllib.request
import requests
import random
import urllib
def thingspeak_post():
    bs = random.randint(10000, 15000);
    data = urllib.request.urlopen("https://api.thingspeak.com/update?api_key=G9HBHF71ORH6AASL&field2=0" + str(bs));
    data1 = data.read()
    print(data1);

def read_data_thingspeak():
    URL='https://api.thingspeak.com/channels/1630987/fields/2.json?results='
    KEY='READ KEY 0NOUL5HBK8VP7HU5  '
    HEADER='&results=2'
    NEW_URL=URL+KEY+HEADER
    print(" Result ",NEW_URL)

    get_data=requests.get(NEW_URL).json()
    #print(get_data)
    channel_id=get_data['channel']['id']

    feild_1=get_data['feeds']
    #print(feild_1)

    t=[]
    for x in feild_1:
        print(x['field2'])
        t.append(x['field2'])

if __name__ == '__main__':

    thingspeak_post()
    read_data_thingspeak()