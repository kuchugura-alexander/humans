from django.db import models
import datetime


class AbsModel(models.Model):
    pub_date = models.DateTimeField(auto_now_add=True,
                                    blank=False, verbose_name="Date Published:", help_text="Дата создания записи.")

    class Meta:
        abstract = True


class Human(AbsModel):
    nickname = models.CharField(max_length=200, default="",
                                blank=True, verbose_name="Nickname:", help_text="Псевдоним.")
    email = models.EmailField(max_length=200, default="",
                              blank=True, verbose_name="E-mail:", help_text="E-mail главный.")
    email_first = models.EmailField(max_length=200, default="",
                                    blank=True, verbose_name="E-mail first:", help_text="E-mail дополнительный 1.")
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
                               related_name='humans_gender', related_query_name='human_gender',
                               blank=True, verbose_name="Gender:", help_text="Пол.")
    # description = models.('Gender', on_delete=models.PROTECT, null=True, related_name='human_gender',
    #                            blank=True, verbose_name="Gender:", help_text="Пол.")

    def __str__(self):
        return "{0} {1} - {2}".format(self.surname, self.name, self.email)

    class Meta:
        verbose_name = "Человек"
        verbose_name_plural = "Человеки"


# class City(models.Model):
#     pub_date = models.DateTimeField(auto_now_add=True,
#                                     blank=False, verbose_name="Date Published:", help_text="Дата создания записи.")
#     question = models.ForeignKey(Question, on_delete=models.CASCADE)
#     choice_text = models.CharField(max_length=200)
#     votes = models.IntegerField(default=0)

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

