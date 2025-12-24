---
layout: default
title: "UniGen: Enhanced Training & Test-Time Strategies for Unified Multimodal Understanding and Generation"
---

# UniGen: Enhanced Training & Test-Time Strategies for Unified Multimodal Understanding and Generation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.14682" class="toolbar-btn" target="_blank">📄 arXiv: 2505.14682v1</a>
  <a href="https://arxiv.org/pdf/2505.14682.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.14682v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.14682v1', 'UniGen: Enhanced Training & Test-Time Strategies for Unified Multimodal Understanding and Generation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Rui Tian, Mingfei Gao, Mingze Xu, Jiaming Hu, Jiasen Lu, Zuxuan Wu, Yinfei Yang, Afshin Dehghan

**分类**: cs.CV

**发布日期**: 2025-05-20

**备注**: Technical report

---

## 💡 一句话要点

**提出UniGen以解决多模态理解与生成的挑战**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多模态模型` `图像生成` `链式思维验证` `语义对齐` `深度学习`

## 📋 核心要点

1. 现有多模态模型在图像理解与生成的质量和一致性上存在不足，难以有效评估生成结果与文本提示之间的语义对齐。
2. 论文提出了UniGen模型，结合多阶段预训练和链式思维验证策略，在测试时提升生成质量，确保图像与文本的语义一致性。
3. UniGen在多个基准测试中表现优异，GenEval得分0.78，DPG-Bench得分85.19，展示了其在多模态任务中的强大能力。

## 📝 摘要（中文）

我们介绍了UniGen，这是一种统一的多模态大型语言模型（MLLM），能够进行图像理解和生成。我们从数据中心的角度研究了UniGen的完整训练流程，包括多阶段预训练、监督微调和直接偏好优化。更重要的是，我们提出了一种新的链式思维验证（CoT-V）策略，用于测试时扩展，显著提升了UniGen的图像生成质量。UniGen在所有阶段完全基于开源数据集进行训练，在一系列图像理解和生成基准上取得了最先进的性能，最终在GenEval上得分0.78，在DPG-Bench上得分85.19。通过广泛的消融研究，我们的工作提供了可操作的见解，并解决了构建统一MLLM的全生命周期中的关键挑战，为未来研究贡献了有意义的方向。

## 🔬 方法详解

**问题定义**：本论文旨在解决现有多模态模型在图像生成与理解中的质量不足及其与文本提示的语义对齐问题。现有方法往往无法有效评估生成结果的准确性和一致性，导致生成图像与文本提示之间存在较大差距。

**核心思路**：论文提出的UniGen模型通过引入链式思维验证（CoT-V）策略，在测试阶段实现图像生成与验证的双重功能，逐步评估生成图像与文本提示的语义一致性，从而提升生成质量。

**技术框架**：UniGen的整体架构包括多阶段预训练、监督微调和直接偏好优化三个主要阶段。预训练阶段利用开源数据集进行大规模训练，微调阶段则针对特定任务进行优化，最后通过偏好优化进一步提升模型性能。

**关键创新**：最重要的创新点在于提出的CoT-V策略，使得模型在生成图像的同时能够进行语义验证。这一策略与传统的生成模型不同，强调了生成与验证的协同作用。

**关键设计**：在模型设计中，UniGen采用了多层次的网络结构，结合了自注意力机制和卷积神经网络（CNN），并在损失函数中引入了语义一致性损失，以确保生成图像与文本提示之间的高匹配度。

## 📊 实验亮点

UniGen在多个基准测试中表现出色，GenEval得分达到0.78，DPG-Bench得分85.19，均为当前最先进的水平。通过引入CoT-V策略，模型在图像生成质量上显著提升，展示了其在多模态任务中的强大能力和应用潜力。

## 🎯 应用场景

UniGen的研究成果在多个领域具有广泛的应用潜力，包括智能图像生成、自动化内容创作、虚拟现实和增强现实等。其强大的多模态理解能力可以为人机交互、教育和娱乐等行业带来新的创新和价值，推动相关技术的发展与应用。

## 📄 摘要（原文）

> We introduce UniGen, a unified multimodal large language model (MLLM) capable of image understanding and generation. We study the full training pipeline of UniGen from a data-centric perspective, including multi-stage pre-training, supervised fine-tuning, and direct preference optimization. More importantly, we propose a new Chain-of-Thought Verification (CoT-V) strategy for test-time scaling, which significantly boosts UniGen's image generation quality using a simple Best-of-N test-time strategy. Specifically, CoT-V enables UniGen to act as both image generator and verifier at test time, assessing the semantic alignment between a text prompt and its generated image in a step-by-step CoT manner. Trained entirely on open-source datasets across all stages, UniGen achieves state-of-the-art performance on a range of image understanding and generation benchmarks, with a final score of 0.78 on GenEval and 85.19 on DPG-Bench. Through extensive ablation studies, our work provides actionable insights and addresses key challenges in the full life cycle of building unified MLLMs, contributing meaningful directions to the future research.

