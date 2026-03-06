# RC Circuit — Base model

## Physical system

Serie RC circuit with:
- input voltage $$V_{in}(t)$$
- resistor $$R$$
- capacitor $$C$$

Output:
- capacitor voltage $$v_C(t)$$

## Governing equations

Kirchhoff voltage law:

$$
V_{in}(t) = v_R(t) + v_C(t)
$$

Resistor law:

$$
v_R(t) = R i(t)
$$

Capacitor law:

$$
i(t) = C \frac{dv_C(t)}{dt}
$$

Substituting:

$$
V_{in}(t) = RC \frac{dv_C(t)}{dt} + v_C(t)
$$

First-order model:

$$
\frac{dv_C(t)}{dt} = \frac{1}{RC}\left(V_{in}(t) - v_C(t)\right)
$$

Time constant:

$$
\tau = RC
$$

## Base case

Input:

$$
V_{in}(t) = V_0
$$

Initial condition:

$$
v_C(0)=0
$$

Analytical solution:

$$
v_C(t)=V_0\left(1-e^{-t/(RC)}\right)
$$
