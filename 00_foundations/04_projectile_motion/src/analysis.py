from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

from simulation import run_simulation


def analytical_solution(t: np.ndarray, v0: float, theta_deg: float, g: float):
    """
    Analytical solution for ideal 2D projectile motion without drag.
    """
    theta_rad = np.deg2rad(theta_deg)

    vx0 = v0 * np.cos(theta_rad)
    vy0 = v0 * np.sin(theta_rad)

    x = vx0 * t
    y = vy0 * t - 0.5 * g * t**2
    vx = np.full_like(t, vx0)
    vy = vy0 - g * t

    return x, y, vx, vy


def compute_errors(
    x_num: np.ndarray,
    y_num: np.ndarray,
    vy_num: np.ndarray,
    x_ana: np.ndarray,
    y_ana: np.ndarray,
    vy_ana: np.ndarray,
):
    """
    Compute maximum absolute errors between numerical and analytical solutions.
    """
    error_x = np.max(np.abs(x_num - x_ana))
    error_y = np.max(np.abs(y_num - y_ana))
    error_vy = np.max(np.abs(vy_num - vy_ana))

    return error_x, error_y, error_vy


def plot_comparison(
    t: np.ndarray,
    x_num: np.ndarray,
    y_num: np.ndarray,
    vy_num: np.ndarray,
    x_ana: np.ndarray,
    y_ana: np.ndarray,
    vy_ana: np.ndarray,
) -> None:
    """
    Plot numerical vs analytical results and save the figure.
    """
    project_root = Path(__file__).resolve().parent.parent
    results_dir = project_root / "results"
    results_dir.mkdir(exist_ok=True)

    output_path = results_dir / "projectile_analytical_comparison.png"

    fig, axes = plt.subplots(2, 2, figsize=(12, 8))

    axes[0, 0].plot(x_num, y_num, label="Numerical")
    axes[0, 0].plot(x_ana, y_ana, linestyle="--", label="Analytical")
    axes[0, 0].set_title("Trajectory Comparison")
    axes[0, 0].set_xlabel("x [m]")
    axes[0, 0].set_ylabel("y [m]")
    axes[0, 0].grid(True)
    axes[0, 0].legend()

    axes[0, 1].plot(t, x_num, label="Numerical x(t)")
    axes[0, 1].plot(t, x_ana, linestyle="--", label="Analytical x(t)")
    axes[0, 1].set_title("Horizontal Position Comparison")
    axes[0, 1].set_xlabel("Time [s]")
    axes[0, 1].set_ylabel("x [m]")
    axes[0, 1].grid(True)
    axes[0, 1].legend()

    axes[1, 0].plot(t, y_num, label="Numerical y(t)")
    axes[1, 0].plot(t, y_ana, linestyle="--", label="Analytical y(t)")
    axes[1, 0].set_title("Vertical Position Comparison")
    axes[1, 0].set_xlabel("Time [s]")
    axes[1, 0].set_ylabel("y [m]")
    axes[1, 0].grid(True)
    axes[1, 0].legend()

    axes[1, 1].plot(t, vy_num, label="Numerical vy(t)")
    axes[1, 1].plot(t, vy_ana, linestyle="--", label="Analytical vy(t)")
    axes[1, 1].set_title("Vertical Velocity Comparison")
    axes[1, 1].set_xlabel("Time [s]")
    axes[1, 1].set_ylabel("vy [m/s]")
    axes[1, 1].grid(True)
    axes[1, 1].legend()

    fig.tight_layout()
    fig.savefig(output_path, dpi=300)

    print(f"Figure saved to: {output_path}")

    plt.show()


def main():
    result = run_simulation()

    t = result["t"]
    state = result["y"]

    x_num = state[0]
    y_num = state[1]
    vy_num = state[3]

    params = result["params"]
    v0 = params["v0"]
    theta_deg = params["theta_deg"]
    g = params["g"]

    x_ana, y_ana, vx_ana, vy_ana = analytical_solution(t, v0, theta_deg, g)

    error_x, error_y, error_vy = compute_errors(
        x_num, y_num, vy_num,
        x_ana, y_ana, vy_ana,
    )

    print("Numerical vs analytical comparison")
    print(f"Max |x_num - x_ana|  = {error_x:.6e} m")
    print(f"Max |y_num - y_ana|  = {error_y:.6e} m")
    print(f"Max |vy_num - vy_ana| = {error_vy:.6e} m/s")

    plot_comparison(t, x_num, y_num, vy_num, x_ana, y_ana, vy_ana)


if __name__ == "__main__":
    main()