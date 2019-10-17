from abc import ABC, abstractmethod

class UIControl(ABC):
    @abstractmethod
    def draw(self):
        print('UIControl')


class DropDownList(UIControl):
    def draw(self):
        print('Dropdown')


class TextBox(UIControl):
    def draw(self):
        print('Textbox')


def draw(controls):
    for control in controls:
        control.draw()


ddl = DropDownList()
txt = TextBox()
# print(isinstance(ddl, UIControl)) # True
draw([ddl, txt])