# p2-m06

# Como executar

Entre na pasta src e execute, em sequência, os arquivos extract_frames.py, face_detection.py e make_up_video.py

`$ python3 <nome-do-arquivo>`

# Perguntas técnicas

## 2.1
A técnica utilizada foi o Haar Cascade. Ele é uma técnica poderosa e eficiente para a detecção de objetos em imagens, como rostos, carros, e outros objetos comuns, detectando-os de maneira rápida. Ele utiliza uma série de imagens positivas e negativas em cascata, que influenciam nas cascatas posteriores.

## 2.2
Considerando termos como viabilidade técnica, facilidade de implementação e versatilidade da solução, é possível dizer que o CNN seria uma boa primeira opção, já que pode resolver problemas mais complexos, não lineares. 

Em seguida, colocaria o NN, rede neural com uma camada de neurônios, considerando que é relativamente simples de implementá-lo e consegue ser utilizado para problemas de detecção de faces.

Em terceiro, colocaria o Haar Cascade, que, embora não seja tão preciso, também é relativamente simples de implementá-lo.

Por fim, coloco o filtro e correlação cruzada, que é usado para detectar padrões em imagens, mas não é tão preciso e não se adapta bem a esse problema de detectar faces.

## 2.3
Considerando viabilidade técnica, e pelos mesmos motivos da 2.2, a ordem fica:
CNN
NN
Haar Cascade
Correlação cruzada

## 2.4
Sim, o Haar Cascade, por exemplo, consegue ser implementado por meio de várias cascatas, sendo que uma cascata pode influenciar a próxima.

## 2.5
Vini Jr.
