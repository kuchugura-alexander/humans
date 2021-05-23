from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
import datetime


class AbsModel(models.Model):
    pub_date = models.DateTimeField(auto_now_add=True,
                                    blank=False, verbose_name="Date Published:", help_text="Дата создания записи.")

    class Meta:
        abstract = True


class Human(AbsModel):
    nickname = models.CharField(max_length=200, default="",
                                blank=True, verbose_name="Nickname:", help_text="Псевдоним.")
    phone = PhoneNumberField(default="",
                             blank=True, verbose_name="Phone:", help_text="Номер телефона.")
    email = models.EmailField(max_length=200, default="",
                              blank=True, verbose_name="E-mail:", help_text="E-mail главный.")
    email_first = models.EmailField(max_length=200, default="",
                                    blank=True, verbose_name="E-mail first:", help_text="E-mail дополнительный 1 (*@hubbiton.info).")
    email_second = models.EmailField(max_length=200, default="",
                                     blank=True, verbose_name="E-mail second:", help_text="E-mail дополнительный 2.")
    email_third = models.EmailField(max_length=200, default="",
                                    blank=True, verbose_name="E-mail third:", help_text="E-mail дополнительный 3.")
    surname = models.CharField(max_length=200, default="",
                               blank=False, verbose_name="Surname:", help_text="Фамилия.")
    name = models.CharField(max_length=200, default="",
                            blank=False, verbose_name="Name:", help_text="Имя.")
    middle_name = models.CharField(max_length=200, default="",
                                   blank=True, verbose_name="Middle name:", help_text="Отчество.")
    gender = models.ForeignKey('Gender', on_delete=models.PROTECT, null=True,
                               related_name='humans', related_query_name='human',
                               blank=False, verbose_name="Gender:", help_text="Пол.")
    city = models.ForeignKey('City', on_delete=models.PROTECT, null=True,
                             related_name='humans', related_query_name='human',
                             blank=False, verbose_name="City:", help_text="Город.")
    level_english = models.ForeignKey('LevelLanguage', on_delete=models.PROTECT, null=True,
                                      related_name='humans', related_query_name='human',
                                      blank=False, verbose_name="Level English:", help_text="Уровень Английского.")
    language_programming = models.ManyToManyField('LanguageProgramming',
                                                  related_name='humans', related_query_name='human',
                                                  blank=False, verbose_name="Languages:", help_text="Языки.")
    framework_programming = models.ManyToManyField('FrameworkProgramming',
                                                   related_name='humans', related_query_name='human',
                                                   blank=False, verbose_name="Frameworks:", help_text="ФрэймВорки.")
    skills_programming = models.ManyToManyField('SkillsProgramming',
                                                related_name='humans', related_query_name='human',
                                                blank=False, verbose_name="Skills:", help_text="Навыки.")
    interval_works = models.ManyToManyField('IntervalWorks',
                                            related_name='humans', related_query_name='human',
                                            blank=False, verbose_name="Intervals:", help_text="Интервалы.")

    def __str__(self):
        return "{0} {1} - {2}".format(self.surname, self.name, self.email)

    class Meta:
        verbose_name = "Человек"
        verbose_name_plural = "Человеки"

####################################################################################


class Gender(AbsModel):
    gender = models.CharField(max_length=100, default="",
                              blank=False, verbose_name="Gender:", help_text="Пол.")
    description = models.TextField(max_length=400, default="",
                                   blank=True, verbose_name="Description:", help_text="Описание.")

    def __str__(self):
        return "{0}".format(self.gender)

    class Meta:
        verbose_name = "Пол"
        verbose_name_plural = "Полы"


####################################################################################


class City(AbsModel):
    title = models.CharField(max_length=50, default="",
                             blank=False, verbose_name="City:", help_text="Город.")
    description = models.TextField(max_length=400, default="",
                                   blank=True, verbose_name="Description:", help_text="Описание.")
    country = models.ForeignKey('Country', on_delete=models.PROTECT, null=True,
                                related_name='cities', related_query_name='city',
                                blank=True, verbose_name="Country:", help_text="Страна.")
    timezone = models.ForeignKey('TimeZoneResidence', on_delete=models.PROTECT, null=True,
                                 related_name='cities', related_query_name='city',
                                 blank=True, verbose_name="Time Zone:", help_text="Временная зона.")

    def __str__(self):
        return "{0} {1} ({2})".format(self.title, self.country, self.timezone)

    class Meta:
        verbose_name = "Город"
        verbose_name_plural = "Города"


class Country(AbsModel):
    domen = models.CharField(max_length=5, default="",
                             blank=False, verbose_name="Domen:", help_text="Домен.")
    title = models.CharField(max_length=50, default="",
                             blank=False, verbose_name="Country:", help_text="Страна.")
    description = models.TextField(max_length=400, default="",
                                   blank=True, verbose_name="Description:", help_text="Описание.")

    def __str__(self):
        return "{0} - {1}".format(self.domen, self.title)

    class Meta:
        verbose_name = "Стран"
        verbose_name_plural = "Страны"


