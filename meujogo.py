import arcade
import random

#criar constantes
Altura = 600
Largura = 800
Titulo = "Meu Jogo"

#personagem
class Player(arcade.Sprite):
    def __init__(self):
        super().__init__("mcqueen_direita.png", scale=0.10)
        self.textura_direita = arcade.load_texture("mcqueen_direita.png")
        self.textura_esquerda = arcade.load_texture("mcqueen_esquerda1.png")

    #atualizar personagem
    def update(self, delta_time):
        #permitir movimentação do personagem
        self.center_x += self.change_x
        self.center_y += self.change_y

        #verificar a direção do movimento para mudar o personagem (esquerda e direita)
        #se for zero, o personagem mantem a textura atual
        if(self.change_x > 0):
            self.texture = self.textura_direita
        elif(self.change_x < 0):
            self.texture = self.textura_esquerda

        #parar o personagem antes dele sair da tela
        if(self.right > Largura):
            self.change_x = 0
            self.right = Largura
        elif(self.left < 0):
            self.change_x = 0
            self.left = 0
        
        if(self.top > Altura):
            self.change_y = 0
            self.top = Altura
        elif(self.bottom < 0):
            self.change_y = 0
            self.bottom = 0


     
#Cria a classe do combustivel que herda da classe Sprite do Arcade
class Combustivel(arcade.Sprite):
    #O método init é o construtor, onde fica as caracteristicas do personagem (objeto)
    def __init__(self):
        super().__init__("combustivel.png", scale= 0.10)  
    # O update é chamado  a cada frame do jogo, ele atualiza o personagem (faz andar, etc)
    def update(self, delta_time):
        #adicionar movimentação no eixo x e y
        self.center_x += self.change_x
        self.center_y += self.change_y

        #parar o personagem antes dele sair da tela
        #temos os lados right, left, top e bottom
        if(self.right > Largura):
            self.change_x *= -1 #faz o efeito rebot, o pérsonagem bate na borda da tela e volta
        elif(self.left < 0):
            self.change_x *= -1
        
        if(self.top > Altura):
            self.change_y *= -1
        elif(self.bottom < 0):
            self.change_y *= -1  

class Combustivel_Especial(arcade.Sprite):
    #O método init é o construtor, onde fica as caracteristicas do personagem (objeto)
    def __init__(self):
        super().__init__("combustivel.png", scale= 0.10)  
    # O update é chamado  a cada frame do jogo, ele atualiza o personagem (faz andar, etc)
    def update(self, delta_time):
        #adicionar movimentação no eixo x e y
        self.center_x += self.change_x
        self.center_y += self.change_y

        #parar o personagem antes dele sair da tela
        #temos os lados right, left, top e bottom
        if(self.right > Largura):
            self.change_x *= -1 #faz o efeito rebot, o pérsonagem bate na borda da tela e volta
        elif(self.left < 0):
            self.change_x *= -1
        
        if(self.top > Altura):
            self.change_y *= -1
        elif(self.bottom < 0):
            self.change_y *= -1

class Inimigo(arcade.Sprite):
    def __init__(self):
        super().__init__("inimigo.png", 0.06) 

        self.atingido = False



class Bomba(arcade.Sprite):
    # Adicionamos 'textura_explosao' aqui nos parâmetros:
    def __init__(self, textura_explosao):
        # Inicializa o sprite com a imagem normal da bomba
        super().__init__("bomba.png", 0.09) 
        
        # Guarda a textura recebida e cria as variáveis de controle
        self.textura_explosao = textura_explosao
        self.explodindo = False
        self.tempo_explosao = 0.0
        
    
    def update(self, delta_time):
    #adicionar movimentação no eixo x e y
        # Faz a bomba se mover na tela usando a velocidade dela
        self.center_x += self.change_x
        self.center_y += self.change_y

        # Lógica para rebater nas paredes (se você tiver)
        if self.left < 0 or self.right > 800:
            self.change_x *= -1
        if self.bottom < 0 or self.top > 600:
            self.change_y *= -1

