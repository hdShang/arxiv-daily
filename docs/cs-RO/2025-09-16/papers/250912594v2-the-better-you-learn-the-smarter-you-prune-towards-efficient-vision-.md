---
layout: default
title: "The Better You Learn, The Smarter You Prune: Towards Efficient Vision-language-action Models via Differentiable Token Pruning"
---

# The Better You Learn, The Smarter You Prune: Towards Efficient Vision-language-action Models via Differentiable Token Pruning

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.12594" class="toolbar-btn" target="_blank">📄 arXiv: 2509.12594v2</a>
  <a href="https://arxiv.org/pdf/2509.12594.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.12594v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.12594v2', 'The Better You Learn, The Smarter You Prune: Towards Efficient Vision-language-action Models via Differentiable Token Pruning')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Titong Jiang, Xuefeng Jiang, Yuan Ma, Xin Wen, Bailin Li, Kun Zhan, Peng Jia, Yahui Liu, Sheng Sun, Xianpeng Lang

**分类**: cs.RO, cs.CL, cs.CV

**发布日期**: 2025-09-16 (更新: 2025-09-21)

**备注**: Under review. Project site: https://liauto-research.github.io/LightVLA

---

## 💡 一句话要点

**LightVLA：通过可微Token剪枝提升视觉-语言-动作模型的效率与性能**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `视觉-语言-动作模型` `Token剪枝` `可微学习` `机器人控制` `模型压缩`

## 📋 核心要点

1. 现有VLA模型计算量大，难以部署在资源受限的机器人平台上，尤其是在处理大量视觉Token时。
2. LightVLA通过动态查询评估Token重要性，并使用Gumbel softmax实现可微剪枝，自适应地保留重要Token。
3. 实验表明，LightVLA在降低FLOPs和延迟的同时，提高了任务成功率，无需额外参数且兼容现有框架。

## 📝 摘要（中文）

本文提出了一种简单而有效的可微Token剪枝框架LightVLA，用于提升视觉-语言-动作(VLA)模型的效率。VLA模型在执行现实世界机器人任务中表现出令人印象深刻的能力，但其部署在资源受限的平台上通常受到基于大量视觉Token的繁重注意力计算的限制。LightVLA通过自适应的、性能驱动的视觉Token剪枝来解决这一挑战：它生成动态查询来评估视觉Token的重要性，并采用Gumbel softmax来实现可微的Token选择。通过微调，LightVLA学会保留信息量最大的视觉Token，同时剪枝对任务执行没有贡献的Token，从而同时提高效率和性能。值得注意的是，LightVLA不需要启发式魔法数字，也不引入额外的可训练参数，使其与现代推理框架兼容。实验结果表明，LightVLA在LIBERO基准测试的各种任务中优于不同的VLA模型和现有的Token剪枝方法，以显著降低的计算开销实现了更高的成功率。具体而言，LightVLA将FLOPs和延迟分别降低了59.1%和38.2%，同时任务成功率提高了2.6%。同时，我们还研究了基于可学习查询的Token剪枝方法LightVLA*，该方法具有额外的可训练参数，也取得了令人满意的性能。我们的工作表明，随着VLA追求最佳性能，LightVLA自发地学会从性能驱动的角度剪枝Token。据我们所知，LightVLA是第一个将自适应视觉Token剪枝应用于VLA任务，并同时实现效率和性能目标的，这标志着朝着更高效、更强大和更实用的实时机器人系统迈出了重要一步。

## 🔬 方法详解

**问题定义**：论文旨在解决视觉-语言-动作(VLA)模型在资源受限平台上部署困难的问题。现有VLA模型通常依赖于对大量视觉Token进行注意力计算，导致计算量巨大，难以满足实时性要求。现有方法缺乏有效的Token选择机制，无法在保证性能的同时降低计算开销。

