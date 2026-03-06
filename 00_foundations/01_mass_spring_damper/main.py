import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt
from pathlib import Path


def mass_spring_damper(t, y, m, c, k):
    """
    Mass-spring-damper system in first-order form.

    Parameters
    ----------
    t : float
        Time.
    y : list or np.ndarray
        State vector [x, v], where:
        x = position
        v = velocity
    m : float
        Mass [kg].
    c : float
        Damping coefficient [N·s/m].
    k : float
        Spring stiffness [N/m].

    Returns
    -------
    list
        State derivatives [dx/dt, dv/dt].
    """
    x, v = y

    dxdt = v
    dvdt = -(c / m) * v - (k / m) * x

    return [dxdt, dvdt]


if __name__ == "__main__":
    # System parameters
    m = 1.0   # kg
    c = 0.8   # N·s/m
    k = 10.0  # N/m

    # Initial conditions
    x0 = 0.1  # m
    v0 = 0.0  # m/s
    y0 = [x0, v0]

    # Simulation time
    t_start = 0.0
    t_end = 10.0
    t_eval = np.linspace(t_start, t_end, 1000)

    # Numerical simulation
    solution = solve_ivp(
        fun=mass_spring_damper,
        t_span=(t_start, t_end),
        y0=y0,
        t_eval=t_eval,
        args=(m, c, k),
        method="RK45"
    )

    # Check integration result
    if solution.success:
        print("Simulation completed successfully.")
    else:
        print("Simulation failed.")
        print(solution.message)
        raise RuntimeError("Numerical integration did not converge.")

    # Extract results
    t = solution.t
    x = solution.y[0]
    v = solution.y[1]

    # Output directory
    output_dir = Path(__file__).parent / "results"
    output_dir.mkdir(exist_ok=True)

    # Position plot
    plt.figure(figsize=(10, 5))
    plt.plot(t, x, label="Position x(t)")
    plt.title("Mass-Spring-Damper Response")
    plt.xlabel("Time [s]")
    plt.ylabel("Position [m]")
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.savefig(output_dir / "position_response.png", dpi=300)
    plt.show()

    # Velocity plot
    plt.figure(figsize=(10, 5))
    plt.plot(t, v, label="Velocity v(t)")
    plt.title("Mass-Spring-Damper Velocity")
    plt.xlabel("Time [s]")
    plt.ylabel("Velocity [m/s]")
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.savefig(output_dir / "velocity_response.png", dpi=300)
    plt.show()