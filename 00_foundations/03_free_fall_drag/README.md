# Free Fall with Drag
Basic scientific programming project to simulate 1D vertical free fall with quadratic aerodynamic drag.

## Objective
Study the motion of a falling body under:
- gravity
- air drag

The project includes:
- mathematical modeling
- numerical simulation with `solve_ivp`
- ground impact detection
- terminal velocity analysis
- comparison between different bodies

## Model
State variables:

- `h(t)`: height above ground
- `v(t)`: downward velocity

Governing equations:
dh/dt = -v
dv/dt = g - (1 / (2m)) * rho * Cd * A * v^2


Terminal velocity:
v_t = sqrt((2 * m * g) / (rho * Cd * A))


## Project structure
03_free_fall_drag/
├── README.md
├── requirements.txt
├── src/
│   ├── __init__.py
│   ├── model.py
│   ├── simulation.py
│   ├── plots.py
│   └── analysis_terminal_velocity.py
├── results/
├── docs/
│   └── notes.md
└── notebooks/


## Main files
* `src/model.py` → differential equations
* `src/simulation.py` → numerical integration and impact event
* `src/plots.py` → base-case plots
* `src/analysis_terminal_velocity.py` → terminal velocity comparison

## Example results
Generated figures:

* `results/free_fall_base_case.png`
* `results/terminal_velocity_comparison.png`

## How to run
From the project root:


source .venv/bin/activate
cd src
python3 simulation.py
python3 plots.py
python3 analysis_terminal_velocity.py


## Key takeaways
* velocity does not grow indefinitely when air drag is present
* short drops may end before terminal velocity is reached
* long drops converge toward terminal velocity
* mass, frontal area, and drag coefficient strongly affect the fall dynamics

## Stack
* Python
* NumPy
* SciPy
* Matplotlib
