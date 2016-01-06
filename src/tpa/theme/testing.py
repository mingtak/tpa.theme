# -*- coding: utf-8 -*-
from plone.app.contenttypes.testing import PLONE_APP_CONTENTTYPES_FIXTURE
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import applyProfile
from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PloneSandboxLayer
from plone.testing import z2

import tpa.theme


class TpaThemeLayer(PloneSandboxLayer):

    defaultBases = (PLONE_APP_CONTENTTYPES_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        self.loadZCML(package=tpa.theme)

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'tpa.theme:default')


TPA_THEME_FIXTURE = TpaThemeLayer()


TPA_THEME_INTEGRATION_TESTING = IntegrationTesting(
    bases=(TPA_THEME_FIXTURE,),
    name='TpaThemeLayer:IntegrationTesting'
)


TPA_THEME_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(TPA_THEME_FIXTURE,),
    name='TpaThemeLayer:FunctionalTesting'
)


TPA_THEME_ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        TPA_THEME_FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        z2.ZSERVER_FIXTURE
    ),
    name='TpaThemeLayer:AcceptanceTesting'
)
