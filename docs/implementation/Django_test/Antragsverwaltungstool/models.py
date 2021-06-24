import django
from django.db import models


class AdvisoryMember(models.Model):
    flag = models.IntegerField(default=0)
    number = models.CharField(max_length=12, primary_key=True, unique=True)
    date = models.DateField(default=django.utils.timezone.now)
    title = models.CharField(max_length=25, null=True)
    office = models.CharField(max_length=75, null=True)
    name = models.CharField(max_length=25, null=True)
    mail = models.EmailField(max_length=30, null=True)
    text = models.CharField(max_length=260, null=True)
    frg1 = models.CharField(max_length=260, null=True)
    frg2 = models.CharField(max_length=260, null=True)
    frg3 = models.CharField(max_length=260, null=True)
    frg4 = models.CharField(max_length=260, null=True)
    anlagen = models.CharField(max_length=260, null=True)
    aenderung = models.CharField(max_length=260, null=True)
    mehrheit = models.CharField(max_length=25, null=True)
    beschluss = models.CharField(max_length=25, null=True)
    beschlusstext = models.CharField(max_length=25, null=True)
    beschlussgrund = models.CharField(max_length=25, null=True)

    class Meta:
        ordering = ['number']

    def __str__(self):
        return '%s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s' % (
            self.flag, self.number, self.date, self.title, self.office, self.name, self.mail, self.text,
            self.frg1, self.frg2, self.frg3, self.frg4, self.anlagen, self.aenderung, self.mehrheit, self.beschluss,
            self.beschlusstext, self.beschlussgrund)


class Finance(models.Model):
    flag = models.IntegerField(default=0)
    number = models.CharField(max_length=12, primary_key=True, unique=True)
    date = models.DateField(default=django.utils.timezone.now)
    title = models.CharField(max_length=25, null=True)
    office = models.CharField(max_length=75, null=True)
    name = models.CharField(max_length=25, null=True)
    mail = models.EmailField(max_length=30, null=True)
    text = models.CharField(max_length=260, null=True)
    reason = models.CharField(max_length=260, null=True)
    budget = models.CharField(max_length=260, null=True)
    suggestion = models.CharField(max_length=260, null=True)
    anlagen = models.CharField(max_length=260, null=True)
    aenderung = models.CharField(max_length=260, null=True)
    mehrheit = models.CharField(max_length=25, null=True)
    beschluss = models.CharField(max_length=25, null=True)
    beschlusstext = models.CharField(max_length=25, null=True)
    beschlussgrund = models.CharField(max_length=25, null=True)

    class Meta:
        ordering = ['number']

    def __str__(self):
        return '%s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s' % (
            self.flag, self.number, self.date, self.title, self.office, self.name, self.mail, self.text,
            self.reason, self.budget, self.suggestion, self.anlagen, self.aenderung, self.mehrheit, self.beschluss,
            self.beschlusstext, self.beschlussgrund)


class Position(models.Model):
    flag = models.IntegerField(default=0)
    number = models.CharField(max_length=12, primary_key=True, unique=True)
    date = models.DateField(default=django.utils.timezone.now)
    title = models.CharField(max_length=25, null=True)
    office = models.CharField(max_length=75, null=True)
    name = models.CharField(max_length=25, null=True)
    mail = models.EmailField(max_length=30, null=True)
    text = models.CharField(max_length=260, null=True)
    frg1 = models.CharField(max_length=260, null=True)
    frg2 = models.CharField(max_length=260, null=True)
    frg3 = models.CharField(max_length=260, null=True)
    frg4 = models.CharField(max_length=260, null=True)
    frg_spez_1 = models.CharField(max_length=260, null=True)
    frg_spez_2 = models.CharField(max_length=260, null=True)
    frg_spez_3 = models.CharField(max_length=260, null=True)
    anlagen = models.CharField(max_length=260, null=True)
    aenderung = models.CharField(max_length=260, null=True)
    mehrheit = models.CharField(max_length=25, null=True)
    beschluss = models.CharField(max_length=25, null=True)
    beschlusstext = models.CharField(max_length=25, null=True)
    beschlussgrund = models.CharField(max_length=25, null=True)

    class Meta:
        ordering = ['number']

    def __str__(self):
        return '%s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s' % (
            self.flag, self.number, self.date, self.title, self.office, self.name, self.mail, self.text, self.frg1,
            self.frg2, self.frg3, self.frg4, self.frg_spez_1, self.frg_spez_2, self.frg_spez_3, self.anlagen,
            self.aenderung, self.mehrheit, self.beschluss, self.beschlusstext, self.beschlussgrund)


class Universall(models.Model):
    flag = models.IntegerField(default=0)
    number = models.CharField(max_length=12, primary_key=True, unique=True)
    date = models.DateField(default=django.utils.timezone.now)
    title = models.CharField(max_length=25, null=True)
    office = models.CharField(max_length=75, null=True)
    name = models.CharField(max_length=25, null=True)
    mail = models.EmailField(max_length=30, null=True)
    text = models.CharField(max_length=260, null=True)
    reason = models.CharField(max_length=260, null=True)
    suggestion = models.CharField(max_length=260, null=True)
    anlagen = models.CharField(max_length=260, null=True)
    aenderung = models.CharField(max_length=260, null=True)
    mehrheit = models.CharField(max_length=25, null=True)
    beschluss = models.CharField(max_length=25, null=True)
    beschlusstext = models.CharField(max_length=25, null=True)
    beschlussgrund = models.CharField(max_length=25, null=True)

    class Meta:
        ordering = ['number']

    def __str__(self):
        return '%s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s' % (
            self.flag, self.number, self.date, self.title, self.office, self.name, self.mail, self.text, self.reason,
            self.suggestion, self.anlagen, self.aenderung, self.mehrheit, self.beschluss, self.beschlusstext,
            self.beschlussgrund)
