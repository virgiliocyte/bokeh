""" A subset of CSS 3.0 properties. """

from __future__ import absolute_import

import re

from ...core.has_props import HasProps
from ...core.properties import abstract
from ...core.properties import String, Regex, Int, Float, Enum, Tuple, Either as Or, Color, Auto

Length = Regex("^[0-9]+(\.[0-9]+)?(em|ex|ch|ic|rem|vw|vh|vi|vb|vmin|vmax|cm|mm|q|in|pc|pt|px)$", re.I)
Percentage = Regex("^[0-9]+(\.[0-9]+)?%$")

Transparent = Enum("transparent")

BorderStyle = Enum("none", "hidden", "dotted", "dashed", "solid", "double", "groove", "ridge", "inset", "outset")
BorderWidth = Or(Length, Enum("thin", "medium", "thick"))

def Tupled_1_4(tp):
    return Or(tp, Tuple(tp, tp), Tuple(tp, tp, tp), Tuple(tp, tp, tp, tp))

def OneOrTwo(tp):
    return Or(tp, Tuple(tp, tp))

@abstract
class Styles(HasProps):

    # background = TODO
    background_attachment = Enum("scroll", "fixed", "local")
    background_blend_mode = Enum("normal", "multiply", "screen", "overlay", "darken", "lighten", "color-dodge", "saturation", "color", "luminosity")
    background_clip = Enum("border-box", "padding-box", "content-box")
    background_color = Or(Color, Transparent)
    background_image = Enum("none") # TODO
    background_origin = Enum("border-box", "padding-box", "content-box")
    background_position = Or(
        Enum("left", "center", "right", "top", "bottom"),
        Length,
        Percentage,
        Tuple(Or(Enum("left", "center", "right"), Length, Percentage),
              Or(Enum("top", "center", "bottom"), Length, Percentage)),
        # TODO
    )
    background_repeat = Or(Enum("repeat-x", "repeat-y"), OneOrTwo(Enum("repeat", "space", "round", "no-repeat")))
    background_size = Or(OneOrTwo(Or(Length, Percentage, Auto)), Enum("cover", "contain"))

    border = Tuple(BorderWidth, BorderStyle, Or(Color, Transparent))

    border_color = Tupled_1_4(Or(Color, Transparent))
    border_style = Tupled_1_4(BorderStyle)
    border_width = Tupled_1_4(BorderWidth)

    border_top    = Tuple(BorderWidth, BorderStyle, Or(Color, Transparent))
    border_right  = Tuple(BorderWidth, BorderStyle, Or(Color, Transparent))
    border_bottom = Tuple(BorderWidth, BorderStyle, Or(Color, Transparent))
    border_left   = Tuple(BorderWidth, BorderStyle, Or(Color, Transparent))

    border_top_color = Or(Color, Transparent)
    border_top_style = BorderStyle
    border_top_width = BorderWidth

    border_right_color = Or(Color, Transparent)
    border_right_style = BorderStyle
    border_right_width = BorderWidth

    border_bottom_color = Or(Color, Transparent)
    border_bottom_style = BorderStyle
    border_bottom_width = BorderWidth

    border_left_color = Or(Color, Transparent)
    border_left_style = BorderStyle
    border_left_width = BorderWidth

    top    = Or(Length, Percentage, Auto)
    right  = Or(Length, Percentage, Auto)
    bottom = Or(Length, Percentage, Auto)
    left   = Or(Length, Percentage, Auto)

    margin        = Tupled_1_4(Or(Length, Percentage, Auto))
    margin_top    = Or(Length, Percentage, Auto)
    margin_right  = Or(Length, Percentage, Auto)
    margin_bottom = Or(Length, Percentage, Auto)
    margin_left   = Or(Length, Percentage, Auto)

    padding        = Tupled_1_4(Or(Length, Percentage))
    padding_top    = Or(Length, Percentage)
    padding_right  = Or(Length, Percentage)
    padding_bottom = Or(Length, Percentage)
    padding_left   = Or(Length, Percentage)

    color = Color

    float = Enum("left", "right", "none", "inline-start", "inline-end")
    clear = Enum("none", "left", "right", "both", "inline-start", "inline-end")

    font_family = String
    font_size = Or(Enum("xx-small", "x-small", "small", "medium", "large", "x-large", "xx-large"), Enum("larger", "smaller"), Length, Percentage)
    font_style = Enum("normal", "italic", "oblique")
    font_weight = Enum("normal", "bold", "bolder", "lighter", "100", "200", "300", "400", "500", "600", "700", "800", "900")

    line_height = Or(Enum("normal"), Float, Int, Length, Percentage)

    overflow   = Or(Enum("visible", "hidden", "scroll"), Auto)
    overflow_x = Or(Enum("visible", "hidden", "scroll"), Auto)
    overflow_y = Or(Enum("visible", "hidden", "scroll"), Auto)

    text_align = Enum("start", "end", "left", "right", "center", "justify", "match-parent")
    vertical_align = Or(Enum("baseline", "sub", "super", "text-top", "text-bottom", "middle", "top", "bottom"), Length, Percentage)

    display = Enum("none", "inline", "block", "inline-block") # TODO
    visibility = Enum("visible", "hidden", "collapse")

    white_space = Enum("normal", "pre", "nowrap", "pre-wrap", "pre-line")

    word_spacing = Or(Enum("normal"), Length, Percentage)
    letter_spacing = Or(Enum("normal"), Length)

    z_index = Or(Auto, Int)
