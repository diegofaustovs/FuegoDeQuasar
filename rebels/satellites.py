class Kenobi:
    x = -500
    y = -200

    def __init__(self, distance, message):
        self.distance = distance
        self.message = message

    def __str__(self):
        return f'Kenobi X: {self.x}, Y: {self.y}, Distance: {self.distance}, Message: {self.message}'

    def __repr__(self):
        return f'satellites.Sato(X={self.x}, Y={self.y}, Distance={self.distance}, Message={self.message})'


class Skywalker:
    x = 100
    y = -100

    def __init__(self, distance, message):
        self.distance = distance
        self.message = message

    def __str__(self):
        return f'Skywalker X: {self.x}, Y: {self.y}, Distance: {self.distance}, Message: {self.message}'

    def __repr__(self):
        return f'satellites.Sato(X={self.x}, Y={self.y}, Distance={self.distance}, Message={self.message})'


class Sato:
    x = 500
    y = 100

    def __init__(self, distance, message):
        self.distance = distance
        self.message = message

    def __str__(self):
        return f'Sato X: {self.x}, Y: {self.y}, Distance: {self.distance}, Message: {self.message}'

    def __repr__(self):
        return f'satellites.Sato(X={self.x}, Y={self.y}, Distance={self.distance}, Message={self.message})'
