from django.db import models
import datetime

# Create your models here.


class Human(models.Model):
    pub_date = models.DateTimeField(auto_now_add=True,
                                    blank=False, verbose_name="Date Published:", help_text="Дата создания записи.")
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

    def __str__(self):
        return "{0} {1} - {2}".format(self.surname, self.name, self.email)

    class Meta:
        verbose_name = "Человек"
        verbose_name_plural = "Человеки"

# class Choice(models.Model):
#     question = models.ForeignKey(Question, on_delete=models.CASCADE)
#     choice_text = models.CharField(max_length=200)
#     votes = models.IntegerField(default=0)
