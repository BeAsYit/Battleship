class Ship:
    def __init__(self, bow, horizontal, length, hit):
        self.bow = bow
        self.horizontal = horizontal
        self.length = length
        self.hit = hit

    def shoot_at(self, cords):
        pass


class Field:
    def __init__(self, ships):
        self.ships = ships

    def shoot_at(self, cords):
        pass

    def field_without_ships(self):
        pass

    def field_with_ships(self):
        pass


class Player:
    def __init__(self, name):
        self.name = name

    def read_position(self):
        pass


class Game:
    def __init__(self, field, players, current_player):
        self.field = field
        self.players = players
        self.current_player = current_player

    def read_position(self):
        pass

    def field_without_ships(self, damaged):
        pass

    def field_with_ships(self):
        pass
