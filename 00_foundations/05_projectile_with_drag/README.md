# Projectile with Drag
Basic scientific programming project to simulate 2D projectile motion with quadratic aerodynamic drag.

## Objective
Study how air resistance modifies the motion of a projectile compared to the ideal no-drag case.

The project includes:

- physical modeling
- numerical simulation with `solve_ivp`
- ground impact detection
- comparison with the ideal trajectory
- graphical visualization of results

## Model
State variables:
[x, y, vx, vy]


where:

* `x` = horizontal position
* `y` = vertical position
* `vx` = horizontal velocity
* `vy` = vertical velocity

Speed magnitude:
v = sqrt(vx^2 + vy^2)


Governing equations:
dx/dt  = vx
dy/dt  = vy
dvx/dt = -(1 / (2m)) * rho * Cd * A * v * vx
dvy/dt = -g - (1 / (2m)) * rho * Cd * A * v * vy


## Physical parameters
* `m`   → mass
* `g`   → gravity
* `rho` → air density
* `Cd`  → drag coefficient
* `A`   → frontal area
* `v0`  → initial speed
* `theta` → launch angle

## Project structure
05_projectile_with_drag/
├── README.md
├── requirements.txt
├── src/
│   ├── __init__.py
│   ├── model.py
│   ├── simulation.py
│   ├── plots.py
│   └── analysis.py
├── results/
├── docs/
│   └── notes.md
└── notebooks/


## Main files
* `src/model.py` → differential equations
* `src/simulation.py` → numerical integration and impact event
* `src/plots.py` → graphical comparison with the ideal case
* `src/analysis.py` → analytical/physical interpretation extensions

## Example base case
v0    = 30.0 m/s
theta = 45 deg
m     = 0.145 kg
Cd    = 0.47
A     = 0.0042 m^2
rho   = 1.225 kg/m^3
g     = 9.81 m/s^2


## Expected behavior
Compared to the ideal projectile motion:

* the range is reduced
* the maximum height is reduced
* the trajectory is no longer perfectly parabolic
* horizontal velocity is no longer constant

## Example output
Generated figures:
* `results/projectile_with_drag_comparison.png`

## How to run
From the project root:

```bash
source .venv/bin/activate
cd src
python3 simulation.py
python3 plots.py
```

## Stack
* Python
* NumPy
* SciPy
* Matplotlib
