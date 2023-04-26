import json, sqlite3, urllib.request

#==========GET-DATA==========

#data_raw = open("input_test.json", "r")

with open("/home/kiwi/project/serial.txt", "r") as serial_text:
    serial = serial_text.read()

with open("/home/kiwi/project/token.txt", "r") as token_text:
    token = token_text.read()

#Need to remove stray \n from file
token = token.strip()

data_raw = urllib.request.urlopen("https://www.solaxcloud.com/proxyApp/proxy/api/getRealtimeInfo.do?tokenId=%s&sn=%s" % (token, serial)).read() 

#==========PROCESS-DATA======

data_preproc = json.loads(data_raw)

#The nesting of the data has to be removed before it can be inserted into the table

data_dict = {
        "success":          data_preproc["success"],
        "inverterSN":       data_preproc["result"]["inverterSN"],
        "sn":               data_preproc["result"]["sn"],
        "acpower":          data_preproc["result"]["acpower"],
        "yieldtoday":       data_preproc["result"]["yieldtoday"],
        "yieldtotal":       data_preproc["result"]["yieldtotal"],
        "feedinpower":      data_preproc["result"]["feedinpower"],
        "feedinenergy":     data_preproc["result"]["feedinenergy"],
        "consumeenergy":    data_preproc["result"]["consumeenergy"],
        "feedinpowerM2":    data_preproc["result"]["feedinpowerM2"],
        "soc":              data_preproc["result"]["soc"],
        "peps1":            data_preproc["result"]["peps1"],
        "peps2":            data_preproc["result"]["peps2"],
        "peps3":            data_preproc["result"]["peps3"],
        "inverterType":     data_preproc["result"]["inverterType"],
        "inverterStatus":   data_preproc["result"]["inverterStatus"],
        "uploadTime":       data_preproc["result"]["uploadTime"],
        "batPower":         data_preproc["result"]["batPower"],
        "powerdc1":         data_preproc["result"]["powerdc1"],
        "powerdc2":         data_preproc["result"]["powerdc2"],
        "powerdc3":         data_preproc["result"]["powerdc3"],
        "powerdc4":         data_preproc["result"]["powerdc4"],
        "batStatus":        data_preproc["result"]["batStatus"],
}

#Uncomment to get current data
#for x in data_dict:
#    print(data_dict[x])

#==========CONNECT-DATABASE==

con = sqlite3.connect("/home/kiwi/project/solar_data.db")
cur = con.cursor()

#==========INSERT-DATA=======

cur.executemany("""
        insert into DOWNLOADED_SOLAX_INFO (
            success,
            inverterSN,
            sn,
            acpower,
            yieldtoday,
            yieldtotal,
            feedinpower,
            feedinenergy,
            consumeenergy,
            feedinpowerM2,
            soc,
            peps1,
            peps2,
            peps3,
            inverterType,
            inverterStatus,
            uploadTime,
            batPower,
            powerdc1,
            powerdc2,
            powerdc3,
            powerdc4,
            batStatus
        )
        values (
            :success,
            :inverterSN,
            :sn,
            :acpower,
            :yieldtoday,
            :yieldtotal,
            :feedinpower,
            :feedinenergy,
            :consumeenergy,
            :feedinpowerM2,
            :soc,
            :peps1,
            :peps2,
            :peps3,
            :inverterType,
            :inverterStatus,
            :uploadTime,
            :batPower,
            :powerdc1,
            :powerdc2,
            :powerdc3,
            :powerdc4,
            :batStatus
        );""", [data_dict])

con.commit()
