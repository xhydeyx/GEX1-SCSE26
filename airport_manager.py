######################## IMPORTANT ########################
""" Do not rename the variables or functions.
Do not change the function parameters.
Do not add input() calls inside airport_manager.py.
The file must be importable by the tests. """
###########################################################


airport_info = ("OUL", 1, "14-09-2026")
allowed_gates = {"A1", "A2", "A3", "A4", "B1", "B2"}
restricted_destinations = {"Moscow", "Pyongyang"}

flights = {
    "AY450": {
        "destination": "Helsinki",
        "departure": "08:30",
        "gate": "A2",
        "capacity": 5,
        "passengers": ["Alice Wong", "David Kim", "Fatima Ali"]
    },
    "SK271": {
        "destination": "Stockholm",
        "departure": "10:15",
        "gate": "B1",
        "capacity": 4,
        "passengers": ["Chen Wei", "George Smith"]
    },
    "LH2491": {
        "destination": "Munich",
        "departure": "12:40",
        "gate": "A4",
        "capacity": 5,
        "passengers": ["Hana Lee", "Maria Garcia", "Noah Wilson"]
    }
}

## Logic to find if a flight exists
def find_flight(flights, flight_number):
    if flights is None or flight_number is None:
        return None
    target = flight_number.strip().upper()
    for key in flights.keys():
        if key.strip().upper() == target:
            return key
    return None

## Logic to find if a passenger exists
def passenger_exists(passengers, passenger_name):
    if passengers is None or passenger_name is None:
        return False
    target = passenger_name.strip().lower()
    for p in passengers:
        if p.strip().lower() == target:
            return True
    return False

## Logic to check in a passenger
def check_in_passenger(
    flights,
    flight_number,
    passenger_name,
    restricted_destinations
):
    flight_key = find_flight(flights, flight_number)
    if flight_key is None:
        return "FLIGHT_NOT_FOUND"

    if passenger_name is None or passenger_name.strip() == "":
        return "EMPTY_NAME"

    flight = flights[flight_key]
    dest = flight.get("destination", "")
    if restricted_destinations:
        dest_upper = dest.strip().upper()
        for rd in restricted_destinations:
            if rd.strip().upper() == dest_upper:
                return "RESTRICTED"

    passengers = flight.get("passengers", [])
    if passenger_exists(passengers, passenger_name):
        return "DUPLICATE"

    capacity = flight.get("capacity", 0)
    if len(passengers) >= capacity:
        return "FULL"

    formatted_name = passenger_name.strip().title()
    passengers.append(formatted_name)
    return "OK"

## Logic to remove a passenger from a flight
def remove_passenger(
    flights,
    flight_number,
    passenger_name
):
    flight_key = find_flight(flights, flight_number)
    if flight_key is None:
        return "FLIGHT_NOT_FOUND"

    flight = flights[flight_key]
    passengers = flight.get("passengers", [])
    target = passenger_name.strip().lower()
    for i, p in enumerate(passengers):
        if p.strip().lower() == target:
            passengers.pop(i)
            return "OK"

    return "PASSENGER_NOT_FOUND"

# Logic to change the gate of a flight
def change_gate(
    flights,
    flight_number,
    new_gate,
    allowed_gates
):
    flight_key = find_flight(flights, flight_number)
    if flight_key is None:
        return "FLIGHT_NOT_FOUND"

    if not allowed_gates:
        return "INVALID_GATE"

    target_gate = new_gate.strip().upper()
    matched_gate = None
    for g in allowed_gates:
        if g.strip().upper() == target_gate:
            matched_gate = g
            break
    if matched_gate is None:
        return "INVALID_GATE"

    flights[flight_key]["gate"] = matched_gate
    return "OK"

# Logic to get the status of a flight
def flight_status(flight):
    if flight is None:
        return "AVAILABLE"
    capacity = flight.get("capacity", 0)
    passengers = flight.get("passengers", [])
    if capacity == 0:
        return "AVAILABLE"
    percentage = len(passengers) / capacity * 100
    if percentage >= 100:
        return "FULL"
    elif percentage >= 75:
        return "ALMOST FULL"
    else:
        return "AVAILABLE"

# Logic to get the sorted manifest of a flight
def sorted_manifest(
    flights,
    flight_number
):
    flight_key = find_flight(flights, flight_number)
    if flight_key is None:
        return None
    passengers = flights[flight_key].get("passengers", [])
    return sorted(passengers, key=lambda x: x.lower())

# Logic to get the total number of passengers across all flights
def total_passengers(flights):
    if not flights:
        return 0
    total = 0
    for flight in flights.values():
        total += len(flight.get("passengers", []))
    return total

# Logic to check if any flight is full
def any_full_flight(flights):
    if not flights:
        return False
    for flight in flights.values():
        capacity = flight.get("capacity", 0)
        passengers = flight.get("passengers", [])
        if len(passengers) >= capacity:
            return True
    return False

# Logic to check if all flights have at least one passenger
def all_flights_have_passengers(flights):
    if not flights:
        return True
    return all(len(flight.get("passengers", [])) > 0 for flight in flights.values())