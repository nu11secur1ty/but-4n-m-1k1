#!/usr/bin/python
# Idea: Mauro Soria
# Development: nu11secur1ty - 2022

import os
import sys
import time

from jinja2 import Environment, FileSystemLoader

from lib.reports.base import FileBaseReport
from lib.utils.common import human_size


class HTMLReport(FileBaseReport):
    def generate(self, entries):
        file_loader = FileSystemLoader(
            os.path.dirname(os.path.realpath(__file__)) + "/templates/"
        )
        env = Environment(loader=file_loader)
        template = env.get_template("html_report_template.html")
        metadata = {"command": " ".join(sys.argv), "date": time.ctime()}
        results = []

        for entry in entries:
            status_color_class = ""
            if entry.status >= 200 and entry.status <= 299:
                status_color_class = "text-success"
            elif entry.status >= 300 and entry.status <= 399:
                status_color_class = "text-warning"
            elif entry.status >= 400 and entry.status <= 599:
                status_color_class = "text-danger"

            results.append(
                {
                    "url": entry.url,
                    "status": entry.status,
                    "statusColorClass": status_color_class,
                    "contentLength": human_size(entry.length),
                    "contentType": entry.type,
                    "redirect": entry.redirect,
                }
            )

        return template.render(metadata=metadata, results=results)
