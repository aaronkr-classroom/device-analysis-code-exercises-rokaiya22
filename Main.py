from lib.room_sensor import RoomSensor

# Create RoomSensor objects
kitchen = RoomSensor("Kitchen", 31, 72, 180)
bedroom = RoomSensor("Bedroom", 24, 50, 300)
balcony = RoomSensor("Balcony", 28, 65, 150)

# Store them in a list
sensors = [kitchen, bedroom, balcony]

# Loop through and display results
for sensor in sensors:
    sensor.show_info()
    print(f"Comfort Level: {sensor.comfort_level()}")
    print(f"Light Status: {sensor.light_status()}")
    print()