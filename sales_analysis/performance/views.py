import csv
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from performance.models import SalesData
from rest_framework.response import Response
from rest_framework.decorators import api_view
from performance.models import SalesData
from performance.services import generate_feedback

@api_view(['GET'])
def performance_feedback(request, employee_id):
    data = SalesData.objects.filter(employee_id=employee_id).values()
    feedback = generate_feedback(data)
    return Response({'feedback': feedback})

@api_view(['GET'])
def team_performance(request):
    data = SalesData.objects.all().values()
    feedback = generate_feedback(data)
    return Response({'feedback': feedback})

@api_view(['GET'])
def performance_trends(request):
    # Implement trends and forecasting logic here
    return Response({'message': 'Trends and forecasting not implemented yet'})


@csrf_exempt
def load_sales_data(request):
    if request.method == 'POST':
        # Open and read the CSV file
        with open('sales_performance_data.csv', mode='r') as file:
            reader = csv.DictReader(file)
            # Clear existing data
            SalesData.objects.all().delete()
            # Load new data
            for row in reader:
                SalesData.objects.create(**row)
        return JsonResponse({'status': 'success', 'message': 'Data loaded successfully'})
    return JsonResponse({'status': 'error', 'message': 'Invalid request method'})
