import pygame, sys, time, random

pygame.init()

pantalla = pygame.display.set_mode((500, 500))
fuente = pygame.font.Font(None, 30)

fps = pygame.time.Clock()

# Comida
def food():
  random_pos = random.randint(0,49)*10
  comida = [random_pos, random_pos]
  return comida

# Serpiente
def main():
  cabeza = [100, 50]
  cuerpo = [[100, 50], [90,50], [80,50]]
  change = 'RIGHT'
  run = True
  comida = food()
  puntaje = 0

  while run:
    # Controles
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        run = False
      if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_RIGHT:
          change = 'RIGHT'
        if event.key == pygame.K_LEFT:
          change = 'LEFT'
        if event.key == pygame.K_UP:
          change = 'UP'
        if event.key == pygame.K_DOWN:
          change = 'DOWN'
    if change == 'RIGHT':
      cabeza[0] += 10
    if change == 'LEFT':
      cabeza[0] -= 10
    if change == 'UP':
      cabeza[1] -= 10
    if change == 'DOWN':
      cabeza[1] += 10

    cuerpo.insert(0, list(cabeza))
    if cabeza == comida:
      comida = food()
      puntaje += 1
      print(puntaje)
    else:
      cuerpo.pop()


    pantalla.fill((0,0,0))
    for pos in cuerpo:
      pygame.draw.rect(pantalla,(200,200,200), pygame.Rect(pos[0], pos[1], 10, 10))
    pygame.draw.rect(pantalla, (169,6,60), pygame.Rect(comida[0], comida[1], 10, 10))
    texto = fuente.render(str(puntaje),0,(200,60,80))
    pantalla.blit(texto,(480,20))

    # Velocidades
    if puntaje < 10:
      fps.tick(10)
    if puntaje >= 10:
      fps.tick(20)
    if puntaje >=20:
      fps.tick(30)
    if puntaje >=30:
      fps.tick(40)
    if puntaje >=40:
      fps.tick(50)
    
    # Muros
    if cabeza[0] <=0 or cabeza[0] >=500:
      run = False
      print('Perdiste x.x')
    if cabeza[1] <=0 or cabeza[1] >=500:
      run = False
      print('Perdiste x.x')
    

    pygame.display.flip()
    fps.tick(10)
main()
pygame.quit()


