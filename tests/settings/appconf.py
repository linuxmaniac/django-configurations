from .main import Test


class AppConfConfiguration(Test):
    Test.INSTALLED_APPS += ('app1',)
    APP1_VALUE = 'from AppconfConfiguration'
