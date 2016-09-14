from kivy.app import App
from kivy.factory import Factory
from kivy.properties import ObjectProperty
from kivy.lang import Builder

from electrum_arg.bitcoin import RECOMMENDED_FEE
from electrum_arg_gui.kivy.i18n import _

Builder.load_string('''
<FeeDialog@Popup>
    id: popup
    title: _('Transaction Fees')
    size_hint: 0.8, 0.8
    pos_hint: {'top':0.9}
    BoxLayout:
        orientation: 'vertical'
        BoxLayout:
            orientation: 'horizontal'
            size_hint: 1, 0.5
            Label:
                id: fee_per_kb
                text: ''
        BoxLayout:
            orientation: 'horizontal'
            size_hint: 1, 0.5
            Label:
                text: _('Recommended Fee')
            CheckBox:
                id: RECOMMENDED_FEE
                on_active: root.on_checkbox(self.active)
        Widget:
            size_hint: 1, 1
        BoxLayout:
            orientation: 'horizontal'
            size_hint: 1, 0.5
            Button:
                text: 'Cancel'
                size_hint: 0.5, None
                height: '48dp'
                on_release: popup.dismiss()
            Button:
                text: 'OK'
                size_hint: 0.5, None
                height: '48dp'
                on_release:
                    root.on_ok()
                    root.dismiss()
''')

class FeeDialog(Factory.Popup):

    def __init__(self, app, config, callback):
        Factory.Popup.__init__(self)
        self.app = app
        self.config = config
        self.callback = callback
        self.update_text()

    def update_text(self):
        value = int(self.get_fee_text(value))
        self.ids.fee_per_kb.text = self.get_fee_text(value)

    def get_fee_text(self, value):
        return self.app.format_amount_and_units(value) + '/kB'

    def on_ok(self):
        value = int(self.config.set_key('fee_per_kb', value)
        self.callback()

    def on_checkbox(self, b):
        self.update_text()
