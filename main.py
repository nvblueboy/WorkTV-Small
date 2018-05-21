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

import time

from BaseApp import BaseApp

import WeatherApp, TimeZoneApp

class SmallWorkTV(RelativeLayout):

	oldTime = 0
	runTime = 0

	def __init__(self, **kwargs):
		super(SmallWorkTV, self).__init__(**kwargs)

	def setup(self):
		for child in self.children[0].children:
			setupFN = getattr(child, "setup", None)

			if callable(setupFN):
				child.setup()

	def update(self, *args):
		if int(time.time()) != self.oldTime:
			self.oldTime = int(time.time())
			self.runTime += 1

		for child in self.children[0].children:
			updateFN = getattr(child, "update", None)

			if callable(updateFN):
				child.update(self.runTime)


# --------------------------------------
#    Custom app definitions
# --------------------------------------

class AddressApp(BaseApp):

	def __init__(self, **kwargs):
		super(AddressApp, self).__init__(**kwargs)

	def setup(self):
		super(AddressApp, self).setup()

	def update(self, *args):
		super(AddressApp, self).update(*args)


class LogoApp(BaseApp):
	def __init__(self, **kwargs):
		super(LogoApp, self).__init__(**kwargs)

	def setup(self):
		super(LogoApp, self).setup()

	def update(self, *args):
		super(LogoApp, self).update(*args)

class LocalTime(BaseApp):

	timeStr = StringProperty()

	def __init__(self, **kwargs):
		super(LocalTime, self).__init__(**kwargs)

	def setup(self):
		super(LocalTime, self).setup()

	def update(self, *args):
		super(LocalTime, self).update(*args)

		self.timeStr = time.strftime("%I:%M:%S %p").lstrip("0")

# ---------------
# App definition 
# ---------------

class SmallWorkTVApp(App):
	def build(self):
		Config.set('graphics','width','1920')
		Config.set('graphics','height','1080')
		Config.set('graphics','fullscreen',True)

		#Set configuration settings.
		Config.set('kivy', 'log_level', 'info')
		Config.set('kivy', 'log_dir', "logs")
		Config.set('kivy', 'log_name', "log_%y_%m_%d_%H_%M_%S.txt")
		Config.set('kivy', 'log_enable', 1)
		Config.set('kivy', 'log_maxfile', 25)

		self.load_kv('SmallWorkTV.kv')

		self.appWindow = SmallWorkTV()

		Clock.schedule_interval(self.appWindow.update, .2)

		return self.appWindow

	def on_start(self, **kwargs):
		self.appWindow.setup()


if __name__ == "__main__":
	print("Loading app...")
	SmallWorkTVApp().run()