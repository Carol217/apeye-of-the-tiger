'''
Carol Pan 
SoftDev1 pd7
HW13 -- A RESTful Journey Skyward
2017-11-10
'''

from flask import Flask, render_template
import urllib2
import json

app = Flask(__name__)


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
