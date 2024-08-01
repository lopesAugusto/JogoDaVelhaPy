import tkinter as tk
from tkinter import messagebox

class JogoDaVelha:
    def __init__(self):
        self.janela = tk.Tk()
        self.tabuleiro = [""] * 9
        self.vez_jogador = "X"
        self.janela.title(f"Jogo da Velha: {self.vez_jogador}")
        self.mensagem = ""

        for i in range(9):
            btn = tk.Button(self.janela, text="", command=lambda i=i: self.clique(i))
            btn.grid(row=i // 3, column=i % 3, sticky="NSEW")

        # tamanho
        self.janela.geometry('300x300')

        for i in range(3):
            self.janela.rowconfigure(i, weight= 1)
            self.janela.columnconfigure(i, weight= 1)

    def atualiza_botao(self, posicao):
        btn = self.janela.winfo_children()[posicao]
        if btn["text"] != "":
            btn.config(bg="yellow")
        btn.config(text=self.tabuleiro[posicao])

    def verifica_vencedor(self):
        # Lógica para verificar o vencedor (linhas, colunas, diagonais)

        # verifica se a posisção jogada é valida
        # verifica se coluna um coluna 2 ou coluna 3 tem o mesmo simbolo
        # verifica se linha um linha 2 ou linha 3 tem o mesmo simbolo
        # verifiva verticalmente
        # horizontal
        if self.tabuleiro[0] == self.tabuleiro[1] and self.tabuleiro[0] == self.tabuleiro[2] and self.tabuleiro[0] != "":
            self.mensagem = f"linha 1 venceu com {self.vez_jogador}"
            self.atualiza_botao(0)
            self.atualiza_botao(1)
            self.atualiza_botao(2)
            return True
        elif self.tabuleiro[3] == self.tabuleiro[4] and self.tabuleiro[3] == self.tabuleiro[5] and self.tabuleiro[3] != "":
            self.mensagem = f"linha 2 venceu com {self.vez_jogador}"
            self.atualiza_botao(3)
            self.atualiza_botao(4)
            self.atualiza_botao(5)
            return True
        elif self.tabuleiro[6] == self.tabuleiro[7] and self.tabuleiro[6] == self.tabuleiro[8] and self.tabuleiro[6] != "":
            self.mensagem = f"linha 3 venceu com {self.vez_jogador}"
            self.atualiza_botao(6)
            self.atualiza_botao(7)
            self.atualiza_botao(8)
            return True

        # vertical
        elif self.tabuleiro[0] == self.tabuleiro[3] and self.tabuleiro[0] == self.tabuleiro[6] and self.tabuleiro[0] != "":
            self.mensagem = f"coluna 1 venceu com {self.vez_jogador}"
            self.atualiza_botao(0)
            self.atualiza_botao(3)
            self.atualiza_botao(6)
            return True
        elif self.tabuleiro[1] == self.tabuleiro[4] and self.tabuleiro[1] == self.tabuleiro[7] and self.tabuleiro[1] != "":
            self.mensagem = f"coluna 2 venceu com {self.vez_jogador}"
            self.atualiza_botao(1)
            self.atualiza_botao(4)
            self.atualiza_botao(7)
            return True
        elif self.tabuleiro[2] == self.tabuleiro[5] and self.tabuleiro[2] == self.tabuleiro[8] and self.tabuleiro[2] != "":
            self.mensagem = f"coluna 3 venceu com {self.vez_jogador}"
            self.atualiza_botao(2)
            self.atualiza_botao(5)
            self.atualiza_botao(8)
            return True

        # diagonais
        elif self.tabuleiro[0] == self.tabuleiro[4] and self.tabuleiro[0] == self.tabuleiro[8] and self.tabuleiro[0] != "":
            self.mensagem = f"diagonais venceu com {self.vez_jogador}"
            self.atualiza_botao(0)
            self.atualiza_botao(4)
            self.atualiza_botao(8)
            return True
        elif self.tabuleiro[2] == self.tabuleiro[4] and self.tabuleiro[2] == self.tabuleiro[6] and self.tabuleiro[2] != "":
            self.mensagem = f"diagonais venceu com {self.vez_jogador}"
            self.atualiza_botao(2)
            self.atualiza_botao(4)
            self.atualiza_botao(6)
            return True
        
        elif not("" in self.tabuleiro):
            self.mensagem = "velhou"
            return True
        else:
            return False

        # 0 | 1 | 2
        # ----------
        # 3 | 4 | 5
        # ----------
        # 6 | 7 | 8

    def clique(self, posicao):
        if self.tabuleiro[posicao] == "":
            self.tabuleiro[posicao] = self.vez_jogador
            self.atualiza_botao(posicao)
            vencedor = self.verifica_vencedor()
            if vencedor:
                messagebox.showinfo("Fim do Jogo", f"{self.mensagem} ")
                self.janela.quit()
            else:
                self.vez_jogador = "O" if self.vez_jogador == "X" else "X"
                self.janela.title(f"Jogo da Velha: {self.vez_jogador}")


if __name__ == "__main__":
    jogo = JogoDaVelha()
    jogo.janela.mainloop()
