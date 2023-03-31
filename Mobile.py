from kivy.lang import Builder
from kivy.properties import ObjectProperty

from kivymd.app import MDApp
from kivymd.uix.scrollview import MDScrollView

from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ListProperty, StringProperty

from Logic import objectF

KV = '''
<ContentNavigationDrawer>

    MDList:

        OneLineListItem:
            text: "Дневник"
            on_press:
                root.nav_drawer.set_state("close")
                root.screen_manager.current = "Dnevnik"

        OneLineListItem:
            text: "Успеваемость"
            on_press:
                root.nav_drawer.set_state("close")
                root.screen_manager.current = "Grade"

        OneLineListItem:
            text: "Выйти"
            on_press:
                root.nav_drawer.set_state("close")
                root.screen_manager.current = "Exit"



MDScreen:

    MDTopAppBar:
        pos_hint: {"top": 1}
        elevation: 4
        left_action_items: [["Logo.png", lambda x: nav_drawer.set_state("open")]]
        shadow_color: "brown"

    MDNavigationLayout:

        MDScreenManager:
            id: screen_manager

            MDScreen:
                name: "Dnevnik"

                MDLabel:
                    id: LabelDnevnik
                    text: app.fulldate
                    halign: "center"

            MDScreen:
                name: "Grade"

                MDLabel:
                    text: "Успеваемость"
                    halign: "center"

            MDScreen:
                name: "Exit"

                MDLabel:
                    text: "Выйти"
                    halign: "center"


        MDNavigationDrawer:
            id: nav_drawer
            radius: (0, 16, 16, 0)

            ContentNavigationDrawer:
                screen_manager: screen_manager
                nav_drawer: nav_drawer
'''


class ContentNavigationDrawer(MDScrollView):
    screen_manager = ObjectProperty()
    nav_drawer = ObjectProperty()
    


class Example(MDApp):
    fulldate = StringProperty()
    def build(self):
        self.fulldate = objectF.M + objectF.Tu
        self.theme_cls.primary_palette = "Red"
        self.theme_cls.theme_style = "Dark"
        return Builder.load_string(KV)


Example().run()