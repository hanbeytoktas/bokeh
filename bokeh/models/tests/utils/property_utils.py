#-----------------------------------------------------------------------------
# Copyright (c) 2012 - 2018, Anaconda, Inc. All rights reserved.
#
# Powered by the Bokeh Development Team.
#
# The full license is in the file LICENSE.txt, distributed with this software.
#-----------------------------------------------------------------------------

#-----------------------------------------------------------------------------
# Boilerplate
#-----------------------------------------------------------------------------
from __future__ import absolute_import, division, print_function, unicode_literals

import pytest ; pytest

#-----------------------------------------------------------------------------
# Imports
#-----------------------------------------------------------------------------

# Standard library imports
from itertools import chain

# External imports

# Bokeh imports
from bokeh.core.enums import NamedColor as Color, LineJoin, LineCap

# Module under test

#-----------------------------------------------------------------------------
# Setup
#-----------------------------------------------------------------------------

# enums
FILL = ["fill_color", "fill_alpha"]
LINE = ["line_color", "line_width", "line_alpha", "line_join", "line_cap", "line_dash", "line_dash_offset"]
TEXT = ["text_font", "text_font_size", "text_font_style", "text_color", "text_alpha", "text_align", "text_baseline", "text_line_height"]

ANGLE = ["angle", "angle_units"]

PROPS = ["name", "tags", "js_property_callbacks", "js_event_callbacks", "subscribed_events"]
GLYPH = []

MARKER = ["x", "y", "size", "angle", "angle_units"]

#-----------------------------------------------------------------------------
# General API
#-----------------------------------------------------------------------------

def prefix(prefix, props):
    return [prefix + p for p in props]

def check_properties_existence(model, *props):
    expected = set(chain(PROPS, *props))
    found = set(model.properties())
    missing = expected.difference(found)
    extra = found.difference(expected)
    assert len(missing) == 0, "Properties missing: {0}".format(", ".join(sorted(missing)))
    assert len(extra) == 0, "Extra properties: {0}".format(", ".join(sorted(extra)))

def check_fill_properties(model, prefix="", fill_color=Color.gray, fill_alpha=1.0):
    assert getattr(model, prefix + "fill_color") == fill_color
    assert getattr(model, prefix + "fill_alpha") == fill_alpha

def check_line_properties(model, prefix="", line_color=Color.black, line_width=1.0, line_alpha=1.0):
    assert getattr(model, prefix + "line_color") == line_color
    assert getattr(model, prefix + "line_width") == line_width
    assert getattr(model, prefix + "line_alpha") == line_alpha
    assert getattr(model, prefix + "line_join") == LineJoin.bevel
    assert getattr(model, prefix + "line_cap") == LineCap.butt
    assert getattr(model, prefix + "line_dash") == []
    assert getattr(model, prefix + "line_dash_offset") == 0

def check_text_properties(model, prefix="", font_size='12pt', baseline='bottom', font_style='normal', align="left"):
    assert getattr(model, prefix + "text_font") == "helvetica"
    assert getattr(model, prefix + "text_font_size") == {"value": font_size}
    assert getattr(model, prefix + "text_font_style") == font_style
    assert getattr(model, prefix + "text_color") == "#444444"
    assert getattr(model, prefix + "text_alpha") == 1.0
    assert getattr(model, prefix + "text_align") == align
    assert getattr(model, prefix + "text_baseline") == baseline

def check_marker_properties(marker):
    assert marker.x is None
    assert marker.y is None
    assert marker.size == 4

#-----------------------------------------------------------------------------
# Dev API
#-----------------------------------------------------------------------------

#-----------------------------------------------------------------------------
# Private API
#-----------------------------------------------------------------------------

#-----------------------------------------------------------------------------
# Code
#-----------------------------------------------------------------------------
