from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import HttpResponse
from .models import Vehicle
from .serializers import VehicleListSerializer, VehicleCreateSerializer
from datetime import datetime
from django.forms import ValidationError
from rest_framework import status

#1. GET Method - Heartbeat of the server. It return with epoch time.
@api_view(['GET'])
def heartbeat(request):
    try:
        current_time = datetime.now()
        microseconds = int(current_time.timestamp() * 1000000)
        return HttpResponse(microseconds, content_type='text/plain', status=200)
    except SystemError:
        return Response({"Internal server error."}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    except Exception as e:
        return Response({'Unexpected error: {}'.format(str(e))},status=status.HTTP_500_INTERNAL_SERVER_ERROR)

#2. GET Method - It returns all vehicles information.
@api_view(['GET'])
def vehicles_list(request):
    try:
        vehicles = Vehicle.objects.all()
        serializer = VehicleListSerializer(vehicles, many=True) 
        if not vehicles:  # Check if the list is empty
            return Response({"No vehicles available."}, status=status.HTTP_404_NOT_FOUND)
        else:
            return Response(serializer.data, status=status.HTTP_200_OK)
    except SystemError:
        return Response({"Internal server error."}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    except Exception as e:
        return Response({'Unexpected error: {}'.format(str(e))},status=status.HTTP_500_INTERNAL_SERVER_ERROR)

#3. GET Method - It returns specific vehicle information.
@api_view(['GET'])
def vehicle_detail(request,vehicle_id):
    try:
        vehicle = Vehicle.objects.get(id=vehicle_id)
        serializer = VehicleListSerializer(vehicle, many=False) 
        return Response(serializer.data, status=status.HTTP_200_OK)
    except ValueError:
        return Response({"Bad request. Likely data validation error. The vehicle id must be a number."}, status=status.HTTP_400_BAD_REQUEST) 
    except Vehicle.DoesNotExist:
        return Response({"Resource not found. Specified vehicle is not avaliable."}, status=status.HTTP_404_NOT_FOUND)
    except SystemError:
        return Response({"Internal server error."}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    except Exception as e:
        return Response({'Unexpected error: {}'.format(str(e))},status=status.HTTP_500_INTERNAL_SERVER_ERROR)

#4. POST Method - It create a new vehicle information.
@api_view(['POST'])
def vehicle_create(request):
    try:
        serializer = VehicleCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except ValidationError as e:
        return Response({'Error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
    except SystemError:
        return Response({"Internal server error."}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    except Exception as e:
        return Response({'Unexpected error: {}'.format(str(e))}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


#5. PUT Method - It create new vehicle if not exist, update if exist.
@api_view(['PUT'])
def vehicle_create_or_update(request, vehicle_id):
    try:
        vehicle = Vehicle.objects.filter(id=vehicle_id).first()
        if vehicle is None:
            serializer = VehicleCreateSerializer(data=request.data)
        else:
            serializer = VehicleCreateSerializer(instance=vehicle, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK if vehicle else status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except SystemError:
        return Response({"Internal server error."}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    except Exception as e:
        return Response({'Unexpected error: {}'.format(str(e))}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

#6. PATCH and GET Method - It update vehicle information.
@api_view(['PATCH', 'GET'])
def vehicle_update(request, vehicle_id):
    try:
        vehicle = Vehicle.objects.get(id=vehicle_id)
        serializer = VehicleCreateSerializer(instance=vehicle, data=request.data, partial=True) 
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except ValueError:
        return Response({"Bad request. Likely data validation error. The vehicle id must be a number."}, status=status.HTTP_400_BAD_REQUEST)
    except Vehicle.DoesNotExist:
        return Response({"Vehicle not found"}, status=status.HTTP_404_NOT_FOUND)
    except SystemError:
        return Response({"Internal server error."}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    except Exception as e:
        return Response({'Unexpected error: {}'.format(str(e))}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

#7. DELETE Method - It delete vehicle information.
@api_view(['DELETE', 'GET'])
def vehicle_delete(request, vehicle_id):
    try:
        vehicle = Vehicle.objects.get(id=vehicle_id)
        serializer = VehicleListSerializer(vehicle)
        if request.method == 'DELETE':
            vehicle.delete()
            return Response("Vehicle successfully deleted!", status=status.HTTP_204_NO_CONTENT)
        elif request.method == 'GET':
            return Response(serializer.data)
    except ValueError:
        return Response({"Bad request. Likely data validation error. The vehicle id must be a number."}, status=status.HTTP_400_BAD_REQUEST)
    except Vehicle.DoesNotExist:
        return Response({"Vehicle not found."}, status=status.HTTP_404_NOT_FOUND) 
    except SystemError:
        return Response({"Internal server error."}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    except Exception as e:
        return Response({'Unexpected error: {}'.format(str(e))}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)