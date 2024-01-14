import pygame
from random import *
from pygame.locals import *
import sqlite3
import getpass


# Окно заставки
class InitialWindow:
    def __init__(self):
        pygame.mixer.pre_init(44100, -16, 1, 512)
        pygame.init()
        pygame.time.set_timer(pygame.USEREVENT, 2000)
        pygame.display.set_caption('SkyFarm_2')
        self.font = pygame.font.SysFont('arial', 30)

        self.main_clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((950, 600))
        for i in range(10000):
            self.screen.fill(pygame.Color('white'), (random() * 950, random() * 700, 1, 1))

        self.white = pygame.transform.scale(pygame.image.load('images/white.jpg').convert(), (170, 120))
        self.car = pygame.transform.scale(pygame.image.load('images/car.jpg').convert_alpha(), (170, 100))

        # Загружаем фотографии фонов для создания кнопок
        self.background1 = pygame.transform.scale(pygame.image.load('images/background_1.jpg').convert(), (150, 100))
        self.background2 = pygame.transform.scale(pygame.image.load('images/background_2.jpg').convert(), (150, 100))
        self.background3 = pygame.transform.scale(pygame.image.load('images/background_3.jpg').convert(), (150, 100))
        self.background4 = pygame.transform.scale(pygame.image.load('images/background_4.jpg').convert(), (150, 100))
        self.background5 = pygame.transform.scale(pygame.image.load('images/background_5.jpg').convert(), (150, 100))
        self.background6 = pygame.transform.scale(pygame.image.load('images/background_6.jpg').convert(), (150, 100))
        self.background7 = pygame.transform.scale(pygame.image.load('images/background_7.jpg').convert(), (150, 100))
        self.background8 = pygame.transform.scale(pygame.image.load('images/background_8.jpg').convert(), (150, 100))

        self.font = pygame.font.SysFont('arial', 30)
        self.click = False

        # Создание фона для кнопок
        self.white1 = pygame.Rect(90, 190, 170, 120)
        self.white2 = pygame.Rect(290, 190, 170, 120)
        self.white3 = pygame.Rect(490, 190, 170, 120)
        self.white4 = pygame.Rect(690, 190, 170, 120)
        self.white5 = pygame.Rect(90, 340, 170, 120)
        self.white6 = pygame.Rect(290, 340, 170, 120)
        self.white7 = pygame.Rect(490, 340, 170, 120)
        self.white8 = pygame.Rect(690, 340, 170, 120)

        self.button1 = pygame.Rect(100, 200, 150, 100)
        self.button2 = pygame.Rect(300, 200, 150, 100)
        self.button3 = pygame.Rect(500, 200, 150, 100)
        self.button4 = pygame.Rect(700, 200, 150, 100)
        self.button5 = pygame.Rect(100, 350, 150, 100)
        self.button6 = pygame.Rect(300, 350, 150, 100)
        self.button7 = pygame.Rect(500, 350, 150, 100)
        self.button8 = pygame.Rect(700, 350, 150, 100)

        self.run()

    def run(self):
        while True:
            # Размещение кнопок
            self.screen.blit(self.white, self.white1)
            self.screen.blit(self.white, self.white2)
            self.screen.blit(self.white, self.white3)
            self.screen.blit(self.white, self.white4)
            self.screen.blit(self.white, self.white5)
            self.screen.blit(self.white, self.white6)
            self.screen.blit(self.white, self.white7)
            self.screen.blit(self.white, self.white8)

            self.screen.blit(self.background1, self.button1)
            self.screen.blit(self.background2, self.button2)
            self.screen.blit(self.background3, self.button3)
            self.screen.blit(self.background4, self.button4)
            self.screen.blit(self.background5, self.button5)
            self.screen.blit(self.background6, self.button6)
            self.screen.blit(self.background7, self.button7)
            self.screen.blit(self.background8, self.button8)

            self.screen.blit(self.font.render('Select background:', 1, (255, 255, 255)), (350, 90))

            mx, my = pygame.mouse.get_pos()

            # Проверка условий: создается экземпляр класса Menu с выбранным фоном
            if self.button1.collidepoint((mx, my)):
                if self.click:
                    Menu()
            if self.button2.collidepoint((mx, my)):
                if self.click:
                    Menu('images/background_2.jpg')
            if self.button3.collidepoint((mx, my)):
                if self.click:
                    Menu('images/background_3.jpg')
            if self.button4.collidepoint((mx, my)):
                if self.click:
                    Menu('images/background_4.jpg')
            if self.button5.collidepoint((mx, my)):
                if self.click:
                    Menu('images/background_5.jpg')
            if self.button6.collidepoint((mx, my)):
                if self.click:
                    Menu('images/background_6.jpg')
            if self.button7.collidepoint((mx, my)):
                if self.click:
                    Menu('images/background_7.jpg')
            if self.button8.collidepoint((mx, my)):
                if self.click:
                    Menu('images/background_8.jpg')

            for event in pygame.event.get():
                if event.type == QUIT:
                    exit()
                if event.type == MOUSEBUTTONDOWN:
                    if event.button == 1:
                        self.click = True

            pygame.display.update()
            self.main_clock.tick(60)


