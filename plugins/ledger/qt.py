import threading

from PyQt4.Qt import (QDialog, QInputDialog, QLineEdit,
                      QVBoxLayout, QLabel, SIGNAL)
import PyQt4.QtCore as QtCore

from electrum_arg.i18n import _
from .ledger import LedgerPlugin, BTChipWallet
from ..hw_wallet.qt import QtHandlerBase, QtPluginBase
from electrum_arg_gui.qt.util import *
from electrum_arg.plugins import hook

class Plugin(LedgerPlugin):

    @hook
    def load_wallet(self, wallet, window):
        if type(wallet) != BTChipWallet:
            return
        wallet.handler = BTChipQTHandler(window)
        if self.btchip_is_connected(wallet):
            if not wallet.check_proper_device():
                window.show_error(_("This wallet does not match your Ledger device"))
                wallet.force_watching_only = True
        else:
            window.show_error(_("Ledger device not detected.\nContinuing in watching-only mode."))
            wallet.force_watching_only = True


class Plugin(LedgerPlugin, QtPluginBase):
    icon_unpaired = ":icons/ledger_unpaired.png"
    icon_paired = ":icons/ledger.png"

    def create_handler(self, window):
        return Ledger_Handler(window)


class Ledger_Handler(QtHandlerBase):

    def __init__(self, win):
        super(Ledger_Handler, self).__init__(win, 'Ledger')

    def word_dialog(self, msg):
        response = QInputDialog.getText(self.top_level_window(), "Ledger Wallet Authentication", msg, QLineEdit.Password)
        if not response[1]:
            self.word = None
        else:
            self.word = str(response[0])
        self.done.set()
