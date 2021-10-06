# rest
from rest_framework.test import APITestCase
from rest_framework.test import APIRequestFactory
# core
from ..models import Billing
from ..api.billing_views import BillingViewSet


class TestSetUp(APITestCase):

    def setUp(self):
        self.billing_1 = Billing.objects.create(
            title='one',
            billing=1000,
            is_over_draft=False
        )

        self.billing_2 = Billing.objects.create(
            title='two',
            billing=0,
            is_over_draft=True
        )

        self.factory = APIRequestFactory()
        self.view = BillingViewSet.as_view({'get': 'list',
                                            'post': 'create', })

        return super().setUp()

    def tearDown(self) -> None:
        return super().tearDown()