# Окно Меню
class Menu:
    def __init__(self, fon='images/background_1.jpg'):
        pygame.mixer.pre_init(44100, -16, 1, 512)
        pygame.init()
        pygame.time.set_timer(pygame.USEREVENT, 2000)
        pygame.display.set_caption('SkyFarm_2')

        self.fon = fon

        self.main_clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((1000, 700))
        self.background = pygame.transform.scale(pygame.image.load(self.fon).convert(), (1000, 700))
        self.font = pygame.font.SysFont('arial', 30)
        self.button_image = pygame.transform.scale(pygame.image.load('images/button.jpg').convert_alpha(), (200, 50))

        self.click = False

        # Создание кнопок
        self.button1 = pygame.Rect(400, 250, 200, 50)
        self.button2 = pygame.Rect(400, 350, 200, 50)
        self.button3 = pygame.Rect(400, 450, 200, 50)

        self.run()

    def run(self):
        while True:
            self.screen.blit(self.background, (0, 0))
            mx, my = pygame.mouse.get_pos()

            # Создается экземпляр класса Main с соответствующим уровнем сложности
            if self.button1.collidepoint((mx, my)):
                if self.click:
                    Main(self.fon)
            if self.button2.collidepoint((mx, my)):
                if self.click:
                    Main(self.fon, normal=True)
            if self.button3.collidepoint((mx, my)):
                if self.click:
                    Main(self.fon, hard=True)

            # Отрисовка кнопок
            self.screen.blit(self.button_image, self.button1)
            self.screen.blit(self.button_image, self.button2)
            self.screen.blit(self.button_image, self.button3)

            self.screen.blit(self.font.render('Easy', 1, (255, 255, 255)), (460, 257))
            self.screen.blit(self.font.render('Normal', 1, (255, 255, 255)), (450, 357))
            self.screen.blit(self.font.render('Hard', 1, (255, 255, 255)), (465, 457))

            self.click = False
            for event in pygame.event.get():
                if event.type == QUIT:
                    exit()
                if event.type == MOUSEBUTTONDOWN:
                    if event.button == 1:
                        self.click = True

            pygame.display.update()
            self.main_clock.tick(60)


