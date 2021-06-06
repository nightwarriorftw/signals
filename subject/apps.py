from django.apps import AppConfig


class SubjectConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'subject'

    def ready(self) -> None:
        from subject.receivers import book_published_receiver