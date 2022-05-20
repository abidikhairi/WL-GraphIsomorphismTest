import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation



def make_animation(graph, snapshots, filename, graph_title):
    def AnimationFunction(frame):
        plt.clf()
        plt.title('{}: Color Refinement at iteration {}'.format(graph_title, frame))
        nx.draw(graph, node_color=snapshots[frame])

    figure = plt.figure(figsize=(15, 10))
    plt.title('{}: Color Refinement at iteration 0'.format(graph_title))
    nx.draw(graph, node_color=list(nx.get_node_attributes(graph, 'color').values()))
    
    anim = FuncAnimation(figure, AnimationFunction, frames=len(snapshots), interval=500)
    anim.save(filename, writer='imagemagick')
    plt.close()


def plot_graphs(g1, g2, title, filenames):
    plt.figure(figsize=(15, 10))
    plt.title(title)
    plt.subplot(121)
    
    plt.title('Graph 1: {} nodes and {} edges'.format(g1.number_of_nodes(), g1.number_of_edges()))
    nx.draw(g1, node_color=list(nx.get_node_attributes(g1, 'color').values()))
    plt.savefig(filenames[0])
    plt.subplot(122)

    plt.title('Graph 2: {} nodes and {} edges'.format(g2.number_of_nodes(), g2.number_of_edges()))
    nx.draw(g2, node_color=list(nx.get_node_attributes(g2, 'color').values()))
    plt.savefig(filenames[1])
    plt.show()


def hash(neighbors, num_nodes):
    return sum(list(neighbors)) % num_nodes


def color_refinement(graph, k):
    snapshots = []
    num_nodes = graph.number_of_nodes()
    for _ in range(k):
        for node, _ in graph.nodes(data=True):
            colors = []
            for n in graph.neighbors(node):
                colors.append(graph.nodes[n]['prev'])

            prev = graph.nodes[node]['color']
            graph.nodes[node]['color'] = hash(colors, num_nodes)
            graph.nodes[node]['prev'] = prev
        
        snapshots.append(list(nx.get_node_attributes(graph, 'color').values()))

    return graph, snapshots
