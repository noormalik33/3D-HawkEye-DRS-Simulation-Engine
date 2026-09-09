import streamlit as st
import numpy as np
import ball_tracker as tracker
import daa_core_engine as engine
import telemetry_analytics as telemetry
import cricket_rules_validator as validator
import animator_engine as animator

# Load CSS
with open("style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

st.markdown("<div class='main-header'>✨ HAWK-EYE DRS ENGINE</div>", unsafe_allow_html=True)

# Sidebar
choice = st.sidebar.selectbox("Scenario:", ["1) Fast Ball", "2) Spin Ball", "3) Straight Ball"])
mode = {"1) Fast Ball": "fast", "2) Spin Ball": "spin", "3) Straight Ball": "straight"}[choice]

# Logic
raw_x, raw_y, raw_z = tracker.get_delivery_data(mode)
speed, spin = telemetry.calculate_match_stats(raw_x, raw_y, raw_z)
fn_y, fn_z = engine.compute_trajectory_coefficients(raw_x, raw_y, raw_z)
pred_x, pred_y, pred_z = engine.predict_future_coordinates(fn_y, fn_z, 17.5, 20.0)
decision = validator.calculate_umpires_call(pred_y[-1], pred_z[-1])

# UI Elements
col1, col2, col3 = st.columns(3)
col1.markdown(f"<div class='metric-card'><h3>Speed</h3><h2>{speed} km/h</h2></div>", unsafe_allow_html=True)
col2.markdown(f"<div class='metric-card'><h3>Spin</h3><h2>{spin}°</h2></div>", unsafe_allow_html=True)
col3.markdown(f"<div class='metric-card'><h3>Result</h3><h2>{decision}</h2></div>", unsafe_allow_html=True)

# Animation
st.markdown("<div class='section-title'>🎬 Live 3D Simulation</div>", unsafe_allow_html=True)
st.plotly_chart(animator.create_3d_animation(raw_x, raw_y, raw_z, pred_x, pred_y, pred_z), use_container_width=True)

# DAA Table
st.markdown("<div class='section-title'>⚙️ DAA Complexity Audit</div>", unsafe_allow_html=True)
st.markdown("""<table class='daa-table'><tr><th>Stage</th><th>Algorithm</th><th>Complexity</th></tr>
<tr><td>Tracking</td><td>Polynomial Regression</td><td><code>O(n)</code></td></tr>
<tr><td>Projection</td><td>Horner's Scheme</td><td><code>O(k)</code></td></tr>
<tr><td>Decision</td><td>Spatial Boundary Check</td><td><code>O(1)</code></td></tr></table>""", unsafe_allow_html=True)