
# Implementação de algoritmos de processamento de imagens com Python

Este código contém a implementação de diversos algoritmos de processamento de imagens em Python utilizando a biblioteca OpenCV. Abaixo está uma breve descrição de cada algoritmo:




## Histogram Stretching e Mapeamento Linear

Esses dois algoritmos foram implementados sem a utilização de bibliotecas externas. O Histogram Stretching aumenta o contraste da imagem ao esticar o seu histograma para ocupar todo o intervalo de intensidades disponível (0-255). Já o Mapeamento Linear realiza uma transformação linear para aumentar o contraste da imagem, mapeando o menor valor de intensidade para 0 e o maior valor para 255.

## Histogram Equalization

O algoritmo de Equalização de Histograma foi implementado com a utilização de bibliotecas. Ele aumenta o contraste da imagem ao distribuir igualmente as intensidades dos pixels em todo o intervalo de 0 a 255.

## Histogram Specification

O algoritmo de Especificação de Histograma também foi implementado com a utilização de bibliotecas. Ele mapeia o histograma da imagem original para o histograma de uma imagem de referência, aumentando o contraste da imagem de acordo com o histograma da imagem de referência.

## CLAHE

O algoritmo CLAHE (Contrast Limited Adaptive Histogram Equalization) foi implementado com a utilização de bibliotecas. Ele divide a imagem em pequenas regiões, equalizando o histograma de cada região separadamente, evitando assim a distorção do contraste global da imagem.

## Autores

- [@igorbezerrar](https://www.github.com/igorbezerrar)

