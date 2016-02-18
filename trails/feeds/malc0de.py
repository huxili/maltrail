#!/usr/bin/env python

"""
Copyright (c) 2014-2016 Miroslav Stampar (@stamparm)
See the file 'LICENSE' for copying permission
"""

from core.common import retrieve_content

__url__ = "http://malc0de.com/bl/ZONES"
__check__ = "malc0de"
__info__ = "malware distribution"
__reference__ = "malc0de.com"

def fetch():
    retval = {}
    content = retrieve_content(__url__)

    if __check__ in content:
        for match in re.finditer(r'(?i)zone\s+"([^"]+)"\s+{"', content):
            retval[match.group(1)] = (__info__, __reference__)

    return retval
