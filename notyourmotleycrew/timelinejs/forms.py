# encoding: utf-8
from django import forms

FILTER_DN = ('dn', 'DN Kulturs hantering')
FILTER_CENTRAL = ('default', 'De centrala händelserna')
FILTER_EVERYTHING = ('everything', 'Hela databasen')


CHOICES = (
        FILTER_CENTRAL,
        FILTER_DN,
        FILTER_EVERYTHING,
        )
FILTER_DICT = {}
for key, value in CHOICES:
    FILTER_DICT[key] = (key, value)


class FilterForm(forms.Form):
    filter = forms.fields.ChoiceField(choices = CHOICES)
