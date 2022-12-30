"""
This program demonstrates a GUI interface.
"""

from breezypythongui import EasyFrame

class helloWorldGUI(EasyFrame):
    #__init__ method definition
    def __init__(self):
        EasyFrame.__init__(self)
        self.addLabel(text = "Hello, World!", row = 0, column = 0)

def main():
    helloWorldGUI().mainloop()

if __name__ == "__main__":
    main()
