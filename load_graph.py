import osmnx as ox

G = ox.graph_from_place('Hyde Park, Illinois, USA', network_type='drive')
ox.io.save_graphml(G)
    


