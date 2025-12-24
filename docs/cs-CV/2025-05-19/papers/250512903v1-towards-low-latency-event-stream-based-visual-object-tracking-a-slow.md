---
layout: default
title: "Towards Low-Latency Event Stream-based Visual Object Tracking: A Slow-Fast Approach"
---

# Towards Low-Latency Event Stream-based Visual Object Tracking: A Slow-Fast Approach

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.12903" class="toolbar-btn" target="_blank">📄 arXiv: 2505.12903v1</a>
  <a href="https://arxiv.org/pdf/2505.12903.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.12903v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.12903v1', 'Towards Low-Latency Event Stream-based Visual Object Tracking: A Slow-Fast Approach')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Shiao Wang, Xiao Wang, Liye Jin, Bo Jiang, Lin Zhu, Lan Chen, Yonghong Tian, Bin Luo

**分类**: cs.CV, cs.AI

**发布日期**: 2025-05-19

**🔗 代码/项目**: [GITHUB](https://github.com/Event-AHU/SlowFast_Event_Track)

---

## 💡 一句话要点

**提出Slow-Fast跟踪方法以解决低延迟视觉目标跟踪问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `视觉目标跟踪` `事件摄像头` `低延迟` `知识蒸馏` `图基表示学习` `FlashAttention` `慢-快跟踪`

## 📋 核心要点

1. 现有的视觉目标跟踪方法在低延迟性能和资源受限环境中表现不佳，难以满足实时应用需求。
2. 提出的SFTrack方法结合高精度慢跟踪器与高效快速跟踪器，灵活适应不同的计算资源和延迟要求。
3. 在多个公共基准测试上进行的实验表明，SFTrack在跟踪精度和速度上均有显著提升，适用于多种实际场景。

## 📝 摘要（中文）

现有的跟踪算法通常依赖低帧率RGB摄像头和计算密集型深度神经网络架构来实现有效跟踪。然而，这些基于帧的方法在低延迟性能上面临挑战，并且在资源受限环境中常常表现不佳。近年来，基于生物启发的事件摄像头在视觉目标跟踪中展现出低延迟应用的优势。本文提出了一种新颖的Slow-Fast跟踪范式（SFTrack），灵活适应不同的操作需求，支持高精度慢跟踪器和高效快速跟踪器。通过图基表示学习和FlashAttention视觉骨干网络的结合，快速跟踪器实现了低延迟，并通过知识蒸馏策略进一步提升性能。大量实验表明该方法在不同真实场景中的有效性和效率。

## 🔬 方法详解

**问题定义**：本文旨在解决现有基于帧的视觉目标跟踪方法在低延迟和资源受限环境中的不足，尤其是在实时应用中的挑战。

**核心思路**：提出的Slow-Fast跟踪范式通过结合高精度和高效的跟踪器，灵活适应不同的操作需求，旨在实现低延迟和高精度的目标跟踪。

**技术框架**：该框架首先从高时间分辨率的事件流中进行图基表示学习，然后将学习到的图结构信息整合到两个FlashAttention基础视觉网络中，分别生成慢跟踪器和快跟踪器。

**关键创新**：最重要的创新在于将图基表示学习与FlashAttention网络结合，形成了高效的快速跟踪器，并通过知识蒸馏策略提升其性能，这与传统方法的设计理念有本质区别。

**关键设计**：快速跟踪器采用轻量级网络设计，能够在单次前向传播中生成多个边界框输出，此外，通过监督微调和知识蒸馏进一步优化了模型性能。

## 📊 实验亮点

在FE240、COESOT和EventVOT等公共基准测试上，SFTrack在跟踪精度和速度上均表现出色，快速跟踪器在多个场景中实现了显著的低延迟，提升幅度达到XX%。

## 🎯 应用场景

该研究的潜在应用领域包括智能监控、无人驾驶、增强现实等需要实时目标跟踪的场景。通过提高跟踪的精度和速度，SFTrack能够在资源受限的环境中有效应用，具有重要的实际价值和未来影响。

## 📄 摘要（原文）

> Existing tracking algorithms typically rely on low-frame-rate RGB cameras coupled with computationally intensive deep neural network architectures to achieve effective tracking. However, such frame-based methods inherently face challenges in achieving low-latency performance and often fail in resource-constrained environments. Visual object tracking using bio-inspired event cameras has emerged as a promising research direction in recent years, offering distinct advantages for low-latency applications. In this paper, we propose a novel Slow-Fast Tracking paradigm that flexibly adapts to different operational requirements, termed SFTrack. The proposed framework supports two complementary modes, i.e., a high-precision slow tracker for scenarios with sufficient computational resources, and an efficient fast tracker tailored for latency-aware, resource-constrained environments. Specifically, our framework first performs graph-based representation learning from high-temporal-resolution event streams, and then integrates the learned graph-structured information into two FlashAttention-based vision backbones, yielding the slow and fast trackers, respectively. The fast tracker achieves low latency through a lightweight network design and by producing multiple bounding box outputs in a single forward pass. Finally, we seamlessly combine both trackers via supervised fine-tuning and further enhance the fast tracker's performance through a knowledge distillation strategy. Extensive experiments on public benchmarks, including FE240, COESOT, and EventVOT, demonstrate the effectiveness and efficiency of our proposed method across different real-world scenarios. The source code has been released on https://github.com/Event-AHU/SlowFast_Event_Track.

