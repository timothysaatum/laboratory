from django.apps import AppConfig


class LdmsappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'LDMSApp'

    '''
    import ldmsapp signals
    '''
'''
    def ready(self):
        import LDMSApp.signals
'''