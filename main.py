import pygame.event
import env
import sensors

environment = env.BuildEnvironment((600, 1200))
environment.originalMap = environment.map.copy()
laser = sensors.LaserSensor(200, environment.originalMap, uncertainity=(0.5, 0.01))
environment.map.fill((0, 0, 0))
environment.infoMap = environment.map.copy()

running = True
while running:
    sensorOn = False
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if pygame.mouse.get_focused():
            sensorOn = True
        elif not pygame.mouse.get_focused():
            sensorOn = False
    if sensorOn:
        position = pygame.mouse.get_pos()
        laser.position = position
        sensor_data = laser.sense_obstacles()
        if sensor_data:
            environment.dataStorage(sensor_data)
            environment.show_sensorData()
    environment.map.blit(environment.infoMap, (0, 0))
    pygame.display.update()
