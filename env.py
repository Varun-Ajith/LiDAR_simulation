import math
import pygame


class BuildEnvironment:
    def __init__(self, mapDimensions):
        pygame.init()
        self.pointCloud = []
        self.externalMap = pygame.image.load('map.png')
        self.maph, self.mapw = mapDimensions
        self.mapWindowName = 'LiDAR Simulation'
        pygame.display.set_caption(self.mapWindowName)
        self.map = pygame.display.set_mode((self.mapw, self.maph))
        self.map.blit(self.externalMap, (0, 0))

        self.Black = (0, 0, 0)
        self.White = (255, 255, 255)
        self.Blue = (0, 0, 255)
        self.Green = (0, 255, 0)
        self.Red = (255, 0, 0)
        self.Grey = (70, 70, 70)

    def AD2pos(self, distance, angle, robotPosition):
        x = distance * math.cos(angle) + robotPosition[0]
        y = -distance * math.sin(angle) + robotPosition[1]
        return (int(x), int(y))

    def dataStorage(self, data):
        print(len(self.pointCloud))
        for element in data:
            point = self.AD2pos(element[0], element[1], element[2])
            if point not in self.pointCloud:
                self.pointCloud.append(point)

    def show_sensorData(self):
        self.infoMap = self.map.copy()
        for point in self.pointCloud:
            self.infoMap.set_at((int(point[0]), int(point[1])), (255, 0, 0))
