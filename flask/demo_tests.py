"""Module to define test suite for the application test cases."""
import unittest
from rackspace_app.models import db_cache_mixin_test

# Test suite.
SUITE = unittest.TestLoader().loadTestsFromTestCase(
        db_cache_mixin_test.TestDbCacheMixin)
unittest.TextTestRunner(verbosity=2).run(SUITE)
