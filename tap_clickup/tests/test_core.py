"""Tests standard tap features using the built-in SDK tests library."""

import datetime
import os

from singer_sdk.testing import get_tap_test_class

from tap_clickup.tap import TapClickUp

SAMPLE_CONFIG = {
    "start_date": datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%d"),
    "api_token": os.environ["TAP_CLICKUP_API_TOKEN"],
}


# Run standard built-in tap tests from the SDK:
def test_standard_tap_tests():
    """Run standard tap tests from the SDK."""
    tests = get_tap_test_class(TapClickUp, config=SAMPLE_CONFIG)
    for test in tests:
        test()
