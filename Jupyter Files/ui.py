
from tkinter import *


class UIElement:
	pass


class M_Text:
	def SetText(self, text):
		self.text.set(text)
	
	def __init__(self, text):
		self.text = StringVar()
		self.SetText(text)


class UIFrame(UIElement):
	def __init__(self, root=None, bd=1):
		self.list = []
		if root != None:
			self.root = root
			self._Place(root, border=bd)

	def _Place(self, frame, push=TOP, border=0):
		self.frame = Frame(frame, bd=border)
		self.frame.pack(side=push)
	
	def Add(self, uiElement, side=TOP, color='white'):
		uiElement._Place(self.frame, color, push=side)
		self.list.append(uiElement)


class UILabel(UIElement, M_Text):
	def __init__(self, text=''):
		M_Text.__init__(self, text)
		
	def _Place(self, frame, color, push=TOP, text_font='Helvetica'):
		self.label = Label(frame, font=text_font, bg=color, textvariable = self.text)
		self.label.pack(side=push)


class UIButton(UIElement, M_Text):
	def __init__(self, action, data = None, text = ''):
		M_Text.__init__(self, text)
		self.action = action
		self.data = data
		
	def _Place(self, frame, color, push=TOP, text_font='Helvetica'):
		self.button = Button(frame, font=text_font, fg=color, textvariable = self.text, command = self._Command)
		self.button.pack(side=push)
		
	def _Command(self):
		self.action(self.data)
