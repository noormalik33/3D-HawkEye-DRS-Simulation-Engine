# 3D Hawk-Eye DRS Simulation Engine

A **3D Hawk-Eye DRS Simulation Engine** that mathematically simulates cricket ball tracking and Decision Review System (DRS) decision-making using **trajectory modeling, numerical analysis, computational geometry, and 3D visualization**.

The system takes 3D ball-tracking coordinates, models the ball's trajectory using **Polynomial Regression via Ordinary Least Squares (OLS)**, extrapolates its future path using **Horner's Method**, calculates telemetry such as release speed, and finally determines the umpire's decision using a **3D bounding-box validation algorithm**.

The complete system is presented through an interactive **Streamlit dashboard with Plotly 3D visualization**. 

---

## 🎯 Project Overview

In cricket, DRS technology is used to determine whether a delivery would have hit the wickets when the ball's path is partially or completely obscured by the batsman's body.

This project provides a **mathematical simulation of that process**.

Instead of relying on a Machine Learning model or historical training dataset, the engine works as a **deterministic algorithmic system**. It processes ball coordinates and applies mathematical and computational techniques to reconstruct and predict the ball's trajectory. 

### Core Pipeline

```text
3D Ball Coordinates
        │
        ▼
Trajectory Modeling
Polynomial Regression / OLS
        │
        ▼
Future Path Prediction
Horner's Method
        │
        ▼
Telemetry Analytics
Speed & Spin Analysis
        │
        ▼
3D Wicket Validation
Bounding Box Check
        │
        ▼
Umpire's Decision
OUT / UMPIRE'S CALL / MISS
```

---

## ✨ Key Features

*  3D ball trajectory tracking
*  Polynomial trajectory modeling
*  Ordinary Least Squares (OLS) regression
*  Future trajectory extrapolation
*  Horner's Method for polynomial evaluation
*  Release-speed calculation
*  Spin-angle analytics
*  3D wicket collision validation
*  Umpire's Call detection
*  Cricket DRS decision simulation
*  Interactive Streamlit dashboard
*  Interactive Plotly 3D visualization
*  Linear overall algorithmic complexity **O(n)**

---

# 🧠 System Architecture

The system is divided into a **three-layer algorithmic pipeline**.

## Layer 1 — Data Modeling

### Polynomial Regression via OLS

The first stage receives 3D ball-tracking points from the tracking system.

Since the ball follows a curved trajectory, the system models the path using a **quadratic polynomial**.

The implementation uses:

```python
poly_y = np.polyfit(x, y, 2)
poly_z = np.polyfit(x, z, 2)
```

This generates mathematical functions representing the ball's trajectory in 3D space.

**Implementation:**

```text
File: daa_core_engine.py
Function: compute_trajectory_coefficients(x, y, z)
```

The fixed-size polynomial system allows the trajectory calculation to operate in **O(n)** time with respect to the number of input tracking points. 

---

# 🔮 Layer 2 — Analysis & Extrapolation

## Horner's Method

Once the ball reaches the batsman's pad, the camera may no longer observe its complete path toward the wickets.

The engine therefore extrapolates the trajectory to predict where the ball would travel.

Horner's Method provides an efficient way to evaluate polynomial functions for future points.

```text
File: daa_core_engine.py
Function: predict_future_coordinates(fn_y, fn_z, start_x, end_x)
```

The system generates future X coordinates and evaluates the trajectory functions:

```python
future_x = np.linspace(start_x, end_x, intervals)
future_y = fn_y(future_x)
future_z = fn_z(future_x)
```

The future prediction stage operates in **O(k)**, where `k` represents the number of future prediction points. 

---

## 📊 Telemetry Analytics

The engine also calculates ball telemetry using **numerical differentiation**.

For example, the spatial difference between consecutive coordinates is used to calculate the ball's movement and release speed.

```python
dx, dy, dz = x[1]-x[0], y[1]-y[0], z[1]-z[0]

distance = np.sqrt(dx**2 + dy**2 + dz**2)

speed_kph = (distance / time_per_frame) * 3.6
```

