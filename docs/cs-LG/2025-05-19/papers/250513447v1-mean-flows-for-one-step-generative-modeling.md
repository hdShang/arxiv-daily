---
layout: default
title: Mean Flows for One-step Generative Modeling
---

# Mean Flows for One-step Generative Modeling

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.13447" class="toolbar-btn" target="_blank">📄 arXiv: 2505.13447v1</a>
  <a href="https://arxiv.org/pdf/2505.13447.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.13447v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.13447v1', 'Mean Flows for One-step Generative Modeling')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Zhengyang Geng, Mingyang Deng, Xingjian Bai, J. Zico Kolter, Kaiming He

**分类**: cs.LG, cs.CV

**发布日期**: 2025-05-19

**备注**: Tech report

---

## 💡 一句话要点

**提出MeanFlow模型以解决一阶段生成建模问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `生成建模` `流场建模` `平均速度` `神经网络` `图像生成` `深度学习` `性能提升`

## 📋 核心要点

1. 现有的一阶段生成建模方法在性能上存在不足，尤其是在生成质量和训练效率方面。
2. 论文提出的MeanFlow模型通过引入平均速度来表征流场，避免了瞬时速度的局限性，且无需复杂的预训练过程。
3. 实验结果显示MeanFlow在ImageNet数据集上达到了3.43的FID，显著优于现有的一阶段生成模型，展示了其强大的生成能力。

## 📝 摘要（中文）

我们提出了一种原则性和有效的一阶段生成建模框架。我们引入了平均速度的概念来表征流场，这与流匹配方法中建模的瞬时速度形成对比。我们推导出平均速度与瞬时速度之间的明确关系，并利用这一关系指导神经网络的训练。我们的模型称为MeanFlow，具有自包含性，无需预训练、蒸馏或课程学习。MeanFlow在ImageNet 256x256上从零开始训练时，单次函数评估（1-NFE）取得了3.43的FID，显著超越了之前的一阶段扩散/流模型。我们的研究大大缩小了一阶段扩散/流模型与多阶段前身之间的差距，期望能激励未来研究重新审视这些强大模型的基础。

## 🔬 方法详解

**问题定义**：本论文旨在解决一阶段生成建模中的性能瓶颈，现有方法多依赖瞬时速度，导致生成质量不理想和训练效率低下。

**核心思路**：论文的核心思路是引入平均速度来表征流场，通过建立平均速度与瞬时速度之间的关系，优化神经网络的训练过程，从而提升生成效果。

**技术框架**：整体架构包括数据输入、平均速度计算、神经网络训练和生成输出四个主要模块。首先计算输入数据的平均速度，然后利用该信息指导网络的训练，最后生成高质量的样本。

**关键创新**：最重要的技术创新在于提出了平均速度的概念，并通过明确的数学关系将其与瞬时速度联系起来，从而为生成建模提供了新的视角和方法。

**关键设计**：在模型设计中，采用了特定的损失函数来优化平均速度的计算，并设计了适合一阶段生成的网络结构，确保了训练过程的高效性和生成结果的质量。

## 📊 实验亮点

实验结果表明，MeanFlow模型在ImageNet 256x256数据集上实现了3.43的FID，且仅需一次函数评估（1-NFE），显著优于之前的一阶段扩散/流模型，展示了其在生成建模领域的强大性能。

## 🎯 应用场景

该研究的潜在应用领域包括图像生成、视频合成和虚拟现实等。MeanFlow模型的高效性和生成质量使其在实际应用中具有重要价值，能够推动相关领域的发展，尤其是在需要快速生成高质量内容的场景中。

## 📄 摘要（原文）

> We propose a principled and effective framework for one-step generative modeling. We introduce the notion of average velocity to characterize flow fields, in contrast to instantaneous velocity modeled by Flow Matching methods. A well-defined identity between average and instantaneous velocities is derived and used to guide neural network training. Our method, termed the MeanFlow model, is self-contained and requires no pre-training, distillation, or curriculum learning. MeanFlow demonstrates strong empirical performance: it achieves an FID of 3.43 with a single function evaluation (1-NFE) on ImageNet 256x256 trained from scratch, significantly outperforming previous state-of-the-art one-step diffusion/flow models. Our study substantially narrows the gap between one-step diffusion/flow models and their multi-step predecessors, and we hope it will motivate future research to revisit the foundations of these powerful models.

