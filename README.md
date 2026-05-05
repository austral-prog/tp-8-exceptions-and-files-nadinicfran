# TP8 - Trabajo Práctico 8

## Temas evaluados

Manejo de **archivos** y **excepciones** en Python, combinados con los temas que ya conocen: **listas**, **diccionarios**, **tuplas**, **strings** y **bucles**.

Todos los ejercicios requieren leer (y en algunos casos escribir) archivos de texto, y varios piden manejar explícitamente excepciones como `FileNotFoundError` o `ValueError`.

## Cómo ejecutar los tests

Para verificar todos los ejercicios en el directorio actual:

```bash
python3 -m unittest discover
```

Para verificar un ejercicio en particular:

```bash
python3 -m unittest test_tp8_01_read_lines
```

O ejecutar directamente:

```bash
python3 test_tp8_01_read_lines.py
```

## Estructura de los ejercicios

Cada ejercicio está en su propio archivo (`exercise_01_*.py`, `exercise_02_*.py`, ...). Cada uno tiene su archivo de tests correspondiente (`test_tp8_01_*.py`, `test_tp8_02_*.py`, ...).

**Importante:** los tests crean y eliminan archivos temporales. No hace falta que tengas archivos de datos preparados: los tests generan los archivos que necesitan antes de cada caso y los borran al terminar.

## Pruebas manuales

En la carpeta `data/` hay archivos de ejemplo para que puedas probar tus implementaciones a mano, ejecutando los ejercicios directamente (por ejemplo con un bloque `if __name__ == "__main__":`). Ver `data/README.md` para el detalle de qué archivo usa cada ejercicio.

---

## Ejercicio 1 — `read_lines`

**Archivo:** `exercise_01_read_lines.py`
**Conceptos:** lectura de archivos, listas, strings (`strip`), excepciones.

**Consigna:** Implementar `read_lines(filename)` que lea el archivo cuyo nombre se pasa y retorne una **lista de strings**, donde cada string es una línea del archivo **sin el salto de línea final** y sin espacios al inicio o al final.

- Si el archivo no existe, debe propagar (o lanzar) `FileNotFoundError`.
- Si el archivo está vacío, retornar una lista vacía `[]`.
- No incluir líneas vacías en el resultado (si una línea tiene solo espacios o está en blanco, se ignora).

**Ejemplo:** Si `datos.txt` contiene:

```
manzana
  banana
pera
```

Entonces:

```python
read_lines('datos.txt')
# → ['manzana', 'banana', 'pera']

read_lines('no_existe.txt')
# → FileNotFoundError
```

---

## Ejercicio 2 — `count_words`

**Archivo:** `exercise_02_count_words.py`
**Conceptos:** lectura de archivos, diccionarios, strings (`split`, `lower`).

**Consigna:** Implementar `count_words(filename)` que lea el archivo y retorne un **diccionario** donde las claves son las palabras (en minúsculas) y los valores son la cantidad de veces que aparecen.

- Las palabras se separan por espacios en blanco.
- Se deben contar **sin distinguir mayúsculas y minúsculas** (`"Hola"` y `"hola"` cuentan como la misma palabra).
- Si el archivo no existe, debe propagar `FileNotFoundError`.
- Si el archivo está vacío, retornar un diccionario vacío `{}`.

**Ejemplo:** Si `texto.txt` contiene:

```
Hola mundo hola
mundo python
```

Entonces:

```python
count_words('texto.txt')
# → {'hola': 2, 'mundo': 2, 'python': 1}
```

---

## Ejercicio 3 — `read_sales` y `process_sales`

**Archivo:** `exercise_03_sales_by_product.py`
**Conceptos:** lectura de archivos, diccionarios de listas, strings (`split`), formateo de salida.

**Contexto:** Tenés un archivo donde cada venta tiene el formato `producto:valor` y las ventas están separadas por punto y coma `;`, todo en una sola línea.

**Ejemplo de archivo:**

```
producto1:100;producto2:200;producto1:150;producto3:50;producto2:100;
```