**核心思路**：论文的核心思路是自适应地剪枝对任务执行贡献较小的视觉Token，从而降低计算量并提高效率。通过学习动态查询来评估Token的重要性，并采用可微的Token选择机制，使得模型能够自动学习哪些Token应该被保留，哪些应该被剪枝。这种性能驱动的剪枝方法旨在在不损失甚至提升任务性能的前提下，显著降低计算开销。

**技术框架**：LightVLA框架主要包含以下几个阶段：1) 输入视觉和语言信息；2) 使用动态查询评估视觉Token的重要性；3) 使用Gumbel softmax进行可微的Token选择，确定需要保留的Token子集；4) 基于选择后的Token子集进行后续的VLA任务处理。整个过程是端到端可训练的，允许模型在训练过程中学习最佳的Token选择策略。

**关键创新**：LightVLA的关键创新在于其自适应的、性能驱动的Token剪枝方法。与传统的Token剪枝方法不同，LightVLA不依赖于启发式规则或固定的阈值，而是通过学习动态查询来评估Token的重要性，并使用可微的Token选择机制来实现自适应的剪枝。此外，LightVLA不需要额外的可训练参数，使其易于集成到现有的VLA模型中。

**关键设计**：LightVLA的关键设计包括：1) 动态查询生成模块，用于根据输入信息生成与Token相关的查询向量；2) 基于Gumbel softmax的可微Token选择模块，用于实现Token的概率选择，并允许梯度反向传播；3) 损失函数的设计，旨在平衡任务性能和计算开销，鼓励模型选择更少的Token，同时保持或提高任务成功率。具体参数设置和网络结构的选择取决于具体的VLA模型和任务。

## 📊 实验亮点

LightVLA在LIBERO基准测试中表现出色，相较于现有VLA模型和Token剪枝方法，在任务成功率上提升了2.6%的同时，将FLOPs降低了59.1%，延迟降低了38.2%。LightVLA*（带有可学习查询的版本）也取得了令人满意的性能，验证了该方法在不同配置下的有效性。实验结果表明，LightVLA能够有效地平衡计算效率和任务性能。

## 🎯 应用场景

LightVLA具有广泛的应用前景，尤其是在资源受限的机器人应用中，如移动机器人、无人机等。通过降低VLA模型的计算开销，LightVLA可以使这些模型能够在低功耗设备上实时运行，从而实现更智能、更高效的机器人控制。此外，该方法还可以应用于其他需要处理大量视觉信息的任务，如视频分析、图像搜索等。

## 📄 摘要（原文）

> We present LightVLA, a simple yet effective differentiable token pruning framework for vision-language-action (VLA) models. While VLA models have shown impressive capability in executing real-world robotic tasks, their deployment on resource-constrained platforms is often bottlenecked by the heavy attention-based computation over large sets of visual tokens. LightVLA addresses this challenge through adaptive, performance-driven pruning of visual tokens: It generates dynamic queries to evaluate visual token importance, and adopts Gumbel softmax to enable differentiable token selection. Through fine-tuning, LightVLA learns to preserve the most informative visual tokens while pruning tokens which do not contribute to task execution, thereby improving efficiency and performance simultaneously. Notably, LightVLA requires no heuristic magic numbers and introduces no additional trainable parameters, making it compatible with modern inference frameworks. Experimental results demonstrate that LightVLA outperforms different VLA models and existing token pruning methods across diverse tasks on the LIBERO benchmark, achieving higher success rates with substantially reduced computational overhead. Specifically, LightVLA reduces FLOPs and latency by 59.1% and 38.2% respectively, with a 2.6% improvement in task success rate. Meanwhile, we also investigate the learnable query-based token pruning method LightVLA* with additional trainable parameters, which also achieves satisfactory performance. Our work reveals that as VLA pursues optimal performance, LightVLA spontaneously learns to prune tokens from a performance-driven perspective. To the best of our knowledge, LightVLA is the first work to apply adaptive visual token pruning to VLA tasks with the collateral goals of efficiency and performance, marking a significant step toward more efficient, powerful and practical real-time robotic systems.

