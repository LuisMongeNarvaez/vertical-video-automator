# 🎬 Vertical Video Automator (FFmpeg + Python)

[![English](https://img.shields.io/badge/lang-English-blue.svg)](README.md)
[![Español](https://img.shields.io/badge/lang-Español-red.svg)](README.es.md)

**Convierte videos horizontales en contenido vertical (9:16) perfecto para TikTok, Instagram Reels y YouTube Shorts — en segundos.**

---

## 🎥 Antes y Después

<p align="center">
  <strong>Antes (Horizontal)</strong><br>
  <img src="Before.png" width="320" alt="Antes"/>
</p>

<p align="center">
  <strong>Después (Vertical con Desenfoque)</strong><br>
  <img src="After.png" width="320" alt="Después"/>
</p>

---

## ¿Por qué este herramienta?

Convertir videos manualmente para redes sociales es tedioso y consume mucho tiempo.  
**Vertical Video Automator** automatiza todo el proceso usando Python y FFmpeg.

Solo coloca tus videos horizontales en una carpeta, ejecuta el script y obtén versiones verticales limpias con un hermoso fondo desenfocado y el contenido perfectamente centrado — sin barras negras ni editores de video pesados.

---

## ✨ Características

- 🎥 **Conversión Inteligente** — Horizontal a vertical (9:16)
- 🌫️ **Fondo Desenfocado** — Aspecto moderno sin barras negras
- ⚡ **Procesamiento por Lotes** — Maneja múltiples videos a la vez
- 🧠 **Centrado Inteligente** — Mantiene el sujeto principal bien enmarcado
- 🐍 **Python + FFmpeg** — Herramienta CLI ligera y rápida

---

## 🚀 Instalación y Uso

## ✨ Instalación 

git clone https://github.com/LuisMongeNarvaez/vertical-video-automator.git
cd vertical-video-automator

# Recomendado: usar un entorno virtual
python -m venv venv
source venv/bin/activate          # En Windows: venv\Scripts\activate

pip install -r requirements.txt

## ✨ Uso

# Procesar un solo video
python src/main.py -i tu_video.mp4 -o salida_vertical.mp4

# Procesar por lotes todos los videos de una carpeta
python src/main.py -i ./carpeta_videos/


### Requisitos
- Python 3.8 o superior
- FFmpeg instalado y agregado al PATH

Verifica FFmpeg:
```bash
ffmpeg -version
```
## Autor 
Luis Monge Narvaez
GitHub: @LuisMongeNarvaez

## Licencia
Este proyecto está licenciado bajo la Licencia MIT — consulta el archivo LICENSE para más detalles.

## Contribuir¡

Las contribuciones son bienvenidas!
Siéntete libre de abrir un issue para reportar bugs o sugerir mejoras, o envía un pull request para mejorar el código o la documentación.




ffmpeg -version
