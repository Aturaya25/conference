from django.test import TestCase

import datetime
from django.utils import timezone
from conference.locallibrary.catalog.forms import UserRegistrationForm


class UserRegistrationFormTest(TestCase):

    def test_password_field_label(self):
        form = UserRegistrationForm()
        self.assertTrue(form.fields['password'].label is None or form.fields['password'].label == 'password')

    def test_password2_field_label(self):
        form = UserRegistrationForm()
        self.assertTrue(form.fields['password2'].label is None or form.fields['password2'].label == 'password2')
