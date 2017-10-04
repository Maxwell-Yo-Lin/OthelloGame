# Maxwell Lin 46268364

import math



class Point:
    def __init__(self, frac_x: float, frac_y: float):
        '''
        Initializes a Point object, given its fractional coordinates.
        '''
        self._frac_x = frac_x
        self._frac_y = frac_y


    def frac(self) -> (float, float):
        '''
        Returns an (x, y) tuple that contains fractional coordinates
        for this Point object.
        '''
        return (self._frac_x, self._frac_y)


    def pixel(self, width: float, height: float) -> (float, float):
        '''
        Returns an (x, y) tuple that contains pixel coordinates for
        this Point object.  The total_size parameter specifies the
        total size, in pixels, of the area in which the point needs
        to be specified -- this is used to make the appropriate
        conversion, since the pixel position of a fractional point
        changes as the size changes.
        '''
        return (int(self._frac_x * width), int(self._frac_y * height))


    def frac_distance_from(self, p: 'Point') -> float:
        '''
        Given another Point object, returns the distance, in
        terms of fractional coordinates, between this Point and the
        other Point.
        '''

        # Per the Pythagorean theorem from mathematics, the distance
        # between two points is the square root of the sum of the
        # squares of the differences in the x- and y-coordinates.
        return math.sqrt(
            (self._frac_x - p._frac_x) * (self._frac_x - p._frac_x)
            + (self._frac_y - p._frac_y) * (self._frac_y - p._frac_y))

        # Note, too, that there's a function in the Python standard
        # library, math.hypot, that does exactly this calculation.



# These two functions are used to create Points that are either
# being created from fractional or pixel coordinates.  Given these
# two functions, we'll never create Point objects by calling the
# Point constructor; instead, we'll just call the appropriate
# of these two functions, depending on whether we have fractional or
# pixel coordinates already.
#
# You might be wondering why we would solve the problem this way,
# instead of just using the Point constructor.  The problem is that
# the Point constructor doesn't make clear, when looking at it, whether
# its parameters are fractional or pixel coordinates.  If, instead, we
# say "point.from_frac" or "point.from_pixel", what we've written reads
# like English (e.g., "Make me a point from a fractional coordinate.").


def from_frac(frac_x: float, frac_y: float) -> Point:
    '''Builds a Point given fractional x and y coordinates.'''
    return Point(frac_x, frac_y)



def from_pixel(pixel_x: float, pixel_y: float, width: float, height: float) -> Point:
    '''
    Builds a Point given pixel x and y coordinates, along with
    the width and height of the area (necessary for conversion
    to fractional).
    '''
    return Point(pixel_x / width, pixel_y / height)
