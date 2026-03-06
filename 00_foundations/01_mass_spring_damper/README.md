# Mass-Spring-Damper Simulation

Numerical simulation of a 1D mass-spring-damper system in Python using SciPy.

## Project goal

Build a simple but professional first simulation project for an engineering portfolio focused on:

- dynamic systems
- scientific programming
- simulation
- control foundations

## Physical model

The system consists of:

- mass `m`
- damper `c`
- spring `k`

The governing equation is:

`m*x'' + c*x' + k*x = F(t)`

For the base case:

`F(t) = 0`

So the model becomes:

`m*x'' + c*x' + k*x = 0`

## First-order formulation

Define the state variables:

- `x1 = x`
- `x2 = x'`

Then the system is rewritten as:

- `x1' = x2`
- `x2' = -(c/m)*x2 - (k/m)*x1`

## Base simulation case

Parameters:

- `m = 1.0 kg`
- `c = 0.8 N·s/m`
- `k = 10.0 N/m`

Initial conditions:

- `x(0) = 0.1 m`
- `x'(0) = 0.0 m/s`

Simulation interval:

- `t in [0, 10] s`

## Current status

Implemented:

- physical model
- first-order system formulation
- numerical simulation with `solve_ivp`

Next:

- position and velocity plots
- result interpretation
- project cleanup for portfolio presentation

## Requirements

Install dependencies:

/bash
pip install numpy scipy matplotlib


## Results interpretation

The simulated response shows an underdamped behavior.

Key observations:

- the position oscillates around the equilibrium point
- the oscillation amplitude decreases over time
- the velocity also oscillates and decays to zero
- both state variables converge to zero, indicating a stable system

This behavior is consistent with a damped second-order mechanical system where energy is progressively dissipated by the damper.