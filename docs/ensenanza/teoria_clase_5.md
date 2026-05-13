# Teoría Clase 5: Pruebas y extensiones

## Conceptos clave

- Pruebas automatizadas: scripts que verifican que el código se comporta correctamente.
- Test unitario: prueba de una unidad pequeña de código, como una función.
- Cobertura: qué parte del código está probada.
- Refactorización segura: cambiar el código sin romper la funcionalidad.

## Por qué probar

- Detecta errores antes de desplegar.
- Permite modificar el código con mayor confianza.
- Documenta el comportamiento esperado de la aplicación.

## Tipos de pruebas

- Unitarias: validan funciones individuales.
- De integración: verifican cómo trabajan juntas varias partes.
- De extremo a extremo: prueban la aplicación completa desde el cliente.

## Relevancia para el proyecto

En Mini ArenaSync, los tests permiten comprobar reglas como:
- iniciar un partido con datos válidos
- sumar y restar puntos correctamente
- detectar cuando un set termina
- guardar resultados en JSON

## Extensiones posibles

- Nuevas rutas API.
- Mejoras de interfaz.
- Nuevas validaciones.
- Guardar metadatos adicionales como fecha, hora y nombre del árbitro.

## Conclusión

Las pruebas son una base sólida para desarrollar un proyecto que puede crecer sin comprometer su estabilidad. Comenzar con tests simples hace más seguro cualquier cambio futuro.
