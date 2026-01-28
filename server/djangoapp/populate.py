from .models import CarMake, CarModel


def initiate():
    # 1. Prepare CarMake data
    car_make_data = [
        {"name": "NISSAN", "description": "Japanese technology", "country": "Japan"},
        {"name": "Mercedes", "description": "German luxury", "country": "Germany"},
        {"name": "Audi", "description": "German engineering", "country": "Germany"},
        {"name": "Kia", "description": "Korean technology", "country": "South Korea"},
        {"name": "Toyota", "description": "Japanese reliability", "country": "Japan"},
    ]

    car_make_instances = []
    for data in car_make_data:
        car_make_instances.append(
            CarMake.objects.create(
                name=data['name'],
                description=data['description'],
                country_of_origin=data['country']
            )
        )

    # 2. CarModel data to match all choices
    car_model_data = [
    {
        "name": "Pathfinder", "type": "SUV", "year": 2023, 
        "fuel": "Gasoline", "car_make": car_make_instances[0]
    },
    {
        "name": "Z-Proto", "type": "Coupe", "year": 2023, 
        "fuel": "Gasoline", "car_make": car_make_instances[0]
    },
    {
        "name": "Leaf", "type": "Hatchback", "year": 2023, 
        "fuel": "Electric", "car_make": car_make_instances[0]
    },
    {
        "name": "A-Class", "type": "SUV", "year": 2023, 
        "fuel": "Diesel", "car_make": car_make_instances[1]
    },
    {
        "name": "SL-Roadster", "type": "Convertible", "year": 2023, 
        "fuel": "Gasoline", "car_make": car_make_instances[1]
    },
    {
        "name": "EQS", "type": "Sedan", "year": 2023, 
        "fuel": "Electric", "car_make": car_make_instances[1]
    },
    {
        "name": "A4", "type": "Sedan", "year": 2023, 
        "fuel": "Gasoline", "car_make": car_make_instances[2]
    },
    {
        "name": "TT", "type": "Coupe", "year": 2023, 
        "fuel": "Gasoline", "car_make": car_make_instances[2]
    },
    {
        "name": "RS6", "type": "Wagon", "year": 2023, 
        "fuel": "Gasoline", "car_make": car_make_instances[2]
    },
    {
        "name": "Sorrento", "type": "SUV", "year": 2023, 
        "fuel": "Gasoline", "car_make": car_make_instances[3]
    },
    {
        "name": "Carnival", "type": "Wagon", "year": 2023, 
        "fuel": "Gasoline", "car_make": car_make_instances[3]
    },
    {
        "name": "Cerato", "type": "Sedan", "year": 2023, 
        "fuel": "Gasoline", "car_make": car_make_instances[3]
    },
    {
        "name": "Corolla", "type": "Hatchback", "year": 2023, 
        "fuel": "Gasoline", "car_make": car_make_instances[4]
    },
    {
        "name": "Camry", "type": "Sedan", "year": 2023, 
        "fuel": "Gasoline", "car_make": car_make_instances[4]
    },
    {
        "name": "Hilux", "type": "Truck", "year": 2023, 
        "fuel": "Diesel", "car_make": car_make_instances[4]
    },
]

    for data in car_model_data:
        CarModel.objects.create(
            name=data['name'],
            car_make=data['car_make'], 
            type=data['type'],
            year=data['year'],
            fuel_type=data['fuel'],
            dealer_id=1
        )
