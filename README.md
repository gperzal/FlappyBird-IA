# 🎮 Algoritmo Genético - Flappy Bird AI

## 📋 Tabla de Contenidos

- [🎯 Descripción](#-descripción)
- [🧬 Características](#-características)
- [🚀 Instalación](#-instalación)
- [💻 Uso](#-uso)
- [🧠 Red Neuronal](#-red-neuronal)
- [⚙️ Algoritmo Genético](#️-algoritmo-genético)
- [🛠️ Tecnologías](#️-tecnologías)
- [📊 Resultados](#-resultados)
- [🌟 Contribuciones](#-contribuciones)


## 🎯 Descripción

Este proyecto implementa una inteligencia artificial que aprende a jugar Flappy Bird mediante algoritmos genéticos. La IA evoluciona a través de generaciones, optimizando su comportamiento para alcanzar puntuaciones cada vez más altas.

<div align="center">
  <img src="https://github.com/gperzal/FlappyBird-IA/blob/main/images/flappybird.gif" alt="Flappy Bird AI Demo" height="400">
</div>

## 🧬 Características

| Característica  | Descripción                               |
| --------------- | ----------------------------------------- |
| 🤖 IA Evolutiva | Aprendizaje mediante algoritmos genéticos |
| 🎯 Optimización | Mejora continua a través de generaciones  |
| 📊 Análisis     | Seguimiento de rendimiento y evolución    |
| 🎮 Modos        | Juego manual y modo IA                    |

## 🚀 Instalación

```bash
# Clonar el repositorio
git clone https://github.com/gperzal/flappybird-ai.git

# Instalar dependencias
pip install -r requirements.txt
```

## 💻 Modos de Uso

- 🎮 Modo jugador          
- 🤖 Ver IA jugando        
- 🧠 Entrenar nuevo modelo 

## 🧠 Red Neuronal

La red neuronal procesa 5 inputs clave:

- Distancia al próximo tubo
- Altura del pájaro
- Altura del tubo superior
- Altura del tubo inferior
- Velocidad del pájaro

## ⚙️ Algoritmo Genético

### Proceso Evolutivo

1. 🐣 **Inicialización**: Generación población inicial
2. 📊 **Evaluación**: Medición de fitness
3. 🔄 **Selección**: Supervivencia mejores individuos
4. 🧬 **Cruce**: Combinación de características
5. 🔮 **Mutación**: Introducción variabilidad

## 🛠️ Tecnologías

| Tecnología                                                                                             | Uso                |
| ------------------------------------------------------------------------------------------------------ | ------------------ |
| ![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)    | Lenguaje principal |
| ![PyTorch](https://img.shields.io/badge/PyTorch-EE4C2C?style=flat-square&logo=pytorch&logoColor=white) | Red neuronal       |
| ![Pygame](https://img.shields.io/badge/Pygame-2C2D72?style=flat-square&logo=python&logoColor=white)    | Motor del juego    |

## 📊 Resultados

| Generación | Puntuación Media | Mejor Puntuación |
| ---------- | ---------------- | ---------------- |
| 1          | 10               | 25               |
| 10         | 50               | 120              |
| 50         | 200              | 500+             |

---- 

<div align="center">
  <p>Desarrollado con ❤️ por GXPZ Developer Full Stack © 2025</p>
</div>

