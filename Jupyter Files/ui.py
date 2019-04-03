
from tkinter import *
from enum import Flag, Enum
import math
from abc import ABC, abstractmethod

class LanguageType(Enum):
	ENGLISH = 0
	PIGLATIN = 1

class ElementType(Flag):
	NONE = 0
	HAS_TEXT = 1
	HAS_ACTION = 2
	IS_CONTAINER = 4

class UIElement(ABC):
	UILanguage = LanguageType.ENGLISH

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
		if isinstance(text, dict):
			self.textList = text
			text = ''
			if UIElement.UILanguage in self.textList:
				text = self.textList[UIElement.UILanguage]
		self.text.set(text)
		
	def __init__(self, text):
		self.text = StringVar()
		self.SetText(text)
		self.type = ElementType.HAS_TEXT

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
					i._EnterPressed()

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
			# root.bind('<KeyPress>', UIFrame._Down)
			# root.bind('<KeyRelease>', UIFrame._Up)
	
	def _Place(self, frame, push=TOP, **kwargs):
		self.kwargs.update(kwargs)
		self.frame = Frame(frame, **self.kwargs)
		self.side = push
		self.frame.pack(side=push)
		
	def _Show(self):
		self.frame.pack(side=self.side)

	def _Hide(self):
		self.frame.pack_forget()
	
	def Add(self, uiElement, side=TOP, hide=False, **kwargs):
		kwargs.pop("hide", None)
		uiElement._Place(self.frame, push=side, **kwargs)
		self.list.append(uiElement)
		uiElement.owner = self
		uiElement.side = side
		if hide:
			uiElement._Hide()

	def ShowElements(self, name):
		for i in self.FindEachElementByName(name):
			i._Show()

	def HideElements(self, name):
		for i in self.FindEachElementByName(name):
			i._Hide()
		
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
		
class UIRoot(UIFrame):
	_singleton = None

	def __new__(cls, *args, **kwargs):
		if not cls._singleton:
			cls._singleton = super(UIRoot, cls).__new__(cls)
		return cls._singleton

	def __init__(self, name="root", **kwargs):
		kwargs.pop("root", None)
		self.root = Tk()
		UIFrame.__init__(self, root=self.root, name=name, **kwargs)

	def MainLoop(self):
		self.root.mainloop()

#http://effbot.org/tkinterbook/label.htm
class UILabel(UIElement, M_Text):
	def __init__(self, text='', name=None, **kwargs):
		UIElement.__init__(self, name=name)
		M_Text.__init__(self, text)
		kwargs.pop("textvariable", None) #we use our own textvariable
		self.kwargs = kwargs
	
	def _Place(self, frame, push=TOP, **kwargs):
		kwargs.pop("textvariable", None) #we use our own textvariable
		self.kwargs.update(kwargs)
		self.label = Label(frame, textvariable=self.text, **self.kwargs)
		self.side = push
		self.label.pack(side=push)
		
	def _Show(self):
		self.label.pack(side=self.side)

	def _Hide(self):
		self.label.pack_forget()

	def __str__(self):
		return "Label: " + self.text.get() #because self.text is StringVar not string

# http://effbot.org/tkinterbook/canvas.htm
class UIImage(UIElement):
	def __init__(self, path, name=None, **kwargs):
		UIElement.__init__(self, name=name)
		self.kwargs = kwargs
		self.path = path
		self.photo = PhotoImage(file=path)

	def _Place(self, frame, push=TOP, **kwargs):
		self.kwargs.update(kwargs)
		self.image = Canvas(master=frame, width=self.photo.width(), height=self.photo.height(), **self.kwargs)
		self.side = push
		self.image.pack(side=push)
		self.imageID = self.image.create_image(0, 0, image=self.photo, anchor=NW)

	def _Show(self):
		self.image.pack(side=self.side)

	def _Hide(self):
		self.image.pack_forget()

	def __str__(self):
		return "Image: " + self.path
		
#http://effbot.org/tkinterbook/button.htm
class UIButton(UIElement, M_Text):
	def __init__(self, action, data=None, text='', name=None, **kwargs):
		UIElement.__init__(self, name=name)
		M_Text.__init__(self, text)
		self.type |= ElementType.HAS_ACTION
		kwargs.pop("command", None) #action replaces command
		kwargs.pop("textvariable", None) #we use our own textvariable
		self.kwargs = kwargs
		self.action = action
		self.data = data
		
	def _PreCopy(self, action, data, text, name):
		self.newAction = self.action if action == None else action
		self.newData = self.data if action == None else data
		self.newText = self.text.get() if text == None else text
		self.newName = self.name if name == None else name

	def CopySelf(self, action=None, data=None, text=None, name=None, addToSameFrame=False, **override_args):
		self._PreCopy(self, action, data, text, name)
		myCopy = UIButton(self.newAction, data=self.newData, text=self.newText, name=self.newName, **self.kwargs)
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
		self.side = push
		self.button.pack(side=push)

	def _Show(self):
		self.button.pack(side=self.side)

	def _Hide(self):
		self.button.pack_forget()

	def _Command(self):
		self.action(self.data)
		
	def __str__(self):
		return "Button: " + self.text.get() #because self.text is StringVar not string

	def _EnterPressed(self):
			self._Command()

