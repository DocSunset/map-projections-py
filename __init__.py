"""Functions for converting geographic coordinates to 2D coordinates"""

import math

def vector_to_coordinates(vector):
  """Convert a vector with 3 values to latitude and longitude

  The prime meridian assumed to pass through the positive y-axis, the equator
  is assumed to lie on the x-y plane, and the poles are assumed to lie on the
  z-axis. Positive longitudes are east of the prime meridian, and positive
  latitudes are north of the equator.

  :param vector: a list, tuple, or other indexable object with 3 numerical values
  :returns: a tuple of the form (latitude, longitude), in radians.
  """

  norm = math.sqrt(vector[0] * vector[0] + vector[1] * vector[1] + vector[2] * vector[2])
  x = vector[0] / norm
  y = vector[1] / norm
  z = vector[2] / norm

  return (math.asin(z), math.atan2(-x, y))

def radians_to_degrees(coordinates):
  """ Convert a (latitude, longitude) coordinate pair from radians to degrees

  :param coordinates: the input latitude and longitude in radians
  :returns: a tuple (latitude, longitude) in degrees
  """
  return coordinates[0] / math.pi * 180, coordinates[1] / math.pi * 180

def degrees_to_radians(coordinates):
  """ Convert a (latitude, longitude) coordinate pair from degrees to radians

  :param coordinates: the input latitude and longitude in degrees
  :returns: a tuple (latitude, longitude) in radians
  """
  return coordinates[0] / 180 * math.pi, coordinates[1] / 180 * math.pi

def forward_equirectangular(coordinates, screen_size, border=10):
  """ A simple cylindrical projection

  https://en.wikipedia.org/wiki/Equirectangular_projection

  :param coordinates: the coordinates to project in radians
  :param screen_size: the size of the output rectangular region, e.g. (width, height) in pixels
  :returns: the cartesian coordinate of the projected point
  """
  lat, lon = coordinates
  width, height = screen_size
  width = width - 2*border
  height = height - 2*border
  if width < 2 * height:
    return (lon / math.pi * width/2 + width/2 + border, lat / math.pi * width/2 + height/2 + border)
  else:
    return (lon / (math.pi/2) * height/2 + width/2 + border, lat / (math.pi/2) * height/2 + height/2 + border)
