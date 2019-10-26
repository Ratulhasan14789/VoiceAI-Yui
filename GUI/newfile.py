#    

from kivy.app import App

from kivy.uix.button import Button

class FirstKivy(App):
    
    def build(self):
        
        return Button(text="Welcome to LikeGeeks!",background_color=(0,2,21,1))
    
#FirstKivy().run

from kivy.uix.button import Button

from kivy.app import App

from functools import partial

class KivyButton(App):

    def disable(self, instance, *args):

        instance.disabled = True

    def update(self, instance, *args):
        global x
        x=0
        x+=1
        instance.text = "I am Disabled!"+str(x)
        instance.background_color=(0,2,21,1)
    def build(self):

        mybtn = Button(text="Click me to disable")

        mybtn.bind(on_press=partial(self.disable, mybtn))

        mybtn.bind(on_press=partial(self.update, mybtn))

        return mybtn



#KivyButton().run()

class KivyButton(App):

    def build(self):

        return Button(text="Welcome to LikeGeeks!", pos=(150,280), size_hint = (.55, .9))

#KivyButton().run()

from kivy.app import App

from kivy.uix.boxlayout import BoxLayout

from kivy.lang import Builder

Builder.load_string("""

<KivyButton>:

    Button:

        text: "Hello Button!"

        size_hint: .12, .12

        Image:

            source: 'images.jpg'

            center_x: self.parent.center_x

            center_y: self.parent.center_y  
    
""")

class KivyButton(App, BoxLayout):
    
    def build(self):
        
        return self
    
#KivyButton().run()

from kivy.app import App

from kivy.uix.recycleview import RecycleView

from kivy.lang import Builder

Builder.load_string('''

<ExampleRV>:

    viewclass: 'Button'
    
    RecycleBoxLayout:
    
        size_hint_y: None
        
        height: self.minimum_height
        
        orientation: 'vertical'
        
''')

class ExampleRV(RecycleView):

    def __init__(self, **kwargs):

        super(ExampleRV, self).__init__(**kwargs)

        self.data = [{'text': str(x)} for x in range(20)]

class RecycleApp(App):

    def build(self):

        return ExampleRV()

#RecycleApp().run()

from kivy.base import runTouchApp

from kivy.lang import Builder

root = Builder.load_string(r'''

ScrollView:

    Label:
    
        text: 'Scrollview Example' * 100
        
        font_size: 30
        
        size_hint_x: 1.0
        
        size_hint_y: None
        
        text_size: self.width, None
        
        height: self.texture_size[1]
        
''')

#runTouchApp(root)

from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput


class LoginScreen(GridLayout):

    def __init__(self, **kwargs):
        super(LoginScreen, self).__init__(**kwargs)
        self.cols = 2
        self.add_widget(Label(text='User Name'))
        self.username = TextInput(multiline=False)
        self.add_widget(self.username)
        self.add_widget(Label(text='password'))
        self.password = TextInput(password=True, multiline=False)
        self.add_widget(self.password)


class MyApp(App):

    def build(self):
        return LoginScreen()


#MyApp().run()

