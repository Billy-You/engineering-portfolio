# RC Circuit Simulation

Python simulation of the time response of a series RC circuit.

## Portfolio location

`00_foundations/02_rc_circuit/`

## Goal

Model and simulate the capacitor voltage and circuit current in a first-order RC circuit under a constant voltage input.

## System

Series RC circuit with:

- input voltage `Vin(t)`
- resistor `R`
- capacitor `C`

Main outputs:

- capacitor voltage `vC(t)`
- current `i(t)`

## Model

Base equations:

`Vin(t) = vR(t) + vC(t)`

`vR(t) = R * i(t)`

`i(t) = C * dvC(t)/dt`

Governing equation:

`dvC(t)/dt = (1 / (R * C)) * (Vin(t) - vC(t))`

## Base case

Input:

`Vin(t) = V0`

Initial condition:

`vC(0) = 0`

Expected voltage response:

`vC(t) = V0 * (1 - exp(-t / (R * C)))`

Expected current response:

`i(t) = (V0 / R) * exp(-t / (R * C))`

## Recommended parameters

`R = 1000 ohm`

`C = 100e-6 F`

`V0 = 5 V`

`tau = 0.1 s`

`t_final = 0.5 s`

## Run

```bash
python main.py