from aqt import mw
from aqt.qt import QAction

from .hooks import update_gui_hooks


def preference_menu():
    addon_menu = mw.form.menuTools.addMenu("Disable autoplay in webview")

    config = mw.addonManager.getConfig(__name__)
    for label, key in [
        ("Disable autoplay in editor", "disable_autoplay_in_editor"),
        ("Disable autoplay in browser", "disable_autoplay_in_browser")
    ]:
        action = QAction(label, mw)
        action.setCheckable(True)
        action.setChecked(config[key])
        action.triggered.connect(lambda toggled_value, k=key: update_config(k, toggled_value))
        addon_menu.addAction(action)


def update_config(key: str, value: bool):
    config = mw.addonManager.getConfig(__name__)
    config[key] = value
    mw.addonManager.writeConfig(__name__, config)

    update_gui_hooks(config)
