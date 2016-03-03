import pytest

from geometry.geometry import Point, Line2D, Canvas

# Point #######################################################################

def test_should_initialize_point_coordinates():
	p = Point(1, 2, 3)
	assert p.x1 == 1.0
	assert p.x2 == 2.0
	assert p.x3 == 3.0

def test_should_return_right_point_dimension():
	p = Point(1)
	assert p.dimension == 1

	p2 = Point(0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
	assert p2.dimension == 10

# def test_should_not_change_point_dimension():
# 	p = Point(1, 2, 3) 			# p dimension is 3
# 	p.coordinates = (1, 2, 3, 4)
# 	assert p.dimension == 3 	# dimension is still 3

@pytest.mark.xfail(raises=ValueError)
def test_should_not_initialize_point():
	"""We cannot create a zero dimensional point"""
	p = Point()

def test_that_point_implements_getitem():
	p = Point(1, 2)
	assert p[0] == 1.0
	assert p[1] == 2.0


def test_that_point_implements_setitem():
	p = Point(1, 2)
	p[0] = 11
	assert p[0] == 11.0
	p[1] = 22
	assert p[1] == 22.0

# Line ########################################################################

def test_should_initialize_line_with_points_given_as_tuple():
	line = Line2D(p1=(1, 2), p2=(2, 3))
	assert line.p1 == (1, 2)
	assert line.p2 == (2, 3)


def test_should_initialize_line_with_3d_points():
	line = Line2D((1, 2, 3), (4, 5, 6))
	assert line.p1 == (1, 2)
	assert line.p2 == (4, 5)


@pytest.mark.xfail(raises=ValueError)
def test_should_not_initialize_line():
	line = Line2D((1, ), (2, ))

def test_should_initialize_canvas():
	canvas = Canvas(100, 100)
	assert canvas.width == 100
	assert canvas.heigtt == 100
