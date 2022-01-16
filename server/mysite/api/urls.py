from django.urls import path
from .views import Items
from .views import ItemsSingular
from .views import ApiEndpoint
from .views import ItemsList
from .views import ItemsListUsernameFiltered
urlpatterns = [
    path("api/item", Items.as_view()),
    path("api/item/<int:item_id>", ItemsSingular.as_view()),
    path("api/items", ItemsList.as_view()),
    path("api/items?<str:username>",ItemsListUsernameFiltered.as_view()),
    #path("api", index),
    path("api",ApiEndpoint.as_view()),
]
    

#Test for adding item 2 cart
"""
curl -X POST -H "Content-Type: application/json" https://8000-eorge-frameworksandla-s8jvndsus9i.ws-eu27.gitpod.io/api/item -d "{\"username\":\"name\",\"lat\":\"41.5\",\"lon\":\"50.5\",\"image\":\"1\",\"keywords\":\"I like trains\",\"description\":\"Please work jesus\"}"

curl -X POST -H "Content-Type: application/json" https://8000-eorge-frameworksandla-s8jvndsus9i.ws-eu27.gitpod.io/api/item -d "{\"user_id\":\"name\",\"lat\":\"41.5\",\"lon\":\"50.5\",\"image\":\"1\",\"keywords\":\"I like trains\",\"description\":\"Please work jesus\"}"

curl -X GET https://8000-eorge-frameworksandla-s8jvndsus9i.ws-eu27.gitpod.io
curl -X OPTIONS https://8000-eorge-frameworksandla-s8jvndsus9i.ws-eu27.gitpod.io/api/item -i
    ITEM = {
        'user_id': "user1234",
        'keywords': ["hammer", "nails", "tools"],
        "description": "A hammer and nails set. In canterbury",
        "lat": 51.2798438,
        "lon": 1.0830275,
    }

curl -X GET https://8000-eorge-frameworksandla-s8jvndsus9i.ws-eu27.gitpod.io/api/item/1
curl -X GET https://8000-eorge-frameworksandla-s8jvndsus9i.ws-eu27.gitpod.io/api/items
curl -X POST -H "Content-Type: application/json" https://8000-eorge-frameworksandla-s8jvndsus9i.ws-eu27.gitpod.io/api/item -d "{\"user_id\":\"name\",\"lat\":\"41.5\",\"lon\":\"50.5\",\"image\":\"1\",\"keywords\":\"bob\",\"description\":\"Please work jesus\"}"
 """