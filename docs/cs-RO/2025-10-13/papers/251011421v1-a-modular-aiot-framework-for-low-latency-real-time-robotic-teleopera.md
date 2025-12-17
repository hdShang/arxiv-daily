---
layout: default
title: A Modular AIoT Framework for Low-Latency Real-Time Robotic Teleoperation in Smart Cities
---

# A Modular AIoT Framework for Low-Latency Real-Time Robotic Teleoperation in Smart Cities

**arXiv**: [2510.11421v1](https://arxiv.org/abs/2510.11421) | [PDF](https://arxiv.org/pdf/2510.11421.pdf)

**作者**: Shih-Chieh Sun, Yun-Cheng Tsai

---

## 💡 一句话要点

**提出模块化AIoT框架，实现低延迟实时机器人遥操作，适用于智慧城市场景。**

**关键词**: `机器人遥操作` `AIoT框架` `低延迟通信` `实时对象检测` `智慧城市应用` `模块化部署`

## 📋 核心要点

1. 核心问题：智慧城市中远程机器人操作需低延迟实时交互与智能感知。
2. 方法要点：集成Flutter移动界面、MQTT控制、WebRTC视频流与YOLOv11-nano对象检测。
3. 实验或效果：在VPN场景下，执行器响应低至0.2秒，视频延迟低于1.2秒。

## 📄 摘要（原文）

> This paper presents an AI-driven IoT robotic teleoperation system designed
> for real-time remote manipulation and intelligent visual monitoring, tailored
> for smart city applications. The architecture integrates a Flutter-based
> cross-platform mobile interface with MQTT-based control signaling and WebRTC
> video streaming via the LiveKit framework. A YOLOv11-nano model is deployed for
> lightweight object detection, enabling real-time perception with annotated
> visual overlays delivered to the user interface. Control commands are
> transmitted via MQTT to an ESP8266-based actuator node, which coordinates
> multi-axis robotic arm motion through an Arduino Mega2560 controller. The
> backend infrastructure is hosted on DigitalOcean, ensuring scalable cloud
> orchestration and stable global communication. Latency evaluations conducted
> under both local and international VPN scenarios (including Hong Kong, Japan,
> and Belgium) demonstrate actuator response times as low as 0.2 seconds and
> total video latency under 1.2 seconds, even across high-latency networks. This
> low-latency dual-protocol design ensures responsive closed-loop interaction and
> robust performance in distributed environments. Unlike conventional
> teleoperation platforms, the proposed system emphasizes modular deployment,
> real-time AI sensing, and adaptable communication strategies, making it
> well-suited for smart city scenarios such as remote infrastructure inspection,
> public equipment servicing, and urban automation. Future enhancements will
> focus on edge-device deployment, adaptive routing, and integration with
> city-scale IoT networks to enhance resilience and scalability.

