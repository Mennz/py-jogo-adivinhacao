# Jogo de adivinhação

Jogo de terminal em Python: o computador sorteia um número e você tenta adivinhar,
recebendo dicas de "maior" ou "menor" a cada palpite errado.

Tem três níveis de dificuldade, cada um com um intervalo de números e um limite de
tentativas diferente. Se o limite acabar antes de você acertar, o programa revela o
número e pergunta se você quer jogar de novo.

## O que pratiquei

- `random.randint` para sortear o número secreto
- `while` com condição de parada (limite de tentativas) e `break` no acerto
- organizar o jogo numa função para poder chamá-la de novo no loop de replay
- validar entrada do usuário sem travar o programa com `ValueError`

## Como rodar

```
python jogo.py
```

Escolha a dificuldade (1, 2 ou 3) e vá digitando os palpites.
