# 🚀 Demo de FastMCP para Python Paraguay 🇵🇾

¡Bienvenido al repositorio de la demo de FastMCP presentada en Python Paraguay! Este proyecto es un
ejemplo simple de cómo crear y exponer herramientas utilizando el framework `FastMCP`.

## ✨ Resumen

Esta demo muestra una herramienta simple de "sumador" que ilustra los conceptos básicos del
Protocolo de Contexto de Modelo (MCP). Sirve como ejemplo práctico para desarrolladores interesados
en crear herramientas para agentes AI con Python.

## 📋 Características

- **API Sencilla:** Expone una única herramienta, `sumador`, que suma dos números enteros.
- **Integración con FastMCP:** Construido sobre la librería ligera y eficiente `FastMCP`.
- **Listo para Ejecutar:** Requiere una configuración mínima para poner en marcha el servidor.

## 🚀 Cómo Empezar

Sigue estas instrucciones para obtener una copia del proyecto y ejecutarla en tu máquina local.

### Prerrequisitos

Asegúrate de tener instalado lo siguiente:

- [Python 3.8+](https://www.python.org/downloads/)
- [uv](https://github.com/astral-sh/uv) (un instalador y resolvedor de paquetes de Python rápido)

### Instalación

1.  **Clona el repositorio:**
    ```bash
    git clone https://github.com/Maxi91f/mcp_example.git
    cd mcp_example
    ```

2.  **Instala las dependencias:**
    Este proyecto utiliza `uv` para gestionar las dependencias. Para instalarlas, ejecuta:
    ```bash
    uv sync
    ```

## 🏃‍♀️ Uso

Para iniciar el servidor MCP, simplemente ejecuta el script `main.py`:

```bash
uv run python main.py
```

El servidor se iniciará y podrás interactuar con la herramienta `sumador` a través de cualquier
cliente MCP compatible. El servidor estará disponible en `/mcp` a través de Server-Sent Events
(SSE).

## 🔧 Cómo Funciona

La lógica principal se encuentra en `main.py`:

1.  **Instancia de `FastMCP`:** Creamos una instancia de `FastMCP`.
2.  **Decorador `@mcp.tool`:** La función `sumador` está decorada con `@mcp.tool`, registrándola
    automáticamente como una herramienta disponible para el agente.
3.  **`mcp.run()`:** Este comando inicia el servidor, haciendo que la herramienta sea accesible.
