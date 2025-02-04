from aqt import gui_hooks
from aqt.browser import Browser


def on_editor_web_view_init(editor_web_view):
    editor_web_view.setPlaybackRequiresGesture(True)

def set_browser_webview_gesture(browser: Browser):
    browser.editor.web.setPlaybackRequiresGesture(True)

gui_hooks.editor_web_view_did_init.append(on_editor_web_view_init)
gui_hooks.browser_will_show.append(set_browser_webview_gesture)

