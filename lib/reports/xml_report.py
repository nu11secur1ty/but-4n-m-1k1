#!/usr/bin/python
# Idea: Mauro Soria
# Development: nu11secur1ty - 2022

import time
import sys

from xml.dom import minidom
from xml.etree import ElementTree as ET

from lib.core.settings import DEFAULT_ENCODING
from lib.reports.base import FileBaseReport


class XMLReport(FileBaseReport):
    def generate(self, entries):
        tree = ET.Element("dirsearchscan", args=" ".join(sys.argv), time=time.ctime())

        for entry in entries:
            target = ET.SubElement(tree, "target", url=entry.url)
            ET.SubElement(target, "status").text = str(entry.status)
            ET.SubElement(target, "contentLength").text = str(entry.length)
            ET.SubElement(target, "contentType").text = entry.type
            if entry.redirect:
                ET.SubElement(target, "redirect").text = entry.redirect

        output = ET.tostring(tree, encoding=DEFAULT_ENCODING, method="xml")
        # Beautify XML output
        return minidom.parseString(output).toprettyxml()
