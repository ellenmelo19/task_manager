# Gerenciamento de Tarefas com Python e MongoDB

Este projeto implementa um sistema simples de gerenciamento de tarefas utilizando Python e MongoDB. Ele permite criar, listar, atualizar e deletar tarefas armazenadas em um banco de dados MongoDB local.

## Configuração

Certifique-se de ter Python e MongoDB instalados no seu ambiente de desenvolvimento.

### Instalação das Dependências

Instale as dependências necessárias utilizando o seguinte comando:

```
pip install pymongo
```

### Configuração do MongoDB

Certifique-se de ter um servidor MongoDB em execução localmente na porta padrão `27017`. O banco de dados utilizado pelo projeto é `task_management`.

## Funcionalidades

- **Criar Tarefa:** Permite criar uma nova tarefa especificando título e descrição.
- **Listar Tarefas:** Lista todas as tarefas armazenadas no banco de dados, mostrando título, descrição e status.
- **Atualizar Tarefa:** Permite atualizar o título, descrição ou status de uma tarefa existente.
- **Deletar Tarefa:** Remove uma tarefa do banco de dados com base no seu ID.

  OBS: Selecionar tarefa antes de Atualizar ou Deletar

## Uso

Execute o script `task_manager.py` (localizado na master branch) e siga as instruções do menu para interagir com o sistema de gerenciamento de tarefas.

```
python task_manager.py
```

### Requisitos
- Python 3.x
- MongoDB
- Bibliotecas: pymongo, tkinter (ou outra biblioteca de interface gráfica que você esteja usando)

## Melhorias
Melhorias planejadas para este projeto: 
- ~~Implementar a GUI (Interface Gráfica)~~
- Notificações e Lembretes
- Filtros e Ordenação

## Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para enviar pull requests para melhorar este projeto.


## Licença

Este projeto está licenciado sob a [Licença MIT](./LICENSE).

---
