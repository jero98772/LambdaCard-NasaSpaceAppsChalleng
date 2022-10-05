#!/usr/bin/env python
# -*- coding: utf-8 -*-"
#labdaOrbit - by lambdaCard

from flask import Flask, render_template, request, flash, redirect ,session
from .tools.tools import *
import datetime
import os
SAVESFOLDER="core/static/wav/"
IMGFOLDER="core/static/img/wefax/"
app = Flask(__name__)
app.config["TEMPLATES_AUTO_RELOAD"] = True
app.config['SECRET_KEY']  = str(datetime.datetime.now())
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
		filename,img=noaaResample(name,SAVESFOLDER,IMGFOLDER)
		return render_template("noaaTolkitOut.html",name="img/wefax/"+filename)
	@app.route("/noaaTolkit/out/<string:name>")
	def out(name):
		filename,img=noaa(name,SAVESFOLDER,IMGFOLDER)
		#img=imgload(IMGFOLDER+filename)
		#print(img)
		#img2=grayScale(img)
		#print(type(img2))
		#save(IMGFOLDER+filename,img2)
		return render_template("noaaTolkitOut.html",name="img/wefax/"+filename)
	@app.route("/analizeAI.html",methods=['GET','POST'])
	def analizeAI():
		report=""
		if request.method == 'POST':
			report="see image"
		return render_template("analizeAI.html",report=report)
	@app.route("/websdr.html")
	def websdr():
		return render_template("websdr.html")

	@app.route("/configurations.html")
	def configurations():
		return render_template("configurations.html")
	@app.route("/wifi.html" ,methods=['GET','POST'])
	def wifi():
		data=getData()
		ssid=data["ssid"]
		if data["ssid"]=="":
			data["ssid"]="Lambda-Orbit-EyeSky"
		if request.method == 'POST':
			data["ssid"]=request.form["ssid"]
			writetxt("data/data.py","data="+str(data))
			return redirect("/wifi.html")
			#password=request.form["password"]
		return render_template("wifi.html",ssid=ssid)
	@app.route("/location.html",methods=['GET','POST'])
	def location():
		if request.method == 'POST':
			lat=request.form["lat"]
			lot=request.form["lot"]
			visible=request.form["visible"]
		return render_template("location.html")
	@app.route("/shedule.html",methods=['GET','POST'])
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
	@app.route("/comunity.html")
	def comunity():
		return render_template("comunity.html")

	@app.route("/map.html")
	def map():
		return render_template("map.html")