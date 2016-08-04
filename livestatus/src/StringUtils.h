// +------------------------------------------------------------------+
// |             ____ _               _        __  __ _  __           |
// |            / ___| |__   ___  ___| | __   |  \/  | |/ /           |
// |           | |   | '_ \ / _ \/ __| |/ /   | |\/| | ' /            |
// |           | |___| | | |  __/ (__|   <    | |  | | . \            |
// |            \____|_| |_|\___|\___|_|\_\___|_|  |_|_|\_\           |
// |                                                                  |
// | Copyright Mathias Kettner 2014             mk@mathias-kettner.de |
// +------------------------------------------------------------------+
//
// This file is part of Check_MK.
// The official homepage is at http://mathias-kettner.de/check_mk.
//
// check_mk is free software;  you can redistribute it and/or modify it
// under the  terms of the  GNU General Public License  as published by
// the Free Software Foundation in version 2.  check_mk is  distributed
// in the hope that it will be useful, but WITHOUT ANY WARRANTY;  with-
// out even the implied warranty of  MERCHANTABILITY  or  FITNESS FOR A
// PARTICULAR PURPOSE. See the  GNU General Public License for more de-
// tails. You should have  received  a copy of the  GNU  General Public
// License along with GNU Make; see the file  COPYING.  If  not,  write
// to the Free Software Foundation, Inc., 51 Franklin St,  Fifth Floor,
// Boston, MA 02110-1301 USA.

#ifndef StringUtils_h
#define StringUtils_h

#include "config.h"   // IWYU pragma: keep
#include <algorithm>  // IWYU pragma: keep
#include <string>
#include <utility>
#include <vector>

namespace mk {
std::string unsafe_tolower(const std::string &str);
std::string unsafe_toupper(const std::string &str);

bool starts_with(const std::string &input, const std::string &test);

std::vector<std::string> split(const std::string &str, char delimiter);

std::string lstrip(const std::string &str,
                   const std::string &chars = " \t\n\v\f\r");

std::string rstrip(const std::string &str,
                   const std::string &chars = " \t\n\v\f\r");

std::string strip(const std::string &str,
                  const std::string &chars = " \t\n\v\f\r");

std::pair<std::string, std::string> nextField(
    const std::string &str, const std::string &chars = " \t\n\v\f\r");

}  // namespace

#endif  // StringUtils_h
