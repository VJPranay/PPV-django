from django.apps import AppConfig

class StreamsAppConfig(AppConfig):
    name = 'streams'
    
    def ready(self):
        import streams.signals
