# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Aprender a construir uma API REST com FastAPI, criando endpoints para leitura, criação e atualização de recursos. Ao final, o aluno deve conseguir estruturar rotas, validar dados com Pydantic e retornar respostas HTTP apropriadas.

## 📝 Tasks

### 🛠️ Create a Basic FastAPI App and Read Endpoints

#### Descrição
Inicie uma aplicação FastAPI com uma lista em memória de itens e implemente endpoints de leitura para testar a estrutura da API.

#### Requisitos
O programa concluído deve:

- Criar uma instância `FastAPI()` no arquivo principal
- Implementar `GET /` retornando uma mensagem simples de status da API
- Implementar `GET /items` retornando todos os itens cadastrados em memória
- Implementar `GET /items/{item_id}` retornando um item específico pelo ID
- Retornar erro 404 quando o item solicitado não existir


### 🛠️ Add Create and Update Endpoints with Validation

#### Descrição
Expanda a API com criação e atualização de itens usando modelos Pydantic para validar entradas e manter os dados consistentes.

#### Requisitos
O programa concluído deve:

- Definir um modelo `Item` com campos `name`, `description` e `price`
- Implementar `POST /items` para adicionar novos itens e gerar ID automaticamente
- Implementar `PUT /items/{item_id}` para atualizar um item existente
- Retornar código HTTP 201 ao criar item com sucesso
- Validar que `price` seja maior que zero e retornar erro de validação quando inválido
