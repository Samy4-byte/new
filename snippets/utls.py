from django.db import models


class User():
    name = models.CharFields(max=150)