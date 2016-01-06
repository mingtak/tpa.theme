# -*- coding: utf-8 -*-
"""Setup tests for this package."""
from tpa.theme.testing import TPA_THEME_INTEGRATION_TESTING  # noqa
from plone import api

import unittest


class TestSetup(unittest.TestCase):
    """Test that tpa.theme is properly installed."""

    layer = TPA_THEME_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_product_installed(self):
        """Test if tpa.theme is installed with portal_quickinstaller."""
        self.assertTrue(self.installer.isProductInstalled('tpa.theme'))

    def test_browserlayer(self):
        """Test that ITpaThemeLayer is registered."""
        from tpa.theme.interfaces import ITpaThemeLayer
        from plone.browserlayer import utils
        self.assertIn(ITpaThemeLayer, utils.registered_layers())


class TestUninstall(unittest.TestCase):

    layer = TPA_THEME_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')
        self.installer.uninstallProducts(['tpa.theme'])

    def test_product_uninstalled(self):
        """Test if tpa.theme is cleanly uninstalled."""
        self.assertFalse(self.installer.isProductInstalled('tpa.theme'))

    def test_browserlayer_removed(self):
        """Test that ITpaThemeLayer is removed."""
        from tpa.theme.interfaces import ITpaThemeLayer
        from plone.browserlayer import utils
        self.assertNotIn(ITpaThemeLayer, utils.registered_layers())
