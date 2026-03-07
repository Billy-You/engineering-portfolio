import numpy as np
from scipy.integrate import solve_ivp

from model import projectile_with_drag


def hit_ground_event(
    t: float,
    state: list[float],
    m: float,
    g: float,
    rho: float,
    cd: float,
    area: float,
) -> float:
    """
    Event function to stop integration when the projectile hits the ground.

    The event is triggered when y = 0.
    """
    _, y, _, _ = state
    return y


hit_ground_event.terminal = True
hit_ground_event.direction = -1


def run_simulation(
    v0: float = 30.0,
    theta_deg: float = 45.0,
    m: float = 0.145,
    g: float = 9.81,
    rho: float = 1.225,
    cd: float = 0.47,
    area: float = 0.0042,
    x0: float = 0.0,
    y0: float = 0.0,
    t_end: float = 10.0,
    num_points: int = 800,
):
    """
    Run a 2D projectile simulation with quadratic drag.
    """
    theta_rad = np.deg2rad(theta_deg)

    vx0 = v0 * np.cos(theta_rad)
    vy0 = v0 * np.sin(theta_rad)

    initial_state = [x0, y0, vx0, vy0]
    t_eval = np.linspace(0.0, t_end, num_points)

    solution = solve_ivp(
        fun=projectile_with_drag,
        t_span=(0.0, t_end),
        y0=initial_state,
        t_eval=t_eval,
        args=(m, g, rho, cd, area),
        events=hit_ground_event,
    )

    t = solution.t.copy()
    y = solution.y.copy()

    impact_detected = solution.t_events[0].size > 0

    if impact_detected:
        impact_time = solution.t_events[0][0]
        impact_state = solution.y_events[0][0]

        if not np.isclose(t[-1], impact_time):
            t = np.append(t, impact_time)
            y = np.column_stack((y, impact_state))

    return {
        "t": t,
        "y": y,
        "raw_solution": solution,
        "impact_detected": impact_detected,
        "impact_time": solution.t_events[0][0] if impact_detected else None,
        "impact_state": solution.y_events[0][0] if impact_detected else None,
        "params": {
            "v0": v0,
            "theta_deg": theta_deg,
            "m": m,
            "g": g,
            "rho": rho,
            "cd": cd,
            "area": area,
            "x0": x0,
            "y0": y0,
        },
    }


if __name__ == "__main__":
    result = run_simulation()

    t = result["t"]
    state = result["y"]

    x = state[0]
    y = state[1]
    vx = state[2]
    vy = state[3]

    print("Simulation status:", result["raw_solution"].message)
    print(f"Final time: {t[-1]:.2f} s")
    print(f"Final x: {x[-1]:.2f} m")
    print(f"Final y: {y[-1]:.2f} m")
    print(f"Final vx: {vx[-1]:.2f} m/s")
    print(f"Final vy: {vy[-1]:.2f} m/s")

    if result["impact_detected"]:
        impact_time = result["impact_time"]
        impact_state = result["impact_state"]

        print("\nImpact detected:")
        print(f"Impact time: {impact_time:.2f} s")
        print(f"Impact x: {impact_state[0]:.2f} m")
        print(f"Impact y: {impact_state[1]:.2f} m")
        print(f"Impact vx: {impact_state[2]:.2f} m/s")
        print(f"Impact vy: {impact_state[3]:.2f} m/s")