# Основное окно с игрой
class Main:
    def __init__(self, fon='images/background_1.jpg', normal=False, hard=False):
        pygame.mixer.pre_init(44100, -16, 1, 512)
        pygame.init()
        pygame.time.set_timer(pygame.USEREVENT, 2000)
        pygame.display.set_caption('SkyFarm_2')
        pygame.mixer.music.load('sounds/bird.mp3')
        pygame.mixer.music.play(-1)

        self.fon = fon
        self.normal = normal
        self.hard = hard

        self.BLACK = (0, 0, 0)
        self.W, self.H = 1000, 700
        self.screen_main = pygame.display.set_mode((self.W, self.H))

        # Загрузка звуков
        self.s_catch = pygame.mixer.Sound('sounds/catch.mp3')
        self.lose_sound = pygame.mixer.Sound('sounds/sound_lose.mp3')
        self.explosion_sound = pygame.mixer.Sound('sounds/explosion_sound.mp3')

        self.clock = pygame.time.Clock()
        self.FPS = 60
        self.font = pygame.font.SysFont('arial', 30)
        self.lives = 5
        self.last = pygame.time.get_ticks()
        self.cooldown = 5000
        self.cooldown_speed = 2000
        self.last_speed = pygame.time.get_ticks()
        self.index = 0
        self.speed = 10
        self.game_score = 0

        # Загрузка картинок
        self.background = pygame.transform.scale(pygame.image.load(self.fon).convert(), (1000, 700))
        self.score = pygame.image.load('images/score_fon.png').convert_alpha()
        self.telega = pygame.transform.scale(pygame.image.load('images/telega.png').convert_alpha(), (270, 150))
        self.bomb = pygame.transform.scale(pygame.image.load('images/bomb.jpg').convert_alpha(), (70, 108))
        self.heart = pygame.transform.scale(pygame.image.load('images/heart1.png').convert_alpha(), (52, 50))
        self.moderator = pygame.transform.scale(pygame.image.load('images/speed.png').convert_alpha(), (60, 60))
        self.explosion1 = pygame.transform.scale(pygame.image.load('images/explosion1.png').convert_alpha(), (300, 300))
        self.explosion2 = pygame.transform.scale(pygame.image.load('images/explosion2.png').convert_alpha(), (300, 300))
        self.explosion3 = pygame.transform.scale(pygame.image.load('images/explosion3.png').convert_alpha(), (300, 300))
        self.explosion4 = pygame.transform.scale(pygame.image.load('images/explosion4.png').convert_alpha(), (300, 300))
        self.explosion5 = pygame.transform.scale(pygame.image.load('images/explosion5.png').convert_alpha(), (300, 300))
        self.explosion_frames = [self.explosion1, self.explosion2, self.explosion3, self.explosion4, self.explosion5]

        # Размещение телеги
        self.t_rect = self.telega.get_rect(centerx=self.W // 2, bottom=self.H - 5)

        # Информация о каждом овоще
        self.veg_data = ({'path': 'artichoke.png', 'score': 50},
                         {'path': 'arugula.png', 'score': 150},
                         {'path': 'asparagus.png', 'score': 200},
                         {'path': 'asparagus2.png', 'score': 100},
                         {'path': 'bamboo.png', 'score': 30},
                         {'path': 'beans.png', 'score': 70},
                         {'path': 'beet.png', 'score': 20},
                         {'path': 'beet2.png', 'score': 40},
                         {'path': 'broccoli.png', 'score': 90},
                         {'path': 'brussel.png', 'score': 110},
                         {'path': 'cabbage.png', 'score': 60},
                         {'path': 'cauliflower.png', 'score': 180},
                         {'path': 'celery.png', 'score': 130},
                         {'path': 'cherry_tomatoes.png', 'score': 140},
                         {'path': 'chinese_cabbage.png', 'score': 170},
                         {'path': 'corn.png', 'score': 190},
                         {'path': 'cucumber.png', 'score': 35},
                         {'path': 'cucumber2.png', 'score': 105},
                         {'path': 'eggplant.png', 'score': 75},
                         {'path': 'garlic.png', 'score': 95},
                         {'path': 'garlic2.png', 'score': 65},
                         {'path': 'ginger.png', 'score': 115},
                         {'path': 'grass.png', 'score': 135},
                         {'path': 'grass2.png', 'score': 85},
                         {'path': 'green_cabbage.png', 'score': 185},
                         {'path': 'green_pepper.png', 'score': 165},
                         {'path': 'horseradish.png', 'score': 175},
                         {'path': 'leek.png', 'score': 125},
                         {'path': 'lettuce.png', 'score': 145},
                         {'path': 'onion.png', 'score': 65},
                         {'path': 'onion2.png', 'score': 55},
                         {'path': 'peas.png', 'score': 15},
                         {'path': 'pepper.png', 'score': 25},
                         {'path': 'potatoe.png', 'score': 95},
                         {'path': 'pumpkin.png', 'score': 75},
                         {'path': 'purple_carrot.png', 'score': 45},
                         {'path': 'purple_tomatoes.png', 'score': 80},
                         {'path': 'radish.png', 'score': 15},
                         {'path': 'red_pepper.png', 'score': 210},
                         {'path': 'root.png', 'score': 215},
                         {'path': 'squash.png', 'score': 125},
                         {'path': 'sunflower.png', 'score': 155},
                         {'path': 'sweet_potatoe.png', 'score': 195},
                         {'path': 'tomatoe.png', 'score': 220},
                         {'path': 'wolfberry.png', 'score': 225},
                         {'path': 'zucchini.png', 'score': 230},
                         {'path': 'zucchini2.png', 'score': 235})

        self.veg_surf = [pygame.image.load('images/' + data['path']).convert_alpha() for data in self.veg_data]

        # Создание различных групп спрайтов
        self.vegetables = pygame.sprite.Group()
        self.bombs = pygame.sprite.Group()
        self.moderators = pygame.sprite.Group()
        self.hearts = pygame.sprite.Group()
        self.all_sprites = pygame.sprite.Group()

        self.run()

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()
                elif event.type == pygame.USEREVENT:
                    # Вызов функций, соответствующих уровню сложности игры
                    self.create_vegetable(self.vegetables)
                    if self.normal:
                        self.create_bomb(self.bombs)
                    if self.hard:
                        self.create_moderator(self.moderators)
                        self.hearts_display(self.hearts)
                        self.create_bomb(self.bombs)

            # Движение телеги
            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT]:
                self.t_rect.x -= self.speed
                if self.t_rect.x < 0:
                    self.t_rect.x = 0
            elif keys[pygame.K_RIGHT]:
                self.t_rect.x += self.speed
                if self.t_rect.x > self.W - self.t_rect.width:
                    self.t_rect.x = self.W - self.t_rect.width

            # Столкновение с объектами
            self.collide_vegetables()
            self.collide_bombs()
            self.collide_hearts()
            self.collide_moderators()

            # Отображение фона, счетчика, счета и количества жизней
            self.screen_main.blit(self.background, (0, 0))
            self.screen_main.blit(self.score, (0, 0))
            self.screen_main.blit(self.font.render(str(self.game_score), 1, (94, 138, 14)), (20, 10))
            self.screen_main.blit(self.font.render('Lives: ' + str(self.lives), 1, (255, 255, 255)), (800, 15))

            # Отрисовка групп спрайтов
            self.vegetables.draw(self.screen_main)
            self.bombs.draw(self.screen_main)
            self.hearts.draw(self.screen_main)
            self.moderators.draw(self.screen_main)

            # Отображение телеги
            self.screen_main.blit(self.telega, self.t_rect)
            pygame.display.update()
            self.clock.tick(self.FPS)

            # Обновление групп спрайтов
            self.vegetables.update(self.H)
            self.bombs.update(self.H)
            self.hearts.update(self.H)
            self.moderators.update(self.H)

    # Создание спрайта овоща
    def create_vegetable(self, group):
        index = randint(0, len(self.veg_surf) - 1)
        x = randint(20, self.W - 20)
        speed = randint(2, 4)

        return Ball(x, speed, self.veg_surf[index], self.veg_data[index]['score'],
                    group, self.lives, self.score)

    # Столкновение телеги со спрайтом овоща
    def collide_vegetables(self):
        for vegetable in self.vegetables:
            if vegetable.rect.centery >= 700:
                self.lives_change()
                self.lose_sound.play()
                vegetable.kill()
            elif self.t_rect.collidepoint(vegetable.rect.center):
                self.s_catch.play()
                self.game_score += vegetable.score
                vegetable.kill()

    # Столкновение телеги со спрайтом сердца
    def collide_hearts(self):
        for heart in self.hearts:
            if self.t_rect.collidepoint(heart.rect.center):
                self.s_catch.play()
                heart.kill()
                self.heart_plus()

    # Увеличение числа жизней после столкновения со спрайтом сердца
    def heart_plus(self):
        if self.lives < 5:
            self.lives += 1

    # Уменьшение числа жизней после пропуска овоща
    def lives_change(self):
        if self.lives == 1:
            Terminate(self.game_score)
        else:
            self.lives -= 1

    # Отображение числа жизней
    def hearts_display(self, group):
        x = randint(20, self.W - 20)
        speed = randint(1, 4)
        now = pygame.time.get_ticks()
        if now - self.last >= self.cooldown:
            self.last = now
            return Heart(x, speed, self.heart, group)

    # Создание спрайта ускорителя
    def create_moderator(self, group):
        x = randint(20, self.W - 20)
        speed = randint(1, 4)
        now = pygame.time.get_ticks()
        if now - self.last_speed >= self.cooldown_speed:
            self.last_speed = now
            return Moderator(x, speed, self.moderator, group)

    # Столкновение телеги со спрайтом ускорителя
    def collide_moderators(self):
        for moderator in self.moderators:
            if self.t_rect.collidepoint(moderator.rect.center):
                moderator.kill()
                self.s_catch.play()
                self.speed_plus()

    # Увеличене скорости телеги после столкновения с ускорителем
    def speed_plus(self):
        self.speed *= 2
        now = pygame.time.get_ticks()
        if now - self.last_speed >= self.cooldown_speed:
            self.last_speed = now

    # Создание спрайта бомбы
    def create_bomb(self, group):
        x = randint(20, self.W - 20)
        speed = randint(1, 4)

        return Bomb(x, speed, self.bomb, group)

    # Столкновение телеги со спрайтом бомбы
    def collide_bombs(self):
        for bomb in self.bombs:
            if self.t_rect.collidepoint(bomb.rect.center):
                self.explosion_sound.play()
                explosion = Explosion(bomb.rect.centerx, bomb.rect.centery, self.explosion_frames)
                self.bombs.remove(bomb)
                self.all_sprites.add(explosion)
                terminate = False
                while not terminate:
                    self.all_sprites.update()
                    self.all_sprites.draw(self.screen_main)
                    pygame.display.flip()
                    self.clock.tick(25)
                    if len(self.all_sprites) == 0:
                        terminate = True
                Terminate(self.game_score)


