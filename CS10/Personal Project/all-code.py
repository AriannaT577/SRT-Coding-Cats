import cv2
import numpy as np

def detect_type_based_on_edges(image_path, edge_threshold=0.10):
    # Load image
    image = cv2.imread(image_path)
    if image is None:
        print("Error: Unable to load image.")
        return

    # Convert to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Detect edges using Canny
    edges = cv2.Canny(gray, 100, 200)

    # Compute edge density
    edge_pixels = np.count_nonzero(edges)
    total_pixels = edges.shape[0] * edges.shape[1]
    edge_density = edge_pixels / total_pixels

    # Classification based on threshold
    if edge_density > edge_threshold:
        classification = "Text"
    else:
        classification = "Natural Image or Photo"

    # Print analysis
    print(f"Edge Pixels: {edge_pixels}")
    print(f"Total Pixels: {total_pixels}")
    print(f"Edge Density: {edge_density:.4f}")
    print(f"Classification: {classification}")

    # Show images
    cv2.imshow('Original Image', image)
    cv2.imshow('Grayscale', gray)
    cv2.imshow('Edge Density (Canny)', edges)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Example usage
image_path_sign = 'picture_espeon.jpg'
detect_type_based_on_edges(image_path_sign)
#image_path_pokemon = 'picture_espeon.jpg'  
#detect_type_based_on_edges(image_path_pokemon)
