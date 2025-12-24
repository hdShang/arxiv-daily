---
layout: default
title: "STAR: Stage-Wise Attention-Guided Token Reduction for Efficient Large Vision-Language Models Inference"
---

# STAR: Stage-Wise Attention-Guided Token Reduction for Efficient Large Vision-Language Models Inference

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.12359" class="toolbar-btn" target="_blank">📄 arXiv: 2505.12359v1</a>
  <a href="https://arxiv.org/pdf/2505.12359.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.12359v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.12359v1', 'STAR: Stage-Wise Attention-Guided Token Reduction for Efficient Large Vision-Language Models Inference')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yichen Guo, Hanze Li, Zonghao Zhang, Jinhao You, Kai Tang, Xiande Huang

**分类**: cs.LG, cs.CV

**发布日期**: 2025-05-18

---

## 💡 一句话要点

**提出STAR框架以解决大规模视觉语言模型推理效率问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `视觉语言模型` `标记剪枝` `多模态学习` `注意力机制` `推理效率`

## 📋 核心要点

1. 现有的标记剪枝方法多采用单一阶段策略，忽视了模型内部的信息流，导致高剪枝比率下性能显著下降。
2. STAR框架通过阶段性注意力引导的方式进行标记剪枝，分为早期和后期两个阶段，分别去除冗余特征和无关标记。
3. 实验结果显示，STAR在多个LVLM架构上实现了显著的加速，同时在某些情况下性能有所提升。

## 📝 摘要（中文）

尽管大型视觉语言模型（LVLMs）利用丰富的视觉标记表示在多模态任务中取得了良好表现，但这些标记在推理过程中也带来了显著的计算开销。现有的无训练标记剪枝方法通常采用单阶段策略，关注视觉自注意力或视觉-文本交叉注意力，导致信息流的局部视角忽视，尤其在高剪枝比率下性能显著下降。本文提出了STAR（阶段性注意力引导的标记减少），一个无训练、即插即用的框架，从全局视角进行标记剪枝。STAR在两个互补阶段进行注意力引导的减少，早期阶段基于视觉自注意力去除冗余低级特征，后期阶段通过跨模态注意力引导丢弃与任务无关的标记。这种整体方法显著降低了计算成本，同时更好地保留了任务关键的信息。大量实验表明，STAR在多个LVLM架构和基准上实现了强大的加速，同时保持了可比的甚至更好的性能。

## 🔬 方法详解

**问题定义**：本文旨在解决大型视觉语言模型在推理过程中由于标记数量庞大而导致的计算开销问题。现有方法通常采用单阶段剪枝，无法有效利用全局信息，导致性能下降。

**核心思路**：STAR框架通过阶段性注意力引导的方式进行标记剪枝，首先在早期阶段去除冗余的低级特征，然后在后期阶段基于跨模态注意力丢弃与任务无关的标记，从而实现更高效的推理。

**技术框架**：STAR的整体架构包括两个主要阶段：第一阶段利用视觉自注意力进行早期剪枝，第二阶段通过跨模态注意力进行后期剪枝。每个阶段都针对特定的特征进行优化，以确保信息的有效保留。

**关键创新**：STAR的创新在于其阶段性剪枝策略，区别于传统的单阶段方法，通过全局视角优化剪枝过程，显著提高了剪枝效率和模型性能。

**关键设计**：在设计中，STAR采用了注意力机制来指导剪枝过程，确保在每个阶段都能有效识别和去除冗余信息。具体的参数设置和损失函数设计尚未详细披露，可能为未知。

## 📊 实验亮点

实验结果表明，STAR在多个LVLM架构上实现了显著的加速，推理速度提升可达XX%（具体数据需查阅原文），同时在某些基准上性能保持可比或有所提升，展示了其优越性。

## 🎯 应用场景

该研究的潜在应用领域包括图像和文本的联合理解、智能问答系统以及多模态内容生成等。通过提高推理效率，STAR框架能够在资源受限的环境中实现更快速的响应，具有重要的实际价值和未来影响。

## 📄 摘要（原文）

> Although large vision-language models (LVLMs) leverage rich visual token representations to achieve strong performance on multimodal tasks, these tokens also introduce significant computational overhead during inference. Existing training-free token pruning methods typically adopt a single-stage strategy, focusing either on visual self-attention or visual-textual cross-attention. However, such localized perspectives often overlook the broader information flow across the model, leading to substantial performance degradation, especially under high pruning ratios. In this work, we propose STAR (Stage-wise Attention-guided token Reduction), a training-free, plug-and-play framework that approaches token pruning from a global perspective. Instead of pruning at a single point, STAR performs attention-guided reduction in two complementary stages: an early-stage pruning based on visual self-attention to remove redundant low-level features, and a later-stage pruning guided by cross-modal attention to discard task-irrelevant tokens. This holistic approach allows STAR to significantly reduce computational cost while better preserving task-critical information. Extensive experiments across multiple LVLM architectures and benchmarks show that STAR achieves strong acceleration while maintaining comparable, and in some cases even improved performance.

