from django.test import TestCase
from django.urls import reverse

from conference.locallibrary.catalog.models import Presentation


class PresentationTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        number_of_presentation = 13
        for presentation_num in range(number_of_presentation):
            Presentation.objects.create(presentation_name='Some present %s' % presentation_num,
                                        author='Author %s' % presentation_num,)

    def test_view_url_exists_at_desired_location(self):
        resp = self.client.get('/catalog/presentation/')
        self.assertEqual(resp.status_code, 200)

    def test_view_url_accessible_by_name(self):
        resp = self.client.get(reverse('presentation'))
        self.assertEqual(resp.status_code, 200)
