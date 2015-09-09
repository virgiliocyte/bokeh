""" Overlay shown during model reloading, in develop mode """

from __future__ import absolute_import

from ...properties import Instance
from ...plot_object import PlotObject
from .errorpanel import ErrorPanel
from .reloading import Reloading
from .debugtoolbar import DebugToolbar

class DevelopShell(PlotObject):
    """DevelopShell isn't useful to manipulate directly; it's the UI for develop mode.
    """

    error_panel = Instance(ErrorPanel, help="""
    Panel to display errors.
    """)

    reloading = Instance(Reloading, help="""
    Reloading indicator.
    """)

    debug_toolbar = Instance(DebugToolbar, help="""
    Panel to display errors.
    """)

    def __init__(self, **kwargs):
        if "error_panel" not in kwargs:
            kwargs["error_panel"] = ErrorPanel(visible=False)
        if "reloading" not in kwargs:
            kwargs["reloading"] = Reloading(visible=False)
        if "debug_toolbar" not in kwargs:
            kwargs["debug_toolbar"] = DebugToolbar(visible=True)
        super(DevelopShell, self).__init__(**kwargs)
