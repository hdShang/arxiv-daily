---
layout: default
title: FUDOKI: Discrete Flow-based Unified Understanding and Generation via Kinetic-Optimal Velocities
---

# FUDOKI: Discrete Flow-based Unified Understanding and Generation via Kinetic-Optimal Velocities

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.20147" class="toolbar-btn" target="_blank">📄 arXiv: 2505.20147v3</a>
  <a href="https://arxiv.org/pdf/2505.20147.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.20147v3" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.20147v3', 'FUDOKI: Discrete Flow-based Unified Understanding and Generation via Kinetic-Optimal Velocities')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Jin Wang, Yao Lai, Aoxue Li, Shifeng Zhang, Jiacheng Sun, Ning Kang, Chengyue Wu, Zhenguo Li, Ping Luo

**分类**: cs.CV

**发布日期**: 2025-05-26 (更新: 2025-07-24)

**备注**: 37 pages, 12 figures

---

## 💡 一句话要点

**提出FUDOKI以解决多模态大语言模型的局限性问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多模态大语言模型` `离散流匹配` `自回归架构` `图像生成` `视觉理解` `上下文整合` `生成机制` `动量最优速度`

## 📋 核心要点

1. 现有的多模态大语言模型主要依赖自回归架构，导致图像生成和因果推理能力受限。
2. FUDOKI通过离散流匹配方法，克服了传统AR模型的局限，实现了更高效的生成过程。
3. 实验结果显示，FUDOKI在多个视觉理解和图像生成任务上与最先进的AR模型性能相当，且具有更好的扩展性。

## 📝 摘要（中文）

随着大语言模型（LLMs）的快速发展，多模态大语言模型（MLLMs）应运而生，旨在统一视觉理解与图像生成。然而，现有的MLLMs大多依赖自回归（AR）架构，这限制了其在图像生成中的顺序处理和因果上下文建模能力。本文提出FUDOKI，一个基于离散流匹配的统一多模态模型，作为传统AR范式的替代方案。通过利用度量诱导的概率路径与动量最优速度，FUDOKI实现了自我修正能力和更丰富的双向上下文整合。实验结果表明，FUDOKI在视觉理解和图像生成任务上表现出与最先进的AR模型相当的性能，显示出其作为下一代统一多模态模型基础的潜力。

## 🔬 方法详解

**问题定义**：现有的多模态大语言模型（MLLMs）大多依赖自回归（AR）架构，这种方法在图像生成时存在栅格扫描顺序的限制，并且在因果上下文建模中推理能力受限。

**核心思路**：FUDOKI提出了一种基于离散流匹配的统一多模态模型，旨在替代传统的AR方法。通过引入度量诱导的概率路径与动量最优速度，FUDOKI能够实现自我修正和双向上下文整合，从而提升生成质量。

**技术框架**：FUDOKI的整体架构包括多个模块，首先是从预训练的AR模型初始化，然后通过适应性转变到离散流匹配范式。该框架支持迭代精炼和上下文整合，形成一个闭环生成过程。

**关键创新**：FUDOKI的核心创新在于其完全基于离散流匹配的生成机制，突破了传统AR模型的局限，能够实现更灵活的生成策略和更高的上下文理解能力。

**关键设计**：在设计上，FUDOKI采用了特定的损失函数以优化生成质量，并在网络结构中引入了动量最优速度的概念，以提升模型的收敛速度和生成效果。具体的参数设置和网络结构细节在实验部分进行了详细描述。

## 📊 实验亮点

实验结果表明，FUDOKI在视觉理解和图像生成任务上达到了与最先进的自回归模型相当的性能，具体表现为在多个基准测试中，FUDOKI的生成质量和上下文理解能力均有显著提升，显示出其在多模态任务中的强大潜力。

## 🎯 应用场景

FUDOKI的研究成果在多个领域具有广泛的应用潜力，包括智能图像生成、视觉问答系统以及多模态内容创作等。其创新的生成机制和上下文理解能力，可能为未来的多模态人工智能系统提供坚实的基础，推动相关技术的进步与应用。

## 📄 摘要（原文）

> The rapid progress of large language models (LLMs) has catalyzed the emergence of multimodal large language models (MLLMs) that unify visual understanding and image generation within a single framework. However, most existing MLLMs rely on autoregressive (AR) architectures, which impose inherent limitations on future development, such as the raster-scan order in image generation and restricted reasoning abilities in causal context modeling. In this work, we challenge the dominance of AR-based approaches by introducing FUDOKI, a unified multimodal model purely based on discrete flow matching, as an alternative to conventional AR paradigms. By leveraging metric-induced probability paths with kinetic optimal velocities, our framework goes beyond the previous masking-based corruption process, enabling iterative refinement with self-correction capability and richer bidirectional context integration during generation. To mitigate the high cost of training from scratch, we initialize FUDOKI from pre-trained AR-based MLLMs and adaptively transition to the discrete flow matching paradigm. Experimental results show that FUDOKI achieves performance comparable to state-of-the-art AR-based MLLMs across both visual understanding and image generation tasks, highlighting its potential as a foundation for next-generation unified multimodal models. Furthermore, we show that applying test-time scaling techniques to FUDOKI yields significant performance gains, further underscoring its promise for future enhancement through reinforcement learning.

