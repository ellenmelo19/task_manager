from pymongo import MongoClient

try:
    client = MongoClient('localhost', 27017)
    client.server_info()  # Força uma conexão com o servidor
    print("Conectado ao MongoDB com sucesso!")
except Exception as e:
    print(f"Erro ao conectar ao MongoDB: {e}")
