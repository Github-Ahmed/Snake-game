
# Creating a class

class Constants():
    FPS = 9
    Menu_FPS = 60

    # Dimensions
    Window_width = 640
    Window_height = 480
    Cell_size = 20
    assert Window_width % Cell_size == 0, "Window width must be a multiple of cell size."
    assert Window_height % Cell_size == 0, "Window height must be a multiple of cell size."

    # Cell dimensions
    Cell_width = int(Window_width / Cell_size)
    Cell_height = int(Window_height / Cell_size)

    # Colors
    WHITE = (255, 255, 255)
    BLACK = (0,   0,   0)
    RED = (255,   0,   0)
    GREEN = (0, 255,   0)
    DARKGREEN = (0, 155,   0)
    DARKGRAY = (40,  40,  40)
    BG_COLOR = BLACK


# ---------------------------------------------------------------------------------------
# This is the end of Constants.py
