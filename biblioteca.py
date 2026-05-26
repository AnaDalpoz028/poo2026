import arcade

#personagem
class Player(arcade.Sprite):
    def __init__(self):
        super().__init__("mcqueen_direita.png", scale=0.20)
        self.textura_direita = arcade.load_texture("mcqueen_direita.png")
        self.textura_esquerda = arcade.load_texture("mcqueen_esquerda1.png")
        
        

    #atualizar personagem
    def update(self, delta_time):
       pass

class JanelaJogo(arcade.Window):
    def __init__(self):
         super().__init__(800, 600, "Meu Jogo")
         #cor RGB (vermelho, verde, azul)
         arcade.set_background_color(  (0, 0, 0)  )
        #criar personagem
         self.personagem = Player()
         #posicionar ele na tela
         self.personagem.center_x = 150
         self.personagem.center_y = 400
         
         

    #metodo para desenhar na tela
    def on_draw(self):
        self.clear()
        #desenhar meu personagem
        arcade.draw_sprite(self.personagem)
       
        

    def on_update(self, delta_time):
        pass
    
def main():
    jogo = JanelaJogo()
    arcade.run()


if __name__== "__main__":
    main()
