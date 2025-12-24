---
layout: default
title: From Local Cues to Global Percepts: Emergent Gestalt Organization in Self-Supervised Vision Models
---

# From Local Cues to Global Percepts: Emergent Gestalt Organization in Self-Supervised Vision Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.00718" class="toolbar-btn" target="_blank">📄 arXiv: 2506.00718v1</a>
  <a href="https://arxiv.org/pdf/2506.00718.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.00718v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.00718v1', 'From Local Cues to Global Percepts: Emergent Gestalt Organization in Self-Supervised Vision Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Tianqin Li, Ziqi Wen, Leiran Song, Jun Liu, Zhi Jing, Tai Sing Lee

**分类**: cs.CV, cs.AI

**发布日期**: 2025-05-31

---

## 💡 一句话要点

**提出DiSRT以评估自监督视觉模型的整体感知能力**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱七：动作重定向 (Motion Retargeting)**

**关键词**: `自监督学习` `视觉变换器` `格式塔原则` `整体感知` `扭曲空间关系测试`

## 📋 核心要点

1. 现有视觉模型在处理局部线索时，缺乏有效的整体感知能力，难以模拟人类视觉的格式塔组织特性。
2. 论文提出了扭曲空间关系测试平台（DiSRT），用于评估视觉模型对全球空间结构的敏感性，探索自监督学习的潜力。
3. 实验结果显示，自监督模型（如MAE、CLIP）在整体感知能力上优于监督基线，且ConvNeXt模型在特定条件下也表现出类似能力。

## 📝 摘要（中文）

人类视觉通过格式塔原则将局部线索组织成一致的整体形式。本文研究现代视觉模型是否表现出类似行为，以及在何种训练条件下这些行为会出现。研究发现，使用掩蔽自编码（MAE）训练的视觉变换器（ViTs）展现出与格式塔法则一致的激活模式，包括虚幻轮廓完成、凸性偏好和动态图形-背景分离。通过引入扭曲空间关系测试平台（DiSRT），评估模型对全球空间扰动的敏感性，结果表明自监督模型在性能上超越了监督基线，甚至有时超过了人类表现。ConvNeXt模型在MAE训练下也展现出兼容格式塔的表示，表明这种敏感性可以在没有注意力架构的情况下出现。

## 🔬 方法详解

**问题定义**：本文旨在探讨现代视觉模型是否能够像人类一样，通过局部线索形成整体感知，现有方法在这一点上存在不足，尤其是在处理全球空间结构时。

**核心思路**：通过引入扭曲空间关系测试平台（DiSRT），评估模型对全球空间扰动的敏感性，进而分析自监督模型在整体感知中的表现。

**技术框架**：研究首先训练视觉变换器（ViTs）和ConvNeXt模型，使用掩蔽自编码（MAE）进行自监督学习，然后通过DiSRT进行评估，比较不同模型的表现。

**关键创新**：引入DiSRT作为一种新颖的评估工具，能够有效测量模型对全球空间结构的敏感性，并发现自监督模型在这一方面的优势。

**关键设计**：在模型训练中，采用掩蔽自编码技术，并通过调整激活稀疏性机制，恢复模型的全球敏感性，确保在分类微调过程中不会显著降低整体感知能力。

## 📊 实验亮点

实验结果表明，自监督模型（如MAE、CLIP）在DiSRT测试中表现优于监督基线，且在某些情况下超越了人类表现。ConvNeXt模型在MAE训练下也展现出兼容格式塔的表示，显示出自监督学习的巨大潜力。

## 🎯 应用场景

该研究的潜在应用领域包括计算机视觉、机器人感知和自动驾驶等。通过提升视觉模型的整体感知能力，可以改善这些领域中的对象识别、场景理解和决策制定等任务的性能，具有重要的实际价值和未来影响。

## 📄 摘要（原文）

> Human vision organizes local cues into coherent global forms using Gestalt principles like closure, proximity, and figure-ground assignment -- functions reliant on global spatial structure. We investigate whether modern vision models show similar behaviors, and under what training conditions these emerge. We find that Vision Transformers (ViTs) trained with Masked Autoencoding (MAE) exhibit activation patterns consistent with Gestalt laws, including illusory contour completion, convexity preference, and dynamic figure-ground segregation. To probe the computational basis, we hypothesize that modeling global dependencies is necessary for Gestalt-like organization. We introduce the Distorted Spatial Relationship Testbench (DiSRT), which evaluates sensitivity to global spatial perturbations while preserving local textures. Using DiSRT, we show that self-supervised models (e.g., MAE, CLIP) outperform supervised baselines and sometimes even exceed human performance. ConvNeXt models trained with MAE also exhibit Gestalt-compatible representations, suggesting such sensitivity can arise without attention architectures. However, classification finetuning degrades this ability. Inspired by biological vision, we show that a Top-K activation sparsity mechanism can restore global sensitivity. Our findings identify training conditions that promote or suppress Gestalt-like perception and establish DiSRT as a diagnostic for global structure sensitivity across models.

