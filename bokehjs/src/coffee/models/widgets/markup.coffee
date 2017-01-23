import * as p from "../../core/properties"

import {Widget, WidgetView} from "./widget"
import template from "./markup_template"

export class MarkupView extends WidgetView
  template: template

  initialize: (options) ->
    super(options)
    @render()
    @listenTo(@model, 'change', @render)

  render: () ->
    super()

    @$el.empty()
    @$el.html(@template())

    if @model.background_color?
      @el.style.backgroundColor = @model.background_color

export class Markup extends Widget
  type: "Markup"

  initialize: (options) ->
    super(options)

  @define {
    text: [ p.String, '' ]
  }

  @define {
    background_color: [ p.Color ]
  }
