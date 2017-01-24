""" A subset of CSS 3.0 properties. """

from __future__ import absolute_import

import re

from ...model import Model
from ...core.properties import Any, String, Regex, Int, Float, Enum, Tuple, Either as Or, Color, Auto

Length = Regex("^[0-9]+(\.[0-9]+)?(em|ex|ch|ic|rem|vw|vh|vi|vb|vmin|vmax|cm|mm|q|in|pc|pt|px)$", re.I)
Percentage = Regex("^[0-9]+(\.[0-9]+)?%$")

Transparent = Enum("transparent")

BorderStyle = Enum("none", "hidden", "dotted", "dashed", "solid", "double", "groove", "ridge", "inset", "outset", default=None)
BorderWidth = Or(Length, Enum("thin", "medium", "thick"), default=None)

def Tupled_1_4(tp, default=None):
    return Or(tp, Tuple(tp, tp), Tuple(tp, tp, tp), Tuple(tp, tp, tp, tp), default=default)

def OneOrTwo(tp, default=None):
    return Or(tp, Tuple(tp, tp), default=default)

class Styles(Model):

    background = Any(default=None)
    background_attachment = Enum("scroll", "fixed", "local", default=None)
    background_blend_mode = Enum("normal", "multiply", "screen", "overlay", "darken", "lighten", "color-dodge", "saturation", "color", "luminosity", default=None)
    background_clip = Enum("border-box", "padding-box", "content-box", default=None)
    background_color = Or(Color, Transparent, default=None)
    background_image = Enum("none", default=None) # TODO
    background_origin = Enum("border-box", "padding-box", "content-box", default=None)
    background_position = Or(
        Enum("left", "center", "right", "top", "bottom"),
        Length,
        Percentage,
        Tuple(Or(Enum("left", "center", "right"), Length, Percentage),
              Or(Enum("top", "center", "bottom"), Length, Percentage)),
        # TODO
    default=None)
    background_repeat = Or(Enum("repeat-x", "repeat-y"), OneOrTwo(Enum("repeat", "space", "round", "no-repeat")), default=None)
    background_size = Or(OneOrTwo(Or(Length, Percentage, Auto)), Enum("cover", "contain"), default=None)

    border = Tuple(BorderWidth, BorderStyle, Or(Color, Transparent), default=None)

    border_color = Tupled_1_4(Or(Color, Transparent), default=None)
    border_style = Tupled_1_4(BorderStyle, default=None)
    border_width = Tupled_1_4(BorderWidth, default=None)

    border_top    = Tuple(BorderWidth, BorderStyle, Or(Color, Transparent), default=None)
    border_right  = Tuple(BorderWidth, BorderStyle, Or(Color, Transparent), default=None)
    border_bottom = Tuple(BorderWidth, BorderStyle, Or(Color, Transparent), default=None)
    border_left   = Tuple(BorderWidth, BorderStyle, Or(Color, Transparent), default=None)

    border_top_color = Or(Color, Transparent, default=None)
    border_top_style = BorderStyle
    border_top_width = BorderWidth

    border_right_color = Or(Color, Transparent, default=None)
    border_right_style = BorderStyle
    border_right_width = BorderWidth

    border_bottom_color = Or(Color, Transparent, default=None)
    border_bottom_style = BorderStyle
    border_bottom_width = BorderWidth

    border_left_color = Or(Color, Transparent, default=None)
    border_left_style = BorderStyle
    border_left_width = BorderWidth

    top    = Or(Length, Percentage, Auto, default=None)
    right  = Or(Length, Percentage, Auto, default=None)
    bottom = Or(Length, Percentage, Auto, default=None)
    left   = Or(Length, Percentage, Auto, default=None)

    margin        = Tupled_1_4(Or(Length, Percentage, Auto), default=None)
    margin_top    = Or(Length, Percentage, Auto, default=None)
    margin_right  = Or(Length, Percentage, Auto, default=None)
    margin_bottom = Or(Length, Percentage, Auto, default=None)
    margin_left   = Or(Length, Percentage, Auto, default=None)

    padding        = Tupled_1_4(Or(Length, Percentage), default=None)
    padding_top    = Or(Length, Percentage, default=None)
    padding_right  = Or(Length, Percentage, default=None)
    padding_bottom = Or(Length, Percentage, default=None)
    padding_left   = Or(Length, Percentage, default=None)

    color = Color

    float = Enum("left", "right", "none", "inline-start", "inline-end", default=None)
    clear = Enum("none", "left", "right", "both", "inline-start", "inline-end", default=None)

    font_family = String
    font_size = Or(Enum("xx-small", "x-small", "small", "medium", "large", "x-large", "xx-large"), Enum("larger", "smaller"), Length, Percentage, default=None)
    font_style = Enum("normal", "italic", "oblique", default=None)
    font_weight = Enum("normal", "bold", "bolder", "lighter", "100", "200", "300", "400", "500", "600", "700", "800", "900", default=None)

    line_height = Or(Enum("normal"), Float, Int, Length, Percentage, default=None)

    overflow   = Or(Enum("visible", "hidden", "scroll"), Auto, default=None)
    overflow_x = Or(Enum("visible", "hidden", "scroll"), Auto, default=None)
    overflow_y = Or(Enum("visible", "hidden", "scroll"), Auto, default=None)

    text_align = Enum("start", "end", "left", "right", "center", "justify", "match-parent", default=None)
    vertical_align = Or(Enum("baseline", "sub", "super", "text-top", "text-bottom", "middle", "top", "bottom"), Length, Percentage, default=None)

    display = Enum("none", "inline", "block", "inline-block", default=None) # TODO
    visibility = Enum("visible", "hidden", "collapse", default=None)

    white_space = Enum("normal", "pre", "nowrap", "pre-wrap", "pre-line", default=None)

    word_spacing = Or(Enum("normal"), Length, Percentage, default=None)
    letter_spacing = Or(Enum("normal"), Length, default=None)

    z_index = Or(Auto, Int, default=None)
