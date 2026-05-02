import os
import sys
import django

sys.path.append(os.getcwd())
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'uniease.settings')
django.setup()

from campus.models import BusRoute

def update_bus_routes():
    # Clear existing routes to start fresh
    BusRoute.objects.all().delete()
    
    routes_data = [
        {
            'route_number': '51',
            'route_name': 'City Central to College (Morning)',
            'departure_time': '07:30:00',
            'arrival_time': '08:45:00',
            'stops': 'ocity -> venkatrama -> kashibugga -> pocahmmamaidan -> mgm -> ku-errgattugutta -> hasanparthy -> clg',
            'is_delayed': False
        },
        {
            'route_number': '51',
            'route_name': 'College to City Central (Evening)',
            'departure_time': '16:40:00',
            'arrival_time': '17:55:00',
            'stops': 'clg -> hasanparthy -> ku-errgattugutta -> mgm -> pocahmmamaidan -> kashibugga -> venkatrama -> ocity',
            'is_delayed': False
        },
        {
            'route_number': '52',
            'route_name': 'Railway Station to College',
            'departure_time': '08:15:00',
            'arrival_time': '09:00:00',
            'stops': 'Railway Station -> Hanamkonda -> MGM -> KU Cross -> College',
            'is_delayed': False
        },
        {
            'route_number': '53',
            'route_name': 'Airport to College',
            'departure_time': '07:45:00',
            'arrival_time': '09:15:00',
            'stops': 'Airport -> Madikonda -> Kazipet -> Hanamkonda -> College',
            'is_delayed': False
        }
    ]

    for data in routes_data:
        BusRoute.objects.create(**data)
    print("Bus routes updated successfully with bus numbers!")

if __name__ == "__main__":
    update_bus_routes()
