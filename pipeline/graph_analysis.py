from tools.vlm_tools import (
    predict_hamiltonicity,
    count_nodes,
    count_edges,
    detect_planarity
)
from chains.narrative_chain import narrative_chain

def analyze_graph_image(image_path):
    ham = predict_hamiltonicity.run(image_path)
    nodes = count_nodes.run(image_path)
    edges = count_edges.run(image_path)
    planarity = detect_planarity.run(image_path)

    narrative = narrative_chain.run({
        "ham": ham,
        "nodes": nodes,
        "edges": edges,
        "planarity": planarity
    })

    return narrative
