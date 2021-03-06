import math


def calculate_location(p1, p2, p3):
    return get_intersecting_points(p1, p2, p3)
    # return get_intersecting_points_between_bases(p1, p2, p3)


# First approach for trilateration algorithm
def get_intersecting_points(p1, p2, p3):
    A = 2 * p2.x - 2 * p1.x
    B = 2 * p2.y - 2 * p1.y
    C = pow(p1.distance, 2) - pow(p2.distance, 2) - pow(p1.x, 2) + pow(p2.x, 2) - pow(p1.y, 2) + pow(p2.y, 2)
    D = 2 * p3.x - 2 * p2.x
    E = 2 * p3.y - 2 * p2.y
    F = pow(p2.distance, 2) - pow(p3.distance, 2) - pow(p2.x, 2) + pow(p3.x, 2) - pow(p2.y, 2) + pow(p3.y, 2)
    x = (C * E - F * B) / (E * A - B * D)
    y = (C * D - A * F) / (B * D - A * E)
    return [round(x, 2), round(y, 2)]


# Second approach for trilateration algorithm
def get_distance_between_bases(b1, b2):
    return math.sqrt(pow((b1.x - b1.y), 2) + pow((b1.y - b2.y), 2))


def get_intersecting_points_between_two_bases(b1, b2):
    distance = get_distance_between_bases(b1, b2)
    if distance >= (b1.distance + b2.distance) or distance <= math.fabs(b1.distance - b2.distance):
        raise Exception("Can't resolve location - No intersection possible")
    a = (pow(b1.distance, 2) - pow(b2.distance, 2) + pow(distance, 2)) / (2 * distance)
    h = math.sqrt(pow(b1.distance, 2) - pow(a, 2))
    x0 = b1.x + a * (b2.x - b1.x) / distance
    y0 = b1.y + a * (b2.y - b1.y) / distance
    rx = -(b2.x - b1.x) * (h / distance)
    ry = -(b2.y - b1.x) * (h / distance)
    return [[round(x0 + rx, 2), round(y0 - ry, 2)], [round(x0 - rx, 2), round(y0 + ry, 2)]]


def get_intersecting_points_between_bases(b1, b2, b3):
    intersections = [get_intersecting_points_between_two_bases(b1, b2),
                     get_intersecting_points_between_two_bases(b2, b3),
                     get_intersecting_points_between_two_bases(b1, b3)]
    b4 = [x for n, x in enumerate(intersections) if x in intersections[:n]]
    return b4[0]
