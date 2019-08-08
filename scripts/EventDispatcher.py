""" Unique properties of events for further dispatching """
event_props = {
    '0': ['battery', 'mision_id'], # Mission started
    '1': ['gps_data'], # Vehicle deployed 
    '2': ['gps_data'], # Take off 
    '3': ['mision_id'], # Mission ended
    '4': ['gps_data', 'mision_id'], # Destination reached
    '5': ['battery'] # Low battery
}

""" List of Event types for dispatching """
event_list = ['MisionStartedEvent',  'VehicleDeployedEvent', 'TakeOffEvent', 'MisionEndedEvent',  'DestinationReachedEvent', 'LowBatteryEvent']
