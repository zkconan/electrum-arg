from kivy.app import App
from kivy.factory import Factory
from kivy.properties import ObjectProperty
from kivy.lang import Builder

from electrum_arg.bitcoin import RECOMMENDED_FEE
from electrum_arg_gui.kivy.i18n import _

Builder.load_string('''
<BumpFeeDialog@Popup>
    title: _('Bump fee')
    size_hint: 0.8, 0.8
    pos_hint: {'top':0.9}
    BoxLayout:
        orientation: 'vertical'
        padding: '10dp'

        GridLayout:
            height: self.minimum_height
            size_hint_y: None
            cols: 1
            spacing: '10dp'
            BoxLabel:
                id: old_fee
                text: _('Current Fee')
                value: ''
            BoxLabel:
                id: new_fee
                text: _('New Fee')
                value: ''
        Label:
            id: tooltip
            text: ''
            size_hint_y: None
        BoxLayout:
            orientation: 'horizontal'
            size_hint: 1, 0.2
            Label:
                text: _('Final')
            CheckBox:
                id: final_cb
        Widget:
            size_hint: 1, 1
        BoxLayout:
            orientation: 'horizontal'
            size_hint: 1, 0.5
            Button:
                text: 'Cancel'
                size_hint: 0.5, None
                height: '48dp'
                on_release: root.dismiss()
            Button:
                text: 'OK'
                size_hint: 0.5, None
                height: '48dp'
                on_release:
                    root.dismiss()
                    root.on_ok()
''')

class BumpFeeDialog(Factory.Popup):

    def __init__(self, app, fee, size, callback):
        Factory.Popup.__init__(self)
        self.app = app
        self.init_fee = fee
        self.tx_size = size
        self.callback = callback
        self.config = app.electrum_config
        self.ids.old_fee.value = self.app.format_amount_and_units(self.init_fee)
        self.update_text()

    def update_text(self):
        value = int(value*self.tx_size/1000)
        self.ids.new_fee.value = self.app.format_amount_and_units(self.get_fee())

    def get_fee(self):
        return value*self.tx_size/1000

    def on_ok(self):
        new_fee = self.get_fee()
        is_final = self.ids.final_cb.active
        self.callback(self.init_fee, new_fee, is_final)

    def on_slider(self, value):
        self.update_text()

    def on_checkbox(self, b):
        self.update_text()
