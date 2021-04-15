from dearpygui.core import *
from dearpygui.simple import *


def auto_center(sender, data):

    # getting the window sizes
    main_width = get_item_width("Main")
    main_height = get_item_height("Main")

    # doing window calcs and sizing objects
    set_item_height("body", int(0.80*main_height))
    set_item_height("footer", int(0.20*main_height))
    set_item_width("center-spacing", int(0.70*main_width))


with window("Main"):
    with child("body", border=False, autosize_x=True, height=600):
        add_text("this is the main group")
    with child("footer", border=False, autosize_x=True, autosize_y=True):
        add_button("this is the bottom group")
        add_same_line()
        add_dummy(name="center-spacing")
        add_same_line()
        add_button("on the right now")

# this is to remove style borders, padding and spacings from the main window which mess up spacing calculation
set_item_style_var("Main", mvGuiStyleVar_WindowPadding, [0, 0])
set_item_style_var("Main", mvGuiStyleVar_ItemSpacing, [0, 0])
set_item_style_var("Main", mvGuiStyleVar_ItemInnerSpacing, [0, 0])
set_item_style_var("Main", mvGuiStyleVar_WindowBorderSize, [0])

set_render_callback(auto_center)
start_dearpygui(primary_window="Main")