**Implementation:**

```text
File: telemetry_analytics.py
Function: calculate_match_stats(x, y, z, time_per_frame)
```

This stage provides telemetry information such as:

* Ball release speed
* Spatial movement
* Spin-related trajectory analytics 

---

# 🎯 Layer 3 — Validation & Umpire's Decision

## 3D Bounding Box Check

The final predicted ball position is compared against the wicket geometry.

The system defines a fixed wicket boundary using:

* **Wicket height:** `0.72 m`
* **Wicket width:** `0.23 m`
* **Ball radius:** `0.036 m`

The final coordinates are then evaluated using simple range constraints.

**Implementation:**

```text
File: cricket_rules_validator.py
Function: calculate_umpires_call(final_y, final_z)
```

The validation logic determines whether the predicted trajectory results in:

```text
OUT
UMPIRE'S CALL
MISS / NOT OUT
```

Because the validation uses fixed-range conditions without iterative processing, this stage operates in **O(1)** constant time.  

---

# ⏱️ Algorithmic Complexity

A major focus of this project is **Design and Analysis of Algorithms (DAA)**.

The three primary stages have the following complexity:

| Processing Stage    | Algorithm                   | Complexity |
| ------------------- | --------------------------- | ---------: |
| Trajectory Modeling | Polynomial Regression / OLS |   **O(n)** |
| Future Prediction   | Horner's Method             |   **O(k)** |
| Wicket Validation   | 3D Bounding Box Check       |   **O(1)** |

Therefore:

```text
T(n) = O(n) + O(k) + O(1)
```

Since the number of future prediction steps `k` is significantly smaller than the number of tracking points `n`:

```text
k << n
```

the dominant term is:

```text
Overall Complexity = O(n)
```

This makes the algorithmic pipeline efficient for real-time simulation. 

---

# 🖥️ Interactive 3D Dashboard

The mathematical engine is integrated into a modern web-based dashboard using:

* **Streamlit** for the application interface
* **Plotly** for interactive 3D graphics

Users can interact with the simulated delivery and visualize the ball's trajectory in a 3D cricket-pitch environment.

The dashboard includes a **Play Delivery** interaction that animates the simulated ball trajectory and allows the 3D pitch to be inspected from different angles. 

---

# 📁 Project Structure

Based on the documented architecture, the project is organized around separate modules for tracking, trajectory calculation, analytics, validation, animation, and web orchestration.

```text
my3D-HawkEye-DRS-Simulation-Engine/
│
├── web_app.py
├── ball_tracker.py
├── daa_core_engine.py
├── telemetry_analytics.py
├── cricket_rules_validator.py
├── animator_engine.py
│
├── README.md
└── ...
```

### Core Modules

| File                         | Responsibility                              |
| ---------------------------- | ------------------------------------------- |
| `web_app.py`                 | Main application and pipeline orchestration |
| `ball_tracker.py`            | Provides raw 3D ball-tracking data          |
| `daa_core_engine.py`         | Trajectory modeling and future prediction   |
| `telemetry_analytics.py`     | Speed and trajectory analytics              |
| `cricket_rules_validator.py` | Wicket collision and umpire decision        |
| `animator_engine.py`         | 3D delivery animation                       |

The documented architecture specifically separates these algorithms into individual modules, making the system easier to understand, maintain, and demonstrate during DAA evaluation. 

---

# 🔄 Complete System Workflow

