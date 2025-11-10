from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.list import OneLineListItem
from kivymd.uix.textfield import MDTextField
from kivymd.uix.button import MDIconButton


class TodoLayout(MDBoxLayout):
    def add_task(self):
        task_text = self.ids.task_input.text.strip()
        if task_text:
            self.ids.task_list.add_widget(
                OneLineListItem(text=task_text, on_release=self.remove_task)
            )
            self.ids.task_input.text = ""

    def remove_task(self, instance):
        self.ids.task_list.remove_widget(instance)


class TodoApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette = "Blue"
        return TodoLayout()


if __name__ == "__main__":
    TodoApp().run()