
from.models import Category, Products
from rest_framework.views import APIView
from rest_framework.response import Response


# Create your models here.
class CategoryListApiView(APIView):

    def get (self,request):
        categories=Category.objects.all()
        data=[]
        for cat in categories:
            data.append({
                "id":cat.id,
                "name":cat.name
            })
        return Response(data)

    def post(self,request):
        category_name=request.data.get("name")
        if category_name:
            Category.objects.update_or_create(
                name=category_name
            )
        return Response({
            "message":"category created successfully"
        })

    def delete(self,request,pk):

        category=Category.objects.filter(id=pk).first()
        if category:
            msg="category deleted successfully"
            category.delete()
        else:
            msg="category deleted successfully"
        return Response({
            "message" :msg
        })  

    def put (self,request,pk):
        category=Category.objects.filter(id=pk).first()
        if category:
            new_nam =request.data.get("name")
            if new_name:
                category.name=new_nam
                category.save()
            msg='category updated successfully'

        else:
            msg='category not found'
        return Response({
            'message':msg
        })    


           



