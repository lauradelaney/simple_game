def main():
    intro()

class Room():
    name  : str
    north : 'Room'
    east  : 'Room'
    south : 'Room'
    west  : 'Room'

    def __init__(self, name, north=None, east=None, south=None, west=None):
        self.name = name
        self.north = north
        self.east = east
        self.south = south

        if north:
            north.self = self
        if east:
            east.self = self
        if south:
            south.self = self
        if west:
            west.self = self

    def movement(self,direction):
        if direction in ['north','south','east','west']:
            return getattr(self, direction)
        else:
            return None

    def __str__(self):
        return self.name




class Building():
    current_room: Room
    rooms: list[rooms]

# if __name__ == "__main__":
 #   main()
