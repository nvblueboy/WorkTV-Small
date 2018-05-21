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

import pytz, datetime

fmt = "%I:%M:%S %p"

class TimeZoneApp(BaseApp):

	def __init__(self, **kwargs):
		super(TimeZoneApp, self).__init__(**kwargs)

	def setup(self):
		super(TimeZoneApp, self).setup()

	def update(self, *args):
		super(TimeZoneApp, self).update(*args)


class TimeZone(RelativeLayout):

	tz = StringProperty()

	pretty_tz = StringProperty()

	output = StringProperty()

	def __init__(self, **kwargs):
		super(TimeZone, self).__init__(**kwargs)

	def setup(self):
		if self.tz == "":
			self.tz = "US/Pacific"

		self.pacifictz = pytz.timezone("US/Pacific")

		try:
			self.thistz = pytz.timezone(self.tz)
		except:
			self.tz = "US/Pacific"
			self.thistz = pytz.timezone(self.tz)

		if self.pretty_tz == "":
			self.pretty_tz = self.tz.replace("_"," ")

	def update(self, *args):
		now = datetime.datetime.now()
		pacific_dt = self.pacifictz.localize(now)

		this_dt = pacific_dt.astimezone(self.thistz)
		self.output = this_dt.strftime(fmt).lstrip("0")
		