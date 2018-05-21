from kivy.app import App
from kivy.config import Config
from kivy.uix.carousel import Carousel
from kivy.uix.image import AsyncImage
from kivy.clock import Clock
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.relativelayout import RelativeLayout
from kivy.properties import StringProperty
from kivy.logger import Logger

from BaseApp import BaseApp

import urllib

import jsonRequests

import weatherCodes

import time

class WeatherApp(BaseApp):

	location = StringProperty()

	topString = StringProperty()
	forecast = StringProperty()

	def __init__(self, **kwargs):
		super(WeatherApp, self).__init__(**kwargs)

	def setup(self):
		super(WeatherApp, self).setup()

		if self.location == "":
			self.location="San Juan Capistrano, CA"

		self.location = self.location.replace(" ","+")

		self.updateData()

	def update(self, args):
		super(WeatherApp, self).update(args)

	def updateData(self):
		baseurl = "https://query.yahooapis.com/v1/public/yql?q="
		query = "select%20*%20from%20weather.forecast%20where%20woeid%20in%20(select%20woeid%20from%20geo.places(1)%20where%20text%20=%20\""+self.location+"\")"
		fmt = "&format=json"

		response = jsonRequests.getResponse(baseurl + query + fmt)

		if response.status:
			item = response["query"]["results"]["channel"]["item"]

			
			self.temperature = item["condition"]["temp"] + " F"
			self.condition = weatherCodes.codes[item["condition"]["code"]]

			self.topString = self.temperature + " | " + self.condition

			if len(self.children) > 0:
				for child in self.ids["days"].children:
					print(child)
					updateFN = getattr(child, "updateData", None)

					if callable(updateFN):
						child.updateData(item["forecast"])


class WeatherDay(BaseApp):

	#Input properties
	day = StringProperty()

	#Output properties
	date = StringProperty()
	forecast = StringProperty()
	condition = StringProperty()

	def __init__(self, **kwargs):
		super(WeatherDay, self).__init__(**kwargs)

	def setup(self):
		super(WeatherDay, self).setup()

	def update(self, *args):
		super(WeatherDay, self).update(*args)

	def updateData(self, data):
		d = 0
		try:
			d = int(str(self.day))
		except:
			Logger.error("WeatherApp: "+self.day+" is not an integer.")
			return

		fc = data[d]
		high = fc["high"]
		low = fc["low"]
		text = fc["text"]

		d = time.strptime(fc["date"], "%d %b %Y")

		self.date = time.strftime("%A",d)

		self.forecast = high + " / " + low

		self.condition = weatherCodes.codes[fc["code"]]
