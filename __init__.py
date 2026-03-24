# import the main window object (mw) from aqt
# this should work with Version ⁨25.02.7 (1b882285)⁩
import aqt
import aqt.editor
import aqt.gui_hooks
from PyQt6.QtWidgets import QApplication

def editor_loaded_note(editor: aqt.editor.Editor):
    config = aqt.mw.addonManager.getConfig(__name__)
    
    note_type_name = editor.note.note_type()['name']
    
    if note_type_name in config:
        field_name = config[note_type_name]
        if field_name in editor.note:
            field_data = editor.note[field_name]
            clipboard = QApplication.clipboard()
            clipboard.setText(field_data)

aqt.gui_hooks.editor_did_load_note.append(editor_loaded_note)
