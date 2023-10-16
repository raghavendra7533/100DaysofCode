## Window
Like the `screen` in `turtle` we have to initialise `window` in Tkinter.

## Title
Title can be initialised by using `window.title("Hello")`

## Window Sizes
The minimum size can be defined by using `window.minsize(width, height)`

## Label
- A label can be created by initialising using `my_label = tkinter.Label(text = "I am a Label")`
- Arguments that can be passed when initialising the Label is
	1. Text - String
	2. Font - Tuple (font, font-size, font-formatting)
- Label is a `**kwargs` methods

## Pack
- To initialise the will make the initialised objects *like the Label* appear. It is a "geometry-management mechanism". Geometry managers are used to specify the relative positioning of widgets within their container.
- Packer options:
	1. Anchor
	2. fill
	3. expand
	4. `ipadx` and `ipady` - A distance designating internal padding on each side of the slave widget.
	5. `padx` and `pady` - A distance designating external padding on each side of the slave widget.
	6. side - Legal values are 'left', 'right', 'top', 'bottom'.

## 
