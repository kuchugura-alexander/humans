from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class AbsModel(models.Model):
    """
    Abstract model for all classes.
    """
    created_at = models.DateTimeField(auto_now_add=True,
                                      blank=False, verbose_name="Date Published:", help_text="Дата создания записи.")

    modified_at = models.DateField(auto_now=True,
                                   blank=False, verbose_name="Date Modify:", help_text="Дата последнего изменения.")

    class Meta:
        abstract = True


class Human(AbsModel):
    """
    Main models about human.
    """
    nickname = models.CharField(max_length=200, default="",
                                blank=True, verbose_name="Nickname:", help_text="Псевдоним.")
    phone = PhoneNumberField(default="",  unique=True,
                             blank=True, verbose_name="Phone:", help_text="Номер телефона.")
    email = models.EmailField(max_length=200, default="", unique=True,
                              blank=True, verbose_name="E-mail:", help_text="E-mail главный.")
    email_first = models.EmailField(max_length=200, default="", unique=True,
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
    skills_programming = models.ManyToManyField('SkillProgramming',
                                                related_name='humans', related_query_name='human',
                                                blank=False, verbose_name="Skills:", help_text="Навыки.")
    interval_works = models.ManyToManyField('IntervalWork',
                                            related_name='humans', related_query_name='human',
                                            blank=False, verbose_name="Intervals:", help_text="Интервалы.")
    rate_works = models.ManyToManyField('RateWork',
                                        related_name='humans', related_query_name='human',
                                        blank=True, verbose_name="Price:", help_text="Цена.")

    def __str__(self):
        return "{0} {1} - {2}".format(self.surname, self.name, self.email)

    class Meta:
        verbose_name = "Человек"
        verbose_name_plural = "Человеки"
        ordering = ('modified_at', )
        # unique_together = ['phone', 'email', 'email_first']

####################################################################################


class Gender(AbsModel):
    """
    Gender: male, female and others.
    """
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
    """
    Current city. (with Country and TimeZone)
    """
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
        return "{0} - {1} ({2})".format(self.country, self.title, self.timezone)

    class Meta:
        verbose_name = "Город"
        verbose_name_plural = "Города"


class Country(AbsModel):
    """
    Current country. (with TimeZone and Domen)
    """
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
    """
    Time zone for binding to city.
    """
    timezone = models.CharField(max_length=100, default="",
                                blank=False, verbose_name="Time Zone:", help_text="Временная зона города.")
    hours = models.IntegerField(default=0,
                                blank=False, verbose_name="Time Zone Hours(+/-):", help_text="Час +/-.")
    description = models.TextField(max_length=400, default="",
                                   blank=True, verbose_name="Description:", help_text="Описание.")

    def __str__(self):
        if self.hours > 0:
            return "{0} : +{1}".format(self.timezone, self.hours)
        else:
            return "{0} : {1}".format(self.timezone, self.hours)

    class Meta:
        verbose_name = "Тайм Зона"
        verbose_name_plural = "Тайм Зоны"


####################################################################################


class LevelLanguage(AbsModel):
    """
    Level Language: Into CERF system, LevelLanguageTitle, LevelLanguageKnowledge.
    """
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
    """
    Title Level Language: A1, B2 and others.
    """
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
    """
    Knowledge Level Language: BASIC, INDEPENDENT and others.
    """
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


class SkillProgramming(AbsModel):
    """
    Skills.
    """
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


class IntervalWork(AbsModel):
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


class RateWork(AbsModel):
    title = models.CharField(max_length=100, default="",
                             blank=True, verbose_name="Title:", help_text="Название.")
    language = models.ForeignKey('LanguageProgramming', on_delete=models.PROTECT, null=True,
                                 related_name='RateWorks', related_query_name='RateWork',
                                 blank=True, verbose_name="Language:", help_text="Язык.")
    framework = models.ForeignKey('FrameworkProgramming', on_delete=models.PROTECT, null=True,
                                  related_name='RateWorks', related_query_name='RateWork',
                                  blank=True, verbose_name="Framework:", help_text="ФрэймВорк.")
    price_dollar = models.IntegerField(default=20,
                                       blank=False, verbose_name="Price (USA dollar):", help_text="Цена (в долларах).")
    price_rub = models.IntegerField(default=0,
                                    blank=True, verbose_name="Price (RUB):", help_text="Цена (в рублях).")
    description = models.TextField(max_length=400, default="",
                                   blank=True, verbose_name="Description:", help_text="Описание.")

    def __str__(self):
        return "{0} : {1}<->{2} (${3} - RUB{4})".format(self.title, self.language, self.framework,
                                           self.price_dollar, self.price_rub)

    class Meta:
        verbose_name = "Цена работы"
        verbose_name_plural = "Цены работ"