# Создание спрайта овоща, его добавление в группу self.vegetables и его движение по экрану
class Ball(pygame.sprite.Sprite):
    def __init__(self, x, speed, surf, score, group, lives, count):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(surf, (100, 100))
        self.rect = self.image.get_rect(center=(x, 0))
        self.speed = speed
        self.lives = lives
        self.score = score
        self.count = count
        self.lose_sound = pygame.mixer.Sound('sounds/sound_lose.mp3')
        self.add(group)

    def update(self, *args):
        if self.rect.y < args[0] - 20:
            self.rect.y += self.speed


# Создание спрайта бомбы, его добавление в группу self.vegetables и его движение по экрану
class Bomb(pygame.sprite.Sprite):
    def __init__(self, x, speed, surf, group):
        pygame.sprite.Sprite.__init__(self)
        self.image = surf
        self.rect = self.image.get_rect(center=(x, 0))
        self.speed = speed
        self.add(group)

    def update(self, *args):
        if self.rect.y < args[0] - 20:
            self.rect.y += self.speed
        else:
            self.kill()


# Создание спрайта сердца, его добавление в группу self.vegetables и его движение по экрану
class Heart(pygame.sprite.Sprite):
    def __init__(self, x, speed, surf, group):
        pygame.sprite.Sprite.__init__(self)
        self.image = surf
        self.rect = self.image.get_rect(center=(x, 0))
        self.speed = speed
        self.add(group)

    def update(self, *args):
        if self.rect.y < args[0] - 20:
            self.rect.y += self.speed
        else:
            self.kill()


