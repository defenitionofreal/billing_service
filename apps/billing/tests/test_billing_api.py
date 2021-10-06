from django.urls import reverse
from rest_framework import status
# core
from ..models import Billing
from ..serializers import BillingSerializer
# set up
from .test_setup import TestSetUp


class BillingAPITest(TestSetUp):

    def test_get_list(self):
        billings = Billing.objects.all()
        serializer = BillingSerializer(billings, many=True).data
        request = self.factory.get(reverse("billing:billing-list"))
        response = self.view(request)
        self.assertEqual(response.data, serializer)
        self.assertEqual(Billing.objects.count(), 2)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_one(self):
        serializer = BillingSerializer(self.billing_1).data
        url = reverse("billing:billing-detail", args=(self.billing_1.id,))
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(serializer, response.data)

    def test_create(self):
        data = {
            "title": "three",
            "billing": 100,
            "is_over_draft": True
        }
        response = self.client.post(
            reverse("billing:billing-list"), data=data)
        self.assertEqual(Billing.objects.count(), 3)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_update(self):
        data = {
            "billing": 50
        }
        url = reverse("billing:billing-detail", args=(self.billing_1.id,))
        response = self.client.patch(url, data=data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete(self):
        url = reverse("billing:billing-detail", args=(self.billing_1.id,))
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_get_balance(self):
        url = reverse('billing:billing-get_balance')
        data = {"id": self.billing_1.id}
        response = self.client.get(url, data=data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["total"], "1000.00")
