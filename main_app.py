# main_app.py
import numpy as np
import matplotlib.pyplot as plt
import cricket_rules_validator as validator
import telemetry_analytics as telemetry

# Import custom modular components
import ball_tracker as tracker
import daa_core_engine as engine

def main():
    print("="*40)
    print("  MODULAR 3D HAWK-EYE LBW SYSTEM (DAA)")
    print("="*40)
    print("1) Fast Pitching Delivery (Expected: NOT OUT - Too High)")
    print("2) Sharp Spin Delivery (Expected: NOT OUT - Missing Leg)")
    print("3) Standard Straight Delivery (Expected: OUT - Trajectory Plumb)")
    
    choice = input("\nSelect a camera feed scenario (1-3): ")
    scenarios = {"1": "fast", "2": "spin", "3": "straight"}
    mode = scenarios.get(choice, "straight")
    
    # 1. Fetch data from tracking module
    raw_x, raw_y, raw_z = tracker.get_delivery_data(mode)
    
    # Dimensions of standard cricket pitch layout
    IMPACT_X = 17.5  # Where the batsman's pad intercepts the ball
    STUMPS_X = 20.0  # Location of the wicket target plane
    
    print("\n[Executing Pipeline Operations...]")
    
    # 2. Run Telemetry / Match Analytics Module
    # (Moved here so raw data variables actually exist before use!)
    release_speed, spin_angle = telemetry.calculate_match_stats(raw_x, raw_y, raw_z)
    print(f" -> [Telemetry] Calculated Release Speed: {release_speed} km/h")
    print(f" -> [Telemetry] Calculated Spin Deviation: {spin_angle}°")
    
    # 3. Run DAA Core: Trajectory calculation
    fn_y, fn_z = engine.compute_trajectory_coefficients(raw_x, raw_y, raw_z)
    print(f" -> [O(n)] Fitted path coefficients for Height & Sideways deviation.")
    
    # 4. Calculate Impact details
    impact_y, impact_z = fn_y(IMPACT_X), fn_z(IMPACT_X)
    print(f" -> [O(1)] Monitored impact vector at pad plane.")
    
    # 5. Project future prediction vector down to the wickets
    pred_x, pred_y, pred_z = engine.predict_future_coordinates(fn_y, fn_z, IMPACT_X, STUMPS_X)
    print(f" -> [O(k)] Evaluated future projection array over {len(pred_x)} points.")
    
    # 6. Extract final destination coordinates and evaluate collision rules
    target_y, target_z = pred_y[-1], pred_z[-1]
    
    # Real-World Upgrade: Use your validation module rules!
    decision = validator.calculate_umpires_call(target_y, target_z)
    
    print("\n" + "="*40)
    print(f" FINAL DECISION SYSTEM RESULT: {decision}")
    print("="*40)

    # 7. Render 3D Engine Plot
    fig = plt.figure(figsize=(11, 6))
    ax = fig.add_subplot(111, projection='3d')
    
    # Plot historical trajectory
    ax.scatter(raw_x, raw_z, raw_y, color='teal', s=40, label='Logged Camera Inputs')
    hist_dense_x = np.linspace(2, IMPACT_X, 40)
    ax.plot(hist_dense_x, fn_z(hist_dense_x), fn_y(hist_dense_x), color='teal', alpha=0.7)
    
    # Plot tracking impact event
    ax.scatter([IMPACT_X], [impact_z], [impact_y], color='darkorange', marker='X', s=200, label='Pad Contact Interface')
    
    # Plot predictive physics path
    ax.plot(pred_x, pred_z, pred_y, color='crimson', linestyle='--', linewidth=2.5, label='Projected Path Vector')
    
    # Build 3D Stumps graphics (Three individual vertical stakes + top bail)
    stump_positions_z = [-0.115, 0.0, 0.115]
    for sz in stump_positions_z:
        ax.plot([STUMPS_X, STUMPS_X], [sz, sz], [0, 0.72], color='black', linewidth=4)
    ax.plot([STUMPS_X, STUMPS_X], [-0.115, 0.115], [0.72, 0.72], color='black', linewidth=3, label='Target Wickets')
    
    # Chart Styling (Now including live telemetry variables in the title!)
    ax.set_title(f"DRS Ball Tracking Matrix Simulation\nVerdict: {decision} | Speed: {release_speed}km/h", fontsize=11, fontweight='bold')
    ax.set_xlabel('Pitch Length (X-axis meters)')
    ax.set_ylabel('Lateral Deviation (Z-axis meters)')
    ax.set_zlabel('Elevation Height (Y-axis meters)')
    ax.set_xlim(0, 22)
    ax.set_ylim(-1, 1)
    ax.set_zlim(0, 2.5)
    ax.legend(loc='upper left')
    
    print("\nLaunching 3D Interactive Graph Engine... Close panel to terminate.")
    plt.show()

if __name__ == "__main__":
    main()