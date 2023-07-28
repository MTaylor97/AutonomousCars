import pygame
from sys import exit
import numpy as np

pygame.init()

# create screen
screen = pygame.display.set_mode((1400, 900))
pygame.display.set_caption('Autonomous Cars')
clock = pygame.time.Clock()
background = pygame.image.load(
    'C:\\Users\\markt\\OneDrive - Loughborough University\\Personal Python Projects\\AutonomousCars\\Assets\\Background.png')

font = pygame.font.Font('freesansbold.ttf', 16)

# load vehicle asset images
car1 = pygame.image.load(
    'C:\\Users\\markt\\OneDrive - Loughborough University\\Personal Python Projects\\AutonomousCars\\Assets\\car1.png')
car1Down = pygame.image.load(
    'C:\\Users\\markt\\OneDrive - Loughborough University\\Personal Python Projects\\AutonomousCars\\Assets\\car1Down.png')
car1Left = pygame.image.load(
    'C:\\Users\\markt\\OneDrive - Loughborough University\\Personal Python Projects\\AutonomousCars\\Assets\\car1Left.png')
car1Right = pygame.image.load(
    'C:\\Users\\markt\\OneDrive - Loughborough University\\Personal Python Projects\\AutonomousCars\\Assets\\car1Right.png')
car2 = pygame.image.load(
    'C:\\Users\\markt\\OneDrive - Loughborough University\\Personal Python Projects\\AutonomousCars\\Assets\\car2.png')
car2Down = pygame.image.load(
    'C:\\Users\\markt\\OneDrive - Loughborough University\\Personal Python Projects\\AutonomousCars\\Assets\\car2Down.png')
car2Left = pygame.image.load(
    'C:\\Users\\markt\\OneDrive - Loughborough University\\Personal Python Projects\\AutonomousCars\\Assets\\car2Left.png')
car2Right = pygame.image.load(
    'C:\\Users\\markt\\OneDrive - Loughborough University\\Personal Python Projects\\AutonomousCars\\Assets\\car2Right.png')
van1 = pygame.image.load(
    'C:\\Users\\markt\\OneDrive - Loughborough University\\Personal Python Projects\\AutonomousCars\\Assets\\van1.png')
van1Down = pygame.image.load(
    'C:\\Users\\markt\\OneDrive - Loughborough University\\Personal Python Projects\\AutonomousCars\\Assets\\van1Down.png')
van1Left = pygame.image.load(
    'C:\\Users\\markt\\OneDrive - Loughborough University\\Personal Python Projects\\AutonomousCars\\Assets\\van1Left.png')
van1Right = pygame.image.load(
    'C:\\Users\\markt\\OneDrive - Loughborough University\\Personal Python Projects\\AutonomousCars\\Assets\\van1Right.png')

# define starting locations
startPointTop1 = [625, 0]
startPointTop2 = [685, 0]
startPointTop3 = [745, 0]
startPointBottom = [700, 900]
startPointLeft1 = [0, 373]
startPointLeft2 = [0, 432]
startPointLeft3 = [0, 493]
startPointRight = [1400, 450]


def CollisionDetector(smartcar, v1, v2, v3, v4):
    if v1 == 0:
        return
    for t in range(1, 180, 1):
        aX1 = smartcar.rect.topleft[0] + t * v1
        aY1 = smartcar.rect.topleft[1]
        aX2 = smartcar.rect.bottomright[0] + t * v1
        aY2 = smartcar.rect.bottomright[1]

        bX1 = dummy1.rect.topleft[0]
        bY1 = dummy1.rect.topleft[1] + t * v2
        bX2 = dummy1.rect.bottomright[0]
        bY2 = dummy1.rect.bottomright[1] + t * v2

        if (aX1 < bX2) and (aX2 > bX1) and (aY1 < bY2) and (aY2 > bY1):
            return True

        bX1 = dummy2.rect.topleft[0]
        bY1 = dummy2.rect.topleft[1] + t * v3
        bX2 = dummy2.rect.bottomright[0]
        bY2 = dummy2.rect.bottomright[1] + t * v3

        if (aX1 < bX2) and (aX2 > bX1) and (aY1 < bY2) and (aY2 > bY1):
            return True

        bX1 = dummy3.rect.topleft[0]
        bY1 = dummy3.rect.topleft[1] + t * v4
        bX2 = dummy3.rect.bottomright[0]
        bY2 = dummy3.rect.bottomright[1] + t * v4

        if (aX1 < bX2) and (aX2 > bX1) and (aY1 < bY2) and (aY2 > bY1):
            return True

    return False


# define Car class
class Car(pygame.sprite.Sprite):
    def __init__(self, x, y, direction):
        self.type = "car1"
        self.direction = direction
        self.model = car1
        self.direction = "Down"
        self.speedX = 5
        self.speedY = 5
        self.rect = self.model.get_rect()
        self.rect.x = x
        self.rect.y = y

    # method to draw car to background
    def Draw(self, surface):
        surface.blit(self.model, (self.rect.x, self.rect.y))
        # pygame.draw.rect(surface, "red", width=1, rect=[self.rect.topleft[0], self.rect.topleft[1], self.rect.width, self.rect.height])

    # method to drive the car vertically one 'step' of speed
    def DriveVertically(self):
        # choose the correct asset to display
        if (self.type == "car1") and (self.speedY < 0):
            self.model = car1
        elif (self.type == "car1") and (self.speedY > 0):
            self.model = car1Down
        elif (self.type == "car2") and (self.speedY < 0):
            self.model = car2
        elif (self.type == "car2") and (self.speedY > 0):
            self.model = car2Down
        elif (self.type == "van1") and (self.speedY < 0):
            self.model = van1
        elif (self.type == "van1") and (self.speedY > 0):
            self.model = van1Down
        # update car objects vertical position
        self.rect.y = self.rect.y + self.speedY
        self.Draw(screen)

    # method to drive the car horizontally one 'step' of speed
    def DriveHorizontally(self):
        # choose the correct asset to display
        if (self.type == "car1") and (self.speedX < 0):
            self.model = car1Left
        elif (self.type == "car1") and (self.speedX > 0):
            self.model = car1Right
        elif (self.type == "car2") and (self.speedX < 0):
            self.model = car2Left
        elif (self.type == "car2") and (self.speedX > 0):
            self.model = car2Right
        elif (self.type == "van1") and (self.speedX < 0):
            self.model = van1Left
        elif (self.type == "van1") and (self.speedX > 0):
            self.model = van1Right
        # update car objects horizontal position
        self.rect.x = self.rect.x + self.speedX
        self.Draw(screen)


