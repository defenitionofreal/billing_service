from django.urls import reverse
from rest_framework import status, serializers
# set up
from .test_setup import TestSetUp


class TransferAPITest(TestSetUp):

    def test_create(self):
        url = reverse("billing:transfer-list")
        data = {
            'sender': self.billing_1.id,
            'amount': 100,
            'receiver': self.billing_2.id
        }
        response = self.client.post(
            url,
            data=data,
        )
        self.billing_1.refresh_from_db()
        self.billing_2.refresh_from_db()
        self.assertEqual(status.HTTP_201_CREATED, response.status_code)
        self.assertEqual(self.billing_1.billing, 900.00)
        self.assertEqual(self.billing_2.billing, 100.00)

    def test_validation_if_sum_greater_than_sender_has(self):
        url = reverse("billing:transfer-list")
        data = {
            'sender': self.billing_1.id,
            'amount': 10000,
            'receiver': [self.billing_2.id]
        }
        response = self.client.post(
            url,
            data=data,
        )
        self.assertEqual(status.HTTP_400_BAD_REQUEST, response.status_code)
        self.assertRaises(serializers.ValidationError)

    def test_if_sum_greater_than_sender_has_but_over_draft_is_true(self):
        url = reverse("billing:transfer-list")
        data = {
            'sender': self.billing_2.id,
            'amount': 100000,
            'receiver': [self.billing_1.id]
        }
        response = self.client.post(
            url,
            data=data,
        )
        self.assertEqual(status.HTTP_201_CREATED, response.status_code)

    def test_incorrect_receivers_id(self):
        url = reverse("billing:transfer-list")
        data = {
            'sender': self.billing_1.id,
            'amount': 10000,
            'receiver': '111111111111'
        }
        response = self.client.post(
            url,
            data=data,
        )
        self.assertEqual(status.HTTP_400_BAD_REQUEST, response.status_code)
        self.assertRaises(serializers.ValidationError)

    def test_get_list(self):
        url = reverse("billing:transfer-list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
