---
layout: default
title: Scaling Instruction-Based Video Editing with a High-Quality Synthetic Dataset
---

# Scaling Instruction-Based Video Editing with a High-Quality Synthetic Dataset

<div class="paper-toolbar">
  <div class="toolbar-left">
    <a href="https://arxiv.org/abs/2510.15742" target="_blank" class="toolbar-btn">arXiv: 2510.15742v1</a>
    <a href="https://arxiv.org/pdf/2510.15742.pdf" target="_blank" class="toolbar-btn">PDF</a>
  </div>
  <div class="toolbar-right">
    <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.15742v1" 
            onclick="toggleFavorite(this, '2510.15742v1', 'Scaling Instruction-Based Video Editing with a High-Quality Synthetic Dataset')" title="收藏">
      ☆ 收藏
    </button>
    <button class="toolbar-btn share-btn" onclick="copyLink()" title="复制链接">
      🔗 分享
    </button>
  </div>
</div>


**作者**: Qingyan Bai, Qiuyu Wang, Hao Ouyang, Yue Yu, Hanlin Wang, Wen Wang, Ka Leong Cheng, Shuailei Ma, Yanhong Zeng, Zichen Liu, Yinghao Xu, Yujun Shen, Qifeng Chen

**分类**: cs.CV

**发布日期**: 2025-10-17

**备注**: Project page: https://ezioby.github.io/Ditto_page Code: https://github.com/EzioBy/Ditto

---

## 💡 一句话要点

**提出Ditto框架，通过高质量合成数据集Editto-1M，显著提升指令驱动的视频编辑能力。**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `指令驱动视频编辑` `合成数据生成` `数据增强` `课程学习` `智能代理`

## 📋 核心要点

1. 现有指令驱动视频编辑方法缺乏大规模高质量训练数据，限制了模型性能和泛化能力。
2. Ditto框架通过结合图像编辑器和视频生成器，以及智能代理驱动的数据生成和过滤，构建大规模高质量合成数据集。
3. 在Ditto-1M数据集上训练的Editto模型，在指令遵循能力上表现出色，达到了指令驱动视频编辑领域的新高度。

## 📝 摘要（中文）

指令驱动的视频编辑有望普及内容创作，但其发展受到大规模、高质量训练数据匮乏的严重阻碍。我们提出了Ditto，一个旨在解决这一根本挑战的整体框架。Ditto的核心是一个新颖的数据生成流程，它融合了领先图像编辑器的创造性多样性和上下文视频生成器，克服了现有模型的局限性。为了使这一过程可行，我们的框架通过采用高效的、经过蒸馏的模型架构，并辅以时间增强器，解决了高昂的成本-质量权衡问题，从而同时降低了计算开销并提高了时间一致性。最后，为了实现完全的可扩展性，整个流程由一个智能代理驱动，该代理生成多样化的指令并严格过滤输出，从而确保大规模的质量控制。利用该框架，我们投入了超过12,000个GPU-days来构建Ditto-1M，一个包含一百万个高保真视频编辑示例的新数据集。我们使用课程学习策略在Ditto-1M上训练了我们的模型Editto。结果表明，Editto具有卓越的指令遵循能力，并在指令驱动的视频编辑领域建立了新的最先进水平。

## 🔬 方法详解

**问题定义**：论文旨在解决指令驱动视频编辑任务中，缺乏大规模、高质量训练数据的问题。现有方法依赖于真实视频数据，但获取成本高昂且难以覆盖各种编辑指令。因此，模型训练受限，难以泛化到复杂场景。

**核心思路**：论文的核心思路是利用合成数据来弥补真实数据的不足。通过构建一个自动化的数据生成流程，可以低成本地生成大量高质量的视频编辑示例，从而有效训练指令驱动的视频编辑模型。关键在于如何保证合成数据的质量和多样性。

**技术框架**：Ditto框架包含三个主要模块：1) 数据生成流水线，融合图像编辑器和视频生成器，生成初始视频编辑结果；2) 时间增强器，用于提高视频的时间一致性；3) 智能代理，负责生成多样化的编辑指令，并对生成结果进行质量过滤。整个流程自动化运行，实现大规模数据生成。

**关键创新**：该论文的关键创新在于构建了一个可扩展的、高质量的合成数据生成框架。通过结合图像编辑器的创造性和视频生成器的时序性，以及智能代理的控制，实现了低成本、高质量的数据生成。此外，时间增强器的引入进一步提升了视频的真实感。

**关键设计**：数据生成流水线利用预训练的图像编辑器进行初始编辑，然后使用视频生成模型进行时序扩展。时间增强器可能采用光流或类似技术来平滑视频帧之间的过渡。智能代理使用强化学习或类似方法来学习生成多样化的编辑指令，并根据预定义的指标对生成结果进行质量评估和过滤。课程学习策略用于逐步提升模型的训练难度。

## 📊 实验亮点

论文构建了包含一百万个高保真视频编辑示例的Ditto-1M数据集，并在该数据集上训练了Editto模型。实验结果表明，Editto模型在指令遵循能力上显著优于现有方法，并在指令驱动的视频编辑任务上取得了新的state-of-the-art。具体性能数据和对比基线在论文中有详细展示。

## 🎯 应用场景

该研究成果可广泛应用于视频内容创作、自动化视频编辑、个性化视频生成等领域。例如，用户可以通过简单的指令快速修改视频内容，无需专业的视频编辑技能。此外，该技术还可以用于生成各种风格的视频内容，满足不同用户的需求。未来，该技术有望成为视频内容创作的重要工具。

## 📄 摘要（原文）

> Instruction-based video editing promises to democratize content creation, yet its progress is severely hampered by the scarcity of large-scale, high-quality training data. We introduce Ditto, a holistic framework designed to tackle this fundamental challenge. At its heart, Ditto features a novel data generation pipeline that fuses the creative diversity of a leading image editor with an in-context video generator, overcoming the limited scope of existing models. To make this process viable, our framework resolves the prohibitive cost-quality trade-off by employing an efficient, distilled model architecture augmented by a temporal enhancer, which simultaneously reduces computational overhead and improves temporal coherence. Finally, to achieve full scalability, this entire pipeline is driven by an intelligent agent that crafts diverse instructions and rigorously filters the output, ensuring quality control at scale. Using this framework, we invested over 12,000 GPU-days to build Ditto-1M, a new dataset of one million high-fidelity video editing examples. We trained our model, Editto, on Ditto-1M with a curriculum learning strategy. The results demonstrate superior instruction-following ability and establish a new state-of-the-art in instruction-based video editing.

