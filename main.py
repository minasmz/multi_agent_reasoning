from pipeline.graph_analysis import analyze_graph_image

if __name__ == "__main__":
    image_path = "example_graph.png"  # Replace with your image path
    result = analyze_graph_image(image_path)
    print("\n--- Graph Analysis Narrative ---\n")
    print(result)