class UIRadioButton(UIButton):
	def __init__(self, action, data=None, text='', name=None, **kwargs):
		UIButton.__init__(self, action=action, data=data, text=text, name=name, **kwargs)

	def CopySelf(self, action=None, data=None, text=None, name=None, addToSameFrame=False, **override_args):
		self._PreCopy(action, data, text, name)
		myCopy = UIRadioButton(action=self.newAction, data=self.newData, text=self.newText, name=self.newName, **self.kwargs)
		override_args.pop("command", None)  # action replaces command
		override_args.pop("textvariable", None)  # we use our own textvariable
		myCopy.kwargs.update(override_args)
		if addToSameFrame:
			self.owner.Add(myCopy, self.side)
		return myCopy

	def _Place(self, frame, push=TOP, **kwargs):
		kwargs.pop("command", None)  # action replaces command
		kwargs.pop("textvariable", None)  # we use our own textvariable
		self.kwargs.update(kwargs)
		if not hasattr(frame, "radioVar"):
			frame.radioVar = IntVar()
			frame.radioIndex = 1
		else:
			frame.radioIndex += 1
		self.myIndex = frame.radioIndex
		self.button = Radiobutton(frame, command=self._Command, textvariable=self.text,
									variable=frame.radioVar, value=frame.radioIndex, **self.kwargs)
		self.side = push
		self.button.pack(side=push, anchor=W)

	def _Show(self):
		self.button.pack(side=self.side, anchor=W)

	def _Hide(self):
		self.button.pack_forget()

	def _Command(self):
		if self.action != None:
			self.action(self.data, self.myIndex)

	def __str__(self):
		return "Radio Button: " + self.text.get()  # because self.text is StringVar not string

	def _EnterPressed(self):
			pass

class UIButtonPair(UIElement):
	def __init__(self, name=None, **kwargs):
		UIElement.__init__(self, name=name)
		self.type = ElementType.NONE
		kwargs.pop("root", None)
		self.kwargs = kwargs

	def Button1Action(self, data):
		pass

	def Button1Text(self):
		return ""

	def Button2Action(self, data):
		pass

	def Button2Text(self):
		return ""

	def _Place(self, frame, push=TOP, **kwargs):
		kwargs.pop("root", None)
		self.kwargs.update(kwargs)
		self.frame = UIFrame(**kwargs)
		self.frame._Place(frame, push=push, **kwargs)

		self.button1 = UIButton(action=self.Button1Action, text=self.Button1Text())
		self.button2 = UIButton(action=self.Button2Action, text=self.Button2Text())

		self.frame.Add(self.button1, side=LEFT)
		self.frame.Add(self.button2, side=LEFT)

	def _Show(self):
		self.frame._Show()

	def _Hide(self):
		self.frame._Hide()

	def __str__(self):
		return str(self.frame)

class UIOkCancel(UIButtonPair):
	def __init__(self, action, data=None, name=None, **kwargs):
		self.action = action
		self.data = data
		self.hideElement = hideElement
		kwargs.pop("action", None)
		kwargs.pop("data", None)
		UIButtonPair.__init__(self, name=name, **kwargs)

	def Button1Action(self, data):
		self.action(self.data)
		if self.hideElement != None:
			self.hideElement._Hide()
		else:
			self._Hide()

	def Button1Text(self):
		return "OK"

	def Button2Action(self, data):
		if self.hideElement != None:
			self.hideElement._Hide()
		else:
			self._Hide()

	def Button2Text(self):
		return "Cancel"

def _ElementLogWrapper(cls, func):
	def wrapper(*args, **kwargs):
		print("Created " + cls.__name__)
		return_value = func(*args, **kwargs)
		return return_value
	return wrapper

_ElementLoggingOn = False
def TurnOnElementCreationLogging():
	global _ElementLoggingOn
	if not _ElementLoggingOn:
		UIFrame.__init__ = _ElementLogWrapper(UIFrame, UIFrame.__init__)
		UILabel.__init__ = _ElementLogWrapper(UILabel, UILabel.__init__)
		UIButton.__init__ = _ElementLogWrapper(UIButton, UIButton.__init__)
		_ElementLoggingOn = True
