import requests
import numpy as np
import networkx as nx
# pip install python-louvain
import community.community_louvain as community_louvain
from access_token import TOKEN
import matplotlib.pyplot as plt


domain = "https://api.vk.com/method"

def get_friends(user_id):
    url = f"{domain}/friends.get?&user_id={user_id}&access_token={TOKEN}&v=5.199"
    response = requests.get(url) # Ответ сервера на посланный нами запрос
    src = response.json()
    
    return src["response"]["items"]

def get_adjacency_matrix(users_ids):
    n = len(users_ids)
    size = (n, n)
    adjacency_matrix = np.zeros(size)

    for i in range(0, n):
        try:
            friends = get_friends(users_ids[i])
        except:
            continue
        
        for j in range(0, n):
            if users_ids[j] in friends:
                adjacency_matrix[i, j] = 1
                adjacency_matrix[j, i] = 1
            else:
                adjacency_matrix[i, j] = 0
    
    return adjacency_matrix

def build_network(users_ids):
    adjacency_matrix = get_adjacency_matrix(users_ids)
    
    # Создаем граф на основе матрицы смежности
    G = nx.Graph(adjacency_matrix)

    # Выполняем алгоритм Лувена для определения сообществ
    partition = community_louvain.best_partition(G)

    # Определяем позиции узлов для отображения
    pos = nx.spring_layout(G)  
    plt.figure(figsize=(8, 6))

    # Рисуем узлы
    nx.draw_networkx_nodes(G, pos, node_size=300, cmap=plt.get_cmap('viridis'), node_color=list(partition.values()))
    # Рисуем ребра
    nx.draw_networkx_edges(G, pos, alpha=0.5)

    # Добавляем имена вершин
    node_names = {node: str(node) for node in G.nodes()} 
    nx.draw_networkx_labels(G, pos, labels=node_names)

    plt.show()


# Сначала определяется выборка пользователей, которая представляет из себя друзей конкретного пользователя
# Затем происходит построение графа, представляемяего в виде матрицы смежности, путем определения взаимосвязи между каждым пользователем; если друзья, то существует ребро, иначе этого ребра нет
# По этой матрице происходит поиск сообществ
user_id = 513939745
users_ids = get_friends(user_id)
build_network(users_ids)