
def calculate_footprint(inputs):
    emission_factors = {
        'electricity': 0.4,
        'gas': 0.2,
        'oil': 0.27,
        'car': 0.2,
        'flight': 0.25,
        'diet': {
            'omnivore': 2500,
            'vegetarian': 1700,
            'vegan': 1000
        }
    }

    electricity_emissions = inputs['electricity_kwh'] * emission_factors['electricity'] / 1000
    heating_emissions = inputs['heating_kwh'] * emission_factors.get(inputs['heating_type'], 0.2) / 1000
    car_emissions = inputs['car_km'] * emission_factors['car'] / 1000
    flight_emissions = inputs['flights_km'] * emission_factors['flight'] / 1000
    diet_emissions = emission_factors['diet'].get(inputs['diet_type'], 2500) / 1000

    total = electricity_emissions + heating_emissions + car_emissions + flight_emissions + diet_emissions

    return {
        'electricity': electricity_emissions,
        'heating': heating_emissions,
        'car': car_emissions,
        'flights': flight_emissions,
        'diet': diet_emissions,
        'total': total
    }

if __name__ == "__main__":
    example_inputs = {
        'electricity_kwh': 3000,
        'heating_kwh': 5000,
        'heating_type': 'gas',
        'car_km': 8000,
        'flights_km': 2000,
        'diet_type': 'omnivore'
    }
    result = calculate_footprint(example_inputs)
    print("Test output:", result)
    assert isinstance(result, dict)
    assert 'total' in result
    print("All tests passed.")
