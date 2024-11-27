# Proyecto: Generador de Pentagramas en Python

## Descripción
Este proyecto consiste en un programa desarrollado en Python que genera pentagramas a partir de melodías ingresadas por el usuario. El sistema admite dos notaciones musicales (latina y anglosajona) y permite representar alteraciones como sostenidos y bemoles. Las melodías se validan y se representan gráficamente como texto utilizando caracteres.

## Funcionalidades
- **Generación de pentagramas:** Representación textual de melodías ingresadas.
- **Soporte para notaciones musicales:** Latina (Do, Re, Mi, etc.) y anglosajona (C, D, E, etc.).
- **Alteraciones musicales:** Compatible con sostenidos (#) y bemoles (b).
- **Validación de entradas:** Asegura que las melodías sean válidas antes de procesarlas:
  - Uso exclusivo de una notación (latina o anglosajona).
  - Consistencia en el uso de sostenidos o bemoles.
  - Cantidad de notas múltiplo de 4.

## Requisitos
- **Python 3.x**
- No se permite la importación de módulos externos para este proyecto.

## Uso
1. **Ejecutar el programa:**
   El programa solicitará al usuario una melodía a través de un mensaje:
   ```
   Ingrese la melodía: <string>
   ```

2. **Validación:**
   Si la entrada es incorrecta, el programa mostrará:
   ```
   Error en la entrada
   ```
   El usuario deberá corregir la entrada.

3. **Generación de pentagrama:**
   Una vez validada la melodía, se mostrará el pentagrama correspondiente en formato de texto.

### Ejemplo de Entrada y Salida

#### Entrada 1:
```
Ingrese la melodía: Do4 Re4 Mi4 Fa4 Sol4 La4 Si4 Do5
```

#### Salida 1:
```
              O 
----------O------------------------------------
      O                                        
 -O--------------------------------------------
        O                                      
  O--------------------------------------------
------------------------------------------O----
                                      O        
```

#### Entrada 2 (con sostenidos):
```
Ingrese la melodía: Do#4 Re#4 Fa4 Fa#4 Sol#4 La#4
```

#### Salida 2:
```
     #O                                         
-#O-                                            
          #O                                    
  #O--------------------------------------------
------------------------------------------O--#O-
```

## Consideraciones
- El programa maneja notas desde **Do central (Do4 o C4)** hasta **La5**.
- Las líneas adicionales del pentagrama solo se incluyen si las notas lo requieren.
- Cada nota ocupa un ancho de 4 caracteres:
  - Primer carácter: Espacio o guion (`-`).
  - Segundo carácter: Alteración (`#` o `b`) si corresponde.
  - Tercer carácter: Nota (`O`).
  - Cuarto carácter: Espacio o guion (`-`).

## Restricciones
- No se permite la importación de bibliotecas externas.
- El programa debe adherirse a los principios del **Código de Honor**.

## Autor
- DevZatokio
  - GitHub: [DevZatokio](https://github.com/DevZatokio)  
  - Email: [devzatokio@gmail.com](mailto:devzatokio@gmail.com)

## Licencia

- **Licencia**: [MIT](https://opensource.org/licenses/MIT)