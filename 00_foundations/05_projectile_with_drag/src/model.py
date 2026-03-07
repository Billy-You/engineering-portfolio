from typing import Sequence

import numpy as np


def projectile_with_drag(
    t: float,
    state: Sequence[float],
    m: float,
    g: float,
    rho: float,
    cd: float,
    area: float,
) -> list[float]:
    """
    2D projectile motion model with quadratic aerodynamic drag.

    State variables:
    - x: horizontal position [m]
    - y: vertical position [m]
    - vx: horizontal velocity [m/s]
    - vy: vertical velocity [m/s]
    """
    x, y, vx, vy = state

    speed = np.sqrt(vx**2 + vy**2)
    drag_factor = 0.5 * rho * cd * area / m

    dx_dt = vx
    dy_dt = vy
    dvx_dt = -drag_factor * speed * vx
    dvy_dt = -g - drag_factor * speed * vy

    return [dx_dt, dy_dt, dvx_dt, dvy_dt]