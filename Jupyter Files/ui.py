from tkinter import *  # @UnusedWildImport
import math


class UIElement:
	def __init__(self, name=None):
		self.name = name


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
		else:
			self.index = len(self.frame) - 1

	def __iter__(self):
		return self

	def __next__(self):
		if self.index >= len(self.frame) or self.index < 0:
			raise StopIteration
		index = self.index
		if self.forward:
			self.index += 1
		else:
			self.index -= 1
		return self.frame[index]


class UIFrame(UIElement):
	def __init__(self, root=None, name=None, **kwargs):
		UIElement.__init__(self, name=name)
		self.kwargs = kwargs
		self.list = []
		if (root != None):
			self.root = root
			self._Place(root)

	def _Place(self, frame, push=TOP, **kwargs):
		self.kwargs.update(kwargs)
		self.frame = Frame(frame, bd=4, relief=SUNKEN)
		self.frame.pack(side=push)

	def Add(self, uiElement, side=TOP, **kwargs):
		uiElement._Place(self.frame, push=side, **kwargs)
		self.list.append(uiElement)
		uiElement.owner = self

	# check only current frame and members and returns a list
	def FindFrameElementsByName(self, name):
		return [uiEl for uiEl in self.list if uiEl.name == name]

	# recursively check and returns a list
	def FindElementsByName(self, name):
		lst = []
		for i in self.list:
			if name == i.name:
				lst.append(i)
			if isinstance(i, UIFrame):
				uiElements = i.FindFrameElementsByName(name)
				lst.extend(uiElements)
		return lst

	# generator style
	def FindEachElementByName(self, name):
		for i in self.list:
			if i.name == name:
				yield i
			if isinstance(i, Frame):
				yield from i.FindEachElementByName(name)  # this will return each element rather than the whole list

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
		print("used iterator")
		return I_Frame(self)

	def __reversed__(self):
		return I_Frame(self, False)


class UILabel(UIElement, M_Text):
	def __init__(self, text='', name=None, **kwargs):
		UIElement.__init__(self, name=name)
		M_Text.__init__(self, text)
		kwargs.pop("textvariable", None)
		self.kwargs = kwargs

	def _Place(self, frame, push=TOP, **kwargs):
		kwargs.pop("textvariable", None)
		self.kwargs.update(kwargs)
		self.label = Label(frame, textvariable=self.text, **self.kwargs)
		self.label.pack(side=push)

	def __str__(self):
		return "Label: " + self.text.get()


class UIButton(UIElement, M_Text):
	def __init__(self, action, data=None, text='', name=None, **kwargs):
		UIElement.__init__(self, name=name)
		M_Text.__init__(self, text)
		kwargs.pop("textvariable", None)
		kwargs.pop("command", None)
		self.action = action
		self.data = data
		self.kwargs = kwargs

	def _Place(self, frame, push=TOP, **kwargs):
		kwargs.pop("textvariable", None)
		kwargs.pop("command", None)
		self.kwargs.update(kwargs)
		self.button = Button(frame, textvariable=self.text, command=self._Command)
		self.button.pack(side=push)

	def _Command(self):
		self.action(self.data)

	def __str__(self):
		return "Button: " + self.text.get()