class SuperCar(Car):
    def __init__(self, x, y, direction):
        self.type = "car2"
        self.model = car2Right
        self.speedX = 7
        self.direction = direction
        self.direction = "Right"
        self.speedY = 5
        self.rect = self.model.get_rect()
        self.rect.x = x
        self.rect.y = y


class Van(Car):
    def __init__(self, x, y, direction):
        Car.__init__(self, x, y, direction)
        self.type = "van1"
        self.model = van1
        self.speedX = 4


smartcar1 = SuperCar(startPointLeft1[0], startPointLeft1[1], "Left")
smartcar2 = SuperCar(startPointLeft2[0], startPointLeft2[1], "Left")
smartcar3 = SuperCar(startPointLeft3[0], startPointLeft3[1], "Left")
dummy1 = Car(startPointTop1[0], startPointTop1[1], "Down")
dummy2 = Car(startPointTop2[0], startPointTop2[1], "Down")
dummy3 = Car(startPointTop3[0], startPointTop3[1], "Down")

crashed = False
while not crashed:

    # close the window and end the program if the user clicks the close button
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.blit(background, (0, 0))

    v1 = 10
    v2 = 10
    v3 = 7
    v4 = 9
    if smartcar1.direction == "Right":
        v1 = v1 * -1
    if dummy1.direction == "Up":
        v2 = v2 * -1
    if dummy2.direction == "Up":
        v3 = v3 * -1
    if dummy3.direction == "Up":
        v4 = v4 * -1

    while CollisionDetector(smartcar1, v1, v2, v3, v4):
        if v1 < 0:
            v1 = v1 + 1
        else:
            v1 = v1 - 1

    smartcar1.speedX = v1

    v1 = 8
    if smartcar2.direction == "Right":
        v1 = v1 * -1
    while CollisionDetector(smartcar2, v1, v2, v3, v4):
        if v1 < 0:
            v1 = v1 + 1
        else:
            v1 = v1 - 1

    smartcar2.speedX = v1

    v1 = 7
    if smartcar3.direction == "Right":
        v1 = v1 * -1
    while CollisionDetector(smartcar3, v1, v2, v3, v4):
        if v1 < 0:
            v1 = v1 + 1
        else:
            v1 = v1 - 1

    smartcar3.speedX = v1
    dummy1.speedY = v2
    dummy2.speedY = v3
    dummy3.speedY = v4

    if smartcar1.rect.x > 1400:
        smartcar1.speedX = smartcar1.speedX * -1
        smartcar1.direction = "Right"
    elif smartcar1.rect.x < 0:
        smartcar1.speedX = smartcar1.speedX * -1
        smartcar1.direction = "Left"
    smartcar1.DriveHorizontally()

    if smartcar2.rect.x > 1400:
        smartcar2.speedX = smartcar2.speedX * -1
        smartcar2.direction = "Right"
    elif smartcar2.rect.x < 0:
        smartcar2.speedX = smartcar2.speedX * -1
        smartcar2.direction = "Left"
    smartcar2.DriveHorizontally()

    if smartcar3.rect.x > 1400:
        smartcar3.speedX = smartcar3.speedX * -1
        smartcar3.direction = "Right"
    elif smartcar3.rect.x < 0:
        smartcar3.speedX = smartcar3.speedX * -1
        smartcar3.direction = "Left"
    smartcar3.DriveHorizontally()

    if dummy1.rect.y > 900:
        dummy1.speedY = dummy1.speedY * -1
        dummy1.direction = "Up"
    elif dummy1.rect.y < 0:
        dummy1.speedY = dummy1.speedY * -1
        dummy1.direction = "Down"
    dummy1.DriveVertically()

    if dummy2.rect.y > 900:
        dummy2.speedY = dummy2.speedY * -1
        dummy2.direction = "Up"
    elif dummy2.rect.y < 0:
        dummy2.speedY = dummy2.speedY * -1
        dummy2.direction = "Down"
    dummy2.DriveVertically()

    if dummy3.rect.y > 900:
        dummy3.speedY = dummy3.speedY * -1
        dummy3.direction = "Up"
    elif dummy3.rect.y < 0:
        dummy3.speedY = dummy3.speedY * -1
        dummy3.direction = "Down"
    dummy3.DriveVertically()

    if pygame.Rect.colliderect(dummy1.rect, smartcar1.rect) or pygame.Rect.colliderect(dummy2.rect,
                                                                                       smartcar1.rect) or pygame.Rect.colliderect(
            dummy3.rect, smartcar1.rect):
        crash = True

    # update everything
    pygame.display.update()
    clock.tick(60)

while True:
    print("There was a crash!")
