---
layout: default
title: "MambaITD: An Efficient Cross-Modal Mamba Network for Insider Threat Detection"
---

# MambaITD: An Efficient Cross-Modal Mamba Network for Insider Threat Detection

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.05695" class="toolbar-btn" target="_blank">📄 arXiv: 2508.05695v1</a>
  <a href="https://arxiv.org/pdf/2508.05695.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.05695v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.05695v1', 'MambaITD: An Efficient Cross-Modal Mamba Network for Insider Threat Detection')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Kaichuan Kong, Dongjie Liu, Xiaobo Jin, Zhiying Li, Guanggang Geng, Jian Weng

**分类**: cs.CR, cs.LG

**发布日期**: 2025-08-06

**备注**: Submitted to the 2025 IEEE International Conference on Data Mining (ICDM)

---

## 💡 一句话要点

**提出MambaITD以解决内部威胁检测中的多模态融合问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `内部威胁检测` `多模态融合` `Mamba状态空间模型` `自适应阈值优化` `特征融合` `长程依赖建模` `信息安全`

## 📋 核心要点

1. 现有内部威胁检测方法在时间动态特征建模、计算效率和实时性方面存在不足，难以有效识别潜在威胁。
2. MambaITD框架通过多源日志预处理、Mamba编码器和自适应阈值优化，解决了跨模态信息孤岛问题，实现了高效的特征融合。
3. 实验结果表明，MambaITD在建模效率和特征融合能力上显著优于传统方法，尤其是在处理类别不平衡和概念漂移方面表现突出。

## 📝 摘要（中文）

企业面临日益增加的内部威胁风险，而现有检测方法由于缺乏有效的时间动态特征建模、计算效率和实时瓶颈以及跨模态信息孤岛问题，无法有效应对这些挑战。本文提出了一种基于Mamba状态空间模型和跨模态自适应融合的新型内部威胁检测框架MambaITD。首先，通过行为序列编码、区间平滑和统计特征提取，进行多源日志预处理模块以对齐异构数据。其次，Mamba编码器建模行为和区间序列中的长程依赖，并结合门控特征融合机制动态结合序列和统计信息。最后，提出了一种基于最大化类间方差的自适应阈值优化方法，通过分析概率分布动态调整决策阈值，有效识别异常，缓解类别不平衡和概念漂移。与传统方法相比，MambaITD在建模效率和特征融合能力上显示出显著优势，超越了基于Transformer的方法，为内部威胁检测提供了更有效的解决方案。

## 🔬 方法详解

**问题定义**：本文旨在解决内部威胁检测中的多模态数据融合问题，现有方法在时间动态特征建模和实时性上存在显著不足，导致检测效果不佳。

**核心思路**：MambaITD通过引入Mamba状态空间模型和跨模态自适应融合机制，旨在有效整合异构数据源，提升检测的准确性和效率。

**技术框架**：MambaITD的整体架构包括多源日志预处理模块、Mamba编码器和自适应阈值优化模块。预处理模块负责对齐异构数据，编码器则建模长程依赖，最后通过优化模块动态调整决策阈值。

**关键创新**：MambaITD的主要创新在于引入了门控特征融合机制和基于最大化类间方差的自适应阈值优化方法，这些设计使得模型在处理复杂数据时更具灵活性和准确性。

**关键设计**：在模型设计中，采用了行为序列编码和统计特征提取的组合方式，确保了信息的全面性和准确性，同时在阈值优化中引入了概率分布分析，以动态应对类别不平衡和概念漂移问题。

## 📊 实验亮点

实验结果显示，MambaITD在内部威胁检测任务中相较于传统方法提升了建模效率和特征融合能力，尤其在处理类别不平衡和概念漂移时表现出色，具体性能指标超越了基于Transformer的模型，显示出显著的优势。

## 🎯 应用场景

MambaITD框架在企业内部威胁检测中具有广泛的应用潜力，能够有效识别潜在的内部风险，提升企业的信息安全防护能力。未来，该技术还可扩展至其他领域，如金融欺诈检测和网络安全监控，具有重要的实际价值和影响力。

## 📄 摘要（原文）

> Enterprises are facing increasing risks of insider threats, while existing detection methods are unable to effectively address these challenges due to reasons such as insufficient temporal dynamic feature modeling, computational efficiency and real-time bottlenecks and cross-modal information island problem. This paper proposes a new insider threat detection framework MambaITD based on the Mamba state space model and cross-modal adaptive fusion. First, the multi-source log preprocessing module aligns heterogeneous data through behavioral sequence encoding, interval smoothing, and statistical feature extraction. Second, the Mamba encoder models long-range dependencies in behavioral and interval sequences, and combines the sequence and statistical information dynamically in combination with the gated feature fusion mechanism. Finally, we propose an adaptive threshold optimization method based on maximizing inter-class variance, which dynamically adjusts the decision threshold by analyzing the probability distribution, effectively identifies anomalies, and alleviates class imbalance and concept drift. Compared with traditional methods, MambaITD shows significant advantages in modeling efficiency and feature fusion capabilities, outperforming Transformer-based methods, and provides a more effective solution for insider threat detection.

