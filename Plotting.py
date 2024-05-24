import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import geopandas as gpd

def plot_traverse(traverse_df, analysis_results, point1, point2, master):
    """Plot the traverse data and analysis results."""
    try:
        # Create a GeoDataFrame from the traverse data
        traverse_gdf = gpd.GeoDataFrame(traverse_df, geometry=gpd.points_from_xy(traverse_df['Easting'], traverse_df['Northing']))

        # Create a figure and axis
        fig, ax = plt.subplots(figsize=(10, 10))

        # Plot the traverse points and legs
        for i in range(len(traverse_df) - 1):
            point1_obj = traverse_gdf.iloc[i]
            point2_obj = traverse_gdf.iloc[i + 1]
            ax.plot([point1_obj.geometry.x, point2_obj.geometry.x], [point1_obj.geometry.y, point2_obj.geometry.y], color='blue', linewidth=2)
            ax.text(point1_obj.geometry.x, point1_obj.geometry.y, f"Point {point1_obj['Point']}", fontsize=8, va='bottom', ha='right')

        # Plot the selected points
        point1_marker = traverse_gdf.loc[traverse_gdf['Point'] == point1].geometry
        point2_marker = traverse_gdf.loc[traverse_gdf['Point'] == point2].geometry
        ax.plot(point1_marker.x, point1_marker.y, 'ro', markersize=10, label=f'Point {point1}')
        ax.plot(point2_marker.x, point2_marker.y, 'ro', markersize=10, label=f'Point {point2}')

        # Add labels and title
        ax.set_xlabel('Easting')
        ax.set_ylabel('Northing')
        ax.set_title('Traverse Analysis')
        ax.legend()

        # Add grid and axis limits
        ax.grid(True)
        ax.set_xlim(analysis_results['min_easting'] - 10, analysis_results['max_easting'] + 10)
        ax.set_ylim(analysis_results['min_northing'] - 10, analysis_results['max_northing'] + 10)

        # Display the plot in the Tkinter window
        canvas = FigureCanvasTkAgg(fig, master=master)
        canvas.draw()
        canvas.get_tk_widget().pack()

    except Exception as e:
        print(f"Unexpected error: {e}")
