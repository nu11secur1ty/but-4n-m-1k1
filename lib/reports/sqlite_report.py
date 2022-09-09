#!/usr/bin/python
# Idea: Mauro Soria
# Development: nu11secur1ty - 2022

import sqlite3
import time

from lib.core.decorators import locked
from lib.reports.base import FileBaseReport


class SQLiteReport(FileBaseReport):
    def generate(self, entries):
        commands = []
        created_tables = []

        for entry in entries:
            host = entry.url.split("/")[2]
            if host not in created_tables:
                commands.append([f"DROP TABLE IF EXISTS `{host}`"])
                commands.append(
                    [
                        f"""CREATE TABLE `{host}`
                        ([time] TEXT, [url] TEXT, [status_code] INTEGER, [content_length] INTEGER, [content_type] TEXT, [redirect] TEXT)"""
                    ]
                )
                created_tables.append(host)

            commands.append(
                [
                    f"""INSERT INTO `{host}` (time, url, status_code, content_length, content_type, redirect)
                    VALUES
                    (?, ?, ?, ?, ?, ?)""",
                    (
                        time.ctime(),
                        entry.url,
                        entry.status,
                        entry.length,
                        entry.type,
                        entry.redirect,
                    ),
                ]
            )

        return commands

    def open(self):
        self.file = sqlite3.connect(self.output, check_same_thread=False)
        self.cursor = self.file.cursor()

    @locked
    def save(self):
        for command in self.generate():
            self.cursor.execute(*command)

        self.file.commit()
