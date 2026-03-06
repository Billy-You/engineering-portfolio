"""Plot utilities for the RC circuit project."""

from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt

from src.simulation import run_simulation


def plot_voltage_response(output_dir: Path) -> Path:
    """Generate and save the capacitor voltage response plot."""
    time, v_numerical, v_analytical, _, _, _ = run_simulation()

    plt.figure(figsize=(8, 5))
    plt.plot(time, v_numerical, label="Numerical solution")
    plt.plot(time, v_analytical, linestyle="--", label="Analytical solution")
    plt.xlabel("Time [s]")
    plt.ylabel("Capacitor voltage [V]")
    plt.title("RC Circuit - Capacitor Voltage Response")
    plt.grid(True)
    plt.legend()
    plt.tight_layout()

    output_file = output_dir / "rc_voltage_response.png"
    plt.savefig(output_file, dpi=300)
    plt.show()

    return output_file


def plot_current_response(output_dir: Path) -> Path:
    """Generate and save the circuit current response plot."""
    time, _, _, i_numerical, i_analytical, _ = run_simulation()

    plt.figure(figsize=(8, 5))
    plt.plot(time, i_numerical, label="Numerical solution")
    plt.plot(time, i_analytical, linestyle="--", label="Analytical solution")
    plt.xlabel("Time [s]")
    plt.ylabel("Current [A]")
    plt.title("RC Circuit - Current Response")
    plt.grid(True)
    plt.legend()
    plt.tight_layout()

    output_file = output_dir / "rc_current_response.png"
    plt.savefig(output_file, dpi=300)
    plt.show()

    return output_file


def main() -> None:
    """Create and save the base plots."""
    output_dir = Path(__file__).resolve().parents[1] / "results"
    output_dir.mkdir(parents=True, exist_ok=True)

    voltage_file = plot_voltage_response(output_dir)
    current_file = plot_current_response(output_dir)

    print(f"Voltage plot saved to: {voltage_file}")
    print(f"Current plot saved to: {current_file}")


if __name__ == "__main__":
    main()