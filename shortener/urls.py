from rest_framework import routers

from shortener.views import LinkViewSet 

router = routers.DefaultRouter()

router.register('link', LinkViewSet, basename = 'LinkView')