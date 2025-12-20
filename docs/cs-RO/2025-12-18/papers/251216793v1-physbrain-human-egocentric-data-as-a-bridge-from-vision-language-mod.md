---
layout: default
title: PhysBrain: Human Egocentric Data as a Bridge from Vision Language Models to Physical Intelligence
---

# PhysBrain: Human Egocentric Data as a Bridge from Vision Language Models to Physical Intelligence

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.16793" class="toolbar-btn" target="_blank">📄 arXiv: 2512.16793v1</a>
  <a href="https://arxiv.org/pdf/2512.16793.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.16793v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.16793v1', 'PhysBrain: Human Egocentric Data as a Bridge from Vision Language Models to Physical Intelligence')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Xiaopeng Lin, Shijie Lian, Bin Yu, Ruoqi Yang, Changti Wu, Yuzhuo Miao, Yurun Jin, Yukun Shi, Cong Huang, Bojun Cheng, Kai Chen

**分类**: cs.RO

**发布日期**: 2025-12-18

**备注**: 17 pages, 4 figures

---

## 💡 一句话要点

**提出PhysBrain以解决机器人视觉语言模型与物理智能的匹配问题**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱六：视频提取与匹配 (Video Extraction)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `自我中心感知` `物理智能` `视觉语言模型` `机器人控制` `数据集构建` `多层次监督` `因果结构` `长远规划`

## 📋 核心要点

1. 现有的视觉语言模型主要依赖第三人称数据，导致机器人在自我中心感知下的泛化能力不足。
2. 提出了Egocentric2Embodiment翻译管道，将第一人称视频转化为结构化的多层次监督，构建了大规模E2E-3M数据集。
3. PhysBrain在E2E-3M数据集上训练后，展现出更强的自我中心理解能力，VLA微调的样本效率显著提高，成功率达到53.9%。

## 📝 摘要（中文）

机器人泛化依赖于物理智能，即在自我中心感知和行动下推理状态变化、接触丰富的交互和长远规划的能力。然而，大多数视觉语言模型主要在第三人称数据上训练，导致人形机器人面临视角不匹配的问题。收集机器人自我中心数据的规模化仍然不切实际，而大规模的人类自我中心视频提供了一种可扩展的替代方案。本文提出了Egocentric2Embodiment翻译管道，将第一人称视频转化为多层次、基于模式的视觉问答监督，构建了Egocentric2Embodiment数据集（E2E-3M）。通过在该数据集上训练，获得了一个自我中心感知的具身智能体PhysBrain，展现出显著的自我中心理解能力，尤其在EgoThink规划任务中表现优异。

## 🔬 方法详解

**问题定义**：本文旨在解决机器人在自我中心感知下的物理智能不足，现有方法主要依赖第三人称数据，导致视角不匹配和泛化能力不足。

**核心思路**：提出Egocentric2Embodiment翻译管道，将人类自我中心视频转化为结构化的训练监督，利用丰富的交互上下文和因果结构来提升机器人的理解能力。

**技术框架**：整体架构包括数据收集、视频处理、监督生成和模型训练四个主要模块。首先收集人类自我中心视频，然后通过翻译管道生成多层次的视觉问答监督，最后在E2E-3M数据集上训练PhysBrain。

**关键创新**：最重要的创新在于将原始自我中心视频转化为结构化的训练监督，确保了证据的基础和时间一致性，这在现有方法中是缺乏的。

**关键设计**：在翻译管道中，采用了多层次的模式驱动方法，设计了特定的损失函数以确保生成的监督具有高质量和一致性，同时优化了网络结构以适应自我中心数据的特性。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.16793v1/x1.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.16793v1/fig/data_pipeline.jpg" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.16793v1/fig/data_sum.jpg" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

在E2E-3M数据集上训练的PhysBrain展现出显著的自我中心理解能力，尤其在EgoThink任务中表现优异，成功率达到53.9%。与传统方法相比，PhysBrain在样本效率和任务成功率上均有显著提升，展示了从人类自我中心监督到机器人控制的有效转移。

## 🎯 应用场景

该研究的潜在应用领域包括机器人控制、智能家居系统和人机交互等。通过提升机器人在自我中心感知下的理解能力，PhysBrain能够更好地执行复杂的任务，增强机器人在现实环境中的适应性和灵活性，未来可能对智能机器人技术的发展产生深远影响。

## 📄 摘要（原文）

> Robotic generalization relies on physical intelligence: the ability to reason about state changes, contact-rich interactions, and long-horizon planning under egocentric perception and action. However, most VLMs are trained primarily on third-person data, creating a fundamental viewpoint mismatch for humanoid robots. Scaling robot egocentric data collection remains impractical due to high cost and limited diversity, whereas large-scale human egocentric videos offer a scalable alternative that naturally capture rich interaction context and causal structure. The key challenge is to convert raw egocentric videos into structured and reliable embodiment training supervision. Accordingly, we propose an Egocentric2Embodiment translation pipeline that transforms first-person videos into multi-level, schema-driven VQA supervision with enforced evidence grounding and temporal consistency, enabling the construction of the Egocentric2Embodiment dataset (E2E-3M) at scale. An egocentric-aware embodied brain, termed PhysBrain, is obtained by training on the E2E-3M dataset. PhysBrain exhibits substantially improved egocentric understanding, particularly for planning on EgoThink. It provides an egocentric-aware initialization that enables more sample-efficient VLA fine-tuning and higher SimplerEnv success rates (53.9\%), demonstrating effective transfer from human egocentric supervision to downstream robot control.

