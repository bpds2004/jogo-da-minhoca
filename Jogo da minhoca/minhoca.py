import pygame
import sys
import random

pygame.init()

largura_tela = 800
altura_tela = 600
tamanho_bloco = 20
cor_branca = (255, 255, 255)
cor_verde = (0, 255, 0)
cor_vermelha = (255, 0, 0)

tela = pygame.display.set_mode((largura_tela, altura_tela))
pygame.display.set_caption('Jogo da Minhoca')

clock = pygame.time.Clock()

def minhoca(tamanho_bloco, lista_minhoca):
    for x in lista_minhoca:
        pygame.draw.rect(tela, cor_verde, [x[0], x[1], tamanho_bloco, tamanho_bloco])

def jogo():
    sair = False
    game_over = False

    pos_x = largura_tela / 2
    pos_y = altura_tela / 2

    velocidade_x = 0
    velocidade_y = 0

    lista_minhoca = []
    comprimento_minhoca = 1

    comida_x = round(random.randrange(0, largura_tela - tamanho_bloco) / 20.0) * 20.0
    comida_y = round(random.randrange(0, altura_tela - tamanho_bloco) / 20.0) * 20.0

    while not sair:
        while game_over:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sair = True
                    game_over = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_c:
                        jogo()
                    if event.key == pygame.K_s:
                        sair = True
                        game_over = False

            tela.fill(cor_branca)
            fonte = pygame.font.SysFont(None, 50)
            texto = fonte.render('Game Over', True, cor_vermelha)
            tela.blit(texto, (largura_tela / 2 - 100, altura_tela / 2 - 50))
            texto_reiniciar = fonte.render('C - jogar novamente   //   S - para sair', True, cor_vermelha)
            tela.blit(texto_reiniciar, (largura_tela / 2 - 300, altura_tela / 2 + 50))
            pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sair = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    velocidade_x = -tamanho_bloco
                    velocidade_y = 0
                if event.key == pygame.K_RIGHT:
                    velocidade_x = tamanho_bloco
                    velocidade_y = 0
                if event.key == pygame.K_UP:
                    velocidade_y = -tamanho_bloco
                    velocidade_x = 0
                if event.key == pygame.K_DOWN:
                    velocidade_y = tamanho_bloco
                    velocidade_x = 0

        if pos_x >= largura_tela or pos_x < 0 or pos_y >= altura_tela or pos_y < 0:
            game_over = True

        pos_x += velocidade_x
        pos_y += velocidade_y

        tela.fill(cor_branca)
        pygame.draw.rect(tela, cor_vermelha, [comida_x, comida_y, tamanho_bloco, tamanho_bloco])

        cabeca_minhoca = []
        cabeca_minhoca.append(pos_x)
        cabeca_minhoca.append(pos_y)
        lista_minhoca.append(cabeca_minhoca)
        if len(lista_minhoca) > comprimento_minhoca:
            del lista_minhoca[0]

        for segmento in lista_minhoca[:-1]:
            if segmento == cabeca_minhoca:
                game_over = True

        minhoca(tamanho_bloco, lista_minhoca)

        pygame.display.update()

        if pos_x == comida_x and pos_y == comida_y:
            comida_x = round(random.randrange(0, largura_tela - tamanho_bloco) / 20.0) * 20.0
            comida_y = round(random.randrange(0, altura_tela - tamanho_bloco) / 20.0) * 20.0
            comprimento_minhoca += 1

        clock.tick(10)

    pygame.quit()
    sys.exit()

jogo()
