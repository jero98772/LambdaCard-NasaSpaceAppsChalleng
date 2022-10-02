#!/usr/bin/env python
# -*- coding: utf-8 -*-"
#labdaOrbit - by lambdaCard

from flask import Flask, render_template, request, flash, redirect ,session
from .tools.tools import *
import datetime
import os
SAVESFOLDER="core/static/wav/"
#IMGFOLDER="static/img/"
app = Flask(__name__)
class webpage():
	@app.route("/",methods=['GET','POST'])
	def index():
		return render_template("index.html")
	@app.route("/noaaTolkit",methods=['GET','POST'])
	def noaaTolkit():
		if not os.path.exists(SAVESFOLDER):
			print("exist")
			os.mkdir(SAVESFOLDER)
		if request.method == 'POST':
			name="wavnoaa"+str(datetime.datetime.now()).replace(" ","").replace("-","").replace(":","").replace(".","")+".wav"
			file = request.files["file"]
			file.save(SAVESFOLDER+name)
			try:
				resample=request.form["resample"]
				print(resample,type(resample))
			except :
				resample=None
			if resample:
				return redirect("noaaTolkit/outr/"+name)  
			else:
				return redirect("noaaTolkit/out/"+name)
		return render_template("noaaTolkit.html")
	@app.route("/noaaTolkit/outr/<string:name>")
	def noaaTolkitoutr(name):
		filename=noaaResample(SAVESFOLDER+name)
		return render_template("noaaTolkitOut.html",name="img/"+filename)

	@app.route("/noaaTolkit/out/<string:name>")
	def out(name):
		filename=noaa(SAVESFOLDER+name)
		return render_template("noaaTolkitOut.html",name="img/"+filename)
