## Archivo: `docs/notes.md`

````markdown
# Circuito RC — Fundamentos teóricos

## 1. Contexto del proyecto

Este proyecto estudia la respuesta temporal de un circuito RC en serie sometido a una entrada de tensión continua (DC).

Es un sistema dinámico lineal de primer orden y uno de los modelos fundacionales más importantes en ingeniería eléctrica, porque conecta:

- teoría de circuitos
- ecuaciones diferenciales
- respuesta transitoria
- simulación numérica
- programación científica en Python

---

## 2. Sistema físico

El sistema es un circuito RC en serie formado por:

- una fuente de tensión `Vin(t)`
- una resistencia `R`
- un condensador `C`

La variable principal de salida es la tensión en el condensador:

`vC(t)`

La corriente que circula por el circuito es:

`i(t)`

Como es un circuito en serie, la misma corriente atraviesa todos los elementos:

`i(t) = iR(t) = iC(t)`

---

## 3. Tipo de circuito

### 3.1 Excitación en corriente continua

En el caso base, el circuito está excitado por una fuente de tensión continua (DC) aplicada como escalón:

`Vin(t) = V0` para `t >= 0`

Esto significa que, una vez conectada, la fuente entrega una tensión constante.

### 3.2 Topología en serie

La resistencia y el condensador están conectados en serie, por lo que:

- la corriente es la misma en todos los elementos
- la tensión de la fuente se reparte entre resistencia y condensador
- se puede aplicar directamente la ley de tensiones de Kirchhoff al lazo

---

## 4. Significado físico de cada elemento

### Resistencia `R`

La resistencia limita la corriente que circula por el circuito.

Unidad:

`[R] = ohm`

Efecto físico:

- mayor `R` -> menor corriente
- mayor `R` -> carga/descarga más lenta del condensador

### Capacitancia `C`

El condensador almacena carga y energía eléctrica.

Unidad:

`[C] = F`

Ley constitutiva:

`iC(t) = C * dvC(t)/dt`

Efecto físico:

- mayor `C` -> mayor capacidad de almacenamiento
- mayor `C` -> variación de tensión más lenta

---

## 5. Leyes físicas que gobiernan el sistema

El modelo se construye a partir de tres leyes básicas.

### 5.1 Ley de tensiones de Kirchhoff

Para el lazo:

`Vin(t) = vR(t) + vC(t)`

### 5.2 Ley de Ohm

Para la resistencia:

`vR(t) = R * i(t)`

### 5.3 Ley del condensador

Para el condensador:

`i(t) = C * dvC(t)/dt`

---

## 6. Modelo matemático

Sustituyendo las relaciones de resistencia y condensador en la ecuación de Kirchhoff:

`Vin(t) = R * i(t) + vC(t)`

y usando:

`i(t) = C * dvC(t)/dt`

se obtiene:

`Vin(t) = R * C * dvC(t)/dt + vC(t)`

Despejando:

`dvC(t)/dt = (1 / (R * C)) * (Vin(t) - vC(t))`

Esta es la ecuación diferencial ordinaria de primer orden que gobierna el circuito RC.

---

## 7. Naturaleza del sistema

Este circuito RC es un sistema:

- lineal
- invariante en el tiempo
- de primer orden
- de tiempo continuo
- dinámico

Su variable de estado natural es:

`x(t) = vC(t)`

Por tanto, la ecuación de estado puede escribirse como:

`x_dot(t) = (1 / (R * C)) * (Vin(t) - x(t))`

con salida:

`y(t) = x(t) = vC(t)`

---

## 8. Caso base de simulación

El caso base utilizado en el proyecto es:

- circuito RC en serie
- entrada escalón DC
- condensador inicialmente descargado

### Entrada

`Vin(t) = V0`

### Condición inicial

`vC(0) = 0`

Esto representa la conexión de un condensador descargado a una fuente de tensión constante a través de una resistencia.

---

## 9. Solución analítica

Para el caso de carga, la tensión esperada en el condensador es:

`vC(t) = V0 * (1 - exp(-t / (R * C)))`

La corriente es:

`i(t) = (V0 / R) * exp(-t / (R * C))`

---

## 10. Constante de tiempo

Un concepto clave es la constante de tiempo:

`tau = R * C`

Interpretación:

- en `t = tau`, el condensador alcanza aproximadamente el 63.2% de su valor final
- en torno a `t = 5 * tau`, el transitorio puede considerarse prácticamente terminado

Por eso el tiempo de simulación suele elegirse como:

`t_final ~= 5 * tau`

---

## 11. Interpretación de resultados

### Tensión del condensador `vC(t)`

- empieza en cero
- crece rápidamente al inicio
- se aproxima asintóticamente a la tensión de la fuente

Significado físico:

