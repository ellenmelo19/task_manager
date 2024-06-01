import tkinter as tk
from tkinter import messagebox
from bson.objectid import ObjectId
from pymongo import MongoClient

# Configura a conexão com o MongoDB
client = MongoClient('localhost', 27017)
db = client['task_management']
tasks_collection = db['tasks']

def create_task(title, description):
    task = {
        'title': title,
        'description': description,
        'status': 'pending'
    }
    result = tasks_collection.insert_one(task)
    return result.inserted_id

def get_tasks():
    tasks = tasks_collection.find()
    return list(tasks)

def update_task(task_id, updates):
    result = tasks_collection.update_one({'_id': ObjectId(task_id)}, {'$set': updates})
    return result.modified_count

def delete_task(task_id):
    result = tasks_collection.delete_one({'_id': ObjectId(task_id)})
    return result.deleted_count

# Funções da Interface Gráfica
def add_task():
    title = entry_title.get()
    description = entry_description.get()
    if title and description:
        task_id = create_task(title, description)
        list_tasks()
        messagebox.showinfo("Sucesso", f"Tarefa criada com ID: {task_id}")
    else:
        messagebox.showerror("Erro", "Título e descrição são obrigatórios")

def list_tasks():
    tasks = get_tasks()
    listbox_tasks.delete(0, tk.END)
    for task in tasks:
        listbox_tasks.insert(tk.END, f"ID: {task['_id']} - {task['title']} ({task['status']})")

def update_selected_task():
    try:
        selected_task = listbox_tasks.get(listbox_tasks.curselection())
        task_id = selected_task.split(" ")[1]
        title = entry_title.get()
        description = entry_description.get()
        status = status_var.get()
        updates = {}
        if title:
            updates['title'] = title
        if description:
            updates['description'] = description
        if status:
            updates['status'] = status
        update_task(task_id, updates)
        list_tasks()
        messagebox.showinfo("Sucesso", "Tarefa atualizada")
    except IndexError:
        messagebox.showerror("Erro", "Selecione uma tarefa para atualizar")

def delete_selected_task():
    try:
        selected_task = listbox_tasks.get(listbox_tasks.curselection())
        task_id = selected_task.split(" ")[1]
        delete_task(task_id)
        list_tasks()
        messagebox.showinfo("Sucesso", "Tarefa deletada")
    except IndexError:
        messagebox.showerror("Erro", "Selecione uma tarefa para deletar")

# Interface Gráfica com Tkinter
app = tk.Tk()
app.title("Gerenciamento de Tarefas")

frame = tk.Frame(app)
frame.pack(pady=20)

# Entradas de Texto
entry_title = tk.Entry(frame, width=30)
entry_title.grid(row=0, column=1, padx=10, pady=5)
entry_description = tk.Entry(frame, width=30)
entry_description.grid(row=1, column=1, padx=10, pady=5)

tk.Label(frame, text="Título:").grid(row=0, column=0)
tk.Label(frame, text="Descrição:").grid(row=1, column=0)

# Lista de Tarefas
listbox_tasks = tk.Listbox(app, width=100)
listbox_tasks.pack(pady=10)

# Botões
status_var = tk.StringVar()
status_var.set("pending")
tk.OptionMenu(app, status_var, "pending", "complete").pack(pady=5)

button_frame = tk.Frame(app)
button_frame.pack(pady=10)

tk.Button(button_frame, text="Adicionar Tarefa", command=add_task).grid(row=0, column=0, padx=5)
tk.Button(button_frame, text="Listar Tarefas", command=list_tasks).grid(row=0, column=1, padx=5)
tk.Button(button_frame, text="Atualizar Tarefa", command=update_selected_task).grid(row=0, column=2, padx=5)
tk.Button(button_frame, text="Deletar Tarefa", command=delete_selected_task).grid(row=0, column=3, padx=5)

# Inicializa a lista de tarefas
list_tasks()

app.mainloop()
