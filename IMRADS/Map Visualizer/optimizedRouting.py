import os
import pandas as pd
import folium
from folium.plugins import MousePosition, AntPath

SAVE_DIR = os.getcwd()
MAP_NAME = "optimized-routes-map.html"

WORK_LOCATION = {
    "name": "Work Location",
    "lat": 14.1229439319374,
    "lon": 121.1276671138910,
}

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
  .leg-marker.community     { background: #72af26; }
  .leg-marker.shelter-init  { background: #0067a3; }
  .leg-marker.shelter-trans { background: #7b2fbe; }
  .leg-marker.work-loc      { background: #e65100; }
  .leg-line {
    width: 30px; height: 3px;
    border-radius: 2px;
    flex-shrink: 0;
    position: relative;
  }
  .leg-line::after {
    content: '➤';
    position: absolute;
    right: -10px; top: 50%;
    transform: translateY(-50%);
    font-size: 12px;
    line-height: 1;
  }
  .leg-line.route-init  { background: red; }
  .leg-line.route-init::after  { color: red; }
  .leg-line.route-trans { background: purple; }
  .leg-line.route-trans::after { color: purple; }
  .leg-label { color: #333; }
  .leg-divider {
    margin: 8px 0;
    border: none;
    border-top: 1px solid #e0e0e0;
  }
</style>
"""

def build_legend_html(has_transfer, show_work=False):
    rows = """
    <div class="leg-row">
      <div class="leg-marker community"></div>
      <span class="leg-label">Community (Origin)</span>
    </div>
    <div class="leg-row">
      <div class="leg-marker shelter-init"></div>
      <span class="leg-label">Level 1 Shelter</span>
    </div>"""

    if has_transfer:
        rows += """
    <div class="leg-row">
      <div class="leg-marker shelter-trans"></div>
      <span class="leg-label">Level 2 Shelter</span>
    </div>"""

    if show_work:
        rows += """
    <div class="leg-row">
      <div class="leg-marker work-loc"></div>
      <span class="leg-label">Work Location</span>
    </div>"""

    rows += """
    <hr class="leg-divider">
    <div class="leg-row">
      <div class="leg-line route-init"></div>
      <span class="leg-label">Community → Initial Shelter</span>
    </div>"""

    if has_transfer:
        rows += """
    <div class="leg-row">
      <div class="leg-line route-trans"></div>
      <span class="leg-label">Initial → Transfer Shelter</span>
    </div>"""

    return f'<div id="legend"><h4>Legend</h4>{rows}</div>'


def inject_legend(html_path, has_transfer, show_work=False):
    """Inject legend CSS + HTML into the Folium-generated HTML file."""
    with open(html_path, "r", encoding="utf-8") as f:
        content = f.read()

    legend_html = build_legend_html(has_transfer, show_work)

    content = content.replace("</head>", LEGEND_CSS + "\n</head>", 1)
    content = content.replace("</body>", legend_html + "\n</body>", 1)

    with open(html_path, "w", encoding="utf-8") as f:
        f.write(content)


def load_excel(file_path, usecols=None):
    """Load an Excel file into a DataFrame."""
    return pd.read_excel(file_path, usecols=usecols)


def build_coord_dict(df, name_col="Name", lat_col="Latitude", lon_col="Longitude"):
    """Build a {name: {x: lat, y: lon}} lookup dictionary from a DataFrame."""
    return {
        row[name_col]: {"x": row[lat_col], "y": row[lon_col]}
        for _, row in df.iterrows()
    }


def plot_routes(allocation_df, comm_dict, shel_dict, map_name=MAP_NAME, show_work=False):
    """
    Plot community -> initial shelter -> (optional) transfer shelter routes.

    Parameters
    ----------
    allocation_df : pd.DataFrame
        Must contain columns : Community, Shelter Initial
        Optional column      : Shelter Transfer (may be absent or have NaN values)
    comm_dict  : dict  {name: {"x": lat, "y": lon}}
    shel_dict  : dict  {name: {"x": lat, "y": lon}}
    map_name   : str   Output HTML filename.
    show_work  : bool  Whether to plot the Work Location marker.
    """
    allocation_df = allocation_df.copy()

    has_transfer = (
        "Shelter Transfer" in allocation_df.columns
        and allocation_df["Shelter Transfer"].notna().any()
    )

    # --- Attach coordinates ---
    allocation_df["lat_comm"]      = allocation_df["Community"].map(lambda n: comm_dict.get(n, {}).get("x"))
    allocation_df["lon_comm"]      = allocation_df["Community"].map(lambda n: comm_dict.get(n, {}).get("y"))
    allocation_df["lat_shel_init"] = allocation_df["Shelter Initial"].map(lambda n: shel_dict.get(n, {}).get("x"))
    allocation_df["lon_shel_init"] = allocation_df["Shelter Initial"].map(lambda n: shel_dict.get(n, {}).get("y"))

    if has_transfer:
        allocation_df["lat_shel_trans"] = allocation_df["Shelter Transfer"].map(
            lambda n: shel_dict.get(n, {}).get("x") if pd.notna(n) else None
        )
        allocation_df["lon_shel_trans"] = allocation_df["Shelter Transfer"].map(
            lambda n: shel_dict.get(n, {}).get("y") if pd.notna(n) else None
        )

    allocation_df.dropna(subset=["lat_comm", "lon_comm", "lat_shel_init", "lon_shel_init"], inplace=True)

    if allocation_df.empty:
        print("No valid rows to plot after coordinate lookup.")
        return None

    # --- Center map ---
    avg_lat = allocation_df[["lat_comm", "lat_shel_init"]].values.mean()
    avg_lon = allocation_df[["lon_comm", "lon_shel_init"]].values.mean()
    m = folium.Map(location=[avg_lat, avg_lon], zoom_start=13)

    MousePosition(
        position="topright",
        separator=" | ",
        prefix="Coordinates:",
        lat_formatter="function(num) {return num.toFixed(6);}",
        lng_formatter="function(num) {return num.toFixed(6);}"
    ).add_to(m)

    # --- Feature Groups ---
    fg_communities  = folium.FeatureGroup(name="Communities")
    fg_shel_init    = folium.FeatureGroup(name="Initial Shelters")
    fg_routes_init  = folium.FeatureGroup(name="Routes: Community → Initial Shelter")

    if has_transfer:
        fg_shel_trans   = folium.FeatureGroup(name="Transfer Shelters")
        fg_routes_trans = folium.FeatureGroup(name="Routes: Initial → Transfer Shelter")

    if show_work:
        fg_work = folium.FeatureGroup(name="Work Location")

    # --- Markers ---
    added_shelters = set()
    for _, row in allocation_df.iterrows():
        folium.Marker(
            [row["lat_comm"], row["lon_comm"]],
            popup=f"Community: {row['Community']}",
            icon=folium.Icon(color="green")
        ).add_to(fg_communities)

        init_name = row["Shelter Initial"]
        if init_name not in added_shelters:
            folium.Marker(
                [row["lat_shel_init"], row["lon_shel_init"]],
                popup=f"Shelter (Initial): {init_name}",
                icon=folium.Icon(color="blue")
            ).add_to(fg_shel_init)
            added_shelters.add(init_name)

        if has_transfer:
            trans_name = row.get("Shelter Transfer")
            print(row["lat_shel_trans"])
            if trans_name:
                folium.Marker(
                    [row["lat_shel_trans"], row["lon_shel_trans"]],
                    popup=f"Shelter (Transfer): {trans_name}",
                    icon=folium.Icon(color="purple")
                ).add_to(fg_shel_trans)
                added_shelters.add(trans_name)

    # --- Work Location marker ---
    if show_work:
        folium.Marker(
            [WORK_LOCATION["lat"], WORK_LOCATION["lon"]],
            popup=f"Work Location",
            icon=folium.Icon(color="orange", icon="briefcase", prefix="fa")
        ).add_to(fg_work)

    # --- Route paths ---
    for _, row in allocation_df.iterrows():
        comm      = (row["lat_comm"],      row["lon_comm"])
        shel_init = (row["lat_shel_init"], row["lon_shel_init"])

        AntPath([comm, shel_init], color="red", weight=6, delay=1000).add_to(fg_routes_init)

        if has_transfer and pd.notna(row.get("lat_shel_trans")) and pd.notna(row.get("lon_shel_trans")):
            shel_trans = (row["lat_shel_trans"], row["lon_shel_trans"])
            AntPath([shel_init, shel_trans], color="purple", weight=6, delay=1000).add_to(fg_routes_trans)

    # --- Add all groups to map then layer control ---
    fg_communities.add_to(m)
    fg_shel_init.add_to(m)
    fg_routes_init.add_to(m)

    if has_transfer:
        fg_shel_trans.add_to(m)
        fg_routes_trans.add_to(m)

    if show_work:
        fg_work.add_to(m)

    folium.LayerControl(collapsed=False).add_to(m)

    output_path = os.path.join(SAVE_DIR, map_name)
    m.save(output_path)

    inject_legend(output_path, has_transfer, show_work)

    print(f"Map saved to: {output_path}")
    return m


def main(
    communities_file="Talisay community data.xlsx",
    shelters_file="Talisay shelter data.xlsx",
    allocation_file="BST_alloc.xlsx",
):
    communities_df = load_excel(os.path.join(SAVE_DIR, communities_file),
                                usecols=["Name", "Latitude", "Longitude"])
    shelters_df    = load_excel(os.path.join(SAVE_DIR, shelters_file),
                                usecols=["Name", "Latitude", "Longitude"])

    raw_alloc  = pd.read_excel(os.path.join(SAVE_DIR, allocation_file))
    alloc_cols = ["Community", "Shelter Initial"]
    if "Shelter Transfer" in raw_alloc.columns:
        alloc_cols.append("Shelter Transfer")
    allocation_df = raw_alloc[alloc_cols]

    comm_dict = build_coord_dict(communities_df)
    shel_dict = build_coord_dict(shelters_df)

    show_work = (allocation_file == "WORK_alloc.xlsx")

    plot_routes(allocation_df, comm_dict, shel_dict, show_work=show_work)


if __name__ == "__main__":
    main()