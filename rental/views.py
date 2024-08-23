from rest_framework.decorators import api_view
from .serializers import RentalFormSerializer
from rest_framework.response import Response
from rest_framework import status
from .models import RentalForm

@api_view(['GET','POST','DELETE'])
def get_create_delete_rentalform(request):
    if request.method == 'POST':
        serializer = RentalFormSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        else:
            return Response("Invalid Data", status=status.HTTP_400_BAD_REQUEST)
        
    elif request.method == 'GET':
        query = request.GET.get('orderNumber',None)

        if query is None:
            return Response("주문번호가 필요합니다.", status=status.HTTP_400_BAD_REQUEST)
        
        rentalForm = RentalForm.objects.get(orderNumber=query)
        serializer = RentalFormSerializer(instance=rentalForm)

        return Response(serializer.data, status=status.HTTP_200_OK)
    
    else:
        query = request.GET.get('orderNumber',None)

        if query is None:
            return Response("주문번호가 필요합니다.", status=status.HTTP_400_BAD_REQUEST)
        
        rental_form = RentalForm.objects.get(orderNumber=query)
        rental_form.delete()

        return Response('해당하는 대여 신청이 삭제되었습니다.',status=status.HTTP_200_OK)


    