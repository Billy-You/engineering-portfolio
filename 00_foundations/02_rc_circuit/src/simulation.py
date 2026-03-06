"""Base simulation for a first-order RC circuit."""

from __future__ import annotations

import numpy as np
from scipy.integrate import solve_ivp

from src.model import RCCircuit, rc_ode


def analytical_voltage(time: np.ndarray, circuit: RCCircuit) -> np.ndarray:
    """Return the analytical capacitor voltage for the charging case."""
    return circuit.input_voltage * (1.0 - np.exp(-time / circuit.tau))


def analytical_current(time: np.ndarray, circuit: RCCircuit) -> np.ndarray:
    """Return the analytical circuit current for the charging case."""
    return (circuit.input_voltage / circuit.resistance) * np.exp(-time / circuit.tau)


def numerical_current(v_c: np.ndarray, circuit: RCCircuit) -> np.ndarray:
    """Return the current computed from the numerical capacitor voltage."""
    return (circuit.input_voltage - v_c) / circuit.resistance


def run_simulation() -> tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray, np.ndarray, RCCircuit]:
    """Run the base RC charging simulation.

    Returns
    -------
    tuple
        time : np.ndarray
            Time vector [s].
        v_numerical : np.ndarray
            Numerical capacitor voltage [V].
        v_analytical : np.ndarray
            Analytical capacitor voltage [V].
        i_numerical : np.ndarray
            Numerical current [A].
        i_analytical : np.ndarray
            Analytical current [A].
        circuit : RCCircuit
            Circuit parameters.
    """
    circuit = RCCircuit(
        resistance=1000.0,
        capacitance=100e-6,
        input_voltage=5.0,
    )

    t_final = 5.0 * circuit.tau
    num_points = 1000
    time = np.linspace(0.0, t_final, num_points)

    initial_voltage = [0.0]

    solution = solve_ivp(
        fun=lambda t, y: [rc_ode(t, y[0], circuit)],
        t_span=(0.0, t_final),
        y0=initial_voltage,
        t_eval=time,
    )

    v_numerical = solution.y[0]
    v_analytical = analytical_voltage(time, circuit)

    i_numerical = numerical_current(v_numerical, circuit)
    i_analytical = analytical_current(time, circuit)

    return time, v_numerical, v_analytical, i_numerical, i_analytical, circuit


def main() -> None:
    """Execute the base simulation and print a short summary."""
    time, v_numerical, v_analytical, i_numerical, i_analytical, circuit = run_simulation()

    voltage_error = np.max(np.abs(v_numerical - v_analytical))
    current_error = np.max(np.abs(i_numerical - i_analytical))

    print("RC Circuit Simulation")
    print("---------------------")
    print(f"R              = {circuit.resistance:.2f} ohm")
    print(f"C              = {circuit.capacitance:.6f} F")
    print(f"Vin            = {circuit.input_voltage:.2f} V")
    print(f"Tau            = {circuit.tau:.4f} s")
    print(f"Final time     = {time[-1]:.4f} s")
    print(f"Voltage error  = {voltage_error:.6e} V")
    print(f"Current error  = {current_error:.6e} A")


if __name__ == "__main__":
    main()