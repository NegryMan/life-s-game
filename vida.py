import pygame
import time

BLANCO=(255,255,255)
NEGRO=(0,0,0)
GRIS=(128,128,128)
GRIS_CLARO=(64,64,64)
GRIS_OSCURO=(192,192,192)

#Funciones 

##Crear celular
#pos_X*espacio+1, pos_Y*espacio+1, está hecho para colocar los posiciones mediante ints y no posiciones exactas, si se multiplica por 0 dará 1 como respuesta
def vida(pos_X, pos_Y,lienzo, espacio, estado=1):
    if estado==1 :
        print(f'vida en {pos_X} {pos_Y}')
        pygame.draw.rect(lienzo, GRIS , pygame.Rect(pos_X*espacio+1, pos_Y*espacio+1, espacio-1, espacio-1))
    else:
        print(f'muerte en {pos_X} {pos_Y}')
        pygame.draw.rect(lienzo, NEGRO, pygame.Rect(pos_X*espacio+1, pos_Y*espacio+1, espacio-1, espacio-1))
    

##Obtener coordenadas de casillas pintadas

#TODO: 
#-estructura: pintar casillas del iterable anterior, repasar el tablero y buscar las casillas que cumplen los requisitos,       devolver lista de casillas que serán pintadas.

def ciclo(ancho, alto, espacio, lienzo:pygame.Surface):    
    
    pygame.display.flip()    
    
    vida(4,3,lienzo, espacio)
    vida(2,3,lienzo, espacio)

    #recorremos el tablero
    for y in range(1,alto, espacio):            
        for x in range(1,ancho, espacio):
            x_correg=int((x-1)/espacio)
            y_correg=int((y-1)/espacio)                                    
                        
            #puntos donde buscar
            grises= 0
            busqueda = [(x+espacio,y),(x-espacio,y),
                        (x,y+espacio),(x,y-espacio),
                        (x+espacio,y+espacio),(x-espacio,y+espacio),
                        (x+espacio,y-espacio),(x-espacio,y-espacio)]
                                    
            #obtener adyacentes 
            #a traves de las coordenadas en la lista busqueda, si se cumplen las condiciones se ignora esa coordenada y se salta a la siguiente
            for coordenada in busqueda:                
                if coordenada[0]<0 or coordenada[1]<0 or coordenada[0]>ancho-1 or coordenada[1]>alto-1 :
                    continue

                #obtengo el color de la casilla y si es gris, aumenta el contador                
                clr_obt=lienzo.get_at(coordenada)
                if clr_obt == GRIS :                    
                    grises+=1

            
            #se obtiene el color y se agrega al diccionario coords
            color = lienzo.get_at((x,y))                                                               
            if color == GRIS and grises<2:
                vida(x_correg,y_correg,lienzo,espacio,1)

            elif color == NEGRO and grises>=2:
                vida(x_correg,y_correg,lienzo,espacio)
            #time.sleep(0.1)
            #pygame.display.flip()