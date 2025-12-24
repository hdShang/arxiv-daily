---
layout: default
title: "CLONE: Customizing LLMs for Efficient Latency-Aware Inference at the Edge"
---

# CLONE: Customizing LLMs for Efficient Latency-Aware Inference at the Edge

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.02847" class="toolbar-btn" target="_blank">📄 arXiv: 2506.02847v1</a>
  <a href="https://arxiv.org/pdf/2506.02847.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.02847v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.02847v1', 'CLONE: Customizing LLMs for Efficient Latency-Aware Inference at the Edge')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Chunlin Tian, Xinpeng Qin, Kahou Tam, Li Li, Zijian Wang, Yuanzhe Zhao, Minglei Zhang, Chengzhong Xu

**分类**: cs.AR, eess.SY

**发布日期**: 2025-06-03

**备注**: Accepted by USENIX ATC 2025

---

## 💡 一句话要点

**提出CLONE以解决边缘设备上LLM推理延迟与能耗问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `边缘计算` `大型语言模型` `算法硬件协同` `能量优化` `实时推理`

## 📋 核心要点

1. 边缘设备在存储、功耗和重量上存在限制，导致LLM应用部署面临延迟与能耗的平衡挑战。
2. CLONE通过算法与硬件的协同设计，优化了LLM在边缘设备上的实时推理性能与能效。
3. 实验结果显示，CLONE在两个边缘平台上实现了推理加速11.92倍，能耗降低7.36倍，且生成质量保持高水平。

## 📝 摘要（中文）

在边缘设备上部署大型语言模型（LLMs）对于快速响应和数据隐私至关重要。然而，边缘设备的存储、重量和功耗限制使得LLM应用的部署面临挑战。本文首先量化了在现有边缘设备上部署LLM的困难，并提出了CLONE，这是一种在模型和系统层面进行深入算法-硬件协同设计的方法，智能整合实时能量优化，同时保持强大的通用性。为了最大化这些算法在始终在线和中间边缘计算环境中的协同效益，我们专注于28nm可扩展硬件加速器系统。我们在两个现成的边缘平台上实现并广泛评估了CLONE，实验结果表明，CLONE有效加速推理过程达11.92倍，同时节能达7.36倍，并保持高生成质量。

## 🔬 方法详解

**问题定义**：本文旨在解决在边缘设备上部署大型语言模型（LLMs）时面临的延迟和能耗问题。现有方法在资源受限的环境中难以实现高效推理，导致响应时间延长和能量消耗增加。

**核心思路**：CLONE的核心思路是通过算法与硬件的深度协同设计，结合实时能量优化策略，确保在保证推理精度的同时，显著降低延迟和能耗。

**技术框架**：CLONE的整体架构包括模型优化模块和硬件加速模块。模型优化模块负责调整LLM的结构和参数以适应边缘设备的特性，而硬件加速模块则利用28nm技术实现高效的计算能力。

**关键创新**：CLONE的主要创新在于其算法与硬件的联合设计，能够在边缘计算环境中实现实时推理和能量优化的最佳平衡，这与传统的单一优化方法有本质区别。

**关键设计**：在设计中，CLONE采用了特定的损失函数和网络结构，以适应边缘设备的计算能力，并通过动态调整模型参数来实现能效的最大化。

## 📊 实验亮点

实验结果表明，CLONE在两个边缘平台上实现了推理速度提升至11.92倍，能耗降低至7.36倍，显著优于现有基线方法，展示了其在边缘计算中的有效性和潜力。

## 🎯 应用场景

CLONE的研究成果可广泛应用于智能手机、物联网设备和边缘计算平台等领域，能够提升这些设备上LLM应用的响应速度和能效，具有重要的实际价值和未来影响。

## 📄 摘要（原文）

> Deploying large language models (LLMs) on edge devices is crucial for delivering fast responses and ensuring data privacy. However, the limited storage, weight, and power of edge devices make it difficult to deploy LLM-powered applications. These devices must balance latency requirements with energy consumption and model accuracy. In this paper, we first quantify the challenges of deploying LLMs on off-the-shelf edge devices and then we present CLONE, an in-depth algorithm-hardware co-design at both the model- and system-level that intelligently integrates real-time, energy optimization while maintaining robust generality. In order to maximize the synergistic benefits of these algorithms in always-on and intermediate edge computing settings, we specialize in a 28nm scalable hardware accelerator system. We implement and extensively evaluate CLONE on two off-the-shelf edge platforms. Experiments show that CLONE effectively accelerates the inference process up to 11.92x, and saves energy up to 7.36x, while maintaining high-generation.

