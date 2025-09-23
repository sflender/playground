

class Metro:
    def __init__(self):
        self.stations = {
            1: 'Station A',  # Zone 1
            2: 'Station B',  # Zone 1
            3: 'Station C',  # Zone 2
            4: 'Station D',  # Zone 2
            5: 'Station E',  # Zone 3
            6: 'Station F',  # Zone 3
            7: 'Station G',  # Zone 1
            8: 'Station H',  # Zone 2
            9: 'Station I',  # Zone 3
            10: 'Station J'   # Zone 1
        }
        self.zones = {
            1: [1, 2, 7, 10],
            2: [3, 4, 8],
            3: [5, 6, 9]
        }
        self.station_to_zone = {}
        for zone, stations in self.zones.items():
            for station in stations:
                self.station_to_zone[station] = zone

    def get_zone(self, station_id):
        return self.station_to_zone.get(station_id, None)


    def metro_fare(self,num_zones, rider_type):
        """
        Calculate the metro fare based on the number of zones traveled and the type of rider.

        Parameters:
        num_zones (int): The number of zones traveled (1, 2, or 3).
        rider_type (str): The type of rider ('adult', 'child', or 'senior').

        Returns:
        float: The fare for the trip.
        """
        if num_zones not in [1, 2, 3]:
            raise ValueError("num_zones must be 1, 2, or 3")
        
        if rider_type not in ['adult', 'child', 'senior']:
            raise ValueError("rider_type must be 'adult', 'child', or 'senior'")

        fare_chart = {
            'adult': {1: 2.50, 2: 3.75, 3: 5.00},
            'child': {1: 1.25, 2: 1.875, 3: 2.50},
            'senior': {1: 1.00, 2: 1.50, 3: 2.00}
        }

        return fare_chart[rider_type][num_zones]

    def calc_num_zones(self,entry_station_id, exit_station_id):
        """
        Calculate the number of zones traveled based on entry and exit station IDs.

        Parameters:
        entry_station_id (int): The ID of the entry station.
        exit_station_id (int): The ID of the exit station.

        Returns:
        int: The number of zones traveled (1, 2, or 3).
        """
        if not (1 <= entry_station_id <= 10) or not (1 <= exit_station_id <= 10):
            raise ValueError("Station IDs must be between 1 and 10")

        entry_zone = self.get_zone(entry_station_id)
        exit_zone = self.get_zone(exit_station_id)

        return abs(entry_zone - exit_zone) + 1
    

if __name__ == "__main__":
    metro = Metro()
    entry_station = 1  # Station A (Zone 1)
    exit_station = 5   # Station E (Zone 3)
    rider_type = 'adult'

    num_zones = metro.calc_num_zones(entry_station, exit_station)
    fare = metro.metro_fare(num_zones, rider_type)

    print(f"Entry Station: {metro.stations[entry_station]} (Zone {metro.get_zone(entry_station)})")
    print(f"Exit Station: {metro.stations[exit_station]} (Zone {metro.get_zone(exit_station)})")
    print(f"Number of Zones Traveled: {num_zones}")
    print(f"Rider Type: {rider_type.capitalize()}")
    print(f"Total Fare: ${fare:.2f}")