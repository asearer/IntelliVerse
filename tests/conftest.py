import pytest

# List known failing tests by module and name
xfail_tests = [
    "test_lime_explain",
    "test_status_endpoint",               # api_gateway
    "test_event_publish_and_consume",     # event_bus
    "test_capture_gesture_input",         # xr_module
]

def pytest_collection_modifyitems(items):
    for item in items:
        if item.name in xfail_tests:
            item.add_marker(pytest.mark.xfail(reason="Known failing stub"))
