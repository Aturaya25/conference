from django.test import TestCase
from conference.locallibrary.catalog.models import Presentation, Room


class PresentationModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        #Set up non-modified objects used by all test methods
        Presentation.objects.create(presentation_name='School problem', presentation_author='Elen')

    def test_presentation_name_label(self):
        presentation = Presentation.objects.get(id=1)
        field_label = presentation._meta.get_field('presentation_name').verbose_name
        self.assertEquals(field_label, 'presentation name')

    def test_create_date_label(self):
        presentation = Presentation.objects.get(id=1)
        field_label = presentation._meta.get_field('create_date').verbose_name
        self.assertEquals(field_label, 'create date')

    def test_presentation_name_max_length(self):
        presentation = Presentation.objects.get(id=1)
        max_length = presentation._meta.get_field('presentation_name').max_length
        self.assertEquals(max_length, 200)

    def test_object_name_is_presentation_name_comma_presentation_author(self):
        presentation = Presentation.objects.get(id=1)
        expected_object_name = '%s, %s' % (presentation.presentation_name, presentation.presentation_author)
        self.assertEquals(expected_object_name, str(presentation))

    def test_get_absolute_url(self):
        presentation = Presentation.objects.get(id=1)
        self.assertEquals(presentation.get_absolute_url(), '/catalog/presentation/1')


class RoomModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        #Set up non-modified objects used by all test methods
        Room.objects.create(room='1a', places='19', free_places='19')

    def test_room_label(self):
        room = Room.objects.get(id=1)
        field_label = room._meta.get_field('room').verbose_name
        self.assertEquals(field_label, 'room')

    def test_room_max_length(self):
        room = Room.objects.get(id=1)
        max_length = room._meta.get_field('room').max_length
        self.assertEquals(max_length, 10)

    def test_get_absolute_url(self):
        room = Room.objects.get(id=1)
        self.assertEquals(room.get_absolute_url(), '/catalog/room/1')


