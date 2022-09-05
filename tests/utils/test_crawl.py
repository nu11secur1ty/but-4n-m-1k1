#!/usr/bin/python
# Idea: Mauro Soria  
# Development: nu11secur1ty - 2022

from unittest import TestCase

from lib.core.settings import DUMMY_URL
from lib.utils.crawl import Crawler


class TestCrawl(TestCase):
    def test_text_crawl(self):
        html_doc = f'Link: {DUMMY_URL}foobar'
        self.assertEqual(Crawler.text_crawl(DUMMY_URL, DUMMY_URL, html_doc), {"foobar"})

    def test_html_crawl(self):
        html_doc = f'<a href="{DUMMY_URL}foo">link</a><script src="/bar.js"><img src="/bar.png">'
        self.assertEqual(Crawler.html_crawl(DUMMY_URL, DUMMY_URL, html_doc), {"foo", "bar.js"})

    def test_robots_crawl(self):
        robots_txt = """
User-agent: Googlebot
Disallow: /path1

User-agent: *
Allow: /path2"""
        self.assertEqual(Crawler.robots_crawl(DUMMY_URL, DUMMY_URL, robots_txt), {"path1", "path2"})
