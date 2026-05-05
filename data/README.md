# Archivos de datos para testing manual

Estos archivos son ejemplos para que puedas probar tus implementaciones a mano,
sin depender solo de los tests automáticos.

Para usarlos, desde el archivo del ejercicio podés hacer algo como:

```python
from exercise_01_read_lines import read_lines

print(read_lines("data/ej01_frutas.txt"))
```

O agregar un bloque `if __name__ == "__main__":` al final de tu archivo de
ejercicio:

```python
if __name__ == "__main__":
    print(read_lines("data/ej01_frutas.txt"))
```

Y correrlo con `python3 exercise_01_read_lines.py`.

## Listado de archivos

| Archivo                          | Ejercicio | Para qué sirve                                             |
| -------------------------------- | --------- | ---------------------------------------------------------- |
| `ej01_frutas.txt`                | 1         | Probar `read_lines` con líneas vacías y con espacios       |
| `ej02_texto.txt`                 | 2         | Probar `count_words` con mayúsculas/minúsculas             |
| `ej03_ventas.txt`                | 3         | Probar `read_sales` y `process_sales`                      |
| `ej04_numeros.txt`               | 4         | Probar `safe_average` con líneas válidas e inválidas       |
| `ej04_sin_numeros.txt`           | 4         | Probar que `safe_average` lance `ValueError`               |
| `ej05_people.csv`                | 5         | Probar `csv_to_dict`                                       |
| `ej06_notas.txt`                 | 6         | Probar `grades_stats`                                      |
| `ej08_texto.txt`                 | 8         | Probar `find_longest_word`                                 |
| `ej09_a.txt` / `ej09_b.txt`      | 9         | Probar `merge_files` (usá cualquier nombre de salida)      |
| `ej10_server.log`                | 10        | Probar `parse_log` con un archivo válido                   |
| `ej10_server_invalido.log`       | 10        | Probar que `parse_log` lance `ValueError`                  |

**Nota:** Para el ejercicio 7 (`write_inventory`) no hay archivo de entrada
porque tu función es la que escribe el archivo. Podés probarlo así:

```python
write_inventory("data/mi_stock.txt", {"wood": 10, "coal": 3, "iron": 7})
```

y después abrir `data/mi_stock.txt` a mano para verificar el contenido.
