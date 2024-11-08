import osmnx as ox
import folium
import numpy as np

def routeplot(starting_point, ending_point):
    """Finds and plots the shortest route between two points using OSMnx."""
    lat1, lon1 = starting_point
    lat2, lon2 = ending_point

    # Create the road graph within a larger bounding box defined by the points
    roadgraph = ox.graph_from_bbox(lat1 + 0.05, lat2 - 0.05, lon1 + 0.05, lon2 - 0.05, network_type='drive')

    # Check if the road graph is empty
    if roadgraph is None or len(roadgraph.nodes) == 0:
        print("Error: The road graph is empty. Check the bounding box coordinates.")
        return None

    # Find the nearest nodes to the starting and ending points
    start_node = ox.distance.nearest_nodes(roadgraph, lon1, lat1)
    end_node = ox.distance.nearest_nodes(roadgraph, lon2, lat2)

    if start_node is None or end_node is None:
        print("Error: Could not find nodes for the given points.")
        return None

    # Find the shortest path between the nodes
    try:
        route = ox.shortest_path(roadgraph, start_node, end_node)
    except Exception as e:
        print(f"Error: Could not compute shortest path. {e}")
        return None
    
    # Calculate the total route distance
    route_distance = sum(ox.utils_graph.get_route_edge_attributes(roadgraph, route, 'length'))
    print(f"Distance along the road network: {route_distance / 1000:.2f} km")

    # Use the convert module to extract the GeoDataFrame for nodes and edges
    try:
        gdf_nodes, gdf_edges = ox.convert.graph_to_gdfs(roadgraph)
    except Exception as e:
        print(f"Error: Could not convert the graph to GeoDataFrames. {e}")
        return None

    # Check if the nodes GeoDataFrame is valid
    if gdf_nodes is None or gdf_nodes.empty:
        print("Error: No valid nodes found in the graph.")
        return None

    # Get the route coordinates from the nodes
    route_coords = []
    for node in route:
        try:
            # Extract coordinates for each node in the route
            node_data = gdf_nodes.loc[node]
            route_coords.append((node_data['y'], node_data['x']))
        except KeyError:
            print(f"Warning: Node {node} not found in the graph.")
            continue

    if not route_coords:
        print("Error: No valid route coordinates found.")
        return None

    # Create a Folium map centered at the midpoint of the route
    m = folium.Map(location=[(lat1 + lat2) / 2, (lon1 + lon2) / 2], zoom_start=13)

    # Add markers for the starting and ending points
    folium.Marker([lat1, lon1], popup="Start", icon=folium.Icon(color='green')).add_to(m)
    folium.Marker([lat2, lon2], popup="End", icon=folium.Icon(color='red')).add_to(m)

    # Plot the route on the map
    folium.PolyLine(route_coords, color="blue", weight=2.5, opacity=1).add_to(m)

    # Save the map as an HTML file
    m.save('route.html')

    return m

# Generate random points further apart (for example, around Athens, Greece)
starting_point = (14.833799, 120.734049)
ending_point = (14.836125, 120.733770)

# Plot the route
routeplot(starting_point, ending_point)
