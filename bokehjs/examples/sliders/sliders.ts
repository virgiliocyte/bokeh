namespace SliderWidgets {
  import plt = Bokeh.Plotting

  Bokeh.set_log_level("info")
  Bokeh.logger.info(`Bokeh ${Bokeh.version}`)

  function color_slider(color: Color) {
      return Bokeh.Widgets.Slider(height=300, value=127, start=0, end=255, step=1, orientation="vertical", bar_color=color)
  }

  const red   = color_slider("red")
  const green = color_slider("green")
  const blue  = color_slider("blue")

  div = Div(width=100, height=100)
  div.style.background_color=(127, 127, 127)

  cb = CustomJS(args=dict(red=red, green=green, blue=blue, div=div), code=
    div.style.background_color = `rgb(${red.value}, ${green.value}, ${blue.value})`

  red.callback   = cb
  green.callback = cb
  blue.callback  = cb

  Row(children=[
      WidgetBox(width=50, children=[red]),
      WidgetBox(width=50, children=[green]),
      WidgetBox(width=50, children=[blue]),
      div,
  ])

  plt.show(...)
}
