#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from lxml import etree

if __name__ == "__main__":
    dtd = etree.DTD("arggraph.dtd")
    for root, _, filenames in os.walk('.'):
        for filename in filenames:
            if filename.endswith('.xml'):
                p = os.path.join(root, filename)
                e = etree.parse(p)
                v = dtd.validate(e)
                if v:
                    print "%s is valid." % p
                else:
                    print "%s is INVALID:" % p
                    print(dtd.error_log.filter_from_errors()[0])
