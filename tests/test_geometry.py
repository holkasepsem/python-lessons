import pytest


from geometry.geometry import Point

def test_should_initialize_point_coordinates():
	p = Point(1, 2, 3)
	assert p.x1 == 1.0
	assert p.x2 == 2.0
	assert p.x3 == 3.0

def test_should_return_right_point_dimmension():
	p = Point(1)
	assert p.dimension == 1

	p2 = Point(0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
	assert p2.dimension == 10

def test_should_not_change_point_dimension():
	p = Point(1, 2, 3)        # dimension is 3
	p.coordinates = (1, 2, 3, 4)
	assert p.dimension == 3   # dimension is still 3

@pytest.mark.xfail(raises=ValueError)
def test_should_not_initialize_point():
	p = Point()



