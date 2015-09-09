_ = require "underscore"
$ = require "jquery"

#Semantic = require "semantic_ui/semantic"
#Sidebar = require "semantic_ui/components/sidebar"

ContinuumView = require "../common/continuum_view"
HasProperties = require "../common/has_properties"
debugtoolbar_template = require "./debugtoolbar_template"

class DebugToolbarView extends ContinuumView
  initialize: (options) ->
    super(options)
    @$contents = null
    @show_detail = false
    @$el.addClass("bk-debugtoolbar-panel")
    @render()
    # TODO often all three properties change at once,
    # when that happens we render three times
    @listenTo(@model, 'change:message', @changedMessages)
    @listenTo(@model, 'change:message_detail', @changedMessages)
    @listenTo(@model, 'change:visible', @render)

  # the ... stuff is because we want to be able to call
  # jquery show/hide with no args when not animating.
  updateDetailExpansion: (animate...) ->
    if @mget("message_detail").length > 0
      if @show_detail
        @$el.find(".bk-debugtoolbar-expander").addClass("open")
        @$el.find(".bk-debugtoolbar-bottom").show(animate...)
        @$el.find(".bk-debugtoolbar-expand-hint").show()
        @$el.find(".bk-debugtoolbar-expand-hint").css("visibility", "hidden")
      else
        @$el.find(".bk-debugtoolbar-expander").removeClass("open")
        @$el.find(".bk-debugtoolbar-bottom").hide(animate...)
        @$el.find(".bk-debugtoolbar-expand-hint").css("visibility", "visible")
        @$el.find(".bk-debugtoolbar-expand-hint").show()
      @$el.find(".bk-debugtoolbar-expander").show()
    else
      # this is because there are no details, so no animation
      @$el.find(".bk-debugtoolbar-expander").hide()
      @$el.find(".bk-debugtoolbar-bottom").hide()
      @$el.find(".bk-debugtoolbar-expand-hint").hide()

  render: () ->
    if @mget("visible")
      first = @$contents == null
      animate = [500]
      if first
        @$contents = $(debugtoolbar_template(@model.attributes))
        @$el.html(@$contents)
        animate = []
        @$el.find(".bk-debugtoolbar-expander").click (event) =>
          event.preventDefault()
          @show_detail = not @show_detail
          @render()
        @$el.find(".bk-debugtoolbar-expand-hint").click (event) =>
          event.preventDefault()
          @show_detail = not @show_detail
          @render()
      @updateDetailExpansion(animate...)
      @$el.show()
    else
      @$el.hide()
      @invalidateContents()

  invalidateContents: () ->
    @$contents?.detach()
    @$contents = null
    @$el.empty()

  changedMessages: () ->
    @invalidateContents()
    @render()

class DebugToolbar extends HasProperties
  type: "DebugToolbar"
  default_view: DebugToolbarView

  defaults: () ->
    return _.extend {}, super(), {
      visible: false,
      message: "",
      message_detail: ""
    }

module.exports =
  Model: DebugToolbar
  View: DebugToolbarView
