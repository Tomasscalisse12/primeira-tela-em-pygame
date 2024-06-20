#importação da bibilhoteca pygame
import pygame

from pygame.locals import*
#o modulo pygame.locals contem constantes e funções por exemplo
#EVENTOS: Como QUIT, KEYDOWN, KEYUP, etc., que ajudam a gerenciar eventos de saída do jogo ou pressionamento de teclas.
#TECLAS: Como K_UP, K_DOWN, K_LEFT, K_RIGHT, que representam as teclas do teclado.
#MODOS DE TELA: Como FULLSCREEN, DOUBLEBUF, HWSURFACE, que ajudam a configurar a janela do jogo.

from sys import exit

#importação da função exit do modulo sys, a função exit é usada para 
#finalizar a execução do programa

pygame.init()
#essa linha inicia todas as variaveis e configurações necessarias para o pygame
#sem ela muitas coisas não funcionam

largura = 640

altura = 480
#aqui temos duas variaveis que determina a altura e largura da tela

tela = pygame.display.set_mode((largura,altura))
#com as variaveis com os valores ja armazenados esta linha determina a tela
#criamos a variavel tela e a função set_mode é usada para definir o modo de exibição

while True:
    #esse é o loop principal do jogo, que continua rodando enquanto o jogo esta ativado
    
    for event in pygame.event.get():
        #esta linha percorre todos os eventos desde seu ultimo loop
        
        if event.type ==QUIT:
            #verifica se o tipo do evento é QUIT ocorre apos o usuario tentar fechar a janela

            pygame.quit()
            #finaliza todas as funções do pygame necessario para limpar corretamente os recursos

            exit()
            #encerra o programa esta função do modulo sys finaliza o script

        pygame.display.update()  
        #com essa linha atualizamos o conteudo da tela sem ela nenhuma mudança ocorre
 


