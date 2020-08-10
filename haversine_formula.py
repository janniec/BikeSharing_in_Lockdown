from math import radians, cos, sin, atan2, sqrt, ceil
# The haversine formula determines the great-circle distance between two points on a sphere given their longitudes and latitudes.

def lat_lng_distance(start_lat, start_lng, end_lat, end_lng):
    '''
    start_lat [float] = latitude (north-south position) of the location 1
    start_lng [float] = longitude (east-west position) of the location 1
    end_lat [float] = latitude (north-south position) of the trip location 2
    end_lng [float] = longitude (east-west position) of the trip location 2
    Function to calculate distance between two latitude-longitude points in miles.
    distance_miles [float] = distance in terms of miles
    '''
    # convert from degrees to radians
    start_lat = radians(start_lat)
    start_lng = radians(start_lng)
    end_lat = radians(end_lat)
    end_lng = radians(end_lng)
    
    # distance between the latitudes
    dlat = end_lat - start_lat
    # distance between the longitudes
    dlon = end_lng - start_lng 
    
    # haversine formula for calculating distance between lat long points
    a = sin(dlat / 2)**2 + cos(start_lat) * cos(end_lat) * sin(dlon / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1-a)) 
    
    # convert circle distance to miles
    earth_radius_miles = 3956
    distance_miles = c * earth_radius_miles
    
    return distance_miles