# memo

```python
import PySimpleGUIWeb as sg
print(dir(sg))
print(sg.theme_list())
```

## `print(dir(sg))`

```
['AddMenuItem', 'AddToReturnDictionary', 'AddToReturnList', 'B', 'BLUES', 'BROWSE_FILES_DELIMITER', 'BUTTON_TYPE_BROWSE_FILE', 'BUTTON_TYPE_BROWSE_FILES', 'BUTTON_TYPE_BROWSE_FOLDER', 'BUTTON_TYPE_CALENDAR_CHOOSER', 'BUTTON_TYPE_CLOSES_WIN', 'BUTTON_TYPE_CLOSES_WIN_ONLY', 'BUTTON_TYPE_COLOR_CHOOSER', 'BUTTON_TYPE_READ_FORM', 'BUTTON_TYPE_REALTIME', 'BUTTON_TYPE_SAVEAS_FILE', 'Btn', 'BuildResults', 'BuildResultsForSubform', 'Butt', 'Button', 'CB', 'CBox', 'CButton', 'CLASSframe', 'COLOR_SYSTEM_DEFAULT', 'CURRENT_LOOK_AND_FEEL', 'CalendarButton', 'Cancel', 'ChangeLookAndFeel', 'Check', 'Checkbox', 'CloseButton', 'ColorChooserButton', 'Column', 'Combo', 'ConvertArgsToSingleString', 'DEFAULT_AUTOCLOSE_TIME', 'DEFAULT_AUTOSIZE_BUTTONS', 'DEFAULT_AUTOSIZE_TEXT', 'DEFAULT_BACKGROUND_COLOR', 'DEFAULT_BASE64_ICON', 'DEFAULT_BORDER_WIDTH', 'DEFAULT_BUTTON_COLOR', 'DEFAULT_BUTTON_ELEMENT_SIZE', 'DEFAULT_DEBUG_WINDOW_SIZE', 'DEFAULT_ELEMENT_BACKGROUND_COLOR', 'DEFAULT_ELEMENT_PADDING', 'DEFAULT_ELEMENT_SIZE', 'DEFAULT_ELEMENT_TEXT_COLOR', 'DEFAULT_ERROR_BUTTON_COLOR', 'DEFAULT_FONT', 'DEFAULT_FRAME_RELIEF', 'DEFAULT_INPUT_ELEMENTS_COLOR', 'DEFAULT_INPUT_TEXT_COLOR', 'DEFAULT_LISTBOX_SELECT_MODE', 'DEFAULT_MARGINS', 'DEFAULT_METER_ORIENTATION', 'DEFAULT_OUTPUT_ELEMENT_SIZE', 'DEFAULT_PIXELS_TO_CHARS_SCALING', 'DEFAULT_PIXEL_TO_CHARS_CUTOFF', 'DEFAULT_PROGRESS_BAR_BORDER_WIDTH', 'DEFAULT_PROGRESS_BAR_COLOR', 'DEFAULT_PROGRESS_BAR_COLOR_OFFICIAL', 'DEFAULT_PROGRESS_BAR_RELIEF', 'DEFAULT_PROGRESS_BAR_SIZE', 'DEFAULT_PROGRESS_BAR_STYLE', 'DEFAULT_SCROLLBAR_COLOR', 'DEFAULT_SLIDER_BORDER_WIDTH', 'DEFAULT_SLIDER_ORIENTATION', 'DEFAULT_SLIDER_RELIEF', 'DEFAULT_TABLE_SECECT_MODE', 'DEFAULT_TEXT_COLOR', 'DEFAULT_TEXT_ELEMENT_BACKGROUND_COLOR', 'DEFAULT_TEXT_JUSTIFICATION', 'DEFAULT_TOOLTIP_TIME', 'DEFAULT_WINDOW_ICON', 'DEFAULT_WINDOW_LOCATION', 'DebugWin', 'DecodeRadioRowCol', 'Down', 'Drop', 'DropDown', 'DummyButton', 'ELEM_TYPE_BLANK', 'ELEM_TYPE_BUTTON', 'ELEM_TYPE_BUTTONMENU', 'ELEM_TYPE_CANVAS', 'ELEM_TYPE_COLUMN', 'ELEM_TYPE_ERROR', 'ELEM_TYPE_FRAME', 'ELEM_TYPE_GRAPH', 'ELEM_TYPE_IMAGE', 'ELEM_TYPE_INPUT_CHECKBOX', 'ELEM_TYPE_INPUT_COMBO', 'ELEM_TYPE_INPUT_LISTBOX', 'ELEM_TYPE_INPUT_MULTILINE', 'ELEM_TYPE_INPUT_OPTION_MENU', 'ELEM_TYPE_INPUT_RADIO', 'ELEM_TYPE_INPUT_SLIDER', 'ELEM_TYPE_INPUT_SPIN', 'ELEM_TYPE_INPUT_TEXT', 'ELEM_TYPE_MENUBAR', 'ELEM_TYPE_MULTILINE_OUTPUT', 'ELEM_TYPE_OUTPUT', 'ELEM_TYPE_PROGRESS_BAR', 'ELEM_TYPE_SEPARATOR', 'ELEM_TYPE_TAB', 'ELEM_TYPE_TABLE', 'ELEM_TYPE_TAB_GROUP', 'ELEM_TYPE_TEXT', 'ELEM_TYPE_TREE', 'EVENT_TIMEOUT', 'EasyPrint', 'EasyPrintClose', 'EasyProgressMeter', 'EasyProgressMeterCancel', 'EasyProgressMeterDataClass', 'Element', 'EncodeRadioRowCol', 'ErrorElement', 'Exit', 'FileBrowse', 'FileSaveAs', 'FilesBrowse', 'FlexForm', 'FolderBrowse', 'Frame', 'GREENS', 'GetComplimentaryHex', 'Graph', 'Help', 'I', 'Image', 'In', 'InitializeResults', 'Input', 'InputCombo', 'InputOptionMenu', 'InputText', 'LISTBOX_SELECT_MODE_BROWSE', 'LISTBOX_SELECT_MODE_CONTIGUOUS', 'LISTBOX_SELECT_MODE_EXTENDED', 'LISTBOX_SELECT_MODE_MULTIPLE', 'LISTBOX_SELECT_MODE_SINGLE', 'LOOK_AND_FEEL_TABLE', 'Left', 'ListOfLookAndFeelValues', 'Listbox', 'MAX_SCROLLED_TEXT_BOX_HEIGHT', 'MENU_DISABLED_CHARACTER', 'MENU_KEY_SEPARATOR', 'MESSAGE_BOX_LINE_WIDTH', 'Menu', 'MsgBox', 'Multiline', 'MultilineOutput', 'MyWindows', 'NICE_BUTTON_COLORS', 'No', 'OFFICIAL_PYSIMPLEGUI_BUTTON_COLOR', 'OK', 'ObjToString', 'ObjToStringSingleObj', 'Ok', 'OneLineProgressMeter', 'OneLineProgressMeterCancel', 'Open', 'OptionMenu', 'Output', 'POPUP_BUTTONS_CANCELLED', 'POPUP_BUTTONS_ERROR', 'POPUP_BUTTONS_NO_BUTTONS', 'POPUP_BUTTONS_OK', 'POPUP_BUTTONS_OK_CANCEL', 'POPUP_BUTTONS_YES_NO', 'PROGRESS_BAR_STYLES', 'PURPLES', 'PackFormIntoFrame', 'Popup', 'PopupAnnoying', 'PopupAutoClose', 'PopupCancel', 'PopupError', 'PopupGetFile', 'PopupGetFolder', 'PopupGetText', 'PopupNoBorder', 'PopupNoButtons', 'PopupNoFrame', 'PopupNoTitlebar', 'PopupNoWait', 'PopupNonBlocking', 'PopupOK', 'PopupOKCancel', 'PopupQuick', 'PopupQuickMessage', 'PopupScrolled', 'PopupTimed', 'PopupYesNo', 'Print', 'PrintClose', 'ProgressBar', 'PySimpleGUIWeb', 'Queue', 'Quit', 'RButton', 'RELIEF_FLAT', 'RELIEF_GROOVE', 'RELIEF_RAISED', 'RELIEF_RIDGE', 'RELIEF_SOLID', 'RELIEF_SUNKEN', 'RGB', 'Radio', 'ReadButton', 'ReadFormButton', 'RealtimeButton', 'Right', 'SELECT_MODE_BROWSE', 'SELECT_MODE_CONTIGUOUS', 'SELECT_MODE_EXTENDED', 'SELECT_MODE_MULTIPLE', 'SELECT_MODE_SINGLE', 'Save', 'SaveAs', 'ScrolledTextBox', 'SetGlobalIcon', 'SetOptions', 'SimpleButton', 'Slider', 'Spin', 'StartupTK', 'StringIO', 'Submit', 'SuperImage', 'T', 'TABLE_SELECT_MODE_BROWSE', 'TABLE_SELECT_MODE_EXTENDED', 'TABLE_SELECT_MODE_NONE', 'TANS', 'THEME_ALT', 'THEME_CLAM', 'THEME_CLASSIC', 'THEME_DEFAULT', 'THEME_VISTA', 'THEME_WINNATIVE', 'THEME_XPNATIVE', 'TIMEOUT_EVENT', 'TIMEOUT_KEY', 'TITLE_LOCATION_BOTTOM', 'TITLE_LOCATION_BOTTOM_LEFT', 'TITLE_LOCATION_BOTTOM_RIGHT', 'TITLE_LOCATION_LEFT', 'TITLE_LOCATION_RIGHT', 'TITLE_LOCATION_TOP', 'TITLE_LOCATION_TOP_LEFT', 'TITLE_LOCATION_TOP_RIGHT', 'TRANSPARENT_BUTTON', 'Tab', 'TabGroup', 'Table', 'Text', 'ThisRow', 'TimerStart', 'TimerStop', 'Tree', 'TreeData', 'Txt', 'Up', 'VSep', 'VSeperator', 'VerticalSeparator', 'WINDOW_CLOSED', 'WIN_CLOSED', 'WRITE_ONLY_KEY', 'Window', 'YELLOWS', 'Yes', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__path__', '__spec__', 'base64', 'base64_to_style_image', 'binascii', 'calendar', 'change_look_and_feel', 'convert_tkinter_filetypes_to_wx', 'convert_tkinter_size_to_Wx', 'datetime', 'easy_print', 'easy_print_close', 'element_callback_quit_mainloop', 'eprint', 'font_parse_string', 'g_time_delta', 'g_time_end', 'g_time_start', 'get_complimentary_hex', 'list_of_look_and_feel_values', 'logging', 'main', 'mimetypes', 'name', 'obj_to_string', 'obj_to_string_single_obj', 'one_line_progress_meter', 'one_line_progress_meter_cancel', 'os', 'pickle', 'pkg_resources', 'popup', 'popup_annoying', 'popup_auto_close', 'popup_cancel', 'popup_error', 'popup_get_file', 'popup_get_folder', 'popup_get_text', 'popup_no_border', 'popup_no_buttons', 'popup_no_frame', 'popup_no_titlebar', 'popup_no_wait', 'popup_non_blocking', 'popup_ok', 'popup_ok_cancel', 'popup_quick', 'popup_quick_message', 'popup_scrolled', 'popup_timed', 'popup_yes_no', 'port', 'preview_all_look_and_feel_themes', 'print_close', 'quit_mainloop', 'randint', 'remi', 'rgb', 'scrolled_text_box', 'set_global_icon', 'set_options', 'setup_remi_window', 'sprint', 'sys', 'textwrap', 'theme', 'theme_background_color', 'theme_border_width', 'theme_button_color', 'theme_element_background_color', 'theme_element_text_color', 'theme_input_background_color', 'theme_input_text_color', 'theme_list', 'theme_previewer', 'theme_progress_bar_border_width', 'theme_progress_bar_color', 'theme_slider_border_width', 'theme_slider_color', 'theme_text_color', 'theme_text_element_background_color', 'threading', 'time', 'timer_start', 'timer_stop', 'traceback', 'version']
```