class TimeZoneResidence(AbsModel):
    timezone = models.CharField(max_length=100, default="",
                                blank=False, verbose_name="Time Zone:", help_text="Временная зона города.")
    hours = models.IntegerField(default=0,
                                blank=False, verbose_name="Time Zone Hours(+/-):", help_text="Час +/-.")
    description = models.TextField(max_length=400, default="",
                                   blank=True, verbose_name="Description:", help_text="Описание.")

    def __str__(self):
        return "{0} : {1}".format(self.timezone, self.hours)

    class Meta:
        verbose_name = "Тайм Зона"
        verbose_name_plural = "Тайм Зоны"


####################################################################################


class LevelLanguage(AbsModel):
    CHOICE_CEFR = (
        ('CEFR',    'ДА - В системе'),
        ('NO CEFR', 'НЕТ - Наша оценка'),
    )
    CEFR = models.CharField(max_length=100, default="", choices=CHOICE_CEFR,
                            blank=False, verbose_name="CERF ??:", help_text="Уровень Мировой ил Наша интерпретация.")
    level = models.ForeignKey('LevelLanguageTitle', on_delete=models.PROTECT, null=True,
                              related_name='LevelLanguages', related_query_name='LevelLanguage',
                              blank=False, verbose_name="Level:", help_text="Уровень.")
    knowledge = models.ForeignKey('LevelLanguageKnowledge', on_delete=models.PROTECT, null=True,
                                  related_name='LevelLanguages', related_query_name='LevelLanguage',
                                  blank=False, verbose_name="Knowledge:", help_text="Знание.")
    description = models.TextField(max_length=400, default="",
                                   blank=True, verbose_name="Description:", help_text="Описание.")

    def __str__(self):
        return "{0} ({1})".format(self.level, self.knowledge)

    class Meta:
        verbose_name = "Уровень языка"
        verbose_name_plural = "Уровни языков"


class LevelLanguageTitle(AbsModel):
    suffix = models.CharField(max_length=2, default="",
                              blank=True, verbose_name="Suffix:", help_text="Суффикс.")
    title = models.CharField(max_length=100, default="",
                             blank=False, verbose_name="Title:", help_text="Название.")
    description = models.TextField(max_length=400, default="",
                                   blank=True, verbose_name="Description:", help_text="Описание.")

    def __str__(self):
        return "{0} - {1}".format(self.suffix, self.title)

    class Meta:
        verbose_name = "Название уровеня языка"
        verbose_name_plural = "Названия уровней языков"


class LevelLanguageKnowledge(AbsModel):
    title = models.CharField(max_length=100, default="",
                             blank=False, verbose_name="Knowledge:", help_text="Знание.")
    description = models.TextField(max_length=400, default="",
                                   blank=True, verbose_name="Description:", help_text="Описание.")

    def __str__(self):
        return "{0}".format(self.title)

    class Meta:
        verbose_name = "Знание уровеня языка"
        verbose_name_plural = "Знание уровней языков"

####################################################################################


class FrameworkProgramming(AbsModel):
    title = models.CharField(max_length=100, default="",
                             blank=False, verbose_name="Framework:", help_text="Язык программирвоания.")
    language = models.ForeignKey('LanguageProgramming', on_delete=models.PROTECT, null=True,
                                 related_name='FrameworkProgrammings', related_query_name='FrameworkProgramming',
                                 blank=False, verbose_name="Language:", help_text="Язык.")
    description = models.TextField(max_length=400, default="",
                                   blank=True, verbose_name="Description:", help_text="Описание.")

    def __str__(self):
        return "{0} ({1})".format(self.title, self.language)

    class Meta:
        verbose_name = "ФрэймВорк"
        verbose_name_plural = "ФрэймВорки"


class LanguageProgramming(AbsModel):
    title = models.CharField(max_length=100, default="",
                             blank=False, verbose_name="Language:", help_text="Язык программирвоания.")
    description = models.TextField(max_length=400, default="",
                                   blank=True, verbose_name="Description:", help_text="Описание.")

    def __str__(self):
        return "{0}".format(self.title)

    class Meta:
        verbose_name = "Язык программиирование"
        verbose_name_plural = "Языки программирования"


class SkillsProgramming(AbsModel):
    title = models.CharField(max_length=100, default="",
                             blank=False, verbose_name="Skills:", help_text="Навыки и умения.")
    description = models.TextField(max_length=400, default="",
                                   blank=True, verbose_name="Description:", help_text="Описание.")

    def __str__(self):
        return "{0}".format(self.title)

    class Meta:
        verbose_name = "Дополнительный навык"
        verbose_name_plural = "Дополнительный навыки"


####################################################################################


class IntervalWorks(AbsModel):
    title = models.CharField(max_length=100, default="",
                             blank=True, verbose_name="Interval:", help_text="Интервал.")
    timeFrom = models.IntegerField(default=8,
                                   blank=False, verbose_name="Start:", help_text="Начало работы.")
    timeTo = models.IntegerField(default=17,
                                 blank=False, verbose_name="Stop:", help_text="Завершение работы.")
    description = models.TextField(max_length=400, default="",
                                   blank=True, verbose_name="Description:", help_text="Описание.")

    def __str__(self):
        return "{0} ({1} - {2})".format(self.title, self.timeFrom, self.timeTo)

    class Meta:
        verbose_name = "Время работы"
        verbose_name_plural = "Времена работы"

