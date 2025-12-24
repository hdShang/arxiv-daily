---
layout: default
title: "T2I-R1: Reinforcing Image Generation with Collaborative Semantic-level and Token-level CoT"
---

# T2I-R1: Reinforcing Image Generation with Collaborative Semantic-level and Token-level CoT

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.00703" class="toolbar-btn" target="_blank">📄 arXiv: 2505.00703v2</a>
  <a href="https://arxiv.org/pdf/2505.00703.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.00703v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.00703v2', 'T2I-R1: Reinforcing Image Generation with Collaborative Semantic-level and Token-level CoT')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Dongzhi Jiang, Ziyu Guo, Renrui Zhang, Zhuofan Zong, Hao Li, Le Zhuo, Shilin Yan, Pheng-Ann Heng, Hongsheng Li

**分类**: cs.CV, cs.AI, cs.CL, cs.LG

**发布日期**: 2025-05-01 (更新: 2025-07-01)

**备注**: Project Page: https://github.com/CaraJ7/T2I-R1

**🔗 代码/项目**: [GITHUB](https://github.com/CaraJ7/T2I-R1)

---

## 💡 一句话要点

**提出T2I-R1以增强文本到图像生成的推理能力**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `文本到图像生成` `链式思维` `强化学习` `生成模型` `多层次推理` `图像处理` `深度学习`

## 📋 核心要点

1. 现有的文本到图像生成方法在推理能力上存在不足，未能充分利用链式思维和强化学习的优势。
2. 本文提出了T2I-R1模型，通过双层CoT推理过程，分别在高层次和低层次生成阶段进行优化。
3. 实验结果表明，T2I-R1在多个基准测试中表现优异，T2I-CompBench提升13%，WISE基准提升19%。

## 📝 摘要（中文）

近年来，大型语言模型的进展表明，链式思维（CoT）和强化学习（RL）能够提升性能。然而，将这些推理策略应用于视觉生成领域仍然未被充分探索。本文提出了T2I-R1，这是一种新颖的推理增强文本到图像生成模型，利用RL和双层CoT推理过程。具体而言，我们识别出两种CoT层次，分别用于生成的不同阶段：语义层CoT用于高层次的提示规划，令牌层CoT用于逐块生成过程中的低层次像素处理。为更好地协调这两层CoT，我们引入了BiCoT-GRPO，通过生成奖励的集成，在同一训练步骤中无缝优化两种生成CoT。通过将我们的推理策略应用于基线模型Janus-Pro，我们在T2I-CompBench上实现了13%的提升，在WISE基准上实现了19%的提升，甚至超越了当前最先进的模型FLUX。代码可在：https://github.com/CaraJ7/T2I-R1获取。

## 🔬 方法详解

**问题定义**：本文旨在解决现有文本到图像生成模型在推理能力上的不足，尤其是在复杂提示的处理和生成质量方面的挑战。现有方法未能有效结合推理策略与生成过程，导致生成结果的多样性和准确性不足。

**核心思路**：论文提出的T2I-R1模型通过引入双层链式思维（CoT）推理，分别在语义层和令牌层进行优化，从而提升生成过程的整体质量。语义层CoT负责高层次的提示规划，而令牌层CoT则专注于逐块生成的低层次像素处理。

**技术框架**：T2I-R1的整体架构包括两个主要模块：语义层CoT和令牌层CoT。语义层CoT用于生成初步的图像结构，而令牌层CoT则在此基础上进行细化，逐步生成高质量的图像。BiCoT-GRPO则作为优化模块，通过集成生成奖励来协调这两个层次的推理过程。

**关键创新**：T2I-R1的核心创新在于双层CoT推理的引入，以及BiCoT-GRPO的设计，使得两层推理能够在同一训练步骤中协同优化。这种设计与传统的单层推理方法有本质区别，能够更有效地处理复杂的生成任务。

**关键设计**：模型中采用了特定的损失函数来平衡语义层和令牌层的生成质量，同时在网络结构上进行了优化，以支持双层推理的高效执行。具体的参数设置和网络结构细节在论文中有详细描述。

## 📊 实验亮点

T2I-R1在多个基准测试中表现出色，T2I-CompBench上提升了13%，WISE基准上提升了19%。这些结果不仅超越了基线模型Janus-Pro，还超过了当前最先进的模型FLUX，展示了其在文本到图像生成领域的显著优势。

## 🎯 应用场景

T2I-R1模型在文本到图像生成领域具有广泛的应用潜力，能够用于艺术创作、广告设计、虚拟现实等多个场景。其增强的推理能力将推动生成模型在复杂场景下的表现，提升用户体验和生成质量。未来，该模型的技术也可能扩展到其他生成任务，如视频生成和多模态内容创作。

## 📄 摘要（原文）

> Recent advancements in large language models have demonstrated how chain-of-thought (CoT) and reinforcement learning (RL) can improve performance. However, applying such reasoning strategies to the visual generation domain remains largely unexplored. In this paper, we present T2I-R1, a novel reasoning-enhanced text-to-image generation model, powered by RL with a bi-level CoT reasoning process. Specifically, we identify two levels of CoT that can be utilized to enhance different stages of generation: (1) the semantic-level CoT for high-level planning of the prompt and (2) the token-level CoT for low-level pixel processing during patch-by-patch generation. To better coordinate these two levels of CoT, we introduce BiCoT-GRPO with an ensemble of generation rewards, which seamlessly optimizes both generation CoTs within the same training step. By applying our reasoning strategies to the baseline model, Janus-Pro, we achieve superior performance with 13% improvement on T2I-CompBench and 19% improvement on the WISE benchmark, even surpassing the state-of-the-art model FLUX.1. Code is available at: https://github.com/CaraJ7/T2I-R1

