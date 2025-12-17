---
layout: default
title: Cerberus: Real-Time Video Anomaly Detection via Cascaded Vision-Language Models
---

# Cerberus: Real-Time Video Anomaly Detection via Cascaded Vision-Language Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2510.16290" class="toolbar-btn" target="_blank">📄 arXiv: 2510.16290v1</a>
  <a href="https://arxiv.org/pdf/2510.16290.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.16290v1" onclick="toggleFavorite(this, '2510.16290v1', 'Cerberus: Real-Time Video Anomaly Detection via Cascaded Vision-Language Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yue Zheng, Xiufang Shi, Jiming Chen, Yuanchao Shu

**分类**: cs.CV, cs.CL

**发布日期**: 2025-10-18

---

## 💡 一句话要点

**Cerberus：基于级联视觉-语言模型的实时视频异常检测系统**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `视频异常检测` `视觉-语言模型` `实时视频分析` `运动掩码提示` `规则学习`

## 📋 核心要点

1. 现有基于视觉-语言模型的视频异常检测方法计算成本高昂，视觉 grounding 性能不稳定，难以实现实时部署。
2. Cerberus 采用两阶段级联系统，离线学习正常行为规则，在线结合轻量级过滤和细粒度 VLM 推理，实现高效准确的异常检测。
3. Cerberus 通过运动掩码提示引导 VLM 注意力，并利用基于规则的偏差检测识别异常，在速度和精度上均有显著提升。

## 📝 摘要（中文）

视频异常检测（VAD）领域受益于视觉-语言模型（VLMs）的快速发展。尽管这些模型提供了卓越的零样本检测能力，但其巨大的计算成本和不稳定的视觉 grounding 性能阻碍了实时部署。为了克服这些挑战，我们提出了 Cerberus，一个为高效且准确的实时 VAD 设计的两阶段级联系统。Cerberus 离线学习正常行为规则，并在在线推理期间结合轻量级过滤和细粒度的 VLM 推理。Cerberus 的性能提升来自两个关键创新：运动掩码提示和基于规则的偏差检测。前者将 VLM 的注意力引导到与运动相关的区域，而后者将异常识别为与学习到的规范的偏差，而不是枚举可能的异常。在四个数据集上的广泛评估表明，Cerberus 在 NVIDIA L40S GPU 上平均实现了 57.68 fps，速度提升了 151.79 倍，并且达到了与最先进的基于 VLM 的 VAD 方法相当的 97.2% 的准确率，使其成为实时视频分析的实用解决方案。

## 🔬 方法详解

**问题定义**：视频异常检测旨在识别视频中不符合预期或正常模式的事件。现有基于视觉-语言模型的方法虽然在零样本检测方面表现出色，但由于计算复杂度高，难以满足实时性要求。此外，视觉 grounding 的不稳定性也影响了检测的准确性。

**核心思路**：Cerberus 的核心思路是将异常检测过程分解为两个阶段：轻量级过滤和细粒度 VLM 推理。通过轻量级过滤快速排除正常帧，减少 VLM 的计算负担。同时，利用运动掩码提示引导 VLM 关注运动区域，提高视觉 grounding 的准确性。基于规则的偏差检测则将异常定义为与正常行为的偏差，避免了枚举所有可能异常的困难。

**技术框架**：Cerberus 系统包含离线学习和在线推理两个阶段。离线学习阶段，系统学习正常行为的规则。在线推理阶段，首先使用轻量级滤波器快速排除正常帧；然后，对于剩余帧，利用运动掩码提示引导 VLM 进行细粒度推理，并基于学习到的规则检测偏差，从而识别异常。

**关键创新**：Cerberus 的关键创新在于运动掩码提示和基于规则的偏差检测。运动掩码提示通过引导 VLM 关注运动区域，提高了视觉 grounding 的准确性。基于规则的偏差检测将异常定义为与正常行为的偏差，避免了枚举所有可能异常的困难，提高了泛化能力。

**关键设计**：运动掩码的生成方式未知。规则的学习方式未知。轻量级滤波器的具体实现方式未知。VLM 的选择和微调策略未知。损失函数的设计未知。

## 📊 实验亮点

Cerberus 在 NVIDIA L40S GPU 上实现了平均 57.68 fps 的处理速度，相比现有基于 VLM 的 VAD 方法，速度提升了 151.79 倍。同时，Cerberus 达到了 97.2% 的准确率，与最先进的 VLM 方法相当。实验结果表明，Cerberus 在保证高准确率的同时，显著提高了实时性，使其成为一个实用的解决方案。

## 🎯 应用场景

Cerberus 可应用于各种需要实时视频分析的场景，例如智能监控、工业安全、交通管理和智能零售。该系统能够快速准确地检测异常事件，从而提高安全性、效率和运营效率。未来，该技术有望扩展到更复杂的视频分析任务，例如行为识别和事件预测。

## 📄 摘要（原文）

> Video anomaly detection (VAD) has rapidly advanced by recent development of Vision-Language Models (VLMs). While these models offer superior zero-shot detection capabilities, their immense computational cost and unstable visual grounding performance hinder real-time deployment. To overcome these challenges, we introduce Cerberus, a two-stage cascaded system designed for efficient yet accurate real-time VAD. Cerberus learns normal behavioral rules offline, and combines lightweight filtering with fine-grained VLM reasoning during online inference. The performance gains of Cerberus come from two key innovations: motion mask prompting and rule-based deviation detection. The former directs the VLM's attention to regions relevant to motion, while the latter identifies anomalies as deviations from learned norms rather than enumerating possible anomalies. Extensive evaluations on four datasets show that Cerberus on average achieves 57.68 fps on an NVIDIA L40S GPU, a 151.79$\times$ speedup, and 97.2\% accuracy comparable to the state-of-the-art VLM-based VAD methods, establishing it as a practical solution for real-time video analytics.

