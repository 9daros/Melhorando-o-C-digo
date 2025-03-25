# Melhorando-o-C-digo
# Gerenciador de Autenticação e Dados

## Descrição
Este projeto é uma API baseada em Flask para gerenciar autenticação de usuários e armazenamento de dados. Ele inclui rotas protegidas com JWT, um banco de dados SQLite para persistência de dados e melhorias na organização e eficiência do código.

## Melhorias Implementadas
Foram realizadas diversas melhorias no código, visando otimização e clareza:
- **Refatoração e organização:** Código reorganizado para melhor legibilidade e manutenção.
- **Uso de `executescript` na inicialização do banco:** Reduziu múltiplas chamadas `execute`, tornando a inicialização mais eficiente.
- **Uso de `get()` para acesso seguro aos dados JSON:** Evita exceções caso uma chave não esteja presente.
- **Melhoria nas consultas SQL:** Explicitação das colunas nos `SELECTs` para maior clareza.
- **Ajustes de formatação:** Melhor espaçamento e estruturação para facilitar leitura.

## Integrantes do Grupo
- [Henrique Daros](https://github.com/9daros)
- [Eduardo](https://github.com/integrante2)
