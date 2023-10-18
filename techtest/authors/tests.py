from django.test import TestCase

# Create your tests here.
import json

from django.urls import reverse

from techtest.authors.models import Author


class AuthorListViewTestCase(TestCase):
    def setUp(self):
        self.url = reverse("author-list")
        self.Author_1 = Author.objects.create(first_name="first", last_name="last")
        self.Author_2 = Author.objects.create(first_name="first2", last_name="last2")

    def test_serializes_with_correct_data_shape_and_status_code(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertCountEqual(
            response.json(),
            [
                {
                    "id": self.Author_1.id,
                    "first_name": "first",
                    "last_name": "last",
                },
                {
                    "id": self.Author_2.id,
                    "first_name": "first2",
                    "last_name": "last2",
                },
            ],
        )

    def test_creates_new_author(self):
        payload = {
            "first_name": "first_test",
            "last_name": "last_test",
        }
        response = self.client.post(
            self.url, data=json.dumps(payload), content_type="application/json"
        )
        author = Author.objects.last()
        self.assertEqual(response.status_code, 201)
        self.assertIsNotNone(author)
        self.assertEqual(Author.objects.count(), 3)
        self.assertDictEqual(
            {
                "id": author.id,
                "first_name": "first_test",
                "last_name": "last_test",
            },
            response.json(),
        )


class AuthorViewTestCase(TestCase):
    def setUp(self):
        self.author = Author.objects.create(first_name="first", last_name="last")
        self.url = reverse("author-detail", args=[1])

    def test_serializes_single_record_with_correct_data_shape_and_status_code(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertCountEqual(
            response.json(),
            {
                "id": self.author.id,
                "first_name": "first",
                "last_name": "last",
            },
        )

    def test_updates_author(self):
        payload = {
            "id": self.author.id,
            "first_name": "first_test",
            "last_name": "last_test",
        }
        response = self.client.put(
            self.url, data=json.dumps(payload), content_type="application/json"
        )
        author = Author.objects.filter(id=self.author.id).first()
        self.assertEqual(response.status_code, 200)
        self.assertIsNotNone(author)
        self.assertEqual(Author.objects.count(), 1)
        self.assertDictEqual(
            {
                "id": author.id,
                "first_name": "first_test",
                "last_name": "last_test",
            },
            response.json(),
        )

    def test_removes_author(self):
        response = self.client.delete(self.url)
        self.assertEqual(response.status_code, 204)
        self.assertEqual(Author.objects.count(), 0)
