"""
Ukázka dědičnosti.

Abstract base classes (ABCs) enforce that derived classes implement
particular methods from the base class.
"""


class Parent_1(object):
    def print_name(self):
        print("I am Parent1")


class Parent_2():
    def print_name(self):
        print("I am Parent2")

    def print_decorated_name(self):
        """
        Musí být implementována v každém potomkovi.
        Avšak dokud nebudeme volat metodu potomka, který nemá implementovanou
        tuto metodyu, neuvidíme žádný Error.
        """
        raise NotImplementedError


class Child_1(Parent_1):
    pass


class Child_2(Parent_2):
    def print_decorated_name(self):
        print("*** I am Child2 ***")


class Child_12(Parent_1, Parent_2):
    pass


class Child_21(Parent_2, Parent_1):
    pass


if __name__ == "__main__":

    c1 = Child_1()
    c2 = Child_2()

    c1.print_name()
    c2.print_name()

    c2.print_decorated_name()

    # -------------

    c12 = Child_12()
    c21 = Child_21()

    c12.print_name()
    c21.print_name()