# Создание спрайта ускорителя, его добавление в группу self.vegetables и его движение по экрану
class Moderator(pygame.sprite.Sprite):
    def __init__(self, x, speed, surf, group):
        pygame.sprite.Sprite.__init__(self)
        self.image = surf
        self.rect = self.image.get_rect(center=(x, 0))
        self.speed = speed
        self.add(group)

    def update(self, *args):
        if self.rect.y < args[0] - 20:
            self.rect.y += self.speed
        else:
            self.kill()


# Создание анимации взрыва после столкновения телеги с бомбой
class Explosion(pygame.sprite.Sprite):
    def __init__(self, x, y, images):
        super().__init__()
        self.images = images
        self.current_index = 0
        self.image = None
        self.rect = None
        self.load_images()
        self.image = self.images[self.current_index]
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

    def load_images(self):
        for i in range(1, 6):
            image = pygame.image.load(f"images/explosion{i}.png")
            self.images.append(image)

    def update(self):
        self.current_index += 1
        if self.current_index >= len(self.images):
            self.kill()
        else:
            self.image = self.images[self.current_index]


# Окно концовки
class Terminate:
    def __init__(self, score):
        pygame.mixer.pre_init(44100, -16, 1, 512)
        pygame.init()
        pygame.time.set_timer(pygame.USEREVENT, 2000)
        pygame.display.set_caption('SkyFarm_2')
        self.font = pygame.font.SysFont('arial', 30)
        self.click = False

        self.score = score
        self.best_score = self.get_best_score()

        # Создание фона окна концовки
        self.main_clock = pygame.time.Clock()
        self.screen_terminate = pygame.display.set_mode((950, 600))
        for i in range(10000):
            self.screen_terminate.fill(pygame.Color('white'), (random() * 950, random() * 600, 1, 1))

        self.white_rect_exit = pygame.Rect(450, 290, 170, 120)

        self.run()

    def run(self):
        while True:
            mx, my = pygame.mouse.get_pos()

            # Отображение результата и текста на экране
            self.screen_terminate.blit(self.font.render('GAME OVER', 1, (255, 255, 255)), (375, 80))
            self.screen_terminate.blit(self.font.render('Score:', 1, (255, 255, 255)), (390, 180))
            self.screen_terminate.blit(self.font.render(str(self.score), 1, (255, 255, 255)), (490, 180))
            self.screen_terminate.blit(self.font.render('Best score:', 1, (255, 255, 255)), (350, 280))
            self.screen_terminate.blit(self.font.render(str(self.best_score), 1, (255, 255, 255)), (515, 280))
            self.screen_terminate.blit(self.font.render("Press 'SPACE' to restart", 1, (255, 255, 255)), (310, 480))
            self.screen_terminate.blit(self.font.render('Exit', 1, (255, 255, 255)), (440, 380))

            # Игра завершается при нажатии на "Exit"
            if self.white_rect_exit.collidepoint((mx, my)):
                if self.click:
                    exit()

            for event in pygame.event.get():
                if event.type == QUIT:
                    exit()
                if event.type == MOUSEBUTTONDOWN:
                    if event.button == 1:
                        self.click = True
                # Игра начинается заново при нажатии на кнопку пробела
                if event.type == KEYDOWN:
                    if event.key == K_SPACE:
                        InitialWindow()

            pygame.display.update()
            self.main_clock.tick(60)

    # Получение лучшего счета пользователя
    def get_best_score(self):
        # Получение имени пользователя
        user_name = getpass.getuser()

        # Создание базы данных 'game_scores'
        conn = sqlite3.connect('game_scores.db')
        cursor = conn.cursor()

        try:
            cursor.execute("CREATE TABLE scores (user_name TEXT, score INT)")
        except sqlite3.OperationalError:
            pass

        # Получение результата пользователя из базы данных
        cursor.execute("SELECT * FROM scores WHERE user_name = ?", (user_name,))
        result = cursor.fetchone()

        # Результата нет в базе данных
        if result is None:
            # В базу данных добавляется имя пользователя и его результат
            cursor.execute("INSERT INTO scores (user_name, score) VALUES (?, ?)",
                           (user_name, self.score))
        # Результат есть в базе данных
        else:
            # Если новый результат пользователя лучше результата в базе данных
            if self.score > result[1]:
                # Обновляем результат пользователя в базе данных на новый результат
                cursor.execute("UPDATE scores SET score = ? WHERE user_name = ?",
                               (self.score, user_name))

        # Выбираем результат пользователя из базы данных
        cursor.execute("SELECT score FROM scores WHERE user_name = ?", (user_name,))
        best_score = cursor.fetchone()[0]

        conn.commit()
        conn.close()

        return best_score


if __name__ == '__main__':
    InitialWindow()
