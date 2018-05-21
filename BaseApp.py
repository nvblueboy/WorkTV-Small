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

class BaseApp(RelativeLayout):
	updateTime = 60
	oldRunTime = 0

	text_color = (0,0,0,1)

	def __init__(self, **kwargs):
		super(BaseApp, self).__init__(**kwargs)

		self.oldRunTime = 0

	def setup(self):
		if len(self.children) > 0:
			for child in self.children[0].children:
				setupFN = getattr(child, "setup", None)

				if callable(setupFN):
					child.setup()

	def update(self, *args):
		if args[0] > self.oldRunTime + self.updateTime:
			self.oldRunTime = args[0]
			updateDataFN = getattr(self, "updateData", None)

			if callable(updateDataFN):
				self.updateData()

		if len(self.children) > 0:
			for child in self.children[0].children:
				updateFN = getattr(child, "update", None)

				if callable(updateFN):
					child.update(args)