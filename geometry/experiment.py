
def calculate_rectangle_points(p1, p2):
    """
    Zjistí souřadnice koncových bodů druheé úhlopříčky čtyřúhelníku.
    
    obrazovka
    +----------------------+ 
    |  u2              p2  |
    |    +------------+    |
    |    |            |    |
    |    |            |    |
    |    |            |    |
    |    +------------+    |
    |  p1              u1  |
    +----------------------+
    0,0

    :param: Bod v ploše `p1` reprezentovaný objektem s operátorem `[]` (object is subscriptable).
    :param: Bod v ploše `p2` reprezentovaný objektem s operátorem `[]` (object is subscriptable).
    :return: Dva koncové body druhé úhlopříčky `u1` a `u2` reprezentované n-ticemi.
    """
    a, b = [], []
   
    for e1, e2 in zip(p1, p2):
        try:
            a.append(float(e1))
            b.append(float(e2))
        except TypeError:
            raise

    u1 = b[0], a[1]
    u2 = a[0], b[1]

    return u1, u2


def test_should_calculate_rectangle_points():
    try:
        p1 = calculate_rectangle_points((0,0), (0,0))
        assert ((0,0), (0,1)) == p1

        p2 = calculate_rectangle_points()

    except AssertionError:
        print(points)
        raise


points = calculate_rectangle_points((1,2), (3,4))


print(points)
print(type(points))
# ==============================
print("ok")

test_should_calculate_rectangle_points()
