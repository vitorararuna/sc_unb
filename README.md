# sc_unb

Vitor de Oliveira Araujo Araruna
202060980

Thiago Maciel de campos 
180131699

A cifra de Vigenère é um método de criptografia polialfabética inventado por Blaise de Vigenère no século XVI. Ela é uma extensão da cifra de César, que é uma cifra de substituição simples em que cada letra da mensagem é substituída por outra letra deslocada um determinado número de posições no alfabeto.

A grande inovação da cifra de Vigenère é o uso de uma palavra-chave como base para o deslocamento das letras da mensagem. A palavra-chave é repetida várias vezes até ter o mesmo comprimento da mensagem original, formando assim a chamada keystream. Cada letra da mensagem original é então deslocada de acordo com a letra correspondente na keystream.

Essa técnica de cifragem torna a cifra de Vigenère mais segura do que a cifra de César simples, pois o uso da palavra-chave introduz uma variação no deslocamento das letras, dificultando a quebra da cifra por meio de análise estatística.

O algoritmo implementado no código em Python segue os passos básicos da cifra de Vigenère. Ele possui duas funções principais: cipher(cifrador) e decoder(decifrador).

A função cipher recebe uma mensagem e uma chave como entrada. Primeiro, ela gera a keystream chamando a função gerar_chave, que percorre cada caractere da mensagem e atribui a letra correspondente da chave à keystream. Em seguida, a função percorre cada caractere da mensagem original. Se o caractere for uma letra, é aplicada a operação de cifra de Vigenère, somando os valores ASCII do caractere da mensagem e da correspondente letra da keystream e aplicando a aritmética modular para obter o caractere cifrado. Caso contrário, o caractere é mantido inalterado. A função retorna a mensagem cifrada.

A função decoder recebe uma mensagem cifrada (gerada pela funcao acima) e uma chave como entrada. Da mesma forma que o cipher, ela gera a keystream chamando a função gerar_chave. Em seguida, percorre cada caractere da mensagem cifrada e realiza a operação de decifra de Vigenère, subtraindo os valores ASCII do caractere cifrado e da correspondente letra da keystream e aplicando a aritmética modular para obter o caractere decifrado. Os caracteres não alfabéticos são mantidos inalterados. A função retorna a mensagem decifrada.

O código principal solicita ao usuário que digite uma mensagem e uma chave. Em seguida, chama as funções cipher e decoder para cifrar e decifrar a mensagem usando a chave fornecida. Por fim, exibe a mensagem cifrada e a mensagem decifrada.