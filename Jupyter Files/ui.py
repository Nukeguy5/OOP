
from tkinter import *
from enum import Flag
import math
from abc import ABC, abstractmethod

class ElementType(Flag):
	NONE = 0
	HAS_TEXT = 1
	HAS_ACTION = 2
	IS_CONTAINER = 4

class UIElement(ABC):
	def __init__(self, name=None):
		self.name = name
		self.type = ElementType.NONE
		
	def GetType(self):
		return self.type

	@abstractmethod
	def __str__(self):
		pass

class M_Text:
	def SetText(self, text):
		self.text.set(text)
		
	def __init__(self, text):
		self.text = StringVar()
		self.SetText(text)
		
class I_Frame:
	def __init__(self, frame, forward=True):
		self.frame = frame
		self.forward = forward
		if self.forward:
			self.index = 0
			self.dir = 1
		else:
			self.index = len(self.frame) - 1
			self.dir = -1
		
	def __iter__(self):
		return self
    
	def __next__(self):
		if self.index >= len(self.frame) or self.index < 0:
			raise StopIteration
		result = self.frame[self.index]
		self.index += self.dir
		return result
		
#http://effbot.org/tkinterbook/frame.htm
class UIFrame(UIElement):
	keylist = []
	enterList = []

	@classmethod
	def _Down(cls, e):
		if not e.char in cls.keylist:
			cls.keylist.append(e.char)
			if e.char == '\r':
				for i in cls.enterList:
					i._Command()

	@classmethod
	def _Up(cls, e):
		if e.char in cls.keylist:
			cls.keylist.remove(e.char)
			
	@classmethod
	def RegisterEnterPress(cls, button):
		cls.enterList.append(button)

	def __init__(self, root=None, name=None, **kwargs):
		UIElement.__init__(self, name=name)
		self.type = ElementType.IS_CONTAINER
		self.kwargs = kwargs
		self.list = []
		if (root != None):
			self.root = root
			self._Place(root)
			root.bind('<KeyPress>', UIFrame._Down)
			root.bind('<KeyRelease>', UIFrame._Up)
	
	def _Place(self, frame, push=TOP, **kwargs):
		self.kwargs.update(kwargs)
		self.frame = Frame(frame, **self.kwargs)
		self.frame.pack(side=push)
	
	def Add(self, uiElement, side=TOP, **kwargs):
		uiElement._Place(self.frame, push=side, **kwargs)
		self.list.append(uiElement)
		uiElement.owner = self
		uiElement.side = side
		
	#checks only current frame and members and returns a list
	def FindFrameElementsByName(self,name):
		return [i for i in self.list if name == i.name]
	
	#recursively checks and returns a list
	def FindElementsByName(self, name):
		list = []
		for i in self.list:
			if name == i.name:
				list.append(i)
			if isinstance(i, UIFrame):
				uiElements = i.FindElementsByName(name)
				list.extend(uiElements)
		return list
	
	#generator - recursively checks
	def FindEachElementByName(self, name):
		for i in self.list:
			if name == i.name:
				yield i
			if isinstance(i, UIFrame):
				yield from i.FindElementsByName(name)
		
	def __str__(self, tab=0):
		r = "Frame\n"
		for i in self.list:
			if (tab > 0):
				for j in range(tab):
					r += "  "
			r += "  "
			if isinstance(i, UIFrame):
				r += i.__str__(tab=tab+1)
				continue
			r += str(i) + "\n"
		return r
	
	def __iadd__(self, uiElement):
		if issubclass(type(uiElement), UIElement):
			self.Add(uiElement)
			return self
		return NotImplemented
	
	def __len__(self):
		return len(self.list)

	def __getitem__(self, key):
		if isinstance(key, int) or isinstance(key, float):
			if key < -len(self.list) or key >= len(self.list) or key != math.floor(key):
				raise IndexError
			return self.list[key]
		raise TypeError
		
	def __iter__(self):
		return I_Frame(self)
		
	def __reversed__(self):
		return I_Frame(self, False)
		
#http://effbot.org/tkinterbook/label.htm
class UILabel(UIElement, M_Text):
	def __init__(self, text='', name=None, **kwargs):
		UIElement.__init__(self, name=name)
		self.type = ElementType.HAS_TEXT
		M_Text.__init__(self, text)
		kwargs.pop("textvariable", None) #we use our own textvariable
		self.kwargs = kwargs
	
	def _Place(self, frame, push=TOP, **kwargs):
		kwargs.pop("textvariable", None) #we use our own textvariable
		self.kwargs.update(kwargs)
		self.label = Label(frame, textvariable=self.text, **self.kwargs)
		self.label.pack(side=push)
		
	def __str__(self):
		return "Label: " + self.text.get() #because self.text is StringVar not string

#http://effbot.org/tkinterbook/button.htm
class UIButton(UIElement, M_Text):
	def __init__(self, action, data=None, text='', name=None, **kwargs):
		UIElement.__init__(self, name=name)
		M_Text.__init__(self, text)
		self.type = ElementType.HAS_TEXT | ElementType.HAS_ACTION
		kwargs.pop("command", None) #action replaces command
		kwargs.pop("textvariable", None) #we use our own textvariable
		self.kwargs = kwargs
		self.action = action
		self.data = data
		
	def CopySelf(self, action=None, data=None, text=None, name=None, addToSameFrame=False, **override_args):
		newAction = self.action if action == None else action
		newData = self.data if action == None else data
		newText = self.text.get() if text == None else text
		newName = self.name if name == None else name
		myCopy = UIButton(newAction, data=newData, text=newText, name=newName, **self.kwargs)
		override_args.pop("command", None) #action replaces command
		override_args.pop("textvariable", None) #we use our own textvariable
		myCopy.kwargs.update(override_args)
		if addToSameFrame:
			self.owner.Add(myCopy, self.side)
		return myCopy
	
	def _Place(self, frame, push=TOP, **kwargs):
		kwargs.pop("command", None) #action replaces command
		kwargs.pop("textvariable", None) #we use our own textvariable
		self.kwargs.update(kwargs)
		self.button = Button(frame, command=self._Command, textvariable=self.text, **self.kwargs)
		self.button.pack(side=push)
	
	def _Command(self):
		self.action(self.data)
		
	def __str__(self):
		return "Button: " + self.text.get() #because self.text is StringVar not string

def _ElementalLogWrapper(cls, func):
	def wrapper(*args, **kwargs):
		print("Created " + cls.__name__)
		return func(*args, **kwargs)
	return wrapper

_ElementLogginOn = False
def TurnOnElementCreationLogging():
	global _ElementLogginOn
	if not _ElementLogginOn:
		UIFrame.__init__ = _ElementalLogWrapper(UIFrame, UIFrame.__init__)
		UILabel.__init__ = _ElementalLogWrapper(UILabel, UILabel.__init__)
		UIButton.__init__ = _ElementalLogWrapper(UIButton, UIButton.__init__)
		_ElementLogginOn = True