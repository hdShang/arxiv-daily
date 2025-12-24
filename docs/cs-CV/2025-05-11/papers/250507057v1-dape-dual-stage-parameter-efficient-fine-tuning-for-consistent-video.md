---
layout: default
title: DAPE: Dual-Stage Parameter-Efficient Fine-Tuning for Consistent Video Editing with Diffusion Models
---

# DAPE: Dual-Stage Parameter-Efficient Fine-Tuning for Consistent Video Editing with Diffusion Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.07057" class="toolbar-btn" target="_blank">📄 arXiv: 2505.07057v1</a>
  <a href="https://arxiv.org/pdf/2505.07057.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.07057v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.07057v1', 'DAPE: Dual-Stage Parameter-Efficient Fine-Tuning for Consistent Video Editing with Diffusion Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Junhao Xia, Chaoyang Zhang, Yecheng Zhang, Chengyang Zhou, Zhichang Wang, Bochun Liu, Dongshuo Yin

**分类**: cs.CV

**发布日期**: 2025-05-11

---

## 💡 一句话要点

**提出DAPE以解决视频编辑中的一致性与效率问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `视频编辑` `扩散模型` `参数高效微调` `时间一致性` `视觉质量` `多模态任务` `数据集基准`

## 📋 核心要点

1. 现有视频编辑方法在计算成本和性能之间存在权衡，训练方法成本高而无训练方法效果不佳。
2. DAPE框架通过双阶段参数高效微调，第一阶段增强时间一致性，第二阶段提高视觉质量。
3. 实验结果表明，DAPE在多个数据集上显著提升了时间一致性和文本-视频对齐，超越了现有方法。

## 📝 摘要（中文）

基于扩散模型的视频生成是一项具有挑战性的多模态任务，其中视频编辑成为该领域的重要方向。现有的视频编辑方法主要分为两类：需要训练的方法和无训练的方法。训练方法计算成本高，而无训练的方法性能往往不理想。为了解决这些问题，本文提出了DAPE，一个高质量且成本效益高的双阶段参数高效微调框架。在第一阶段，设计了一种高效的规范调整方法，以增强生成视频的时间一致性。第二阶段引入了视觉友好的适配器，以提高视觉质量。此外，本文还识别了现有基准的关键缺陷，包括类别多样性有限、对象分布不均和帧数不一致。为缓解这些问题，本文策划了一个包含232个视频和6个编辑提示的大型数据集基准，能够对先进方法进行客观和全面的评估。大量实验表明，DAPE在时间一致性和文本-视频对齐方面显著提升，超越了之前的最先进方法。

## 🔬 方法详解

**问题定义**：本文旨在解决视频编辑中时间一致性和视觉质量不足的问题。现有方法在计算资源和性能之间存在显著的权衡，导致生成视频的质量不理想。

**核心思路**：DAPE框架采用双阶段的参数高效微调策略，第一阶段通过规范调整提升时间一致性，第二阶段利用视觉适配器增强视觉效果，从而在保证效率的同时提升视频编辑质量。

**技术框架**：DAPE的整体架构分为两个主要阶段：第一阶段为高效的规范调整，旨在改善生成视频的时间一致性；第二阶段引入视觉友好的适配器，专注于提升生成视频的视觉质量。

**关键创新**：DAPE的主要创新在于其双阶段的设计思路，结合了规范调整和视觉适配器，显著提升了视频生成的一致性和质量，与传统方法相比，提供了更高的效率和效果。

**关键设计**：在第一阶段，采用了一种高效的规范调整方法，确保生成视频在时间上的一致性；在第二阶段，设计了视觉适配器以优化视觉输出，具体的参数设置和损失函数设计未详细披露，待进一步研究。

## 📊 实验亮点

在多个数据集（BalanceCC、LOVEU-TGVE、RAVE）上的实验表明，DAPE在时间一致性和文本-视频对齐方面显著优于现有最先进的方法，具体提升幅度达到XX%（具体数据待补充），展示了其在视频编辑领域的强大能力。

## 🎯 应用场景

DAPE框架在视频编辑、影视制作、游戏开发等领域具有广泛的应用潜力。其高效的微调策略和增强的视觉质量能够帮助创作者更快速地生成高质量视频内容，提升创作效率和效果。未来，DAPE可能推动视频生成技术的进一步发展，促进多模态内容创作的普及。

## 📄 摘要（原文）

> Video generation based on diffusion models presents a challenging multimodal task, with video editing emerging as a pivotal direction in this field. Recent video editing approaches primarily fall into two categories: training-required and training-free methods. While training-based methods incur high computational costs, training-free alternatives often yield suboptimal performance. To address these limitations, we propose DAPE, a high-quality yet cost-effective two-stage parameter-efficient fine-tuning (PEFT) framework for video editing. In the first stage, we design an efficient norm-tuning method to enhance temporal consistency in generated videos. The second stage introduces a vision-friendly adapter to improve visual quality. Additionally, we identify critical shortcomings in existing benchmarks, including limited category diversity, imbalanced object distribution, and inconsistent frame counts. To mitigate these issues, we curate a large dataset benchmark comprising 232 videos with rich annotations and 6 editing prompts, enabling objective and comprehensive evaluation of advanced methods. Extensive experiments on existing datasets (BalanceCC, LOVEU-TGVE, RAVE) and our proposed benchmark demonstrate that DAPE significantly improves temporal coherence and text-video alignment while outperforming previous state-of-the-art approaches.

