● art.py: logo

● main.py: arquivo principal

-----------------

<img width="1052" height="885" alt="image" src="https://github.com/user-attachments/assets/1eea6ccc-7173-42e9-af75-e496ccbfe049" />

● Criei as funções que irei utilizar: 

dar 2 cartas ao usuário e máquina, carta adicional para o usuário, carta adicional para a máquina e a soma das cartas de ambos

-----------------

<img width="851" height="492" alt="image" src="https://github.com/user-attachments/assets/14d60f91-265f-4c98-86e6-c8613047ffd7" />

● Criei a lista que contém as cartas e também a lista do usuário e máquina

● Criei mais uma função para saber se a carta "Ace" irá valer 1 ou 11

-----------------

<img width="1428" height="324" alt="image" src="https://github.com/user-attachments/assets/ba55ba4b-7b81-4a74-9e4f-055412db6100" />


● Crio um input para saber se o usuário deseja começar a jogar

● limpo a tela e chamo as funções para o usuário e máquina para terem 2 cartas iniciais

-----------------

<img width="1509" height="728" alt="image" src="https://github.com/user-attachments/assets/fbba95dc-47aa-45ce-9cc0-ff30952ea5e5" />

● Mostro para o usuário as cartas que ele tem atualmente, além da pontuação total

● Mostro também a primeira carta da máquina

● Pergunto se o usuário quer mais uma carta:

    Se sim: chamo a função de adicionar mais uma carta pra ele.

      Continuo perguntando ppara o usuário se ele deseja continuar a pegar mais cartas.
      Porém se a soma do baralho for maior que 21, automaticamente cancelo o input e já defino uma variável pra interromper o loop while()

    Se o usuário responder não: Interrompo o loop e já vai para a próxima seção que irá definir se o usuário ou a máquina ganhou

-----------------
<img width="1256" height="853" alt="image" src="https://github.com/user-attachments/assets/5e68da8d-c013-4008-963c-b0e7f66f6ba4" />

<img width="1227" height="763" alt="image" src="https://github.com/user-attachments/assets/4968e341-2b52-4826-9580-d5a1bbb74b1a" />

    Se a soma do deck do usuário ultrapassar 21, então ele perde
    Se não, a máquina vai adicionar mais cartas, com limite de soma até 17

    Se a soma do deck da máquina superar 21, o usuário ganha

    Se a soma do usuário for maior que a da máquina, usuário ganha e se for o contrário, a máquina ganha

    No final, se não atender nenhuma das condições, então é um empate
