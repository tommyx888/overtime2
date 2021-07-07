
from kivy.lang import Builder
#from kivy.core.window import Window

#Window.size = (300, 500)
from kivy.properties import StringProperty, ObjectProperty, ListProperty
from kivy.uix.boxlayout import BoxLayout
from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.theming import ThemableBehavior
from kivymd.uix.label import MDLabel
from kivymd.uix.list import OneLineIconListItem, MDList


import json

from kivymd.uix.behaviors import MagicBehavior
from kivymd.uix.button import MDFlatButton, MDRaisedButton
from kivymd.uix.dialog import MDDialog
import requests
from kivymd.uix.textfield import MDTextField

help_str = '''
ScreenManager:

    LoginScreen:
    WrongScreen:
    MainScreen:
    MainScreen2:
    SignupScreen:

<LoginScreen>:
    name:'loginscreen'
    canvas.before:
        Rectangle:
            pos: self.pos
            size: self.size
            source: 'pozadielogin.png'

    MDTextField:

        id:login_email
        pos_hint: {'center_y':0.77,'center_x':0.4}
        size_hint : (0.5,0.1)
        hint_text: 'Email'
        helper_text:'Required'
        helper_text_mode:  'on_error'
        icon_right: 'account'
        icon_right_color: app.theme_cls.primary_color
        required: True
        mode: "rectangle"
    MDTextField:
        id:login_password
        pos_hint: {'center_y':0.67,'center_x':0.4}
        size_hint : (0.5,0.1)
        hint_text: 'Password'
        helper_text:'Required'
        helper_text_mode:  'on_error'
        icon_right: 'eye'
        icon_right_color: app.theme_cls.primary_color
        required: True
        mode: "rectangle"
    MDTextField:
        id:login_accounttype
        pos_hint: {'center_y':0.57,'center_x':0.4}
        size_hint : (0.5,0.1)
        hint_text: 'account_type'
        helper_text:'account_type'
        helper_text_mode:  'on_error'
        icon_right: 'account-box'
        icon_right_color: app.theme_cls.primary_color
        required: True
        mode: "rectangle"

    MagicButton:
        text:'Login'
        size_hint: (0.13,0.07)
        pos_hint: {'center_x':0.5,'center_y':0.2}


        on_press:
            app.login()
            app.show_data()

    MDIconButton:

        icon: "language-python" 
        pos_hint: {'center_x':0.6,'center_y':0.4}
        user_font_size: "64sp"
        on_press:
            app.login()
            app.show_data()

<SignupScreen>:
    name:'signupscreen'
    MDLabel:
        text:'Signup'
        font_style:'H2'
        halign:'center'
        pos_hint: {'center_y':0.9}
    MDTextField:
        id:signup_email
        pos_hint: {'center_y':0.6,'center_x':0.5}
        size_hint : (0.7,0.1)
        hint_text: 'Email'
        helper_text:'Required'
        helper_text_mode:  'on_error'
        icon_right: 'account'
        icon_right_color: app.theme_cls.primary_color
        required: True
        mode: "rectangle"
    MDTextField:
        id:signup_username
        pos_hint: {'center_y':0.75,'center_x':0.5}
        size_hint : (0.7,0.1)
        hint_text: 'Username'
        helper_text:'Required'
        helper_text_mode:  'on_error'
        icon_right: 'account'
        icon_right_color: app.theme_cls.primary_color
        required: True
    MDTextField:
        id:signup_password
        pos_hint: {'center_y':0.4,'center_x':0.5}
        size_hint : (0.7,0.1)
        hint_text: 'Password'
        helper_text:'Required'
        helper_text_mode:  'on_error'
        icon_right: 'account'
        icon_right_color: app.theme_cls.primary_color
        required: True
        mode: "rectangle"
    MDRaisedButton:
        text:'Signup'
        size_hint: (0.13,0.07)
        pos_hint: {'center_x':0.5,'center_y':0.2}
        on_press: app.signup()

<WrongScreen>:
    name: 'wrongscreen'
    MDLabel:
        id:username_info
        text:'Wrong login inputs'
        font_style:'H1'
        halign:'center'
    MDTextButton:
        text: 'Back to login'
        pos_hint: {'center_x':0.5,'center_y':0.1}
        on_press:
            root.manager.current = 'loginscreen'
            root.manager.transition.direction = 'down'



<MainScreen>:
    name: 'mainscreen'
    Screen:

    MDNavigationLayout:

        ScreenManager:

            Screen:

                BoxLayout:
                    orientation: 'vertical'

                    MDToolbar:
                        title: "Navigation Drawer"
                        elevation: 10
                        left_action_items: [['menu', lambda x: nav_drawer.set_state("open")]]

                    Widget:


        MDNavigationDrawer:
            id: nav_drawer

            ContentNavigationDrawer:   
                orientation: "vertical"
                padding: "8dp"
                spacing: "8dp"

                AnchorLayout:
                    anchor_x: "left"
                    size_hint_y: None
                    height: avatar.height

                    Image:
                        id: avatar
                        size_hint: None, None
                        size: "56dp", "56dp"
                        source: "kivymd.png"

                MDLabel:
                    text: "KivyMD library"
                    font_style: "Button"
                    size_hint_y: None
                    height: self.texture_size[1]

                MDLabel:
                    text: "kivydevelopment@gmail.com"
                    font_style: "Caption"
                    size_hint_y: None
                    height: self.texture_size[1]

                ScrollView:
                    DrawerList:
                        id: md_list

                        MDList:
                            OneLineIconListItem:
                                text: "Profile"

                                IconLeftWidget:
                                    icon: "face-profile"



                            OneLineIconListItem:
                                text: "Upload"

                                IconLeftWidget:
                                    icon: "upload"


                            OneLineIconListItem:
                                text: "Logout"
                                on_press:
                                    root.manager.current = 'loginscreen'
                                    root.manager.transition.direction = 'down'
                                IconLeftWidget:
                                    icon: "logout"
                                    on_press:
                                        root.manager.current = 'loginscreen'
                                        root.manager.transition.direction = 'down'



<MainScreen2>:
    name: 'mainscreen2'
    MDLabel:
        id: labeltext
        text: root.labeltext
        font_style:'H1'
        halign:'center'
    MDTextButton:
        text: 'Back to login'
        pos_hint: {'center_x':0.5,'center_y':0.1}
        on_press:
            root.manager.current = 'loginscreen'
            root.manager.transition.direction = 'down'
'''

