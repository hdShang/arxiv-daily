---
layout: default
title: A Modular AIoT Framework for Low-Latency Real-Time Robotic Teleoperation in Smart Cities
---

# A Modular AIoT Framework for Low-Latency Real-Time Robotic Teleoperation in Smart Cities

<div class="paper-toolbar">
  <div class="toolbar-left">
    <a href="https://arxiv.org/abs/2510.11421" target="_blank" class="toolbar-btn">arXiv: 2510.11421v1</a>
    <a href="https://arxiv.org/pdf/2510.11421.pdf" target="_blank" class="toolbar-btn">PDF</a>
  </div>
  <div class="toolbar-right">
    <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.11421v1" 
            onclick="toggleFavorite(this, '2510.11421v1', 'A Modular AIoT Framework for Low-Latency Real-Time Robotic Teleoperation in Smart Cities')" title="收藏">
      ☆ 收藏
    </button>
    <button class="toolbar-btn share-btn" onclick="copyLink()" title="复制链接">
      🔗 分享
    </button>
  </div>
</div>


**作者**: Shih-Chieh Sun, Yun-Cheng Tsai

**分类**: cs.RO, cs.HC

**发布日期**: 2025-10-13

---

## 💡 一句话要点

**提出基于AIoT的模块化低延迟机器人遥操作框架，用于智慧城市应用**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)**

**关键词**: `机器人遥操作` `AIoT` `智慧城市` `低延迟` `WebRTC` `MQTT` `目标检测`

## 📋 核心要点

1. 现有遥操作平台在智慧城市应用中面临延迟高、部署复杂等挑战，难以满足实时性和灵活性的需求。
2. 论文提出一种模块化的AIoT框架，结合MQTT控制、WebRTC视频流和轻量级目标检测，实现低延迟的机器人遥操作。
3. 实验结果表明，该系统在不同网络环境下均能实现低延迟的控制和视频传输，适用于远程基础设施检查等场景。

## 📝 摘要（中文）

本文提出了一种基于AI驱动的IoT机器人遥操作系统，专为智慧城市应用中的实时远程操作和智能视觉监控而设计。该架构集成了基于Flutter的跨平台移动界面、基于MQTT的控制信令和通过LiveKit框架实现的WebRTC视频流。系统部署了YOLOv11-nano模型进行轻量级目标检测，从而实现实时感知，并将带有注释的视觉覆盖层传递到用户界面。控制命令通过MQTT传输到基于ESP8266的执行器节点，该节点通过Arduino Mega2560控制器协调多轴机器人手臂的运动。后端基础设施托管在DigitalOcean上，确保可扩展的云编排和稳定的全球通信。在本地和国际VPN场景（包括香港、日本和比利时）下进行的延迟评估表明，即使在高延迟网络中，执行器响应时间也低至0.2秒，总视频延迟低于1.2秒。这种低延迟双协议设计确保了响应迅速的闭环交互和分布式环境中的稳健性能。与传统的遥操作平台不同，该系统强调模块化部署、实时AI感知和适应性通信策略，使其非常适合远程基础设施检查、公共设备维护和城市自动化等智慧城市场景。未来的增强功能将侧重于边缘设备部署、自适应路由以及与城市级IoT网络的集成，以增强弹性和可扩展性。

## 🔬 方法详解

**问题定义**：现有机器人遥操作系统在智慧城市应用中，面临着高延迟、部署复杂、缺乏实时AI感知等问题。传统的遥操作平台难以在分布式、高延迟的网络环境中提供流畅的用户体验，并且缺乏对环境的智能理解能力，限制了其应用范围。

**核心思路**：论文的核心思路是采用模块化的AIoT架构，将控制、视频传输和AI感知解耦，并针对每个模块选择合适的协议和技术，以实现低延迟和高效率。通过轻量级的目标检测模型，为操作员提供实时的环境感知信息，增强操作的准确性和安全性。

**技术框架**：该系统主要包含以下模块：1) 基于Flutter的跨平台移动界面，用于用户交互和控制命令发送；2) 基于MQTT的控制信道，用于传输控制命令到执行器节点；3) 基于LiveKit框架的WebRTC视频流，用于实时视频传输；4) 基于YOLOv11-nano的目标检测模型，用于实时环境感知；5) 基于ESP8266的执行器节点，用于控制机器人手臂的运动；6) 基于Arduino Mega2560的控制器，用于精确控制机器人手臂的各个轴；7) DigitalOcean云平台，提供后端基础设施和全球通信支持。

**关键创新**：该系统的关键创新在于其模块化的设计和低延迟的双协议通信机制。通过将控制和视频流分离，并分别采用MQTT和WebRTC协议，实现了在不同网络条件下的最佳性能。此外，YOLOv11-nano模型的引入，为操作员提供了实时的环境感知能力，增强了系统的智能化水平。

**关键设计**：控制信令采用MQTT协议，保证控制命令的可靠传输。视频流采用WebRTC协议，利用其低延迟和自适应带宽调整的特性。YOLOv11-nano模型经过专门优化，以在资源受限的设备上实现实时目标检测。执行器节点采用ESP8266和Arduino Mega2560的组合，实现对多轴机器人手臂的精确控制。

## 📊 实验亮点

实验结果表明，该系统在本地网络环境下，执行器响应时间低至0.2秒，总视频延迟低于1.2秒。即使在国际VPN环境下（包括香港、日本和比利时），也能保持较低的延迟，证明了其在分布式环境下的稳健性。与传统的遥操作平台相比，该系统在延迟和智能化方面均有显著提升。

## 🎯 应用场景

该研究成果可广泛应用于智慧城市中的远程基础设施检查、公共设备维护、城市自动化等领域。例如，可以利用该系统远程检查桥梁、隧道等基础设施的状况，减少人工巡检的风险和成本。还可以用于远程维护公共设施，如路灯、交通信号灯等，提高维护效率。此外，该系统还可以应用于危险环境下的操作，如核电站维护、灾后救援等。

## 📄 摘要（原文）

> This paper presents an AI-driven IoT robotic teleoperation system designed for real-time remote manipulation and intelligent visual monitoring, tailored for smart city applications. The architecture integrates a Flutter-based cross-platform mobile interface with MQTT-based control signaling and WebRTC video streaming via the LiveKit framework. A YOLOv11-nano model is deployed for lightweight object detection, enabling real-time perception with annotated visual overlays delivered to the user interface. Control commands are transmitted via MQTT to an ESP8266-based actuator node, which coordinates multi-axis robotic arm motion through an Arduino Mega2560 controller. The backend infrastructure is hosted on DigitalOcean, ensuring scalable cloud orchestration and stable global communication. Latency evaluations conducted under both local and international VPN scenarios (including Hong Kong, Japan, and Belgium) demonstrate actuator response times as low as 0.2 seconds and total video latency under 1.2 seconds, even across high-latency networks. This low-latency dual-protocol design ensures responsive closed-loop interaction and robust performance in distributed environments. Unlike conventional teleoperation platforms, the proposed system emphasizes modular deployment, real-time AI sensing, and adaptable communication strategies, making it well-suited for smart city scenarios such as remote infrastructure inspection, public equipment servicing, and urban automation. Future enhancements will focus on edge-device deployment, adaptive routing, and integration with city-scale IoT networks to enhance resilience and scalability.

