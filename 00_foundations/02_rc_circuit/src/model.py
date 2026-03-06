"""RC circuit model definitions.

This module contains the physical parameters and governing equation
for a first-order series RC circuit.
"""

from dataclasses import dataclass


@dataclass
class RCCircuit:
    """Physical parameters of a series RC circuit."""

    resistance: float   # Ohm
    capacitance: float  # Farad
    input_voltage: float  # Volt

    @property
    def tau(self) -> float:
        """Return the time constant tau = R * C."""
        return self.resistance * self.capacitance


def step_input(voltage: float) -> float:
    """Return a constant step input voltage."""
    return voltage


def rc_ode(t: float, v_c: float, circuit: RCCircuit) -> float:
    """Return dvC/dt for the RC circuit.

    Parameters
    ----------
    t : float
        Time [s]. Included for API consistency, although not used here.
    v_c : float
        Capacitor voltage [V].
    circuit : RCCircuit
        Circuit parameters.

    Returns
    -------
    float
        Time derivative of capacitor voltage [V/s].
    """
    vin = step_input(circuit.input_voltage)
    return (vin - v_c) / (circuit.resistance * circuit.capacitance)