from pymongo import MongoClient
from bson.objectid import ObjectId

# Configura a conexão com o MongoDB
client = MongoClient('localhost', 27017)
db = client['task_management']
tasks_collection = db['tasks']

# Função para criar uma nova tarefa
def create_task(title, description):
    task = {
        'title': title,
        'description': description,
        'status': 'pending'
    }
    result = tasks_collection.insert_one(task)
    return result.inserted_id

# Função para obter todas as tarefas
def get_tasks():
    tasks = tasks_collection.find()
    return list(tasks)

# Função para atualizar uma tarefa
def update_task(task_id, updates):
    result = tasks_collection.update_one({'_id': ObjectId(task_id)}, {'$set': updates})
    return result.modified_count

# Função para deletar uma tarefa
def delete_task(task_id):
    result = tasks_collection.delete_one({'_id': ObjectId(task_id)})
    return result.deleted_count

# Interface simples para o usuário
def main():
    while True:
        print("\nMenu de Gerenciamento de Tarefas")
        print("1. Criar tarefa")
        print("2. Listar tarefas")
        print("3. Atualizar tarefa")
        print("4. Deletar tarefa")
        print("5. Sair")
        
        choice = input("Escolha uma opção: ")
        
        if choice == '1':
            title = input("Título da tarefa: ")
            description = input("Descrição da tarefa: ")
            task_id = create_task(title, description)
            print(f"Tarefa criada com ID: {task_id}")
        elif choice == '2':
            tasks = get_tasks()
            for task in tasks:
                print(f"ID: {task['_id']}, Título: {task['title']}, Descrição: {task['description']}, Status: {task['status']}")
        elif choice == '3':
            task_id = input("ID da tarefa: ")
            title = input("Novo título (deixe vazio para não alterar): ")
            description = input("Nova descrição (deixe vazio para não alterar): ")
            status = input("Novo status (pending/complete): ")
            updates = {}
            if title:
                updates['title'] = title
            if description:
                updates['description'] = description
            if status:
                updates['status'] = status
            updated_count = update_task(task_id, updates)
            print(f"Tarefas atualizadas: {updated_count}")
        elif choice == '4':
            task_id = input("ID da tarefa: ")
            deleted_count = delete_task(task_id)
            print(f"Tarefas deletadas: {deleted_count}")
        elif choice == '5':
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == '__main__':
    main()
