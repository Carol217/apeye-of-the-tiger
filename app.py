'''
Carol Pan 
SoftDev1 pd7
HW14 -- Getting More REST: Holiday Edition
2017-11-13
'''

from flask import Flask, render_template
import urllib2
import json

app = Flask(__name__)

test_key = "09ba17e1-1cd2-4afd-a5ac-efeb88d45a43"

base_url= "https://holidayapi.com/v1/holidays?key=" + test_key

#country and year are necessary params
country= "&country="
year="&year="
month="&month="


@app.route("/")
def hello_world():
    
    uResp = urllib2.urlopen(base_url + country + "US" + year + "2016")
    url = uResp.geturl()
    head = uResp.info()
    data = uResp.read()

    formdata = json.loads(data)
    
    return render_template("display.html", heading=head, data=formdata)

app.debug = True
app.run()
