
# Api do sistema de recomendação

O projeto consiste em uma api em Flask com apenas uma rota: `/food/{foodname}`
 
Ao passar o parametro `foodname` a api busca os alimentos mais similares dentro do que foi aprendido

O modelo se trata de um embbeding pré treinado, retirado do [NILC](http://nilc.icmc.usp.br/embeddings) (Interinstitutional Center for Computational Linguistics)

#### Exemplo de Embedding
![Exemplo de Embbeding](https://developers.google.com/machine-learning/crash-course/images/linear-relationships.svg)
[Referência](https://developers.google.com/machine-learning/crash-course/embeddings/translating-to-a-lower-dimensional-space)