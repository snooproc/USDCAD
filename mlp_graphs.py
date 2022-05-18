#graphs courtesy of Andreas Mueller and can be found at https://github.com/amueller/introduction_to_ml_with_python/blob/master/mglearn/plot_nn_graphs.py
from imageio import imread
import graphviz
from pylab import plt, mpl

def plot_regression_graph():
    #import graphviz
    lr_graph = graphviz.Digraph(node_attr={'shape': 'circle', 'fixedsize': 'True'},
                                graph_attr={'rankdir': 'LR', 'splines': 'line'})
    inputs = graphviz.Digraph(node_attr={'shape': 'circle'}, name="cluster_0")
    output = graphviz.Digraph(node_attr={'shape': 'circle'}, name="cluster_2")

    for i in range(4):
        inputs.node("x[%d]" % i, labelloc="c")
    inputs.body.append('label = "inputs"')
    inputs.body.append('color = "white"')

    lr_graph.subgraph(inputs)

    output.body.append('label = "output"')
    output.body.append('color = "white"')
    output.node("y")

    lr_graph.subgraph(output)

    for i in range(4):
        lr_graph.edge("x[%d]" % i, "y", label="w[%d]" % i)
    return lr_graph


def plot_hidden_layer_graph():
    #import graphviz
    nn_graph = graphviz.Digraph(node_attr={'shape': 'circle', 'fixedsize': 'True'},
                                graph_attr={'rankdir': 'LR', 'splines': 'line'})

    inputs = graphviz.Digraph(node_attr={'shape': 'circle'}, name="cluster_0")
    hidden = graphviz.Digraph(node_attr={'shape': 'circle'}, name="cluster_1")
    hidden2 = graphviz.Digraph(node_attr={'shape': 'circle'}, name="cluster_2")

    output = graphviz.Digraph(node_attr={'shape': 'circle'}, name="cluster_3")

    for i in range(4):
        inputs.node("x[%d]" % i)

    inputs.body.append('label = "inputs"')
    inputs.body.append('color = "white"')

    for i in range(3):
        hidden.node("h1[%d]" % i)

    for i in range(3):
        hidden2.node("h2[%d]" % i)

    hidden.body.append('label = "hidden layer 1"')
    hidden.body.append('color = "white"')

    hidden2.body.append('label = "hidden layer 2"')
    hidden2.body.append('color = "white"')

    output.node("y")
    output.body.append('label = "output"')
    output.body.append('color = "white"')

    nn_graph.subgraph(inputs)
    nn_graph.subgraph(hidden)
    nn_graph.subgraph(hidden2)

    nn_graph.subgraph(output)

    for i in range(4):
        for j in range(3):
            nn_graph.edge("x[%d]" % i, "h1[%d]" % j, label="")

    for i in range(3):
        for j in range(3):
            nn_graph.edge("h1[%d]" % i, "h2[%d]" % j, label="")

    for i in range(3):
        nn_graph.edge("h2[%d]" % i, "y", label="")

    return nn_graph


def plot_tree(ax=None):
    #import graphviz
    if ax is None:
        ax = plt.gca()
    mygraph = graphviz.Digraph(node_attr={'shape': 'box'},
                               edge_attr={'labeldistance': "10.5"},
                               format="png")
    mygraph.node("0", "USD1M - CAD1M > 0?")
    mygraph.node("1", "SPX - TSE > 25%?")
    mygraph.node("2", "VIX > 25%?")
    mygraph.node("3", "% USDCAD > 0")
    mygraph.node("4", "% USDCAD < 0")
    mygraph.node("5", "% USDCAD > 0")
    mygraph.node("6", "% USDCAD < 0")
    mygraph.edge("0", "1", label="True")
    mygraph.edge("0", "2", label="False")
    mygraph.edge("1", "3", label="True")
    mygraph.edge("1", "4", label="False")
    mygraph.edge("2", "5", label="True")
    mygraph.edge("2", "6", label="False")
    ax.set_axis_off()
    
    return mygraph
    # mygraph.render("temp")
    # ax.imshow(imread("temp.png"))
    # ax.set_axis_off()
