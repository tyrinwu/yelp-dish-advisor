from geopy.geocoders import Nominatim
from geopy.distance import vincenty

geolocator = Nominatim()

def get_gps_crd(address):
    """Return longitude and latitude of an address
    Arguments:
        address {str}
    """
    return geolocator.geocode(address)[1]

def get_distance(coord1, coord2):
    """Return the distance between 2 location in miles.

    Arguments:
        coord1 {Tuple[float, float]} -- GPS coordinate
        coord2 {Tuple[float, float]} -- GPS coordinate
    """
    return vincenty(coord1, coord2).miles