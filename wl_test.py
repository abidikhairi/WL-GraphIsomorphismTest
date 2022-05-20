import argparse
import networkx as nx
import matplotlib.pyplot as plt
from utils import color_refinement, plot_graphs, make_animation


def main(args):
    num_iterations  = args.num_iterations
    num_nodes = args.num_nodes
    num_edges = args.num_edges

    G1 = nx.gnm_random_graph(num_nodes, num_edges)
    G2 = nx.gnm_random_graph(num_nodes, num_edges)

    nx.set_node_attributes(G1, 1, 'color')
    nx.set_node_attributes(G2, 1, 'color')
    nx.set_node_attributes(G1, 1, 'prev')
    nx.set_node_attributes(G2, 1, 'prev')
    
    plot_graphs(G1, G2, 'Before Color Refinement', ['figures/graph1_before_color_refinement.png', 'figures/graph2_before_color_refinement.png'])    

    G1, g1_snapshots = color_refinement(G1, num_iterations)
    G2, g2_snapshots = color_refinement(G2, num_iterations)
    
    plot_graphs(G1, G2, 'After Color Refinement', ['figures/graph1_after_color_refinement.png', 'figures/graph2_after_color_refinement.png'])
    
    make_animation(G1, g1_snapshots, 'figures/g1_color_refinement.gif', 'Graph 1')
    make_animation(G2, g2_snapshots, 'figures/g2_color_refinement.gif', 'Graph 2')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='WL Graph Isomorphism Test algorithm')

    parser.add_argument('--num-nodes', type=int, default=10, help='Number of nodes in the graph')
    parser.add_argument('--num-edges', type=int, default=20, help='Number of edges in the graph')
    parser.add_argument('--num-iterations', type=int, default=20, help='Number of iterations')

    args = parser.parse_args()
    main(args)
