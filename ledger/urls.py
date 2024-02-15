from django.urls import path
from .views import recipes_list
from .views import recipe_1
from .views import recipe_2
urlpatterns = [
path('recipes/list', recipes_list, name='recipes'),
path('recipe/1/', recipe_1, name='recipe'),
path('recipe/2/', recipe_2, name='recipe')

]
# This might be needed, depending on your Django version
app_name = "ledger"