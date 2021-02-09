import math


def calculate_location(satellites):
    return None


def get_intersecting_points(p1, p2, p3):
    A = 2*p2.x - 2*p1.x
    B = 2*p2.y - 2*p1.y
    C = pow(p1.distance, 2) - pow(p2.distance, 2) - pow(p1.x, 2) + pow(p2.x, 2) - pow(p1.y, 2) + pow(p2.y, 2)
    D = 2*p3.x - 2*p2.x
    E = 2*p3.y - 2*p2.y
    F = pow(p2.distance, 2) - pow(p3.distance, 2) - pow(p2.x, 2) + pow(p3.x, 2) - pow(p2.y, 2) + pow(p3.y, 2)
    x = (C*E - F*B) / (E*A - B*D)
    y = (C*D - A*F) / (B*D - A*E)
    return x, y
