import os
import sys
import time
import datetime


ts = time.time()
sttime = datetime.datetime.fromtimestamp(ts).strftime('%Y/%m/%d-%H:%M:%S - ')
file = open("proddata.log","a")
file.write(sttime + "{""_ref"":""path"",""_tenant"":""company"",""_dig"":""_1_"",""aType"":""ip"",""aValue"":""1.1.1.1"",""type"":""packet"",""threat"":0,""firewall"":""192.168.0.100"",""port"":""80"",""protocol"":""tcp"",""policy_name"":""genericproxy"",""qty"":116}" + "\n")
file.close()