**Consigna (parte 1):** Implementar `read_sales(filename)` que lea el archivo y retorne un diccionario donde la clave es el nombre del producto y el valor es una **lista con todos los montos de ventas** para ese producto (como `float`).

- Si el archivo no existe, debe propagar `FileNotFoundError`.

**Ejemplo:**

```python
read_sales('ventas.txt')
# → {
#     'producto1': [100.0, 150.0],
#     'producto2': [200.0, 100.0],
#     'producto3': [50.0]
#   }
```

**Consigna (parte 2):** Implementar `process_sales(data)` que reciba el diccionario anterior y, **en el orden natural del diccionario**, imprima una línea por producto con el siguiente formato exacto:

```
producto: ventas totales $X.XX, promedio $Y.YY
```

**Ejemplo:** Para el diccionario del ejemplo anterior, imprime:

```
producto1: ventas totales $250.00, promedio $125.00
producto2: ventas totales $300.00, promedio $150.00
producto3: ventas totales $50.00, promedio $50.00
```

---

## Ejercicio 4 — `safe_average`

**Archivo:** `exercise_04_safe_average.py`
**Conceptos:** lectura de archivos, manejo de excepciones, conversión de tipos, bucles.

**Consigna:** Implementar `safe_average(filename)` que lea un archivo donde hay **un número por línea** y retorne el **promedio** de los números válidos.

- Líneas que no se puedan convertir a `float` deben ser **ignoradas** (usar `try/except ValueError`).
- Si el archivo no existe, debe propagar `FileNotFoundError`.
- Si el archivo existe pero **no hay ningún número válido**, lanzar `ValueError("no valid numbers")`.

**Ejemplo:** Si `numeros.txt` contiene:

```
10
20
no_es_un_numero
30
```

Entonces:

```python
safe_average('numeros.txt')   # → 20.0

safe_average('no_existe.txt') # → FileNotFoundError

# Archivo con solo "hola\nmundo\n"
safe_average('no_numeros.txt') # → ValueError("no valid numbers")
```

---

## Ejercicio 5 — `csv_to_dict`

**Archivo:** `exercise_05_csv_to_dict.py`
**Conceptos:** lectura de archivos, listas de diccionarios, strings (`split`, `strip`).

**Consigna:** Implementar `csv_to_dict(filename)` que lea un archivo CSV con el header `name,age,city` y retorne una **lista de diccionarios**, uno por fila, con las claves tomadas del header.

- La primera línea del archivo es siempre el header.
- El campo `age` debe convertirse a `int`.
- `name` y `city` son strings.
- Si el archivo no existe, propagar `FileNotFoundError`.
- Si el archivo está vacío o solo tiene header, retornar `[]`.

**Ejemplo:** Si `people.csv` contiene:

```
name,age,city
Alice,30,Buenos Aires
Bob,25,Rosario
```

Entonces:

```python
csv_to_dict('people.csv')
# → [
#     {'name': 'Alice', 'age': 30, 'city': 'Buenos Aires'},
#     {'name': 'Bob', 'age': 25, 'city': 'Rosario'}
#   ]
```

**Nota:** No se permite usar el módulo `csv` de Python. Usen `split(',')`.

---

## Ejercicio 6 — `grades_stats`

**Archivo:** `exercise_06_grades_stats.py`
**Conceptos:** lectura de archivos, diccionarios, tuplas, listas, bucles.

**Consigna:** Implementar `grades_stats(filename)` que lea un archivo donde cada línea tiene el formato `estudiante:nota1,nota2,...` y retorne un diccionario donde la clave es el nombre del estudiante y el valor es una **tupla** `(promedio, maximo, minimo)` con tres floats.

- El promedio se calcula con todas las notas de la línea.
- Si el archivo no existe, propagar `FileNotFoundError`.
- Si una línea está vacía, se ignora.
- Se garantiza que todas las notas son números válidos.

**Ejemplo:** Si `notas.txt` contiene:

```
Ana:8,9,7
Beto:5,5,10
Cami:10
```

Entonces:

```python
grades_stats('notas.txt')
# → {
#     'Ana': (8.0, 9.0, 7.0),
#     'Beto': (6.666666666666667, 10.0, 5.0),
#     'Cami': (10.0, 10.0, 10.0)
#   }
```

