from rest_framework.routers import DefaultRouter
from django.urls import path, include # Import include to include the router URLs
from patients.views import PatientViewSet

#register the PatientViewSet with the router
router = DefaultRouter()
router.register(r'patients', PatientViewSet, basename='patient')

# Include the router URLs in the urlpatterns
urlpatterns = [
    path('', include(router.urls)),
]