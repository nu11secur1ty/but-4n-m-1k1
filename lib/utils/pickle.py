#!/usr/bin/python
# Idea: Mauro Soria
# Development: nu11secur1ty - 2022

try:
    import cPickle as _pickle
except ModuleNotFoundError:
    import pickle as _pickle

from lib.core.exceptions import UnpicklingError

ALLOWED_PICKLE_CLASSES = (
    "collections.OrderedDict",
    "http.cookiejar.DefaultCookiePolicy",
    "requests.adapters.HTTPAdapter",
    "requests.cookies.RequestsCookieJar",
    "requests.sessions.Session",
    "requests.structures.CaseInsensitiveDict",
    "lib.connection.requester.Requester",
    "lib.connection.response.Response",
    "lib.connection.requester.Session",
    "lib.core.dictionary.Dictionary",
    "lib.core.report_manager.Report",
    "lib.core.report_manager.ReportManager",
    "lib.core.report_manager.Result",
    "lib.core.structures.AttributeDict",
    "lib.core.structures.CaseInsensitiveDict",
    "lib.output.verbose.Output",
    "lib.reports.csv_report.CSVReport",
    "lib.reports.html_report.HTMLReport",
    "lib.reports.json_report.JSONReport",
    "lib.reports.markdown_report.MarkdownReport",
    "lib.reports.plain_text_report.PlainTextReport",
    "lib.reports.simple_report.SimpleReport",
    "lib.reports.xml_report.XMLReport",
    "lib.reports.sqlite_report.SQLiteReport",
    "urllib3.util.retry.Retry",
)


# Reference: https://docs.python.org/3.10/library/pickle.html#restricting-globals
class RestrictedUnpickler(_pickle.Unpickler):
    def find_class(self, module, name):
        if f"{module}.{name}" in ALLOWED_PICKLE_CLASSES:
            return super().find_class(module, name)

        raise UnpicklingError()


def unpickle(*args, **kwargs):
    return RestrictedUnpickler(*args, **kwargs).load()


def pickle(obj, *args, **kwargs):
    return _pickle.Pickler(*args, **kwargs).dump(obj)
