---
layout: default
title: "VideoScore2: Think before You Score in Generative Video Evaluation"
---

# VideoScore2: Think before You Score in Generative Video Evaluation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.22799" class="toolbar-btn" target="_blank">📄 arXiv: 2509.22799v1</a>
  <a href="https://arxiv.org/pdf/2509.22799.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.22799v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.22799v1', 'VideoScore2: Think before You Score in Generative Video Evaluation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Xuan He, Dongfu Jiang, Ping Nie, Minghao Liu, Zhengxuan Jiang, Mingyi Su, Wentao Ma, Junru Lin, Chun Ye, Yi Lu, Keming Wu, Benjamin Schneider, Quy Duc Do, Zhuofeng Li, Yiming Jia, Yuxuan Zhang, Guo Cheng, Haozhe Wang, Wangchunshu Zhou, Qunshu Lin, Yuanxing Zhang, Ge Zhang, Wenhao Huang, Wenhu Chen

**分类**: cs.CV, cs.AI, cs.CL

**发布日期**: 2025-09-26

**🔗 代码/项目**: [PROJECT_PAGE](https://tiger-ai-lab.github.io/VideoScore2/)

---

## 💡 一句话要点

**VideoScore2：提出多维度、可解释的视频生成评估框架，提升评估准确性和可控性。**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `视频生成评估` `多维度评估` `可解释性` `思维链` `强化学习` `GRPO` `文本到视频` `视频质量评估`

## 📋 核心要点

1. 现有视频生成评估方法缺乏可解释性，无法提供细粒度的分析，难以全面评估视频质量。
2. VideoScore2通过多维度评估（视觉质量、语义对齐、物理一致性）和思维链推理，实现可解释的视频评估。
3. 实验表明，VideoScore2在多个基准测试中显著提升了评估准确性，并能有效支持可控视频生成。

## 📝 摘要（中文）

文本到视频生成技术取得了显著进展，但视频评估仍然面临挑战，因为视频在视觉质量、语义对齐和物理一致性等多方面都具有复杂性。现有的评估器和奖励模型通常只提供单一的、不透明的分数，缺乏可解释性，或者只能提供粗略的分析，无法全面捕捉视频质量评估的本质。本文提出了VideoScore2，一个多维度、可解释且与人类对齐的框架，它显式地评估视觉质量、文本到视频的对齐以及物理/常识一致性，并生成详细的思维链推理过程。该模型在包含27168个人工标注视频的大规模数据集VideoFeedback2上进行训练，该数据集包含三个维度的分数和推理轨迹，使用监督微调和基于Group Relative Policy Optimization (GRPO)的强化学习的两阶段流程，以增强分析的鲁棒性。大量实验表明，VideoScore2在我们的领域内基准VideoScore-Bench-v2上实现了44.35 (+5.94)的准确率，并在四个领域外基准（VideoGenReward-Bench、VideoPhy2等）上实现了50.37 (+4.32)的平均性能，同时提供可解释的评估，通过有效的奖励建模来弥合评估和可控生成之间的差距，从而实现Best-of-N采样。

## 🔬 方法详解

**问题定义**：当前文本到视频生成评估方法主要存在三个痛点：一是评估结果缺乏可解释性，难以理解模型判断依据；二是评估维度单一，无法全面衡量视频质量（视觉质量、语义对齐、物理一致性）；三是评估结果与人类感知存在偏差，难以指导视频生成。

**核心思路**：VideoScore2的核心思路是将视频评估分解为多个维度，并引入思维链推理，从而提高评估的可解释性和准确性。通过显式地评估视觉质量、文本到视频的对齐以及物理/常识一致性，并生成详细的推理过程，使得评估结果更易于理解和信任。同时，利用大规模人工标注数据进行训练，使得模型评估结果更符合人类感知。

**技术框架**：VideoScore2采用两阶段训练流程。第一阶段是监督微调（SFT），使用VideoFeedback2数据集，训练模型预测人工标注的分数和推理过程。第二阶段是强化学习（RL），使用Group Relative Policy Optimization (GRPO)算法，进一步优化模型的评估能力，使其更具鲁棒性。整体框架包含视频特征提取模块、文本特征提取模块、多维度评估模块和思维链生成模块。

**关键创新**：VideoScore2的关键创新在于：1) 提出了多维度的视频评估框架，能够全面衡量视频质量；2) 引入了思维链推理，提高了评估的可解释性；3) 使用GRPO算法进行强化学习，增强了模型的鲁棒性。与现有方法相比，VideoScore2不仅能够提供更准确的评估结果，而且能够提供可解释的评估依据，从而更好地指导视频生成。

**关键设计**：VideoScore2的关键设计包括：1) VideoFeedback2数据集，包含27168个人工标注视频，提供了丰富的数据支持；2) 多维度评估模块，分别评估视觉质量、文本到视频的对齐以及物理/常识一致性；3) 思维链生成模块，生成详细的推理过程，解释评估结果；4) GRPO算法，用于强化学习，优化模型的评估能力。具体参数设置和网络结构细节未在摘要中详细说明，属于未知信息。

## 📊 实验亮点

VideoScore2在VideoScore-Bench-v2上实现了44.35的准确率，相比现有方法提升了5.94。在四个领域外基准测试（VideoGenReward-Bench、VideoPhy2等）上，VideoScore2取得了50.37的平均性能，相比现有方法提升了4.32。这些结果表明，VideoScore2具有优越的性能和泛化能力。

## 🎯 应用场景

VideoScore2可应用于文本到视频生成模型的评估和优化，帮助开发者更好地理解模型的优缺点，并进行针对性的改进。此外，该模型还可以用于视频质量评估、视频内容审核等领域，具有广泛的应用前景和实际价值。未来，可以进一步探索VideoScore2在可控视频生成、视频编辑等方面的应用。

## 📄 摘要（原文）

> Recent advances in text-to-video generation have produced increasingly realistic and diverse content, yet evaluating such videos remains a fundamental challenge due to their multi-faceted nature encompassing visual quality, semantic alignment, and physical consistency. Existing evaluators and reward models are limited to single opaque scores, lack interpretability, or provide only coarse analysis, making them insufficient for capturing the comprehensive nature of video quality assessment. We present VideoScore2, a multi-dimensional, interpretable, and human-aligned framework that explicitly evaluates visual quality, text-to-video alignment, and physical/common-sense consistency while producing detailed chain-of-thought rationales. Our model is trained on a large-scale dataset VideoFeedback2 containing 27,168 human-annotated videos with both scores and reasoning traces across three dimensions, using a two-stage pipeline of supervised fine-tuning followed by reinforcement learning with Group Relative Policy Optimization (GRPO) to enhance analytical robustness. Extensive experiments demonstrate that VideoScore2 achieves superior performance with 44.35 (+5.94) accuracy on our in-domain benchmark VideoScore-Bench-v2 and 50.37 (+4.32) average performance across four out-of-domain benchmarks (VideoGenReward-Bench, VideoPhy2, etc), while providing interpretable assessments that bridge the gap between evaluation and controllable generation through effective reward modeling for Best-of-N sampling. Project Page: https://tiger-ai-lab.github.io/VideoScore2/

