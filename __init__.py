from aqt import mw

from .hooks import update_gui_hooks
from .preference import preference_menu


def run():
    config = mw.addonManager.getConfig(__name__)

    update_gui_hooks(config)

    preference_menu()


run()
