import * as p from "core/properties"

import {Widget, WidgetView} from "./widget"
import {Styles} from "./styles"
import template from "./markup_template"

export class MarkupView extends WidgetView
  template: template

  initialize: (options) ->
    super(options)
    @render()
    @listenTo(@model, 'change', @render)
    @listenTo(@model.style, 'change', @render)

  render: () ->
    super()

    @$el.empty()
    @$el.html(@template())

    if @model.style.background_color?
      @el.style.backgroundColor = @model.style.background_color

export class Markup extends Widget
  type: "Markup"

  initialize: (options) ->
    super(options)

  @define {
    text: [ p.String, '' ]
    style: [ p.Instance, () -> new Styles() ]
  }
