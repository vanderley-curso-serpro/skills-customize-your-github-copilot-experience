
# 📘 Assignment: Hangman Game in Python

## 🎯 Objective

Desenvolver um jogo da forca em Python para praticar lógica de programação com strings, loops e condicionais. Ao final, o aluno deve ser capaz de controlar o fluxo de uma partida com regras claras de vitória e derrota.

Objetivo de aprendizagem: aplicar estruturas de controle e manipulação de texto em um projeto completo.

## 📝 Tasks

Tarefas propostas: implemente o núcleo do jogo e depois adicione validações e regras de encerramento.

### 🛠️ Build the Core Hangman Loop

#### Descrição
Implemente a base do jogo escolhendo uma palavra secreta de uma lista e mantendo o loop principal de tentativas até o fim da partida.

#### Requisitos
O programa concluído deve:

- Selecionar uma palavra aleatoriamente de uma lista predefinida
- Exibir a palavra oculta usando `_` para letras ainda não descobertas
- Solicitar um palpite de letra por rodada usando `input()`
- Atualizar corretamente o progresso da palavra quando o palpite estiver certo
- Encerrar a rodada quando todas as letras forem descobertas


### 🛠️ Add Validation, Attempts, and End Messages

#### Descrição
Evolua o jogo com controle de tentativas, validação de entrada e mensagens finais para tornar a experiência completa.

#### Requisitos
O programa concluído deve:

- Definir um número máximo de tentativas incorretas e decrementá-lo quando necessário
- Validar a entrada para aceitar apenas uma letra por vez
- Ignorar ou avisar quando uma letra já tiver sido informada anteriormente
- Exibir mensagem de vitória quando a palavra for adivinhada
- Exibir mensagem de derrota com a palavra correta quando as tentativas acabarem