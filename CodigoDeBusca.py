# Importa as bibliotecas necessárias
import matplotlib.pyplot as plt
import networkx as nx

# Cria um novo grafo vazio
G = nx.Graph()

# Define o atributo "Name" do grafo como "Grafico"
G.graph["Name"] = "Grafico"

# Adiciona os nós ao grafo, cada um com um nome e um atributo "Name"
G.add_nodes_from([
    ("A",{"Name":"Rua 5"}),
    ("B",{"Name":"Rua Ribamar Carvalho"}),
    ("C",{"Name":"Rua 8"}),
    ("D",{"Name":"Rua 9"}),
    ("E",{"Name":"Rua 6"}),
    ("F",{"Name":"Escola"})
])

# Adiciona as arestas ao grafo, especificando os nós conectados e atributos adicionais como "distance"
G.add_edges_from([
    ("A","B",{"distance":12}),
    ("A","C",{"distance":6}),
    ("B","C",{"distance":5}),
    ("B","D",{"distance":9}),
    ("B","E",{"distance":5}),
    ("C","D",{"distance":4}),
    ("D","F",{"distance":6}),
    ("E","F",{"distance":9})
])

# Define a posição de cada nó no espaço 2D
pos = {
    "A":(1,5),
    "B":(4.5,6.6),
    "C":(3.6,1.4),
    "D":(7.1,1.1),
    "E":(7.7,6.6),
    "F":(9.3,3.7),
}

# Define a posição dos rótulos dos nós
pos_node_atributes = {
    "A":(-0.4,5),
    "B":(4.5,7.4),
    "C":(3.6,0.4),
    "D":(7.1,0.1),
    "E":(7.7,7.3),
    "F":(10.8,3.7),
}

# Define os rótulos das arestas
edge_labels={(u,v):d["distance"] for u,v,d in G.edges(data=True)}

# Define os rótulos dos nós
node_labels = {n: d["Name"] for n, d in G.nodes(data=True)}

# Desenha os nós e as arestas do grafo
nx.draw(G, pos=pos, with_labels=True, node_color="red", node_size=2000, font_color="white", font_size=20, font_family="Times New Roman", font_weight="bold", width=5, edge_color="lightgray")

# Adiciona os rótulos dos nós ao desenho
nx.draw_networkx_labels(G, pos=pos_node_atributes, labels=node_labels, font_color="black", font_size=20, font_family="Times New Roman", font_weight="bold")

# Adiciona os rótulos das arestas ao desenho
nx.draw_networkx_edge_labels(G, pos=pos, edge_labels=edge_labels, label_pos=0.5)

# Define as margens do gráfico
plt.margins(0.2)

# Exibe o gráfico
plt.show()
