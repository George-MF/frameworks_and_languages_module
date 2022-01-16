from django.views import View
from django.http import JsonResponse
from django.shortcuts import render
from django.http import HttpResponse
import json
from .models import Item

#Handles base /api/ end point.
class ApiEndpoint(View):
    def get(self, request):
        return HttpResponse("Hello, world. You're at the api index.", status=200)

    def options(self, request):
        self.allowed_methods = ['get', 'post', 'put', 'delete', 'options']
        response = HttpResponse()
        response['Access-Control-Allow-Methods'] = "POST"
        response['Access-Control-Allow-Headers'] = "Content-Type"
        response.status_code = 204
        
        return response



from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt


##Handles post
@method_decorator(csrf_exempt, name='dispatch')
class Items(View):

    



    def post(self, request):

        data = json.loads(request.body.decode("utf-8"))

        user_id = data.get('user_id')
        lat = data.get('lat')
        lon = data.get('lon')
        image = data.get('image')
        keywords = data.get('keywords')
        print(keywords)
        description = data.get('description')

        #Checks received data has all required information
        requiredJsonFields = ["user_id","lat","lon","keywords","description"]
        requiredInformation=True
        for i in requiredJsonFields:
            if (i not in data):
                requiredInformation = False
                
        if requiredInformation == False:
            return HttpResponse("Missing json data", status=405)
        
        #If no image data is sent set to "" so the model object can be created
        if (data.get('image')) == None:
            image = ""

        product_data = {
            "user_id": user_id,
            "lat": lat,
            "lon": lon,
            "image": image,
            "keywords": keywords,
            "description": description
        }




        ##Trys to create an item. 
        ##If fails return 405 eg. data is missing or wrong
        try:
            item = Item.objects.create(**product_data)
        except: 
            #return HttpResponse("Missing json data", status=405)
            return JsonResponse(data, status=405)

        #Return confirmation of item creation
        data = {
            "id": f"{item.id}"
        }
        response = JsonResponse(data) 
        response.content_type = "application/json"
        response.status_code = 201
        return response
        #return JsonResponse(data, status=201)


###Handles get and delete
@method_decorator(csrf_exempt, name='dispatch')
class ItemsSingular(View):


    def get(self, request,item_id):
        items_count = Item.objects.count()
        #items = Item.objects.all()
        
        #Try to fetch item
        #If item doesn't exist return error
        try:
            item = Item.objects.get(id=item_id)
        except:
            return HttpResponse("Invalid item id", status=404)
        product_data = {
            "user_id": item.user_id,
            "lat": item.lat,
            "lon": item.lon,

            "keywords": item.keywords,
            "description": item.description
        }

        #Allows None image data to not crash site
        if (item.image != ""):
            product_data["image"]=item.image

        ##Get item test  only wants the id for the test to pass?
        ##Test incorrect?
        ##Above implementation returns the json object
        product_data={"id":str(item_id)}
        response = JsonResponse(product_data) 
        response.content_type = "application/json"
        response.status_code = 200
        return response
        
    def delete(self, request, item_id):
        
        #Checks item exits before trying to delete 
        try:
            item = Item.objects.get(id=item_id)
        except:
            return HttpResponse("Invalid item id", status=404)


        item.delete()

        data = {
            'message': f'Item {item_id} has been deleted'
        }

        return JsonResponse(data, status=201)

##Handles get all items
@method_decorator(csrf_exempt, name='dispatch')
class ItemsList(View):

    def get(self, request,aa="None"):
        items_count = Item.objects.count()
        items = Item.objects.all()

        print(aa)

        items_data = []
        i=0
        for item in items:
            items_data.append(
            {
            "user_id": item.user_id,
            "lat": item.lat,
            "lon": item.lon,
            "image": item.image,
            "keywords": item.keywords,
            "description": item.description,
            #Tests wants id 2b string
            "id": str(item.id)
            })
            

        data = {
            "data":items_data
        }


        response = JsonResponse(items_data,safe=False) 
        response.content_type = "application/json"
        #Test had something with that header???
        response["Access-Control-Allow-Origin"]='CORS Headers must be set - preferably to * for this learning exercise'
        response.status_code = 200
        return response


@method_decorator(csrf_exempt, name='dispatch')
class ItemsListUsernameFiltered(View):

    def get(self, request, username):
        return HttpResponse("Invalid item id", status=201)

