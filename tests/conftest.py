import pytest
from _pytest.nodes import Item
from pytest_html import extras

@pytest.hookimpl(tryfirst=True)
def pytest_configure(config):
    config._my_extra = {}

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item: Item, call):
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])
    log = item.config._my_extra.get(item.nodeid)
    if log:
        extra.append(extras.text(log, name="Log Output"))
    report.extra = extra

@pytest.fixture
def log_to_report(request):
    def _log(text):
        request.config._my_extra[request.node.nodeid] = text
    return _log
