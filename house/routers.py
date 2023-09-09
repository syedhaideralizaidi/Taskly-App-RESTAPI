from rest_framework import routers
from house.viewsets import HouseViewSets

app_name = "house"

router = routers.DefaultRouter()
router.register('houses', HouseViewSets)