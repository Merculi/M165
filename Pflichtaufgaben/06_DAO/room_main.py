from dao_room import DaoRoom
from room import Room


dao_room = DaoRoom("mongodb://localhost:27017/")

room = Room("Pilatus", 12, True)
room_id = dao_room.create(room)

updated_room = Room("Pilatus", 16, True)
dao_room.update(room_id, updated_room)

all_rooms = dao_room.read()

for room in all_rooms:
    print(room.__dict__)

dao_room.delete(room_id)
