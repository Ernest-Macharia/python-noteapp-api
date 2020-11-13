from rest_framework import routers
from noteapp import views as myapp_views

router = routers.DefaultRouter()
router.register(myapp_views.NoteViewSet)