---

## Ejercicio 7 — `write_inventory`

**Archivo:** `exercise_07_write_inventory.py`
**Conceptos:** escritura de archivos, diccionarios, ordenamiento.

**Consigna:** Implementar `write_inventory(filename, inventory)` que reciba un diccionario `item → cantidad` y escriba en el archivo una línea por item, **ordenadas alfabéticamente por nombre de item**, con el formato `item:cantidad`.

- Cada línea debe terminar con un salto de línea (`\n`).
- Si el diccionario está vacío, el archivo debe crearse **vacío**.
- La función no retorna nada (`None`).

**Ejemplo:**

```python
write_inventory('stock.txt', {'wood': 10, 'coal': 3, 'iron': 7})
```

El archivo `stock.txt` debe contener:

```
coal:3
iron:7
wood:10
```

---

## Ejercicio 8 — `find_longest_word`

**Archivo:** `exercise_08_find_longest_word.py`
**Conceptos:** lectura de archivos, strings, bucles, excepciones.

**Consigna:** Implementar `find_longest_word(filename)` que lea el archivo, lo divida en palabras (separadas por espacios o saltos de línea) y retorne la **palabra más larga**.

- Si hay más de una palabra con la longitud máxima, retornar la **primera** en aparecer.
- Si el archivo no existe, propagar `FileNotFoundError`.
- Si el archivo no tiene ninguna palabra (está vacío o solo tiene espacios), lanzar `ValueError("file has no words")`.

**Ejemplo:** Si `texto.txt` contiene:

```
el gato corre rapido
por el jardin
```

Entonces:

```python
find_longest_word('texto.txt')  # → 'rapido'
```

---

## Ejercicio 9 — `merge_files`

**Archivo:** `exercise_09_merge_files.py`
**Conceptos:** lectura y escritura de archivos, manejo de excepciones.

**Consigna:** Implementar `merge_files(file1, file2, output)` que lea el contenido de `file1` y `file2`, los **concatene** (primero el de `file1`, luego el de `file2`) y escriba el resultado en el archivo `output`.

- Si `file1` o `file2` no existen, **no se debe crear** el archivo de salida y se debe propagar `FileNotFoundError`.
- Si el archivo de salida ya existe, se sobreescribe.
- La función no retorna nada (`None`).

**Ejemplo:** Si `a.txt` contiene `hola\n` y `b.txt` contiene `mundo\n`, entonces:

```python
merge_files('a.txt', 'b.txt', 'out.txt')
# out.txt ahora contiene:
# hola
# mundo
```

---

## Ejercicio 10 — `parse_log`

**Archivo:** `exercise_10_log_parser.py`
**Conceptos:** lectura de archivos, diccionarios de listas, strings (`split`), manejo de excepciones.

**Consigna:** Implementar `parse_log(filename)` que lea un archivo de log donde cada línea tiene el formato `NIVEL: mensaje` (por ejemplo `INFO: servidor iniciado`) y retorne un diccionario donde la clave es el nivel y el valor es una **lista con todos los mensajes** de ese nivel, en el orden en que aparecen.

- Los niveles posibles no están fijados (cualquier string antes del `:` cuenta).
- Si el archivo no existe, propagar `FileNotFoundError`.
- Si alguna línea **no tiene** el carácter `:`, lanzar `ValueError("invalid log line")` (las líneas vacías se ignoran, no son inválidas).
- Los espacios al principio/final del nivel y del mensaje deben ser eliminados (`strip`).

**Ejemplo:** Si `server.log` contiene:

```
INFO: servidor iniciado
ERROR: no se puede conectar
INFO: reintentando
WARN: lento
```

Entonces:

```python
parse_log('server.log')
# → {
#     'INFO': ['servidor iniciado', 'reintentando'],
#     'ERROR': ['no se puede conectar'],
#     'WARN': ['lento']
#   }
```

Si alguna línea es `esto no es un log` (sin `:`), debe lanzar `ValueError("invalid log line")`.
