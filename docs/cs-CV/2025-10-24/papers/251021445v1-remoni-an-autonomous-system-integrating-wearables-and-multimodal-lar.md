---
layout: default
title: REMONI: An Autonomous System Integrating Wearables and Multimodal Large Language Models for Enhanced Remote Health Monitoring
---

# REMONI: An Autonomous System Integrating Wearables and Multimodal Large Language Models for Enhanced Remote Health Monitoring

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2510.21445" class="toolbar-btn" target="_blank">📄 arXiv: 2510.21445v1</a>
  <a href="https://arxiv.org/pdf/2510.21445.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.21445v1" onclick="toggleFavorite(this, '2510.21445v1', 'REMONI: An Autonomous System Integrating Wearables and Multimodal Large Language Models for Enhanced Remote Health Monitoring')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Thanh Cong Ho, Farah Kharrat, Abderrazek Abid, Fakhri Karray

**分类**: cs.CL, cs.AI, cs.CV, cs.LG

**发布日期**: 2025-10-24

**期刊**: 2024 IEEE International Symposium on Medical Measurements and Applications (MeMeA)

**DOI**: [10.1109/MeMeA60663.2024.10596778](https://doi.org/10.1109/MeMeA60663.2024.10596778)

---

## 💡 一句话要点

**REMONI：集成可穿戴设备与多模态大语言模型的自主远程健康监测系统**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `远程健康监测` `多模态大语言模型` `可穿戴设备` `物联网` `人机交互` `异常检测` `跌倒检测`

## 📋 核心要点

1. 现有远程病人监护系统缺乏有效的人机交互，限制了其在实际医疗场景中的应用。
2. REMONI系统通过集成可穿戴设备、物联网和多模态大语言模型，实现了对患者状态的全面感知和智能响应。
3. 实验结果表明，该系统具有实际应用潜力，能够降低医护人员工作量和医疗成本，提升医疗服务效率。

## 📝 摘要（中文）

本文提出REMONI，一个自主远程健康监测系统，它集成了多模态大语言模型（MLLM）、物联网（IoT）和可穿戴设备。该系统自动且持续地从可穿戴设备（如智能手表）收集生命体征和加速度计数据，并从摄像头收集患者视频片段中的视觉数据。这些数据由异常检测模块处理，该模块包含跌倒检测模型和算法，用于识别患者的紧急情况并向护理人员发出警报。该系统的一个显著特点是自然语言处理组件，它使用MLLM开发，能够检测和识别患者的活动和情绪，同时响应医护人员的询问。此外，采用提示工程来无缝集成所有患者信息。因此，医生和护士可以通过用户友好的Web应用程序与智能代理交互，访问实时的生命体征以及患者的当前状态和情绪。实验表明，该系统在实际场景中具有可实施性和可扩展性，有可能减轻医疗专业人员的工作量并降低医疗成本。一个功能齐全的原型已被开发并正在测试中，以展示其各种功能的稳健性。

## 🔬 方法详解

**问题定义**：现有远程健康监测系统主要集中于传感器数据的收集、可视化和分析，以检测特定疾病的异常情况，例如糖尿病、心脏病和抑郁症。然而，这些系统在人机交互方面存在显著不足，医护人员难以实时了解患者的整体状态和情绪，从而影响了诊断和治疗的效率。

**核心思路**：REMONI系统的核心思路是利用多模态大语言模型（MLLM）增强远程健康监测系统的人机交互能力。通过集成来自可穿戴设备和摄像头的多模态数据，并利用MLLM进行自然语言处理和情感识别，系统能够更全面地理解患者的状态，并以自然语言的方式与医护人员进行交流。

**技术框架**：REMONI系统包含以下主要模块：1) 数据采集模块：从可穿戴设备（如智能手表）收集生命体征和加速度计数据，从摄像头收集患者视频数据。2) 异常检测模块：包含跌倒检测模型和算法，用于识别患者的紧急情况。3) 自然语言处理模块：使用MLLM检测和识别患者的活动和情绪，并响应医护人员的询问。4) 提示工程模块：用于无缝集成所有患者信息，以便MLLM能够更好地理解患者的状态。5) 用户界面：一个用户友好的Web应用程序，允许医护人员与智能代理交互，访问实时的生命体征以及患者的当前状态和情绪。

**关键创新**：REMONI系统的关键创新在于将多模态大语言模型（MLLM）集成到远程健康监测系统中，从而实现了对患者状态的全面感知和智能响应。与传统的远程健康监测系统相比，REMONI系统能够更有效地理解患者的需求，并以自然语言的方式与医护人员进行交流，从而提高了诊断和治疗的效率。

**关键设计**：论文中提到使用了prompt engineering来集成患者信息，但没有给出具体的参数设置、损失函数、网络结构等技术细节。这些细节属于实现层面的内容，可能在后续的论文或技术报告中进行更详细的描述。目前，这些细节未知。

## 📊 实验亮点

论文展示了一个功能齐全的原型系统，并对其各种功能的稳健性进行了测试。实验结果表明，该系统在实际场景中具有可实施性和可扩展性，能够减轻医疗专业人员的工作量并降低医疗成本。具体的性能数据和对比基线未在摘要中给出，需要在论文正文中查找。

## 🎯 应用场景

REMONI系统可应用于居家养老、远程医疗、慢性病管理等领域。通过实时监测患者的生理数据和行为状态，并利用智能化的自然语言交互，该系统能够帮助医护人员更好地了解患者的需求，提供更个性化的医疗服务，从而提高患者的生活质量，降低医疗成本，并缓解医疗资源紧张的问题。

## 📄 摘要（原文）

> With the widespread adoption of wearable devices in our daily lives, the demand and appeal for remote patient monitoring have significantly increased. Most research in this field has concentrated on collecting sensor data, visualizing it, and analyzing it to detect anomalies in specific diseases such as diabetes, heart disease and depression. However, this domain has a notable gap in the aspect of human-machine interaction. This paper proposes REMONI, an autonomous REmote health MONItoring system that integrates multimodal large language models (MLLMs), the Internet of Things (IoT), and wearable devices. The system automatically and continuously collects vital signs, accelerometer data from a special wearable (such as a smartwatch), and visual data in patient video clips collected from cameras. This data is processed by an anomaly detection module, which includes a fall detection model and algorithms to identify and alert caregivers of the patient's emergency conditions. A distinctive feature of our proposed system is the natural language processing component, developed with MLLMs capable of detecting and recognizing a patient's activity and emotion while responding to healthcare worker's inquiries. Additionally, prompt engineering is employed to integrate all patient information seamlessly. As a result, doctors and nurses can access real-time vital signs and the patient's current state and mood by interacting with an intelligent agent through a user-friendly web application. Our experiments demonstrate that our system is implementable and scalable for real-life scenarios, potentially reducing the workload of medical professionals and healthcare costs. A full-fledged prototype illustrating the functionalities of the system has been developed and being tested to demonstrate the robustness of its various capabilities.

