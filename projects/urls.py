from rest_framework import routers
from .api import AlumnoViewSet

router = routers.DefaultRouter()
router.register('api/Alumno', AlumnoViewSet, 'projects')

urlpatterns =router.urls