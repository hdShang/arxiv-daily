---
layout: default
title: "Align Your Flow: Scaling Continuous-Time Flow Map Distillation"
---

# Align Your Flow: Scaling Continuous-Time Flow Map Distillation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.14603" class="toolbar-btn" target="_blank">📄 arXiv: 2506.14603v1</a>
  <a href="https://arxiv.org/pdf/2506.14603.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.14603v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.14603v1', 'Align Your Flow: Scaling Continuous-Time Flow Map Distillation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Amirmojtaba Sabour, Sanja Fidler, Karsten Kreis

**分类**: cs.CV, cs.LG

**发布日期**: 2025-06-17

**备注**: Project page: https://research.nvidia.com/labs/toronto-ai/AlignYourFlow/

---

## 💡 一句话要点

**提出连续时间流图蒸馏方法以提升生成模型效率**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `生成模型` `流图` `蒸馏训练` `图像生成` `自引导` `对抗微调`

## 📋 核心要点

1. 现有的扩散和流基模型在生成过程中需要多个采样步骤，导致效率低下，且一致性模型在增加步骤时性能下降。
2. 本文提出了新的连续时间目标和训练技术，旨在通过流图连接不同噪声水平，从而提升生成模型的效率和性能。
3. 在多个图像生成基准上，Align Your Flow模型展示了在少步生成方面的优越性能，尤其在小型高效神经网络上表现突出。

## 📝 摘要（中文）

扩散和流基模型已成为最先进的生成建模方法，但需要多个采样步骤。尽管一致性模型可以将这些模型蒸馏为高效的一步生成器，但其性能在增加步骤时不可避免地下降。流图通过在单步中连接任意两个噪声水平来推广这些方法，并在所有步骤计数中保持有效。本文提出了两种新的连续时间目标用于训练流图，并展示了自引导和对抗微调对性能的提升。我们在图像生成基准上验证了所提出的流图模型，称为Align Your Flow，并在ImageNet 64x64和512x512上实现了最先进的少步生成性能。

## 🔬 方法详解

**问题定义**：本文旨在解决现有生成模型在多个采样步骤下效率低下的问题，尤其是一致性模型在增加步骤时性能下降的痛点。

**核心思路**：通过引入连续时间目标，流图能够在单步中连接不同噪声水平，从而保持在所有步骤计数下的有效性，提升生成效率。

**技术框架**：整体架构包括流图的训练过程，采用新的连续时间目标和训练技术，结合自引导和对抗微调，形成一个高效的生成模型。

**关键创新**：最重要的创新在于提出了新的连续时间目标和训练方法，能够有效地将流图与一致性模型和流匹配目标相结合，显著提升生成性能。

**关键设计**：在训练过程中，采用了低质量模型进行自引导，并通过对抗微调来进一步提升性能，确保样本多样性损失最小化。具体的损失函数和网络结构设计在论文中详细描述。

## 📊 实验亮点

在ImageNet 64x64和512x512的图像生成基准上，Align Your Flow模型实现了最先进的少步生成性能，超越了所有现有的非对抗训练的少步采样器，展示了显著的性能提升。

## 🎯 应用场景

该研究的潜在应用领域包括图像生成、文本到图像合成等，能够为艺术创作、虚拟现实和游戏开发等行业提供高效的生成工具。未来，随着技术的进一步发展，可能会在更多生成任务中发挥重要作用。

## 📄 摘要（原文）

> Diffusion- and flow-based models have emerged as state-of-the-art generative modeling approaches, but they require many sampling steps. Consistency models can distill these models into efficient one-step generators; however, unlike flow- and diffusion-based methods, their performance inevitably degrades when increasing the number of steps, which we show both analytically and empirically. Flow maps generalize these approaches by connecting any two noise levels in a single step and remain effective across all step counts. In this paper, we introduce two new continuous-time objectives for training flow maps, along with additional novel training techniques, generalizing existing consistency and flow matching objectives. We further demonstrate that autoguidance can improve performance, using a low-quality model for guidance during distillation, and an additional boost can be achieved by adversarial finetuning, with minimal loss in sample diversity. We extensively validate our flow map models, called Align Your Flow, on challenging image generation benchmarks and achieve state-of-the-art few-step generation performance on both ImageNet 64x64 and 512x512, using small and efficient neural networks. Finally, we show text-to-image flow map models that outperform all existing non-adversarially trained few-step samplers in text-conditioned synthesis.

