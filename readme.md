# Resumo

Este trabalho tem como objetivo criar uma aplicação web conteinerizada via Docker. Para isso, foi criada uma aplicação web em django a fim de cadastrar album e fotos.

## Como rodar a aplicação

**Baixar a imagem**
Para baixar a imagem hospedada no Dockerhub execute o comando

$ docker pull usuario/nome_da_imagem:tag

**Executar a imagem**
$ docker run -p 8000:8000 -d usuario/nome_da_imagem:tag