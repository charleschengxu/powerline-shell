from powerline_shell.themes.default import DefaultColor


class Color(DefaultColor):
    """Basic theme which only uses colors in 0-15 range"""
    HOSTNAME_FG = 15
    HOSTNAME_BG = 74
    PATH_FG = 15
    PATH_BG = 239
