# -*- coding: utf-8 -*-
import os
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.core.text import LabelBase

# 获取当前脚本所在的目录
current_dir = os.path.dirname(os.path.abspath(__file__))
font_path = os.path.join(current_dir, 'NotoSansCJK-Regular.otf')

# 检查字体文件是否存在
if not os.path.exists(font_path):
    raise FileNotFoundError(f"字体文件未找到: {font_path}")

# 注册中文字体
LabelBase.register(name='ChineseFont', fn_regular=font_path)

class MyApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical', padding=20, spacing=10)

        self.label = Label(
            text='欢迎使用我的第一个安卓App！',
            font_name='ChineseFont',
            font_size='20sp'
        )

        btn = Button(
            text='点击我',
            size_hint=(1, 0.3),
            font_name='ChineseFont'
        )
        btn.bind(on_press=self.on_button_press)

        layout.add_widget(self.label)
        layout.add_widget(btn)
        return layout

    def on_button_press(self, instance):
        self.label.text = '你点击了按钮！中文显示正常 '

if __name__ == '__main__':
    MyApp().run()