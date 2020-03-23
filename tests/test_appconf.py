import os
from django.test import TestCase
from mock import patch


class AppconfTests(TestCase):

    @patch.dict(os.environ, clear=True,
                DJANGO_CONFIGURATION='AppConfConfiguration',
                DJANGO_SETTINGS_MODULE='tests.settings.appconf')
    def test_app1_loaded(self):
        from tests.settings import appconf
        self.assertIn('app1', appconf.INSTALLED_APPS)

    @patch.dict(os.environ, clear=True,
                DJANGO_CONFIGURATION='AppConfConfiguration',
                DJANGO_SETTINGS_MODULE='tests.settings.appconf')
    def test_appconf_ok(self):
        from tests.settings import appconf
        self.assertEqual(appconf.APP1_VALUE, 'from AppconfConfiguration')
        self.assertTrue(appconf.APP1_INTERNAL)

    @patch.dict(os.environ, clear=True,
                DJANGO_CONFIGURATION='AppConfConfiguration',
                DJANGO_SETTINGS_MODULE='tests.settings.appconf')
    def test_appconf_alone(self):
        from tests.app1.conf import App1Conf
        app1_settings = App1Conf()

        self.assertTrue(app1_settings.INTERNAL)
        self.assertEqual(app1_settings.VALUE, 'from App1')

    @patch.dict(os.environ, clear=True,
                DJANGO_CONFIGURATION='AppConfConfiguration',
                DJANGO_SETTINGS_MODULE='tests.settings.appconf')
    def test_appconf_django(self):
        from tests.app1.conf import settings

        self.assertTrue(settings.APP1_INTERNAL)
        self.assertEqual(settings.APP1_VALUE, 'from App1')
