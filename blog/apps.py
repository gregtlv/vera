from django.apps import AppConfig
from watson import search as watson

class BlogConfig(AppConfig):
    name = 'blog'

class YourAppConfig(AppConfig):
    name = "blog"
    def ready(self):
        YourModel = self.get_model("YourModel")
        watson.register(YourModel)
