import os
import pandas as pd
import folium
from folium.plugins import MousePosition

SAVE_DIR = os.getcwd()
MAP_NAME = "all-locations-map.html"

LEGEND_CSS = """
<style>
  #legend {
    position: fixed;
    bottom: 30px;
    left: 14px;
    z-index: 9999;
    background: rgba(255, 255, 255, 0.96);
    border-radius: 10px;
    padding: 14px 18px;
    box-shadow: 0 2px 16px rgba(0,0,0,0.18);
    min-width: 220px;
    font-family: 'Segoe UI', sans-serif;
    font-size: 13px;
    line-height: 1.5;
  }
  #legend h4 {
    font-size: 11px;
    font-weight: 700;
    letter-spacing: 0.08em;
    text-transform: uppercase;
    color: #444;
    margin: 0 0 10px 0;
    padding-bottom: 6px;
    border-bottom: 1px solid #e0e0e0;
  }
  .leg-row {
    display: flex;
    align-items: center;
    gap: 10px;
    margin-bottom: 7px;
  }
  .leg-row:last-child { margin-bottom: 0; }
  .leg-marker {
    width: 16px; height: 16px;
    border-radius: 50% 50% 50% 0;
    transform: rotate(-45deg);
    flex-shrink: 0;
    box-shadow: 0 1px 4px rgba(0,0,0,0.25);
  }
  .leg-marker.community  { background: #72af26; }
  .leg-marker.shelter    { background: #0067a3; }
  .leg-label { color: #333; }
</style>
"""

LEGEND_HTML = """
<div id="legend">
  <h4>Legend</h4>
  <div class="leg-row">
    <div class="leg-marker community"></div>
    <span class="leg-label">Community</span>
  </div>
  <div class="leg-row">
    <div class="leg-marker shelter"></div>
    <span class="leg-label">Shelter</span>
  </div>
</div>
"""


def inject_legend(html_path):
    with open(html_path, "r", encoding="utf-8") as f:
        content = f.read()
    content = content.replace("</head>", LEGEND_CSS + "\n</head>", 1)
    content = content.replace("</body>", LEGEND_HTML + "\n</body>", 1)
    with open(html_path, "w", encoding="utf-8") as f:
        f.write(content)


def load_excel(file_path, usecols=None):
    return pd.read_excel(file_path, usecols=usecols)


def plot_all_locations(
    communities_df,
    shelters_df,
    map_name=MAP_NAME,
):
    """
    Plot all communities and shelters as markers on a Folium map.

    Parameters
    ----------
    communities_df : pd.DataFrame
        Must contain columns: Name, Latitude, Longitude
    shelters_df    : pd.DataFrame
        Must contain columns: Name, Latitude, Longitude
    map_name       : str
        Output HTML filename.
    """
    # Drop rows missing coordinates
    communities_df = communities_df.dropna(subset=["Latitude", "Longitude"]).copy()
    shelters_df    = shelters_df.dropna(subset=["Latitude", "Longitude"]).copy()

    if communities_df.empty and shelters_df.empty:
        print("No valid locations to plot.")
        return None

    # Center map on the average of all coordinates
    all_lats = pd.concat([communities_df["Latitude"], shelters_df["Latitude"]])
    all_lons = pd.concat([communities_df["Longitude"], shelters_df["Longitude"]])
    avg_lat  = all_lats.mean()
    avg_lon  = all_lons.mean()

    m = folium.Map(location=[avg_lat, avg_lon], zoom_start=13)

    MousePosition(
        position="topright",
        separator=" | ",
        prefix="Coordinates:",
        lat_formatter="function(num) {return num.toFixed(6);}",
        lng_formatter="function(num) {return num.toFixed(6);}"
    ).add_to(m)

    fg_communities = folium.FeatureGroup(name="Communities")
    fg_shelters    = folium.FeatureGroup(name="Shelters")

    # --- Community markers ---
    for _, row in communities_df.iterrows():
        folium.Marker(
            location=[row["Latitude"], row["Longitude"]],
            popup=folium.Popup(f"<b>Community:</b> {row['Name']}", max_width=200),
            tooltip=row["Name"],
            icon=folium.Icon(color="green"),
        ).add_to(fg_communities)

    # --- Shelter markers ---
    for _, row in shelters_df.iterrows():
        folium.Marker(
            location=[row["Latitude"], row["Longitude"]],
            popup=folium.Popup(f"<b>Shelter:</b> {row['Name']}", max_width=200),
            tooltip=row["Name"],
            icon=folium.Icon(color="blue"),
        ).add_to(fg_shelters)

    fg_communities.add_to(m)
    fg_shelters.add_to(m)
    folium.LayerControl(collapsed=False).add_to(m)

    output_path = os.path.join(SAVE_DIR, map_name)
    m.save(output_path)
    inject_legend(output_path)

    print(f"Map saved to: {output_path}")
    print(f"  Communities plotted : {len(communities_df)}")
    print(f"  Shelters plotted    : {len(shelters_df)}")
    return m


def main(
    communities_file="Talisay community data.xlsx",
    shelters_file="Talisay shelter data.xlsx",
):
    communities_df = load_excel(
        os.path.join(SAVE_DIR, communities_file),
        usecols=["Name", "Latitude", "Longitude"],
    )
    shelters_df = load_excel(
        os.path.join(SAVE_DIR, shelters_file),
        usecols=["Name", "Latitude", "Longitude"],
    )

    plot_all_locations(communities_df, shelters_df)


if __name__ == "__main__":
    main()