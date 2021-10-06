from rest_framework.routers import DefaultRouter
from .api.billing_views import BillingViewSet
from .api.transfer_views import TransferViewSet

app_name = 'billing'

router = DefaultRouter()
router.register(r'billing', BillingViewSet)
router.register(r'transfer', TransferViewSet)

urlpatterns = [

]

urlpatterns += router.urls
