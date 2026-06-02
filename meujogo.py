import arcade

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
        if(self.right > 800):
            self.change_x = 0
        elif(self.left < 0):
            self.change_x = 0
        
        if(self.top > 600):
            self.change_y = 0
        elif(self.bottom < 0):
            self.change_y = 0


     

class Combustivel(arcade.Sprite):
    def __init__(self):
        super().__init__("combustivel.png", scale= 0.10)  

    def update(self, delta_time):
        #adicionar movimentação no eixo x e y
        self.center_x += self.change_x
        self.center_y += self.change_y

        #parar o personagem antes dele sair da tela
        if(self.right > 800):
            self.change_x = 0
        elif(self.left < 0):
            self.change_x = 0
        
        if(self.top > 600):
            self.change_y = 0
        elif(self.bottom < 0):
            self.change_y = 0     
        
class Bomba(arcade.Sprite):
    def __init__(self):
        super().__init__("bomba.png", scale = 0.20)
    
    def update(self, delta_time):
        pass
    

class JanelaJogo(arcade.Window):
    def __init__(self):
         super().__init__(800, 600, "Meu Jogo")
         #cor RGB (vermelho, verde, azul)
         arcade.set_background_color(  (0, 0, 0)  )
        #definir movimento
         self.movimento = 3
        #criar personagem
         self.personagem = Player()
         self.combustivel = Combustivel()
         self.bomba = Bomba()
         #posicionar ele na tela
         self.personagem.center_x = 150
         self.personagem.center_y = 58
         self.combustivel.center_x = 240
         self.combustivel.center_y = 80
         self.bomba.center_x = 200
         self.bomba.center_y = 200

         self.combustivel.change_x = self.movimento
         self.combustivel.change_y = self.movimento

         self.personagem.change_x = self.movimento
         self.personagem.change_y = self.movimento

         

        #criar lista de personagens
         self.sprite_jogador = arcade.SpriteList()
         self.sprite_combustivel = arcade.SpriteList()
         self.sprite_bomba = arcade.SpriteList()

        #adicionar o personagem no grupo de sprites
         self.sprite_jogador.append(self.personagem)
         self.sprite_combustivel.append(self.combustivel)
         self.sprite_bomba.append(self.bomba)
         

    #metodo para desenhar na tela
    def on_draw(self):
        self.clear()
        #desenhar meu personagem
        self.sprite_jogador.draw()
        self.sprite_combustivel.draw()
        self.sprite_bomba.draw()
       
        
    #atualiza a lógica de jogo e das coisas q estão na tela
    def on_update(self, delta_time):
        #atualizar as listas de sprites, o que chama o método update 
        self.sprite_jogador.update(delta_time)
        self.sprite_combustivel.update(delta_time)
        self.sprite_bomba.update(delta_time)
    
def main():
    jogo = JanelaJogo()
    arcade.run()


if __name__== "__main__":
    main()
