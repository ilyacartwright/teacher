from django.db import models
from django.utils.translation import gettext as _

class Corses(models.Model):
    title = models.CharField(_("Название"), max_length=100)
    abbr = models.CharField(_("Аббревиатура"), max_length=10)

    class Meta:
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'


class LevelCourses(models.Model):
    сorse = models.ForeignKey("corses.Corses", verbose_name=_("Курс"), on_delete=models.CASCADE)
    title = models.CharField(_("Название уровня"), max_length=100)
    level_number = models.IntegerField(_("Номер"))

class ThemesLevelCourses(models.Model):
    сorse = models.ForeignKey("corses.Corses", verbose_name=_("Курс"), on_delete=models.CASCADE)
    level = models.ForeignKey("corses.LevelCourses", verbose_name=_("Уровень"), on_delete=models.CASCADE)
    title = models.CharField(_("Название темы"), max_length=100)
    number = models.IntegerField(_("Номер"))
    is_author = models.BooleanField(_("Авторская тема?"))
