from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

from simulation import run_simulation


def ideal_projectile_solution(t: np.ndarray, v0: float, theta_deg: float, g: float):
    """
    Analytical solution for ideal 2D projectile motion without drag.
    """
    theta_rad = np.deg2rad(theta_deg)

    vx0 = v0 * np.cos(theta_rad)
    vy0 = v0 * np.sin(theta_rad)

    x = vx0 * t
    y = vy0 * t - 0.5 * g * t**2
    speed = np.sqrt(vx0**2 + (vy0 - g * t) ** 2)

    return x, y, speed


def plot_results() -> None:
    """
    Run the projectile-with-drag simulation, compare it against the ideal case,
    and save the figure to the results directory.
    """
    result = run_simulation()

    t = result["t"]
    state = result["y"]

    x_drag = state[0]
    y_drag = state[1]
    vx_drag = state[2]
    vy_drag = state[3]
    speed_drag = np.sqrt(vx_drag**2 + vy_drag**2)

    params = result["params"]
    v0 = params["v0"]
    theta_deg = params["theta_deg"]
    g = params["g"]

    x_ideal, y_ideal, speed_ideal = ideal_projectile_solution(t, v0, theta_deg, g)

    project_root = Path(__file__).resolve().parent.parent
    results_dir = project_root / "results"
    results_dir.mkdir(exist_ok=True)

    output_path = results_dir / "projectile_with_drag_comparison.png"

    fig, axes = plt.subplots(2, 2, figsize=(12, 8))

    axes[0, 0].plot(x_drag, y_drag, label="With drag")
    axes[0, 0].plot(x_ideal, y_ideal, linestyle="--", label="Ideal")
    axes[0, 0].set_title("Trajectory Comparison")
    axes[0, 0].set_xlabel("x [m]")
    axes[0, 0].set_ylabel("y [m]")
    axes[0, 0].grid(True)
    axes[0, 0].legend()

    axes[0, 1].plot(t, x_drag, label="With drag")
    axes[0, 1].plot(t, x_ideal, linestyle="--", label="Ideal")
    axes[0, 1].set_title("Horizontal Position vs Time")
    axes[0, 1].set_xlabel("Time [s]")
    axes[0, 1].set_ylabel("x [m]")
    axes[0, 1].grid(True)
    axes[0, 1].legend()

    axes[1, 0].plot(t, y_drag, label="With drag")
    axes[1, 0].plot(t, y_ideal, linestyle="--", label="Ideal")
    axes[1, 0].set_title("Vertical Position vs Time")
    axes[1, 0].set_xlabel("Time [s]")
    axes[1, 0].set_ylabel("y [m]")
    axes[1, 0].grid(True)
    axes[1, 0].legend()

    axes[1, 1].plot(t, speed_drag, label="With drag")
    axes[1, 1].plot(t, speed_ideal, linestyle="--", label="Ideal")
    axes[1, 1].set_title("Speed Magnitude vs Time")
    axes[1, 1].set_xlabel("Time [s]")
    axes[1, 1].set_ylabel("Speed [m/s]")
    axes[1, 1].grid(True)
    axes[1, 1].legend()

    fig.tight_layout()
    fig.savefig(output_path, dpi=300)

    print(f"Figure saved to: {output_path}")

    plt.show()


if __name__ == "__main__":
    plot_results()