```text
                 ┌───────────────────────┐
                 │   Ball Tracking Data  │
                 │      (x, y, z)        │
                 └───────────┬───────────┘
                             │
                             ▼
                 ┌───────────────────────┐
                 │   Data Modeling       │
                 │ Polynomial Regression │
                 │       O(n)            │
                 └───────────┬───────────┘
                             │
                             ▼
                 ┌───────────────────────┐
                 │ Future Extrapolation  │
                 │   Horner's Method     │
                 │       O(k)            │
                 └───────────┬───────────┘
                             │
                    ┌────────┴────────┐
                    ▼                 ▼
          ┌─────────────────┐  ┌─────────────────┐
          │    Telemetry    │  │  3D Trajectory  │
          │ Speed / Spin    │  │   Projection    │
          └─────────────────┘  └────────┬────────┘
                                         │
                                         ▼
                              ┌────────────────────┐
                              │ Wicket Validation  │
                              │ Bounding Box O(1)  │
                              └─────────┬──────────┘
                                        │
                                        ▼
                              ┌────────────────────┐
                              │ Umpire's Decision  │
                              ├────────────────────┤
                              │ OUT                │
                              │ UMPIRE'S CALL      │
                              │ MISS / NOT OUT     │
                              └────────────────────┘
```

---

# 🚀 Getting Started

## Prerequisites

Make sure you have **Python 3.x** installed.

Check your Python installation:

```bash
python --version
```

---

## Clone the Repository

```bash
git clone https://github.com/noormalik33/my3D-HawkEye-DRS-Simulation-Engine.git
```

Navigate into the project:

```bash
cd my3D-HawkEye-DRS-Simulation-Engine
```

---

## Create a Virtual Environment

### Windows

```powershell
python -m venv venv
```

Activate it:

```powershell
venv\Scripts\activate
```

### Linux / macOS

```bash
python3 -m venv venv
source venv/bin/activate
```

---

## Install Dependencies

Install the required Python packages:

```bash
pip install numpy streamlit plotly
```

If your repository contains a `requirements.txt`, the preferred approach is:

```bash
pip install -r requirements.txt
```

---

# ▶️ Run the Application

The main web application is:

```text
web_app.py
```

Run it using Streamlit:

```bash
streamlit run web_app.py
```

After starting the application, Streamlit will provide a local URL where the interactive DRS simulation dashboard can be accessed.

---

# 🏏 Simulation Output

The application simulates:

### Ball Trajectory

The system reconstructs a smooth 3D trajectory from the available tracking points.

### Future Path

The trajectory is extrapolated beyond the observed ball path to determine its projected position at the wicket plane.

### Telemetry

The system calculates relevant ball-motion statistics including release speed and trajectory-based analytics.

### DRS Decision

The final projected coordinates are evaluated against the wicket boundary to produce:

```text
OUT
```

or

```text
UMPIRE'S CALL
```

or

```text
MISS / NOT OUT
```

---

# 🧮 Algorithms Used

## 1. Polynomial Regression

Used for reconstructing the ball's curved trajectory.

**Complexity:** `O(n)`

---

## 2. Ordinary Least Squares

Used internally for fitting the quadratic trajectory model.

**Purpose:** Find the mathematical curve that best represents the observed tracking points.

---

## 3. Numerical Differentiation

Used for calculating changes between consecutive tracking coordinates and deriving ball-speed information.

**Purpose:**

```text
Coordinate Difference
        ↓
Distance
        ↓
Velocity
        ↓
Speed (km/h)
```

---

## 4. Horner's Method

Used for efficient evaluation of the polynomial trajectory during future path prediction.

**Complexity:** `O(k)`

---

## 5. 3D Bounding Box Check

Used to determine whether the predicted ball position falls within the wicket boundary.

**Complexity:** `O(1)`

---

# 🧪 Deterministic Algorithm — No ML Training

Unlike Machine Learning–based prediction systems, this project does **not require a historical training dataset or model training process**.

The system is deterministic:

```text
Input:
3D Ball Coordinates

        ↓

Mathematical Algorithms

        ↓

Trajectory + Physics Calculations

        ↓

Geometric Validation

        ↓

Decision
```

The same input coordinates and parameters produce the same calculated trajectory and decision. 

---

# 📌 Why This Project?

This project demonstrates the practical application of **Design and Analysis of Algorithms** concepts in a real-world sports technology scenario.

It combines:

* Algorithm design
* Time-complexity analysis
* Polynomial mathematics
* Numerical methods
* Computational geometry
* 3D visualization
* Software engineering
* Interactive web development

