---
layout: default
title: Few-Step Diffusion via Score identity Distillation
---

# Few-Step Diffusion via Score identity Distillation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.12674" class="toolbar-btn" target="_blank">📄 arXiv: 2505.12674v1</a>
  <a href="https://arxiv.org/pdf/2505.12674.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.12674v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.12674v1', 'Few-Step Diffusion via Score identity Distillation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Mingyuan Zhou, Yi Gu, Zhendong Wang

**分类**: cs.CV, cs.LG, stat.ML

**发布日期**: 2025-05-19

**🔗 代码/项目**: [GITHUB](https://github.com/mingyuanzhou/SiD-LSG)

---

## 💡 一句话要点

**提出Score identity Distillation以解决高分辨率图像生成问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱四：生成式动作 (Generative Motion)**

**关键词**: `扩散蒸馏` `图像生成` `无监督学习` `对抗损失` `多样性与对齐性`

## 📋 核心要点

1. 现有的扩散蒸馏方法在高分辨率图像生成中依赖真实或合成图像，且存在对齐与多样性之间的权衡问题。
2. 本文提出了一种数据无关的一步蒸馏框架Score identity Distillation（SiD），旨在优化少步生成过程。
3. 实验结果显示，SiD在SD1.5和SDXL上均实现了最先进的性能，且在缺乏真实图像的情况下表现出良好的鲁棒性。

## 📝 摘要（中文）

扩散蒸馏已成为加速文本到图像（T2I）扩散模型的有效策略，通过将预训练的评分网络蒸馏为单步或少步生成器。现有方法在蒸馏高分辨率T2I扩散模型时，通常依赖真实或教师合成图像，并且使用无分类器引导（CFG）会导致文本图像对齐与生成多样性之间的权衡。本文提出了一种数据无关的一步蒸馏框架Score identity Distillation（SiD），通过理论分析证明将所有生成步骤的输出均匀混合与数据分布匹配的有效性，避免了特定步骤网络的需求，能够无缝集成到现有管道中，在1024x1024分辨率下实现了SDXL的最先进性能。为缓解真实文本图像对的对齐多样性权衡，本文引入了基于扩散GAN的对抗损失，并提出了两种新的引导策略：Zero-CFG和Anti-CFG，灵活的设置提高了多样性而不牺牲对齐性。综合实验表明，在一步和少步生成设置下均实现了最先进的性能，并且对缺乏真实图像具有鲁棒性。

## 🔬 方法详解

**问题定义**：现有的扩散蒸馏方法在高分辨率图像生成中依赖真实或合成图像，且使用无分类器引导（CFG）导致文本图像对齐与生成多样性之间的权衡，限制了生成效果的提升。

**核心思路**：本文提出Score identity Distillation（SiD），通过理论分析证明将所有生成步骤的输出均匀混合与数据分布匹配的有效性，从而避免了特定步骤网络的需求，优化了少步生成过程。

**技术框架**：SiD框架包括数据无关的一步蒸馏过程，结合了基于扩散GAN的对抗损失和两种新的引导策略Zero-CFG与Anti-CFG，能够灵活调整生成多样性与对齐性。

**关键创新**：最重要的技术创新点在于提出了一种无需真实图像的蒸馏方法，并通过对抗损失和新引导策略有效改善了生成的多样性与对齐性，突破了现有方法的局限。

**关键设计**：在损失函数设计上，采用了基于扩散GAN的对抗损失；Zero-CFG策略禁用教师网络中的CFG，而Anti-CFG则在假评分网络中应用负CFG，这些设计提高了生成多样性而不影响对齐性。

## 📊 实验亮点

实验结果表明，SiD在SD1.5和SDXL上实现了最先进的性能，尤其在1024x1024分辨率下，生成质量显著提升，且在一至少步生成设置中均表现出良好的鲁棒性，超越了现有基线。

## 🎯 应用场景

该研究的潜在应用领域包括图像生成、艺术创作、虚拟现实等，能够为生成模型提供更高效的训练方式，提升生成质量和多样性，具有广泛的实际价值和未来影响。

## 📄 摘要（原文）

> Diffusion distillation has emerged as a promising strategy for accelerating text-to-image (T2I) diffusion models by distilling a pretrained score network into a one- or few-step generator. While existing methods have made notable progress, they often rely on real or teacher-synthesized images to perform well when distilling high-resolution T2I diffusion models such as Stable Diffusion XL (SDXL), and their use of classifier-free guidance (CFG) introduces a persistent trade-off between text-image alignment and generation diversity. We address these challenges by optimizing Score identity Distillation (SiD) -- a data-free, one-step distillation framework -- for few-step generation. Backed by theoretical analysis that justifies matching a uniform mixture of outputs from all generation steps to the data distribution, our few-step distillation algorithm avoids step-specific networks and integrates seamlessly into existing pipelines, achieving state-of-the-art performance on SDXL at 1024x1024 resolution. To mitigate the alignment-diversity trade-off when real text-image pairs are available, we introduce a Diffusion GAN-based adversarial loss applied to the uniform mixture and propose two new guidance strategies: Zero-CFG, which disables CFG in the teacher and removes text conditioning in the fake score network, and Anti-CFG, which applies negative CFG in the fake score network. This flexible setup improves diversity without sacrificing alignment. Comprehensive experiments on SD1.5 and SDXL demonstrate state-of-the-art performance in both one-step and few-step generation settings, along with robustness to the absence of real images. Our efficient PyTorch implementation, along with the resulting one- and few-step distilled generators, will be released publicly as a separate branch at https://github.com/mingyuanzhou/SiD-LSG.

