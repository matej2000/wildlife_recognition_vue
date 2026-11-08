<!-- omit in toc -->

# Wildlife recognition dashboard

<p align="center">
  <img src="https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white" alt="Django"/>
  <img src="https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white" alt="FastAPI"/>
  <img src="https://img.shields.io/badge/Nginx-009639?style=for-the-badge&logo=nginx&logoColor=white" alt="Nginx"/>
  <img src="https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white" alt="Docker"/>
  <img src="https://img.shields.io/badge/PyTorch-EE4C2C?style=for-the-badge&logo=pytorch&logoColor=white" alt="PyTorch"/>
  <img src="https://img.shields.io/badge/Vue.js-4FC08D?style=for-the-badge&logo=vuedotjs&logoColor=white" alt="Vue.js"/>
</p>

Extension of my master's thesis, which enables easy use of models trained during my research. It uses Vue.js on the frontend and Python on the backend. If you are interested in my master's thesis check out the repository below:

- [WS-DETR model](https://github.com/matej2000/rtdetr_pytorch_wsdetr)

<!-- omit in toc -->

### Table of Contents

- [Wildlife recognition dashboard](#wildlife-recognition-dashboard)
  - [Table of Contents](#table-of-contents)
  - [Website recordings](#website-recordings)
  - [Website screenshots](#website-screenshots)
    - [Desktop view](#desktop-view)
    - [Mobile view](#mobile-view)
  - [Project Setup](#project-setup)
    - [Build and run for Development](#build-and-run-for-development)
    - [Build for production](#build-for-production)
    - [Stop application](#stop-application)

## Website recordings

**Desktop view:**

<!-- ![Desktop view](assets/desktop_view.gif) -->

<!-- <video controls width="960" height="540">
  <source src="assets/2025-03-06 22-44-23.mp4" type="video/mp4">
</video> -->

<img src="assets/desktop_view.gif" width="960" />

**Mobile view:**

<!-- <video controls width="375">
  <source src="assets/mobile_view.gif" type="video/mp4">
</video> -->

<img src="assets/mobile_view.gif" width="375" />

<!-- ![Mobile view](assets/mobile_view.gif) -->

## Website screenshots

### Desktop view

**Home section:**

<img src="assets/localhost_5173_.png" width="960" />
<!-- ![Home desktop](assets/localhost_5173_.png) -->

**Dashboard:**

<img src="assets/login.png" width="960" />
<!-- ![Dashboard desktop](assets/login.png) -->

### Mobile view

**Home section:**

<img src="assets/localhost_5173_(iPhone SE).png" width="375" />
<!-- ![Home desktop](assets/localhost_5173_(iPhone%20SE).png) -->

**Dashboard:**

<img src="assets/login(iPhone SE).png" width="375" />

<!-- ![Dashboard desktop](assets/login(iPhone%20SE).png) -->

## Project Setup

```sh
git clone https://github.com/matej2000/wildlife_recognition_vue.git
cd wildlife_recognition_vue
```

### Build and run for Development

```sh
docker compose --build -f compose.dev.yaml up
```

### Build for production

```sh
docker compose up --build
```

### Stop application

```sh
docker compose down
```
