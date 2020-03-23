from django.conf import settings
from appconf import AppConf


class App1Conf(AppConf):
    VALUE = "from App1"
    INTERNAL = True

    class Meta:
        prefix = 'app1'
