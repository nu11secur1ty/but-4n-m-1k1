#!/usr/bin/python
# Idea: Mauro Soria
# Development: nu11secur1ty - 2022

import unittest

from tests.connection.test_dns import TestDNS  # noqa: F401
from tests.parse.test_headers import TestHeadersParser  # noqa: F401
from tests.parse.test_url import TestURLParsers  # noqa: F401
from tests.reports.test_reports import TestReports  # noqa: F401
from tests.utils.test_common import TestCommonUtils  # noqa: F401
from tests.utils.test_crawl import TestCrawl  # noqa: F401
from tests.utils.test_diff import TestDiff  # noqa: F401
from tests.utils.test_mimetype import TestMimeTypeUtils  # noqa: F401
from tests.utils.test_random import TestRandom  # noqa: F401
from tests.utils.test_schemedet import TestSchemedet  # noqa: F401


if __name__ == "__main__":
    unittest.main()
