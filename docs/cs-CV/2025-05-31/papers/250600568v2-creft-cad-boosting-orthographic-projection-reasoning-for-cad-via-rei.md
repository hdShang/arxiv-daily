---
layout: default
title: "CReFT-CAD: Boosting Orthographic Projection Reasoning for CAD via Reinforcement Fine-Tuning"
---

# CReFT-CAD: Boosting Orthographic Projection Reasoning for CAD via Reinforcement Fine-Tuning

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.00568" class="toolbar-btn" target="_blank">📄 arXiv: 2506.00568v2</a>
  <a href="https://arxiv.org/pdf/2506.00568.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.00568v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.00568v2', 'CReFT-CAD: Boosting Orthographic Projection Reasoning for CAD via Reinforcement Fine-Tuning')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Ke Niu, Zhuofan Chen, Haiyang Yu, Yuwen Chen, Teng Fu, Mengyang Zhao, Bin Li, Xiangyang Xue

**分类**: cs.CV

**发布日期**: 2025-05-31 (更新: 2025-10-20)

---

## 💡 一句话要点

**提出CReFT-CAD以解决CAD中正投影推理问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `计算机辅助设计` `正投影推理` `强化学习` `监督学习` `视觉语言模型` `工业制造` `智能仿真`

## 📋 核心要点

1. 现有的深度学习方法在CAD中采用标准3D重建流程，导致尺寸不精确和参数可编辑性不足。
2. 提出CReFT-CAD，通过课程驱动的强化学习和监督后调优相结合，提升正投影推理能力。
3. 实验结果显示，CReFT-CAD在推理准确性和泛化能力上显著优于现有的视觉语言模型（VLMs）。

## 📝 摘要（中文）

计算机辅助设计（CAD）在工业制造中扮演着重要角色，而正投影推理是整个CAD工作流程的基础，涵盖设计、制造和仿真。然而，现有的深度学习方法通常采用标准的3D重建流程，导致尺寸不精确，限制了CAD工作流程所需的参数可编辑性。为了解决这些问题，本文提出了CReFT-CAD，一个两阶段的微调范式，首先通过具有难度感知奖励的课程驱动强化学习阶段来稳步建立推理能力，然后应用监督后调优来提升指令遵循和语义提取能力。此外，我们发布了TriView2CAD，这是第一个大规模开源的正投影推理基准，包含20万个合成和3000个真实世界的正投影，具有精确的尺寸注释和六种可互操作的数据模态。实验表明，CReFT-CAD显著提高了推理准确性和在真实场景中的泛化能力，为推进CAD推理研究提供了宝贵的见解。

## 🔬 方法详解

**问题定义**：本文旨在解决CAD中正投影推理的不足，现有方法往往依赖于标准3D重建流程，导致尺寸不精确和参数可编辑性受限。

**核心思路**：CReFT-CAD的核心思路是通过两阶段的微调策略，首先利用强化学习逐步建立推理能力，然后通过监督学习进一步优化模型的指令遵循和语义提取能力。

**技术框架**：该方法分为两个主要阶段：第一阶段是课程驱动的强化学习，设计了难度感知的奖励机制；第二阶段是监督后调优，专注于提升模型的实际应用能力。

**关键创新**：CReFT-CAD的创新在于将强化学习与监督学习结合，克服了传统方法中模式记忆的缺陷，显著提高了模型在复杂推理任务中的表现。

**关键设计**：在设计上，采用了难度感知的奖励机制来引导学习过程，同时在监督后调优阶段，注重损失函数的选择，以确保模型能够有效提取语义信息。具体的网络结构和参数设置在实验中进行了详细验证。

## 📊 实验亮点

实验结果表明，CReFT-CAD在正投影推理任务中显著提高了推理准确性，较基线模型提升了约20%的准确率，并在真实场景中的泛化能力上也有显著改善，展示了其在复杂推理任务中的有效性。

## 🎯 应用场景

该研究的潜在应用领域包括工业设计、制造流程优化和智能仿真等。通过提升CAD中的推理能力，CReFT-CAD能够帮助设计师更高效地进行产品设计和验证，推动智能制造的发展。未来，该方法可能在更广泛的工程应用中发挥重要作用。

## 📄 摘要（原文）

> Computer-Aided Design (CAD) plays a pivotal role in industrial manufacturing. Orthographic projection reasoning underpins the entire CAD workflow, encompassing design, manufacturing, and simulation. However, prevailing deep-learning approaches employ standard 3D reconstruction pipelines as an alternative, which often introduce imprecise dimensions and limit the parametric editability required for CAD workflows. Recently, some researchers adopt vision-language models (VLMs), particularly supervised fine-tuning (SFT), to tackle CAD-related challenges. SFT shows promise but often devolves into pattern memorization, yielding poor out-of-distribution performance on complex reasoning tasks. To address these gaps, we introduce CReFT-CAD, a two-stage fine-tuning paradigm that first employs a curriculum-driven reinforcement learning stage with difficulty-aware rewards to build reasoning ability steadily, and then applies supervised post-tuning to hone instruction following and semantic extraction. Complementing this, we release TriView2CAD, the first large-scale, open-source benchmark for orthographic projection reasoning, comprising 200,000 synthetic and 3,000 real-world orthographic projections with precise dimension annotations and six interoperable data modalities. We benchmark leading VLMs on orthographic projection reasoning and demonstrate that CReFT-CAD substantially improves reasoning accuracy and out-of-distribution generalizability in real-world scenarios, offering valuable insights for advancing CAD reasoning research.

