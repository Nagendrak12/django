from django.test import TestCase
from django.test.client import Client
from django.db import models
# from notesapp.models import MyNotes


# Create your tests here.


# class TestNotes(TestCase):

#     # This is called before every test
#     def setUp(self):
#         # print("Calling setUp()")
#         MyNotes.objects.create(title='Nokia',username="nagendra",password="Chinna@143")

    # def test_notes_add(self):
    #     c = MyNotes.objects.get(title='Nokia')
    #     self.assertEqual(c.title, 'Nokia')

    # def test_expenditures_count(self):
    #     c = Category.objects.get(name='Education')
    #     self.assertEqual(c.expenditure_set.all().count(), 0)

    # def test_category_delete(self):
    #     c = Category.objects.get(name='Education')
    #     c.delete()
    #     self.assertRaises(Category.DoesNotExist,
    #                       Category.objects.get, name='Education')
