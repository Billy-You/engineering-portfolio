import numpy as np

from controller import PIDController
from model import mass_spring_damper_dynamics


def simulate_open_loop(
    m: float = 1.0,
    c: float = 1.0,
    k: float = 10.0,
    x0: float = 1.0,
    v0: float = 0.0,
    t_end: float = 10.0,
    dt: float = 0.01,
):
    """
    Simulate the mass-spring-damper system without control input.
    """
    t = np.arange(0.0, t_end + dt, dt)

    x = np.zeros_like(t)
    v = np.zeros_like(t)
    u = np.zeros_like(t)

    x[0] = x0
    v[0] = v0

    for i in range(len(t) - 1):
        dx_dt, dv_dt = mass_spring_damper_dynamics(
            x=x[i],
            v=v[i],
            u=0.0,
            m=m,
            c=c,
            k=k,
        )

        x[i + 1] = x[i] + dx_dt * dt
        v[i + 1] = v[i] + dv_dt * dt
        u[i] = 0.0

    u[-1] = 0.0

    return {
        "t": t,
        "x": x,
        "v": v,
        "u": u,
        "reference": np.zeros_like(t),
    }


def simulate_closed_loop(
    m: float = 1.0,
    c: float = 1.0,
    k: float = 10.0,
    kp: float = 30.0,
    ki: float = 5.0,
    kd: float = 8.0,
    reference: float = 1.0,
    x0: float = 0.0,
    v0: float = 0.0,
    t_end: float = 10.0,
    dt: float = 0.01,
):
    """
    Simulate the mass-spring-damper system with PID control.
    """
    t = np.arange(0.0, t_end + dt, dt)

    x = np.zeros_like(t)
    v = np.zeros_like(t)
    u = np.zeros_like(t)
    r = np.full_like(t, reference)
    e = np.zeros_like(t)

    x[0] = x0
    v[0] = v0

    controller = PIDController(kp=kp, ki=ki, kd=kd)

    for i in range(len(t) - 1):
        u[i] = controller.compute(
            reference=reference,
            measurement=x[i],
            dt=dt,
        )

        e[i] = reference - x[i]

        dx_dt, dv_dt = mass_spring_damper_dynamics(
            x=x[i],
            v=v[i],
            u=u[i],
            m=m,
            c=c,
            k=k,
        )

        x[i + 1] = x[i] + dx_dt * dt
        v[i + 1] = v[i] + dv_dt * dt

    e[-1] = reference - x[-1]
    u[-1] = controller.compute(reference=reference, measurement=x[-1], dt=dt)

    return {
        "t": t,
        "x": x,
        "v": v,
        "u": u,
        "e": e,
        "reference": r,
        "gains": {
            "kp": kp,
            "ki": ki,
            "kd": kd,
        },
    }


if __name__ == "__main__":
    open_loop = simulate_open_loop()
    closed_loop = simulate_closed_loop()

    print("Open-loop final position:", f"{open_loop['x'][-1]:.4f} m")
    print("Closed-loop final position:", f"{closed_loop['x'][-1]:.4f} m")
    print("Closed-loop final error:", f"{closed_loop['e'][-1]:.4f} m")
    print("Closed-loop max control force:", f"{np.max(np.abs(closed_loop['u'])):.4f} N")