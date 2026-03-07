from typing import Tuple


def mass_spring_damper_dynamics(
    x: float,
    v: float,
    u: float,
    m: float,
    c: float,
    k: float,
) -> Tuple[float, float]:
    """
    Compute the state derivatives of a mass-spring-damper system.

    Parameters
    ----------
    x : float
        Position [m]
    v : float
        Velocity [m/s]
    u : float
        Control force [N]
    m : float
        Mass [kg]
    c : float
        Damping coefficient [N·s/m]
    k : float
        Spring stiffness [N/m]

    Returns
    -------
    Tuple[float, float]
        dx_dt, dv_dt
    """
    dx_dt = v
    dv_dt = (u - c * v - k * x) / m

    return dx_dt, dv_dt