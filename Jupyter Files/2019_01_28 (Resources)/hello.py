
from tkinter import *

def say_hi():
	print("hi there, everyone!")

def main():
	root = Tk()

	frame = Frame(root)
	frame.pack()

	button = Button(frame, text="QUIT", fg="red", command=frame.quit)
	button.pack(side=LEFT)

	hi_there = Button(frame, text="Hello", command=say_hi)
	hi_there.pack(side=LEFT)

	root.mainloop()

if __name__ == "__main__": # only run when not called via 'import' here
	print(sys.argv[1])
	main()