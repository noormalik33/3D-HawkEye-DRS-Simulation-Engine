import numpy as np

def calculate_match_stats(x, y, z, time_per_frame=0.12):
    # Calculates Speed (O(n))
    dx, dy, dz = x[1]-x[0], y[1]-y[0], z[1]-z[0]
    distance = np.sqrt(dx**2 + dy**2 + dz**2)
    speed_kph = (distance / time_per_frame) * 3.6
    
    total_dz, total_dx = z[-1]-z[0], x[-1]-x[0]
    deviation_angle = np.degrees(np.arctan2(total_dz, total_dx))
    return round(speed_kph, 2), round(abs(deviation_angle), 2)