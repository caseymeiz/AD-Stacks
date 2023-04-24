import carla

client = carla.Client('localhost', 2000)
client.set_timeout(2.0)
world = client.get_world()
vehicle = world.get_actors().filter('*vehicle*')[0]
vehicle_transform = vehicle.get_transform()
print(vehicle_transform.location)
