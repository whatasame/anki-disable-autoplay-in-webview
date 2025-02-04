from aqt import gui_hooks

def on_editor_web_view_init(editor_web_view):
    editor_web_view.setPlaybackRequiresGesture(True)

gui_hooks.editor_web_view_did_init.append(on_editor_web_view_init)

