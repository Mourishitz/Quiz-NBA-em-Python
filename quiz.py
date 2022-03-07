# função para iniciar o jogo + declaração de variaveis
def novo_jogo():
    escolha_usuario = []
    escolha_correta = 0
    numero_questao = 1
    for i in questoes:
        print("---------------------------------------------------------------------")
        print(i)
        for j in opcoes[numero_questao-1]:
            print(j)
        # algoritmo para a escolha de respostas e ganho de pontos
        escolha = input("Resposta?: ")
        escolha = escolha.upper()
        escolha_usuario.append(escolha) 
        
        escolha_correta += resposta(questoes.get(i),escolha)
        numero_questao += 1

    pontos(escolha_correta, escolha)


# algoritmo para averiguar a resposta certa e calcular o total de pontos
def resposta(resposta_certa, escolha):

    if resposta_certa == escolha:
        print("CORRETO!")
        return 1
    else:
        print("Resposta Errada :(")
        return 0
# algoritmo de resultado final com base nas escolhas do usuario
def pontos(escolha_correta, escolha):
    print("---------------------------------------------------------------------")
    print("Resultados")
    print("---------------------------------------------------------------------")

    print("Respostas: ", end="")
    for k in questoes:
        print(questoes.get(k), end="")
    print()

    score = int((escolha_correta/len(questoes))*100)
    print("Sua pontuação é de: "+str(score)+"%")
    
# algoritmo para reiniciar o jogo
def jogar_dnv():

    response = input("Você deseja jogar de novo? (sim/nao): ")
    response = response.upper()

    if response == "SIM":
        return True
    else:
        return False
# Questões do jogo em seguida de sua resposta
questoes = {
        "Qual foi o primeiro time a marcar 72-10 em uma temporada regular de Basquete?: ": "A",
        "Qual o jogador com mais titulos de campeão da NBA até 2021?: ": "B",
        "Pela primeira vez na história um time conseguiu vencer uma final tendo uma desvantagem de 3 derrotas e 1 vitória, qual time é este?: ": "C",
        "Quais jogadores faziam parte do famoso 'Big 3' do Miami Heat em 2010?: ": "A"
    }
# Respostas 
opcoes = [
        ["A. Chicago Bulls", "B. Los Angeles Lakers", "C. Boston Celtics", "D. Miami Heat"],
        ["A. Michael Jordan", "B. Bill Russel", "C. Shaquille O'Neal", "D. Lebron James"],
        ["A. Oklahoma City Thunder", "B. Phoenix Suns", "C. Cleveland Cavaliers", "D. Golden State Warriors"],
        ["A. Lebron James, Dwyane Wade, Chris Bosh", "B. Jimmy Butler, Bam Adebayo, Tyler Herro",
         "C. Dwayne Wade, Shaquille O'Neal, Gary Payton", "D. Anthony Davis, Lebron James, Russel Westbrook"]
    ]
novo_jogo()

while jogar_dnv():
    novo_jogo()

print("Obrigado por jogar!")
