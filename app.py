'''
Carol Pan 
SoftDev1 pd7
HW14 -- Getting More REST
2017-11-13
'''

from flask import Flask, render_template
import urllib2
import json

app = Flask(__name__)

test_key = "09ba17e1-1cd2-4afd-a5ac-efeb88d45a43"
live_key = "b069dc05-9030-40d0-a4da-2188bce4dbb1"


@app.route("/")
def hello_world():
    
    uResp = urllib2.urlopen("https://api.nasa.gov/planetary/apod?api_key=JjDqY2lvMbEfSJCAdpITWFOfpdPmPsD1lhRiO3Dt")
    url = uResp.geturl()
    head = uResp.info()
    data = uResp.read()

    formdata = json.loads(data)
    
    return render_template("display.html", heading=head, data=formdata)

app.debug = True
app.run()
