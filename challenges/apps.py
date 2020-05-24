from django.apps import AppConfig


class ChallengesConfig(AppConfig):
    name = 'challenges'

    def ready(self):
        import challenges.signals