Rather than implementing DAA algorithms only as isolated theoretical examples, the project integrates them into a complete simulation pipeline.

---

# ⚡ Performance

The primary trajectory-processing pipeline has an overall asymptotic complexity of:

```text
O(n)
```

where `n` represents the number of observed ball-tracking points.

The architecture is therefore designed around an efficient linear-time processing model. 

---

# ⚠️ Important Scope

This project is a **simulation engine**, not an official Hawk-Eye implementation.

It mathematically simulates the core concepts of:

* Ball trajectory reconstruction
* Trajectory extrapolation
* Wicket-plane projection
* Geometric decision validation
* DRS-style umpire decision logic

Actual professional cricket DRS systems involve specialized hardware, calibrated cameras, proprietary tracking technology, and considerably more complex physics and computer-vision pipelines.

---

# 🔮 Future Enhancements

Potential improvements to the simulation include:

* Real camera-based ball tracking
* Computer-vision-based coordinate extraction
* More advanced physics modeling
* Real-time video input
* Enhanced spin and swing modeling
* More detailed 3D pitch visualization
* Additional cricket DRS scenarios
* Deployment as a standalone web application

---

# 👨‍💻 Project Information

### 3D Hawk-Eye DRS Simulation Engine

**Course:** Design and Analysis of Algorithms (DAA)

The project demonstrates the practical implementation of algorithmic techniques in a cricket DRS simulation environment.

---

# 📚 Concepts Demonstrated

```text
Design & Analysis of Algorithms
        │
        ├── Polynomial Regression
        ├── Ordinary Least Squares
        ├── Numerical Differentiation
        ├── Horner's Method
        ├── Computational Geometry
        ├── Bounding Box Collision Detection
        └── Asymptotic Complexity Analysis
```

---

# 📄 Project Documentation

The project documentation explains the complete system architecture, algorithms, implementation files, complexity analysis, and demonstration workflow. 

---

# ⭐ Conclusion

The **3D Hawk-Eye DRS Simulation Engine** demonstrates how mathematical algorithms and computational techniques can be combined to simulate a real-world cricket DRS decision system.

The engine processes 3D ball-tracking coordinates, reconstructs the ball's trajectory using **Polynomial Regression and OLS**, predicts its future path using **Horner's Method**, calculates telemetry using **Numerical Differentiation**, and validates the final position using **3D Bounding Box Geometry**.

With an overall pipeline complexity of **O(n)** and an interactive **Streamlit + Plotly 3D interface**, the project provides a practical demonstration of DAA concepts within a visually engaging sports-technology application. 

---


---

# 👨‍💻 Developers Team Members 

---

## Ghulam Qadir

* 📧 Email: gqitspecialist@gmail.com
* 💼 LinkedIn: https://www.linkedin.com/in/ghulam-qadir-07a982365/
* 🌐 Portfolio: https://ghulamqadir.netlify.app
* 💻 GitHub: https://github.com/G-Qadir9988

---

## Noor Malik

* 📧 Email: noormalik56500@gmail.com
* 💼 LinkedIn: https://www.linkedin.com/in/noormalik56500/
* 🌐 Portfolio: https://noor-malik-portfolio.netlify.app/
* 💻 GitHub: https://github.com/noormalik33

---

# 🌟 Community & Support

## CoreIT Tech

* 📧 Email: coreittech1@gmail.com
* ▶️ YouTube: https://www.youtube.com/@CoreITTech1
* 📸 Instagram: https://www.instagram.com/coreit.tech

---

# 📜 License

This project is developed for:

🎓 **Artificial Intelligence Lab – Final Semester Project**

Educational & Research Purposes Only.

---

# Acknowledgement

Special thanks to our mentors, instructors, teammates, and the AI research community for supporting this project.

---

<div align="center">

# 🌟 Thank You For Visiting Our Project 🌟

### Made using AI, React, FastAPI & Machine Learning

</div>


## 🏏 3D Hawk-Eye DRS Simulation Engine

**Algorithmically modeled. Mathematically simulated. Visually demonstrated.**
