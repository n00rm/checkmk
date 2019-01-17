#!/usr/bin/python
# -*- encoding: utf-8; py-indent-offset: 4 -*-
# +------------------------------------------------------------------+
# |             ____ _               _        __  __ _  __           |
# |            / ___| |__   ___  ___| | __   |  \/  | |/ /           |
# |           | |   | '_ \ / _ \/ __| |/ /   | |\/| | ' /            |
# |           | |___| | | |  __/ (__|   <    | |  | | . \            |
# |            \____|_| |_|\___|\___|_|\_\___|_|  |_|_|\_\           |
# |                                                                  |
# | Copyright Mathias Kettner 2014             mk@mathias-kettner.de |
# +------------------------------------------------------------------+
#
# This file is part of Check_MK.
# The official homepage is at http://mathias-kettner.de/check_mk.
#
# check_mk is free software;  you can redistribute it and/or modify it
# under the  terms of the  GNU General Public License  as published by
# the Free Software Foundation in version 2.  check_mk is  distributed
# in the hope that it will be useful, but WITHOUT ANY WARRANTY;  with-
# out even the implied warranty of  MERCHANTABILITY  or  FITNESS FOR A
# PARTICULAR PURPOSE. See the  GNU General Public License for more de-
# tails. You should have  received  a copy of the  GNU  General Public
# License along with GNU Make; see the file  COPYING.  If  not,  write
# to the Free Software Foundation, Inc., 51 Franklin St,  Fifth Floor,
# Boston, MA 02110-1301 USA.

from cmk.gui.i18n import _
from cmk.gui.valuespec import (
    Age,
    Dictionary,
    TextAscii,
)
from cmk.gui.plugins.wato import (
    Levels,
    RulespecGroupCheckParametersStorage,
    register_check_parameters,
)

register_check_parameters(
    RulespecGroupCheckParametersStorage,
    "diskstat",
    _("Levels for disk IO"),
    Dictionary(
        help=_(
            "With this rule you can set limits for various disk IO statistics. "
            "Keep in mind that not all of these settings may be applicable for the actual "
            "check. For example, if the check doesn't provide a <i>Read wait</i> information in its "
            "output, any configuration setting referring to <i>Read wait</i> will have no effect."),
        elements=[
            ("read",
             Levels(
                 title=_("Read throughput"),
                 unit=_("MB/s"),
                 default_levels=(50.0, 100.0),
             )),
            ("write",
             Levels(
                 title=_("Write throughput"),
                 unit=_("MB/s"),
                 default_levels=(50.0, 100.0),
             )),
            ("utilization",
             Levels(
                 title=_("Disk Utilization"),
                 unit=_("%"),
                 default_levels=(80.0, 90.0),
             )),
            ("latency", Levels(
                title=_("Disk Latency"),
                unit=_("ms"),
                default_levels=(80.0, 160.0),
            )),
            ("read_wait", Levels(title=_("Read wait"), unit=_("ms"), default_levels=(30.0, 50.0))),
            ("write_wait", Levels(title=_("Write wait"), unit=_("ms"), default_levels=(30.0,
                                                                                       50.0))),
            ("average",
             Age(
                 title=_("Averaging"),
                 help=_(
                     "When averaging is set, then all of the disk's metrics are averaged "
                     "over the selected interval - rather then the check interval. This allows "
                     "you to make your monitoring less reactive to short peaks. But it will also "
                     "introduce a loss of accuracy in your graphs. "),
                 default_value=300,
             )),
            ("read_ios",
             Levels(title=_("Read operations"), unit=_("1/s"), default_levels=(400.0, 600.0))),
            ("write_ios",
             Levels(title=_("Write operations"), unit=_("1/s"), default_levels=(300.0, 400.0))),
        ]),
    TextAscii(
        title=_("Device"),
        help=_(
            "For a summarized throughput of all disks, specify <tt>SUMMARY</tt>,  "
            "a per-disk IO is specified by the drive letter, a colon and a slash on Windows "
            "(e.g. <tt>C:/</tt>) or by the device name on Linux/UNIX (e.g. <tt>/dev/sda</tt>).")),
    "dict",
)
