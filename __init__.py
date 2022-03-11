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

  return (math.atan2(-x, y), math.asin(z))
