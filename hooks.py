from anki.config import Config
from aqt import gui_hooks
from aqt.browser import Browser
from aqt.editor import EditorWebView


def update_gui_hooks(config: Config):
    update_hook(
        config["disable_autoplay_in_editor"],
        gui_hooks.editor_web_view_did_init,
        disable_autoplay_in_editor,
        enable_autoplay_in_editor
    )
    update_hook(
        config["disable_autoplay_in_browser"],
        gui_hooks.browser_will_show,
        disable_autoplay_in_browser,
        enable_autoplay_in_browser
    )


def update_hook(is_disabled: bool, hook, disable_func, enable_func):
    if is_disabled:
        hook.remove(enable_func)
        hook.append(disable_func)
    else:
        hook.remove(disable_func)
        hook.append(enable_func)


def disable_autoplay_in_editor(editor_web_view: EditorWebView) -> None:
    editor_web_view.setPlaybackRequiresGesture(True)


def enable_autoplay_in_editor(editor_web_view: EditorWebView) -> None:
    editor_web_view.setPlaybackRequiresGesture(False)


def disable_autoplay_in_browser(browser: Browser) -> None:
    browser.editor.web.setPlaybackRequiresGesture(True)


def enable_autoplay_in_browser(browser: Browser) -> None:
    browser.editor.web.setPlaybackRequiresGesture(False)
