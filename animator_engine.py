# animator_engine.py
import plotly.graph_objects as go
import numpy as np

def create_3d_animation(raw_x, raw_y, raw_z, pred_x, pred_y, pred_z):
    # Combine actual tracked points and predicted points
    all_x = np.concatenate([raw_x, pred_x])
    all_y = np.concatenate([raw_y, pred_y])
    all_z = np.concatenate([raw_z, pred_z])
    
    fig = go.Figure(
        data=[
            # 1. The Ball (Animated Marker)
            go.Scatter3d(x=[all_x[0]], y=[all_z[0]], z=[all_y[0]], 
                         mode='markers',
                         # REMOVED symbol='sphere' to fix the ValueError
                         marker=dict(color='#ff0055', size=10), 
                         name='Ball'),
            
            # 2. The Path Trail
            go.Scatter3d(x=all_x, y=all_z, z=all_y, 
                         mode='lines',
                         line=dict(color='#00f0ff', width=5), 
                         opacity=0.3, 
                         name='Trajectory'),
            
            # 3. Base point for Wickets
            go.Scatter3d(x=[20, 20, 20], y=[-0.115, 0, 0.115], z=[0, 0, 0],
                         mode='markers', 
                         marker=dict(color='white', size=2), 
                         showlegend=False)
        ],
        layout=go.Layout(
            paper_bgcolor='#0a0f19', 
            plot_bgcolor='#0a0f19',
            scene=dict(
                xaxis=dict(
                    range=[0, 22], title="Pitch Length (m)", color="white", 
                    gridcolor="#333", showbackground=True, backgroundcolor="#0f141e"
                ),
                yaxis=dict(
                    range=[-1, 1], title="Width (m)", color="white", 
                    gridcolor="#333", showbackground=True, backgroundcolor="#0f141e"
                ),
                zaxis=dict(
                    range=[0, 2.5], title="Height (m)", color="white", 
                    gridcolor="#333", showbackground=True, backgroundcolor="#0f141e"
                ),
                aspectmode='manual',
                aspectratio=dict(x=2, y=0.5, z=0.5)
            ),
            font=dict(color="white"),
            margin=dict(l=0, r=0, b=0, t=40),
            legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1),
            updatemenus=[dict(
                type="buttons",
                x=0.1,
                y=0,
                buttons=[dict(
                    label="▶ Play Delivery",
                    method="animate",
                    args=[None, {"frame": {"duration": 40, "redraw": True}, "fromcurrent": True}]
                )]
            )]
        ),
        frames=[go.Frame(data=[go.Scatter3d(x=[all_x[k]], y=[all_z[k]], z=[all_y[k]])]) for k in range(len(all_x))]
    )
    
    # Adding vertical 3D lines for stumps
    for sz in [-0.115, 0, 0.115]:
        fig.add_trace(go.Scatter3d(
            x=[20, 20], y=[sz, sz], z=[0, 0.72],
            mode='lines', 
            line=dict(color='white', width=8), 
            showlegend=False
        ))
        
    return fig