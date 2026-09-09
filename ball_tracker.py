import numpy as np

def get_delivery_data(scenario_type="spin"):
    # x = distance from bowler (0 to 20m)
    x_frames = np.array([2.0, 4.2, 6.0, 8.1, 10.3, 12.0, 14.2, 16.0])
    
    if scenario_type == "spin":
        y_frames = np.array([2.1, 1.8, 1.4, 0.9, 0.52, 0.44, 0.50, 0.62])
        z_frames = np.array([0.3, 0.25, 0.2, 0.15, 0.10, -0.05, -0.22, -0.38])
    elif scenario_type == "fast":
        y_frames = np.array([2.3, 1.9, 1.5, 0.9, 0.95, 1.15, 1.35, 1.55])
        z_frames = np.array([0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0])
    else: # straight
        y_frames = np.array([2.0, 1.7, 1.3, 0.8, 0.45, 0.42, 0.48, 0.55])
        z_frames = np.array([0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0])
        
    return x_frames, y_frames, z_frames