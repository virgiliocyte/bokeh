import {Model} from "../../model"
import * as p from "../../core/properties"

export class Styles extends Model
  type: "Styles"

  @define {
    background: [ p.Any ]
    background_attachment: [ p.Any ]
    background_blend_mode: [ p.Any ]
    background_clip: [ p.Any ]
    background_color: [ p.Any ]
    background_image: [ p.Any ]
    background_origin: [ p.Any ]
    background_position: [ p.Any ]
    background_repeat: [ p.Any ]
    background_size: [ p.Any ]

    border: [ p.Any ]

    border_color: [ p.Any ]
    border_style: [ p.Any ]
    border_width: [ p.Any ]

    border_top   : [ p.Any ]
    border_right : [ p.Any ]
    border_bottom: [ p.Any ]
    border_left  : [ p.Any ]

    border_top_color: [ p.Any ]
    border_top_style: [ p.Any ]
    border_top_width: [ p.Any ]

    border_right_color: [ p.Any ]
    border_right_style: [ p.Any ]
    border_right_width: [ p.Any ]

    border_bottom_color: [ p.Any ]
    border_bottom_style: [ p.Any ]
    border_bottom_width: [ p.Any ]

    border_left_color: [ p.Any ]
    border_left_style: [ p.Any ]
    border_left_width: [ p.Any ]

    top   : [ p.Any ]
    right : [ p.Any ]
    bottom: [ p.Any ]
    left  : [ p.Any ]

    margin       : [ p.Any ]
    margin_top   : [ p.Any ]
    margin_right : [ p.Any ]
    margin_bottom: [ p.Any ]
    margin_left  : [ p.Any ]

    padding       : [ p.Any ]
    padding_top   : [ p.Any ]
    padding_right : [ p.Any ]
    padding_bottom: [ p.Any ]
    padding_left  : [ p.Any ]

    color: [ p.Any ]

    float: [ p.Any ]
    clear: [ p.Any ]

    font_family: [ p.Any ]
    font_size: [ p.Any ]
    font_style: [ p.Any ]
    font_weight: [ p.Any ]

    line_height: [ p.Any ]

    overflow  : [ p.Any ]
    overflow_x: [ p.Any ]
    overflow_y: [ p.Any ]

    text_align: [ p.Any ]
    vertical_align: [ p.Any ]

    display: [ p.Any ]
    visibility: [ p.Any ]

    white_space: [ p.Any ]

    word_spacing: [ p.Any ]
    letter_spacing: [ p.Any ]

    z_index: [ p.Any ]
  }