class ContentNavigationDrawer(BoxLayout):
    pass

class DrawerList(ThemableBehavior, MDList):
    pass


class MainScreen(Screen):
    labeltext = StringProperty('My label')
    screen_manager = ObjectProperty()
    nav_drawer = ObjectProperty()

    pass

class MainScreen2(Screen):
    labeltext = StringProperty('My label')

    pass

class WrongScreen(Screen):
    pass


class LoginScreen(Screen):
    pass


class SignupScreen(Screen):
    pass


class MagicButton(MagicBehavior, MDRaisedButton):
    pass

sm = ScreenManager()


sm.add_widget(MainScreen(name='mainscreen'))
sm.add_widget(MainScreen2(name='mainscreen2'))
sm.add_widget(LoginScreen(name='loginscreen'))
sm.add_widget(SignupScreen(name='signupscreen'))
sm.add_widget(SignupScreen(name='wrongscreen'))

class LoginApp(MDApp):
    def build(self):
        self.strng = Builder.load_string(help_str)
        self.url = "https://overtime-app-fcbd6-default-rtdb.europe-west1.firebasedatabase.app/.json"
        return self.strng



    auth = 'L5sBSuh5APwQwRowKBesp7HhJ0J0RXctgUqtdu5T'

    def login(self):
        loginEmail = self.strng.get_screen('loginscreen').ids.login_email.text
        loginPassword = self.strng.get_screen('loginscreen').ids.login_password.text
        loginaccounttype = self.strng.get_screen('loginscreen').ids.login_accounttype.text
        self.username = "meno"

        self.login_check = False
        supported_loginEmail = loginEmail.replace('.', '-')
        supported_loginPassword = loginPassword.replace('.', '-')
        supported_loginaccounttype = loginaccounttype.replace('.', '-')
        self.username = "meno"

        request = requests.get(self.url + '?auth=' + self.auth)
        data = request.json()
        emails = set()
        for key, value in data.items():
            emails.add(key)
        if supported_loginEmail in emails and supported_loginPassword == data[supported_loginEmail]['Password'] and supported_loginaccounttype == data[supported_loginEmail]['accounttype']:
            self.username = data[supported_loginEmail]['Username']
            self.login_check = True
            if data[supported_loginEmail]['accounttype'] == "majster" :
                self.strng.get_screen('mainscreen').manager.current = 'mainscreen'
                print("supervisor account")
            else:
                self.strng.get_screen('mainscreen2').manager.current = 'mainscreen2'
                print("operator account")
        else:
            self.strng.get_screen('wrongscreen').manager.current = 'wrongscreen'

    def close_username_dialog(self, obj):
        self.dialog.dismiss()

    def show_data(self):
        self.strng.get_screen('mainscreen').labeltext = self.username
        self.strng.get_screen('mainscreen2').labeltext = self.username

    def on_start(self):
        pass



LoginApp().run()