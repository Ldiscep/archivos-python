import pygame
import random

# Inicializar pygame
pygame.init()

# Definir colores
NEGRO = (0, 0, 0)
BLANCO = (255, 255, 255)

# Definir dimensiones de la pantalla
ANCHO = 800
ALTO = 600

# Clase para representar el jugador
class Jugador(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface([50, 50])
        self.image.fill(BLANCO)
        self.rect = self.image.get_rect()
        self.rect.x = ANCHO // 2
        self.rect.y = ALTO - 70

    def update(self):
        # Mover el jugador con las teclas izquierda y derecha
        teclas = pygame.key.get_pressed()
        if teclas[pygame.K_LEFT]:
            self.rect.x -= 5
        if teclas[pygame.K_RIGHT]:
            self.rect.x += 5

        # Limitar el movimiento del jugador dentro de la pantalla
        if self.rect.x < 0:
            self.rect.x = 0
        elif self.rect.x > ANCHO - self.rect.width:
            self.rect.x = ANCHO - self.rect.width

# Clase para representar los obstáculos
class Obstaculo(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface([30, 30])
        self.image.fill(NEGRO)
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(ANCHO - self.rect.width)
        self.rect.y = random.randrange(-100, -40)
        self.velocidad_y = random.randrange(1, 5)

    def update(self):
        self.rect.y += self.velocidad_y
        if self.rect.y > ALTO:
            self.rect.y = random.randrange(-100, -40)
            self.rect.x = random.randrange(ANCHO - self.rect.width)
            self.velocidad_y = random.randrange(1, 5)

# Inicializar pantalla
pantalla = pygame.display.set_mode([ANCHO, ALTO])
pygame.display.set_caption("Esquiva los obstáculos")

# Crear grupo para todos los sprites y para los obstáculos
todos_los_sprites = pygame.sprite.Group()
obstaculos = pygame.sprite.Group()

# Crear jugador
jugador = Jugador()
todos_los_sprites.add(jugador)

# Crear obstáculos
for i in range(8):
    obstaculo = Obstaculo()
    todos_los_sprites.add(obstaculo)
    obstaculos.add(obstaculo)

# Reloj para controlar la velocidad de actualización
reloj = pygame.time.Clock()

# Variable para determinar si el juego está corriendo
jugando = True

# Bucle principal del juego
while jugando:
    # --- Procesamiento de eventos ---
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            jugando = False

    # --- Lógica del juego ---
    todos_los_sprites.update()

    # Comprobar colisión entre jugador y obstáculos
    if pygame.sprite.spritecollide(jugador, obstaculos, False):
        jugando = False

    # --- Renderizado ---
    pantalla.fill(BLANCO)
    todos_los_sprites.draw(pantalla)
    pygame.display.flip()

    # --- Controlar la velocidad del juego ---
    reloj.tick(60)

# Cerrar pygame
pygame.quit()
