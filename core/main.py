#!/usr/bin/env python
# -*- coding: utf-8 -*-"
#labdaOrbit - by lambdaCard

from flask import Flask, render_template, request, flash, redirect ,session
from .tools.tools import *
import datetime
import os
SAVESFOLDER="core/static/wav/"
IMGFOLDER="core/static/img/"
app = Flask(__name__)
class webpage():
	@app.route("/")
	def index():
		return render_template("index.html")
	@app.route("/tools.html")
	def tools():
		return render_template("tools.html")#need content
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
		filename=noaaResample(name,SAVESFOLDER,IMGFOLDER)
		im=img(i)
		im2=grayScale(im)
		return render_template("noaaTolkitOut.html",name="img/"+filename)
	@app.route("/noaaTolkit/out/<string:name>")
	def out(name):
		filename=noaa(name,SAVESFOLDER,IMGFOLDER)
		return render_template("noaaTolkitOut.html",name="img/"+filename)
	@app.route("/analizeAI.html")
	def analizeAI():
		return render_template("analizeAI.html")
	@app.route("/websdr.html")
	def websdr():
		return render_template("websdr.html")

	@app.route("/configurations.html")
	def configurations():
		return render_template("configurations.html")
	@app.route("/wifi.html")
	def wifi():
		password="sky--eye"
		ssid="Lambda-Orbit-EyeSky"
		if request.method == 'POST':
			ssid=request.form["ssid"]
			password=request.form["password"]
		return render_template("wifi.html",password=password,ssid=ssid)
	@app.route("/shedule.html")
	def shedule():
		return render_template("shedule.html")

	@app.route("/reports.html")
	def reports():
		return render_template("reports.html")
	@app.route("/images.html")
	def images():
		return render_template("images.html")
	@app.route("/alert.html")
	def alert():
		return render_template("alert.html")
	@app.route("/predsatelite.html")
	def predsatelite():
		return render_template("predsatelite.html")
