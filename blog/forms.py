__author__ = 'Robert W. Curtiss'

# Author: Robert W. Curtiss
# forms.py was created on August 12 2021 @ 8:30 AM
# Project: rp-portfolio

from django import forms
from django.shortcuts import render

from blog.models import Post, Comment


class CommentForm(forms.Form):
    """
    You’ll also notice an argument widget has been passed to both the fields.
    The author field has the forms.TextInput widget.
    This tells Django to load this field as an HTML text input element in the templates.
    The body field uses a forms.
    TextArea widget instead, so that the field is rendered as an HTML text area element.
    """
    author = forms.CharField(
        max_length=60,
        widget=forms.TextInput(
            attrs={
                "class": 'form-control',
                "placeholder": 'Your Name',
            }
        )
    )
    body = forms.CharField(widget=forms.Textarea(
        attrs={"class": "form-control",
               "placeholder": "Leave a comment!"
               })
    )