- inicialmente, el condensador está descargado
- al almacenar carga, su tensión aumenta
- cuando queda cargado, su tensión tiende al valor de la fuente

### Corriente `i(t)`

- empieza en su valor máximo
- decrece exponencialmente
- tiende a cero

Significado físico:

- la corriente inicial es máxima porque el condensador se comporta como un cortocircuito en `t = 0`
- al aumentar la tensión del condensador, disminuye la tensión en la resistencia
- por tanto, la corriente cae hasta anularse

---

## 12. Conjunto de parámetros recomendado

Valores base usados en el proyecto:

`R = 1000 ohm`

`C = 100e-6 F`

`V0 = 5 V`

Entonces:

`tau = R * C = 0.1 s`

Tiempo de simulación recomendado:

`t_final = 5 * tau = 0.5 s`

Corriente inicial:

`i(0) = V0 / R = 5 / 1000 = 0.005 A`

---

## 13. Esquema del circuito

### Esquema ASCII

```text
      Vin(t)
   + -----( )------/\/\/\------||------ +
                  R             C
   - ----------------------------------- -

Salida: vC(t) en bornes del condensador
Corriente: i(t) por la rama serie
````

### Interpretación simplificada

* la fuente aporta energía
* la resistencia limita la corriente
* el condensador almacena energía
* la salida se mide en el condensador

---

## 14. Idea de simulación numérica

El proyecto resuelve el modelo numéricamente en Python y compara:

* respuesta analítica de tensión
* respuesta numérica de tensión
* respuesta analítica de corriente
* respuesta numérica de corriente

Esto permite validar que la implementación coincide con la teoría.

---

## 15. Nuevos comandos Bash usados en este proyecto

### Ir a la carpeta del proyecto

```bash
cd ~/engineering-portfolio/00_foundations/02_rc_circuit
```

### Crear estructura del proyecto

```bash
mkdir src docs notebooks results
touch README.md requirements.txt main.py
touch src/__init__.py src/model.py src/simulation.py src/plots.py
touch docs/notes.md
```

### Activar entorno virtual

```bash
source .venv/bin/activate
```

### Instalar dependencias

```bash
pip install numpy scipy matplotlib
```

### Guardar dependencias

```bash
pip freeze > requirements.txt
```

### Abrir proyecto en VS Code

```bash
code .
```

### Ejecutar el proyecto

```bash
python main.py
```

### Comprobar estructura

```bash
tree
```

### Ver ruta actual

```bash
pwd
```

### Ver archivos

```bash
ls
find .
```

---

## 16. Nuevos conceptos y comandos de Python usados

### Dataclass

Se usa para agrupar los parámetros físicos de forma limpia:

```python
from dataclasses import dataclass
```

### Type hints

Se usan para mejorar legibilidad y estructura:

```python
def main() -> None:
```

```python
def analytical_voltage(time: np.ndarray, circuit: RCCircuit) -> np.ndarray:
```

### NumPy

Se usa para arrays numéricos y operaciones matemáticas:

```python
import numpy as np
```

Ejemplos:

```python
np.linspace(0.0, t_final, num_points)
np.exp(-time / circuit.tau)
np.max(np.abs(v_numerical - v_analytical))
```

### Solver de SciPy

Se usa para integrar numéricamente la ecuación diferencial:

```python
from scipy.integrate import solve_ivp
```

### Matplotlib

Se usa para generar gráficas:

```python
import matplotlib.pyplot as plt
```

Ejemplos:

```python
plt.plot(time, v_numerical)
plt.xlabel("Time [s]")
plt.ylabel("Capacitor voltage [V]")
plt.grid(True)
plt.savefig(output_file, dpi=300)
plt.show()
```

### Manejo de rutas con Path

Se usa para guardar imágenes de forma robusta:

```python
from pathlib import Path
```

Ejemplo:

```python
output_dir = Path(__file__).resolve().parents[1] / "results"
```

### Main execution guard

Se usa para separar funciones reutilizables de la ejecución principal:

```python
if __name__ == "__main__":
    main()
```

---

## 17. Idea clave de ingeniería

Este proyecto es un ejemplo fundacional de cómo pasar de:

1. sistema físico
2. leyes gobernantes
3. ecuación diferencial
4. implementación numérica
5. simulación y gráficas
6. interpretación de resultados

Es un proyecto pequeño, pero establece el flujo de trabajo correcto para tareas de modelado más avanzadas.

```

## Nota breve

Esta versión está pensada para **VS Code/Markdown estándar**, sin depender de renderizado LaTeX.  
Si quieres, el siguiente paso útil es hacer una segunda nota corta llamada `implementation_summary.md` con el papel exacto de `main.py`, `model.py`, `simulation.py` y `plots.py`.
```
