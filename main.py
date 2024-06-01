import pygame
import itertools
import vida
import time 

ALTO=450
ANCHO=450
ESPACIO = 50

pygame.init()
#se le agrega un pixel para que no se salga de la ventana
screen = pygame.display.set_mode((ANCHO+1,ALTO+1))
fuente=pygame.font.SysFont("bigblueterm437nerdfontmono", 13)   
clock=pygame.time.Clock()
pygame.display.set_caption("Proyecto Vida", "sexo")


while True:    
    for event in pygame.event.get():
        # print(f'---------------------\n{event}\n---------------------\n')        
        if event.type == pygame.QUIT or pygame.key.get_pressed()[120]:                    
            exit()
    
###-----------------------------------------------------###

    #Logica del juego
    screen.fill("black")
    nuevo_ancho , nuevo_alto = pygame.display.get_surface().get_size()

    for i_alto in range(0, nuevo_alto, ESPACIO):
        for i_ancho in range(0, nuevo_ancho, ESPACIO):
            # Horizontales
            pygame.draw.line(screen, vida.BLANCO, [0, i_alto], [nuevo_ancho, i_alto])
            
            # Verticales
            pygame.draw.line(screen, vida.BLANCO, [i_ancho, 0], [i_ancho, nuevo_alto])
            
            #letras
            letras=fuente.render(f'{int(i_ancho/ESPACIO)}-{int(i_alto/ESPACIO)}', True, "white")
            screen.blit(letras,(i_ancho,i_alto))
                                                     
    #loop de celulas
    vida.ciclo(nuevo_ancho, nuevo_alto, ESPACIO, screen)
    
###-----------------------------------------------------###                           
    pygame.display.flip()
    clock.tick(1)    
pygame.quit()