## `print(sg.theme_list())`

```
['Black', 'BlueMono', 'BluePurple', 'BrightColors', 'BrownBlue', 'Dark', 'Dark2', 'DarkAmber', 'DarkBlack', 'DarkBlack1', 'DarkBlue', 'DarkBlue1', 'DarkBlue10', 'DarkBlue11', 'DarkBlue12', 'DarkBlue13', 'DarkBlue14', 'DarkBlue15', 'DarkBlue16', 'DarkBlue17', 'DarkBlue2', 'DarkBlue3', 'DarkBlue4', 'DarkBlue5', 'DarkBlue6', 'DarkBlue7', 'DarkBlue8', 'DarkBlue9', 'DarkBrown', 'DarkBrown1', 'DarkBrown2', 'DarkBrown3', 'DarkBrown4', 'DarkBrown5', 'DarkBrown6', 'DarkGreen', 'DarkGreen1', 'DarkGreen2', 'DarkGreen3', 'DarkGreen4', 'DarkGreen5', 'DarkGreen6', 'DarkGrey', 'DarkGrey1', 'DarkGrey2', 'DarkGrey3', 'DarkGrey4', 'DarkGrey5', 'DarkGrey6', 'DarkGrey7', 'DarkPurple', 'DarkPurple1', 'DarkPurple2', 'DarkPurple3', 'DarkPurple4', 'DarkPurple5', 'DarkPurple6', 'DarkRed', 'DarkRed1', 'DarkRed2', 'DarkTanBlue', 'DarkTeal', 'DarkTeal1', 'DarkTeal10', 'DarkTeal11', 'DarkTeal12', 'DarkTeal2', 'DarkTeal3', 'DarkTeal4', 'DarkTeal5', 'DarkTeal6', 'DarkTeal7', 'DarkTeal8', 'DarkTeal9', 'Default', 'Default1', 'DefaultNoMoreNagging', 'Green', 'GreenMono', 'GreenTan', 'HotDogStand', 'Kayak', 'LightBlue', 'LightBlue1', 'LightBlue2', 'LightBlue3', 'LightBlue4', 'LightBlue5', 'LightBlue6', 'LightBlue7', 'LightBrown', 'LightBrown1', 'LightBrown10', 'LightBrown11', 'LightBrown12', 'LightBrown13', 'LightBrown2', 'LightBrown3', 'LightBrown4', 'LightBrown5', 'LightBrown6', 'LightBrown7', 'LightBrown8', 'LightBrown9', 'LightGray1', 'LightGreen', 'LightGreen1', 'LightGreen10', 'LightGreen2', 'LightGreen3', 'LightGreen4', 'LightGreen5', 'LightGreen6', 'LightGreen7', 'LightGreen8', 'LightGreen9', 'LightGrey', 'LightGrey1', 'LightGrey2', 'LightGrey3', 'LightGrey4', 'LightGrey5', 'LightGrey6', 'LightPurple', 'LightTeal', 'LightYellow', 'Material1', 'Material2', 'NeutralBlue', 'Purple', 'Reddit', 'Reds', 'SandyBeach', 'SystemDefault', 'SystemDefault1', 'SystemDefaultForReal', 'Tan', 'TanBlue', 'TealMono', 'Topanga']
```