#criar tela da vitória
class Tela_vitoria(arcade.View):
    def __init__(self, pontuacao_final, tempo_final):
        
        super().__init__()
        self.textura_fundo_inicial = arcade.load_texture("rua.jpg")

        self.pontuacao = pontuacao_final
        self.cronometro = tempo_final 

    def on_draw(self):
        self.clear()
        arcade.draw_texture_rect(
            texture = self.textura_fundo_inicial,
            rect=arcade.XYWH(
                x=Largura/2,
                y=Altura/2,
                width=Largura,
                height=Altura

            )
        ) 

        arcade.draw_text("END GAME", Largura//2, 400, arcade.color.WHITE, 18, anchor_x= "center")
        arcade.draw_text(f"Sua Pontuação foi {self.pontuacao}!", 280, 150, arcade.color.WHITE, 18, 50)
        arcade.draw_text(f"TEMPO: {self.cronometro}", 280, 100, arcade.color.WHITE, 18, 50) 
        

#criar a tela inicial
class Tela_inicial(arcade.View):
    def __init__(self):
        self.textura_fundo_inicial = arcade.load_texture("rua.jpg")
        super().__init__()

    def on_draw(self):
        self.clear()
        #desenhar cenário do fundo
        arcade.draw_texture_rect(
            texture = self.textura_fundo_inicial,
            rect=arcade.XYWH(
                x=Largura/2,
                y=Altura/2,
                width=Largura,
                height=Altura

            )
        )

        arcade.draw_text("JOGO - Relâmpago Marquinhos", Largura//2, 400, arcade.color.WHITE, 18, anchor_x= "center")
        arcade.draw_text("Pressione [J] para jogar", 280, 100, arcade.color.WHITE, 18, 50)
        arcade.draw_text("Pressione [ESC] para sair", 280, 150, arcade.color.WHITE, 18, 200 )

    def on_key_press(self, key, modifiers):
        if key == arcade.key.J or key == arcade.key.ENTER:
            tela_jogo = Telajogo()
            self.window.show_view(tela_jogo)
        elif key == arcade.key.ESCAPE:
            tela_inicial = Tela_inicial()
            self.window.show_view(tela_inicial)



        

class Telajogo(arcade.View):
    def __init__(self):
         self.textura_fundo = arcade.load_texture("cenario.jpg")
         self.textura_explosao = arcade.load_texture("explosao.png")
         super().__init__()
         #cor RGB (vermelho, verde, azul)
         arcade.set_background_color(  (0, 0, 0)  )
        #definir movimento
         self.movimento = 5
         #criar cromnometro
         self.cronometro = 0.0
         self.cronometro_rodando = True
         
        #criar personagem
         self.personagem = Player()
         self.combustivel = Combustivel()
         self.bomba = Bomba(self.textura_explosao)
         self.inimigo = Inimigo()
         #posicionar ele na tela
         self.personagem.center_x = 0
         self.personagem.center_y = 0
         self.combustivel.center_x = 240
         self.combustivel.center_y = 80
         self.bomba.center_x = 200
         self.bomba.center_y = 200

         self.inimigo.center_x = 10
         self.inimigo.center_y = 20
        #fazer o personagem andar
         self.combustivel.change_x = self.movimento
         self.combustivel.change_y = self.movimento
         #criar pontuação do jogo
         self.pontuacao = 0

        
         

        #criar lista de personagens
         self.sprite_jogador = arcade.SpriteList()
         self.sprite_combustivel = arcade.SpriteList()
         self.sprite_bomba = arcade.SpriteList()
         self.sprite_inimigo = arcade.SpriteList()

         for a in range(5):
             inimigo1 = Inimigo()
             inimigo1.center_x = random.randint(50, Largura - 50)
             inimigo1.center_y = random.randint(50, Altura - 50)

             

             self.sprite_inimigo.append(inimigo1)

        #laço de repetição criar moedas(combustivel)
         for i in range(25):  # quantidade de moedas
             combustivel1 = Combustivel()

             combustivel1.center_x = random.randint(50, Largura - 50)
             combustivel1.center_y = random.randint(50, Altura - 50)

             combustivel1.change_x = random.choice([-2, 2])
             combustivel1.change_y = random.choice([-2, 2])

             self.sprite_combustivel.append(combustivel1)

         for b in range(15): 
            bomba1 = Bomba(self.textura_explosao) # Passa a textura para cada uma
            bomba1.center_x = random.randint(50, 800 - 50)
            bomba1.center_y = random.randint(50, 600 - 40)
            bomba1.change_x = random.choice([-2, 2])
            bomba1.change_y = random.choice([-2, 2])
            self.sprite_bomba.append(bomba1)
         



        #adicionar o personagem no grupo de sprites
         self.sprite_jogador.append(self.personagem)
         self.sprite_combustivel.append(self.combustivel)
         self.sprite_bomba.append(self.bomba)
         self.sprite_inimigo.append(self.inimigo)
         

    #metodo para desenhar na tela
    def on_draw(self):
        self.clear()
        #desenhar cenário do fundo
        arcade.draw_texture_rect(
            texture = self.textura_fundo,
            rect=arcade.XYWH(
                x=Largura/2,
                y=Altura/2,
                width=Largura,
                height=Altura

            )
        )
        #desenhar meu personagem
        self.sprite_jogador.draw()
        self.sprite_combustivel.draw()
        self.sprite_bomba.draw()
        self.sprite_inimigo.draw()

        #escrever pontuação na tela
        arcade.draw_text(f"PONTUAÇÃO: {self.pontuacao}", 10, 570, arcade.color.WHITE, 14)
        arcade.draw_text(f"CRONÔMENTRO: {self.cronometro}", 10, 550, arcade.color.WHITE, 14)
        
       
        
       
        
    #atualiza a lógica de jogo e das coisas q estão na tela
    def on_update(self, delta_time):
        #atualizar as listas de sprites, o que chama o método update 
        #Delta time é o tempo de execussão do jogo, para igualar em diferentes computadores
        self.sprite_jogador.update(delta_time)
        self.sprite_combustivel.update(delta_time)
        self.sprite_bomba.update(delta_time)
        self.sprite_inimigo.update(delta_time)

        #fazer o combustivel sumir qnd o carrinho passar por ele
        combustivel_colidido = arcade.check_for_collision_with_list(self.personagem, self.sprite_combustivel)
        for combustivel in combustivel_colidido:
            combustivel.remove_from_sprite_lists()
            if combustivel == Combustivel_Especial:
                self.pontuacao += 5
            else:
                self.pontuacao += 1
            #aumentar pontuação qnd coletar combustivel
            self.pontuacao += 1

        #fazera bomba sumir qnd o carrinho passar por ele
        bomba_colidida = arcade.check_for_collision_with_list(self.personagem, self.sprite_bomba)
        for b in bomba_colidida:
            if not b.explodindo:
                b.explodindo = True
                b.texture = b.textura_explosao # Transforma na imagem de explosão!
                self.pontuacao -= 1 # Retira pontuação apenas uma vez

         #fazera inimigo sumir qnd o carrinho passar por ele
        inimigo_colidido = arcade.check_for_collision_with_list(self.personagem, self.sprite_inimigo)
        for inimigo in inimigo_colidido:
            if not inimigo.atingido:
                inimigo.atingido = True
                inimigo.remove_from_sprite_lists()
                
                # Perde 3 pontos
                self.pontuacao -= 3
        

        # Controla o tempo de 1 segundo para sumir com as bombas explodidas
        for b in self.sprite_bomba:
            if b.explodindo:
                b.tempo_explosao += delta_time
                if b.tempo_explosao >= 1.0:
                    b.remove_from_sprite_lists()
        



        
            
            #diminuir pontuação qnd bater na bomba
            

         #cronometro
        
        if self.cronometro_rodando:
            self.cronometro += delta_time

       


        if len(self.sprite_combustivel) == 0:
            # 1. Criamos a tela de vitória passando a pontuação e o cronômetro atuais
            tela_fim = Tela_vitoria(self.pontuacao, self.cronometro)
            
            # 2. Mandamos a janela do jogo mudar para essa nova tela
            self.window.show_view(tela_fim)
            
        


    #gerenciar o teclado (teclas pressionadas)
    def on_key_press(self, key, modifiers):
        #key = seta pressionada
        #
        if (key == arcade.key.LEFT):
            self.personagem.change_x -= self.movimento
        if (key == arcade.key.RIGHT):
            self.personagem.change_x += self.movimento
        if (key == arcade.key.UP):
            self.personagem.change_y += self.movimento
        if(key == arcade.key.DOWN):
           self.personagem.change_y -= self.movimento

        if(key == arcade.key.ESCAPE):
            arcade.close_window()


    #evento ao soltar as teclas, para ele parar de andar qnd a tecla for solta
    def on_key_release(self, key, modifiers):
        if (key == arcade.key.LEFT or key == arcade.key.RIGHT ):
            self.personagem.change_x = 0
        if (key == arcade.key.UP or key == arcade.key.DOWN):
            self.personagem.change_y = 0




    
def main():
    #criar janela principal do jogo com os parametros
    jogo = arcade.Window(Largura, Altura, Titulo)
    #cria uma tela inicial
    tela_inicial = Tela_inicial()

    jogo.show_view(tela_inicial)
    
    arcade.run()


if __name__== "__main__":
    main()
