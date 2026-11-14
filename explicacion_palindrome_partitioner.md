# Explicación de `palindrome_partitioner`

## Qué pide el ejercicio

Hay que dividir una cadena en trozos que sean palíndromos y quedarse con la división que use el menor número de cortes.

Un palíndromo es una cadena que se lee igual al derecho y al revés:

- `"a"` es palíndromo.
- `"aa"` es palíndromo.
- `"aba"` es palíndromo.
- `"ab"` no es palíndromo.
- `"aab"` no es palíndromo.

Un corte se representa con una barra `|`. Por ejemplo:

- `"aa|b"` tiene 1 corte.
- `"a|a|b"` tiene 2 cortes.
- `"aba"` tiene 0 cortes porque ya es palíndromo.

## La idea principal

No hay que buscar directamente todos los cortes a la vez. Hay que decidir:

> ¿Cuál es la primera pieza que puedo separar?

Esa primera pieza debe ser un palíndromo. Después de separarla, el problema se repite con el resto de la cadena.

La lógica es:

1. Si el trozo entero ya es palíndromo, no hacen falta cortes.
2. Si no, se prueban todas las primeras piezas que sean palíndromos.
3. Para cada opción se cuenta `1` corte más los cortes que necesite el resto.
4. Se elige la opción que sume menos cortes.

## Ejemplo con `"aab"`

Primero se comprueba si `"aab"` entero es palíndromo. No lo es, así que hay que probar primeras piezas.

Opciones válidas como primera pieza:

- `"a"`, porque es palíndromo.
- `"aa"`, porque es palíndromo.
- `"aab"` no vale porque no es palíndromo.

Si la primera pieza es `"a"`:

- Queda por resolver `"ab"`.
- `"ab"` no es palíndromo, así que necesita 1 corte interno: `"a|b"`.
- Total: 1 corte para separar `"a"` + 1 corte dentro de `"ab"` = 2 cortes.

Si la primera pieza es `"aa"`:

- Queda por resolver `"b"`.
- `"b"` ya es palíndromo, así que necesita 0 cortes.
- Total: 1 corte para separar `"aa"` + 0 cortes en `"b"` = 1 corte.

Entre 2 cortes y 1 corte, el mínimo es 1.

Por eso:

```text
palindrome_partitioner("aab") = 1
```

La partición que se usaría sería:

```text
aa|b
```

## Ejemplo con `"abc"`

`"abc"` no es palíndromo.

Primera pieza posible: `"a"`, que sí es palíndromo.

- Queda `"bc"`.
- `"bc"` no es palíndromo.
- Para `"bc"`, la primera pieza puede ser `"b"`.
- Queda `"c"`, que ya es palíndromo.
- Entonces `"bc"` necesita 1 corte y `"abc"` necesita 2 cortes.

Resultado:

```text
palindrome_partitioner("abc") = 2
```

La partición sería:

```text
a|b|c
```

## Ejemplo con `"aba"`

`"aba"` entero ya es palíndromo, así que no hace falta ningún corte.

Resultado:

```text
palindrome_partitioner("aba") = 0
```

## Cómo traducir esto a código sin perderse

Una forma sencilla es usar una función auxiliar que recibe un trozo de cadena y devuelve cuántos cortes necesita.

La función auxiliar seguiría estos pasos:

1. Si el trozo entero es palíndromo, devolver `0`.
2. Si no, guardar un valor inicial para el mínimo. Un buen valor inicial es el peor caso posible: tantos cortes como letras menos uno.
3. Recorrer todas las posiciones donde se podría hacer el primer corte.
4. Para cada posición:
   - Comprobar si la parte izquierda es palíndromo.
   - Si lo es, calcular `1 + los cortes que necesite la parte derecha`.
   - Si ese resultado es menor que el mínimo actual, actualizar el mínimo.
5. Devolver el mínimo encontrado.

La función principal solo tiene que llamar a la auxiliar con la cadena completa.

La parte importante es que la parte derecha se resuelve llamando otra vez a la misma función auxiliar. Así el problema grande se va reduciendo en problemas más pequeños.

## ¿Se guardan las particiones?

No hace falta guardar las particiones completas.

Solo se necesita saber el número mínimo de cortes. Por eso no hay que crear listas de trozos ni ir acumulando todas las combinaciones posibles.

En este problema se guarda o se devuelve un número, no una lista de cadenas.

## Sobre `is_palindrome`

Antes de implementar la lógica hay que asegurarse de que `is_palindrome` funciona bien.

La idea de un palíndromo es comparar la primera letra con la última, la segunda con la penúltima, y así sucesivamente.

- Si en algún momento las letras son distintas, no es palíndromo.
- Si los índices se cruzan sin encontrar diferencias, sí es palíndromo.

Hay que tener cuidado con las cadenas de longitud par, como `"aa"` o `"abba"`, porque los índices no terminan apuntando a la misma posición: se cruzan.

## Resumen

- Un corte separa dos piezas.
- Cada pieza debe ser palíndromo.
- Se busca el mínimo número de cortes.
- La idea recursiva es: elegir la primera pieza palíndroma, contar un corte si queda resto, resolver el resto igual y quedarse con el mínimo.
- No se guardan particiones completas; solo se calcula el mínimo número de cortes.
