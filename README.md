
1) Observe o trecho de código abaixo:


```
int INDICE = 13, SOMA = 0, K = 0;

enquanto K < INDICE faça

{

K = K + 1;

SOMA = SOMA + K;

}

imprimir(SOMA);



Ao final do processamento, qual será o valor da variável SOMA?
```
R.: [91](1_questao.py)


3) Descubra a lógica e complete o próximo elemento:

- a) 1, 3, 5, 7, ___
    ```R.: 7+2 = 9```

- b) 2, 4, 8, 16, 32, 64, ____
    ```R.: 64*2 = 128```

- c) 0, 1, 4, 9, 16, 25, 36, ____
    ```R.: 7^2 = 49```

- d) 4, 16, 36, 64, ____
    ```R.: 10^2 = 100```

- e) 1, 1, 2, 3, 5, 8, ____
    ```R.: 8 + 5 = 13```

- f) 2,10, 12, 16, 17, 18, 19, ____
    ```R.: Todos começam com a letra 'D', logo o próximo deve ser 200 (duzentos)```

4) Você está em uma sala com três interruptores, cada um conectado a uma lâmpada em uma sala diferente. Você não pode ver as lâmpadas da sala em que está, mas pode ligar e desligar os interruptores quantas vezes quiser. Seu objetivo é descobrir qual interruptor controla qual lâmpada.

```
1. Primeiro, ligue o primeiro interruptor e aguarde alguns minutos antes de desligá-lo.
2. Em seguida, ligue o segundo interruptor e deixe-o ligado.
3. Vá até o primeiro cômodo onde há uma lâmpada e observe:
   * Se a lâmpada estiver acesa, isso significa que ela é controlada pelo segundo interruptor.
   * Se a lâmpada estiver apagada, mas ainda estiver quente, isso significa que ela é controlada pelo primeiro interruptor.
   * Se a lâmpada estiver apagada e fria, isso indica que ela é controlada pelo terceiro interruptor.
4. Repita o mesmo processo, agora indo até o segundo cômodo onde há outra lâmpada.
5. Após essa observação, você saberá, por eliminação, qual interruptor controla o terceiro cômodo, sem precisar entrar nele.

Esse método permite descobrir qual interruptor controla cada lâmpada sem a necessidade de entrar em todos os cômodos.
```