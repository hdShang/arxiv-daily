---
layout: default
title: "BioGAP-Ultra: A Modular Edge-AI Platform for Wearable Multimodal Biosignal Acquisition and Processing"
---

# BioGAP-Ultra: A Modular Edge-AI Platform for Wearable Multimodal Biosignal Acquisition and Processing

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.13728" class="toolbar-btn" target="_blank">📄 arXiv: 2508.13728v2</a>
  <a href="https://arxiv.org/pdf/2508.13728.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.13728v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.13728v2', 'BioGAP-Ultra: A Modular Edge-AI Platform for Wearable Multimodal Biosignal Acquisition and Processing')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Sebastian Frey, Giusy Spacone, Andrea Cossettini, Marco Guermandi, Philipp Schilk, Luca Benini, Victor Kartsch

**分类**: eess.SY, eess.SP

**发布日期**: 2025-08-19 (更新: 2025-12-15)

**备注**: 17 pages, 15 figures

---

## 💡 一句话要点

**提出BioGAP-Ultra以解决可穿戴生物信号监测的多模态需求**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `可穿戴设备` `生物信号监测` `边缘AI` `多模态融合` `低功耗设计`

## 📋 核心要点

1. 现有可穿戴生物信号监测平台在多模态信号采集和处理能力上存在不足，难以满足日益增长的应用需求。
2. BioGAP-Ultra通过支持多种生物信号的同步采集和嵌入式AI处理，提供了一种高效的解决方案，提升了设备的智能化水平。
3. 实验结果显示，BioGAP-Ultra在不同可穿戴形式中表现出色，功耗低且准确性高，适用于多种生物信号应用。

## 📝 摘要（中文）

随着对连续生理监测和人机交互的需求增长，迫切需要灵活、低功耗且具备设备智能的可穿戴平台。本文提出了BioGAP-Ultra，一个先进的多模态生物传感平台，支持同步采集多种电生理和血流动力学信号，如EEG、EMG、ECG和PPG，同时在设备上实现高效的AI处理。BioGAP-Ultra是对之前BioGAP设计的重要扩展，具备更大的存储、改进的无线连接和更多的信号模态。系统展示了其在多种可穿戴形式中的灵活性，并通过两个代表性的设备应用展示了其边缘AI能力。所有硬件和软件设计文件均以开放源代码形式发布。

## 🔬 方法详解

**问题定义**：本文旨在解决现有可穿戴生物信号监测平台在多模态信号采集、处理能力及能效方面的不足，尤其是在实时监测和分析的需求日益增加的背景下。

**核心思路**：BioGAP-Ultra的核心思想是通过集成多种生物信号的同步采集与嵌入式AI处理，提升可穿戴设备的智能化和能效，满足多样化的应用需求。

**技术框架**：BioGAP-Ultra的整体架构包括信号采集模块、数据处理模块和无线传输模块，支持EEG、EMG、ECG和PPG等多种信号的实时采集与分析。

**关键创新**：BioGAP-Ultra的主要创新在于其显著提升的存储能力、无线连接速度和信号模态数量，使其在性能上优于现有平台，尤其是在能效和多样性方面。

**关键设计**：在设计中，BioGAP-Ultra采用了双倍SRAM和四倍FLASH的存储配置，支持高达1.4 Mbit/s的无线带宽，并增加了信号模态和模拟输入通道的数量，确保了高效的数据处理和传输。

## 📊 实验亮点

实验结果表明，BioGAP-Ultra在不同可穿戴设备中表现出色，例如EEG-PPG头带功耗为32.8 mW，EMG袖子为26.7 mW，ECG-PPG胸带仅需9.3 mW。同时，边缘AI应用的准确率达到79.9 %，显示出其在实际应用中的高效性和可靠性。

## 🎯 应用场景

BioGAP-Ultra的潜在应用领域包括健康监测、运动分析和人机交互等。其灵活的设计和高效的能耗使其能够广泛应用于医疗、运动科学和智能家居等场景，具有重要的实际价值和未来影响。

## 📄 摘要（原文）

> The growing demand for continuous physiological monitoring and human-machine interaction in real-world settings calls for wearable platforms that are flexible, low-power, and capable of on-device intelligence. This work presents BioGAP-Ultra, an advanced multimodal biosensing platform that supports synchronized acquisition of diverse electrophysiological and hemodynamic signals such as EEG, EMG, ECG, and PPG while enabling embedded AI processing at state-of-the-art energy efficiency. BioGAP-Ultra is a major extension of our previous BioGAP design aimed at meeting the rapidly growing requirements of wearable biosensing applications. It features (i) increased on-device storage (x2 SRAM, x4 FLASH), (ii) improved wireless connectivity (supporting up to 1.4 Mbit/s bandwidth, x4 higher than BioGAP), (iii) enhanced number of signal modalities (from 3 to 5) and analog input channels (x2). Further, it is accompanied by a real-time visualization and analysis software suite that supports the hardware design, providing access to raw data and real-time configurability on a mobile phone. Finally, we demonstrate the system's versatility through integration into various wearable form factors: an EEG-PPG headband consuming 32.8 mW, an EMG sleeve at 26.7 mW, and an ECG-PPG chestband requiring only 9.3 mW for continuous acquisition and streaming, tailored for diverse biosignal applications. To showcase its edge-AI capabilities, we further deploy two representative on-device applications: (1) ECG-PPG-based PAT estimation at 8.6 mW, and (2) EMG-ACC-based classification of reach-and-grasp motion phases, achieving 79.9 % $\pm$ 5.7 % accuracy at 23.6 mW. All hardware and software design files are also released open-source with a permissive license.

