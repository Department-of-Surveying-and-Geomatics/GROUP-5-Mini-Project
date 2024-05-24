import math

def analyze_traverse_data(traverse_df, point1, point2):
    """Perform the traverse analysis."""
    # Find the minimum and maximum easting and northing values
    min_easting = traverse_df['Easting'].min()
    max_easting = traverse_df['Easting'].max()
    min_northing = traverse_df['Northing'].min()
    max_northing = traverse_df['Northing'].max()

    # Calculate the distance and bearing between the specified points
    point1_obj = traverse_df.loc[traverse_df['Point'] == point1].iloc[0]
    point2_obj = traverse_df.loc[traverse_df['Point'] == point2].iloc[0]
    dx = point2_obj['Easting'] - point1_obj['Easting']
    dy = point2_obj['Northing'] - point1_obj['Northing']
    distance = math.sqrt(dx ** 2 + dy ** 2)
    bearing_radians = math.atan2(dy, dx)
    bearing_degrees = (math.degrees(bearing_radians) + 360) % 360
    bearing_minutes, bearing_seconds = divmod(bearing_degrees * 60, 60)

    return {
        'num_legs': len(traverse_df),
        'min_easting': min_easting,
        'max_easting': max_easting,
        'min_northing': min_northing,
        'max_northing': max_northing,
        'distance': distance,
        'bearing_degrees': int(bearing_degrees),
        'bearing_minutes': int(bearing_minutes),
        'bearing_seconds': int(bearing_seconds)
    }
