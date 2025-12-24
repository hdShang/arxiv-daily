---
layout: default
title: Event-Triggered GAT-LSTM Framework for Attack Detection in Heating, Ventilation, and Air Conditioning Systems
---

# Event-Triggered GAT-LSTM Framework for Attack Detection in Heating, Ventilation, and Air Conditioning Systems

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.03559" class="toolbar-btn" target="_blank">📄 arXiv: 2505.03559v1</a>
  <a href="https://arxiv.org/pdf/2505.03559.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.03559v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.03559v1', 'Event-Triggered GAT-LSTM Framework for Attack Detection in Heating, Ventilation, and Air Conditioning Systems')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Zhenan Feng, Ehsan Nekouei

**分类**: eess.SY

**发布日期**: 2025-05-06

---

## 💡 一句话要点

**提出事件触发GAT-LSTM框架以解决HVAC系统攻击检测问题**

🎯 **匹配领域**: **支柱七：动作重定向 (Motion Retargeting)**

**关键词**: `HVAC系统` `攻击检测` `事件触发` `图注意力网络` `长短期记忆网络` `数据隐私` `云计算`

## 📋 核心要点

1. HVAC系统因其互联性和传感器网络的依赖，面临网络物理攻击的风险，现有检测方法在准确性和数据隐私方面存在不足。
2. 本文提出的框架结合了事件触发单元和云端GAT-LSTM模型，通过本地监测和云端分类实现高效的攻击检测。
3. 实验结果显示，GAT-LSTM模型的整体检测准确率达到98.8%，相比于单独使用GAT和LSTM的基线模型有显著提升。

## 📝 摘要（中文）

供暖、通风和空调（HVAC）系统对于维持室内环境质量至关重要，但其互联特性和对传感器网络的依赖使其易受网络物理攻击。此类攻击可能中断系统操作并通过测量数据泄露敏感个人信息。本文提出了一种新颖的HVAC系统攻击检测框架，集成了事件触发单元（ETU）进行本地监测和基于云的分类系统，使用图注意力网络（GAT）和长短期记忆网络（LSTM）。ETU执行二元分类以识别潜在异常，并选择性触发加密数据传输到云端，从而显著降低通信成本。云端的GAT模块建模HVAC组件之间的空间关系，而LSTM模块捕获加密状态序列中的时间依赖性以分类攻击类型。我们的方案在模拟多种攻击场景的数据集上进行了评估，结果表明该框架在保持数据隐私的同时，实现了高检测准确率。

## 🔬 方法详解

**问题定义**：本文旨在解决HVAC系统在面对网络物理攻击时的检测问题。现有方法在准确性和数据隐私保护方面存在不足，难以有效应对复杂的攻击场景。

**核心思路**：提出的框架通过事件触发单元（ETU）进行本地异常检测，并结合云端的GAT和LSTM模型进行分类，从而实现高效且安全的攻击检测。此设计旨在降低通信成本，同时提高检测准确性。

**技术框架**：整体架构包括ETU模块和云端分类模块。ETU负责本地的二元分类，识别潜在异常并触发数据传输；云端模块则利用GAT建模空间关系，LSTM捕获时间依赖性进行攻击类型分类。

**关键创新**：本研究的主要创新在于将事件触发机制与GAT-LSTM模型相结合，显著提高了检测准确率（98.8%），并有效降低了数据传输量（15%）。与现有方法相比，能够更好地利用HVAC系统的空间-时间特性。

**关键设计**：在设计中，ETU模块采用二元分类器，GAT模块用于建模组件间的空间关系，LSTM模块则处理加密状态序列的时间依赖性。具体的参数设置和损失函数设计未在摘要中详细说明，需参考论文的具体内容。

## 📊 实验亮点

实验结果表明，提出的GAT-LSTM模型在攻击检测中的整体准确率达到98.8%，相比于仅使用GAT（94.2%）和LSTM（91.5%）的模型有显著提升。此外，数据传输量减少至15%，有效降低了通信成本。

## 🎯 应用场景

该研究的潜在应用领域包括智能建筑管理、工业自动化和城市基础设施等。通过提高HVAC系统的安全性和可靠性，能够有效保护用户隐私并提升系统的整体性能，具有重要的实际价值和未来影响。

## 📄 摘要（原文）

> Heating, Ventilation, and Air Conditioning (HVAC) systems are essential for maintaining indoor environmental quality, but their interconnected nature and reliance on sensor networks make them vulnerable to cyber-physical attacks. Such attacks can interrupt system operations and risk leaking sensitive personal information through measurement data. In this paper, we propose a novel attack detection framework for HVAC systems, integrating an Event-Triggering Unit (ETU) for local monitoring and a cloud-based classification system using the Graph Attention Network (GAT) and the Long Short-Term Memory (LSTM) network. The ETU performs a binary classification to identify potential anomalies and selectively triggers encrypted data transmission to the cloud, significantly reducing communication cost. The cloud-side GAT module models the spatial relationships among HVAC components, while the LSTM module captures temporal dependencies across encrypted state sequences to classify the attack type. Our approach is evaluated on datasets that simulate diverse attack scenarios. Compared to GAT-only (94.2% accuracy) and LSTM-only (91.5%) ablations, our full GAT-LSTM model achieves 98.8% overall detection accuracy and reduces data transmission to 15%. These results demonstrate that the proposed framework achieves high detection accuracy while preserving data privacy by using the spatial-temporal characteristics of HVAC systems and minimizing transmission costs through event-triggered communication.

