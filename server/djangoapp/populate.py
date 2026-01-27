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
        # Nissan - Mix of SUV, Coupe, Hatchback
        {"name": "Pathfinder", "type": "SUV", "year": 2023, "fuel": "Gasoline", "car_make": car_make_instances[0]},
        {"name": "Z-Proto", "type": "COUPE", "year": 2023, "fuel": "Gasoline", "car_make": car_make_instances[0]},
        {"name": "Leaf", "type": "HATCHBACK", "year": 2023, "fuel": "Electric", "car_make": car_make_instances[0]},
        
        # Mercedes - Mix of SUV, Convertible, Sedan
        {"name": "A-Class", "type": "SUV", "year": 2023, "fuel": "Diesel", "car_make": car_make_instances[1]},
        {"name": "SL-Roadster", "type": "CONVERTIBLE", "year": 2023, "fuel": "Gasoline", "car_make": car_make_instances[1]},
        {"name": "EQS", "type": "SEDAN", "year": 2023, "fuel": "Electric", "car_make": car_make_instances[1]},
        
        # Audi - Mix of Sedan, Coupe, Wagon
        {"name": "A4", "type": "SEDAN", "year": 2023, "fuel": "Gasoline", "car_make": car_make_instances[2]},
        {"name": "TT", "type": "COUPE", "year": 2023, "fuel": "Gasoline", "car_make": car_make_instances[2]},
        {"name": "RS6", "type": "WAGON", "year": 2023, "fuel": "Gasoline", "car_make": car_make_instances[2]},
        
        # Kia - Mix of SUV, Wagon, Sedan
        {"name": "Sorrento", "type": "SUV", "year": 2023, "fuel": "Gasoline", "car_make": car_make_instances[3]},
        {"name": "Carnival", "type": "WAGON", "year": 2023, "fuel": "Gasoline", "car_make": car_make_instances[3]},
        {"name": "Cerato", "type": "SEDAN", "year": 2023, "fuel": "Gasoline", "car_make": car_make_instances[3]},
        
        # Toyota - Mix of Hatchback, Sedan, Truck
        {"name": "Corolla", "type": "HATCHBACK", "year": 2023, "fuel": "Gasoline", "car_make": car_make_instances[4]},
        {"name": "Camry", "type": "SEDAN", "year": 2023, "fuel": "Gasoline", "car_make": car_make_instances[4]},
        {"name": "Hilux", "type": "TRUCK", "year": 2023, "fuel": "Diesel", "car_make": car_make_instances[4]},
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