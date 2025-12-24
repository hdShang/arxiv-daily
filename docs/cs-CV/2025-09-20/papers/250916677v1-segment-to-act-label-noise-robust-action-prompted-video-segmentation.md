---
layout: default
title: "Segment-to-Act: Label-Noise-Robust Action-Prompted Video Segmentation Towards Embodied Intelligence"
---

# Segment-to-Act: Label-Noise-Robust Action-Prompted Video Segmentation Towards Embodied Intelligence

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.16677" class="toolbar-btn" target="_blank">📄 arXiv: 2509.16677v1</a>
  <a href="https://arxiv.org/pdf/2509.16677.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.16677v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.16677v1', 'Segment-to-Act: Label-Noise-Robust Action-Prompted Video Segmentation Towards Embodied Intelligence')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Wenxin Li, Kunyu Peng, Di Wen, Ruiping Liu, Mengfei Duan, Kai Luo, Kailun Yang

**分类**: cs.CV, cs.LG, cs.RO, eess.IV

**发布日期**: 2025-09-20

**备注**: The established benchmark and source code will be made publicly available at https://github.com/mylwx/ActiSeg-NL

**🔗 代码/项目**: [GITHUB](https://github.com/mylwx/ActiSeg-NL)

---

## 💡 一句话要点

**提出ActiSeg-NL基准，研究标签噪声下动作引导的视频分割，并提出PMHM提升鲁棒性。**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `视频物体分割` `具身智能` `标签噪声` `动作引导` `鲁棒性学习`

## 📋 核心要点

1. 现有基于动作的视频分割方法依赖大量精确标注，成本高且易受噪声干扰，例如文本提示错误和掩码边界不准确。
2. 论文提出ActiSeg-NL基准，研究文本提示和掩码标注噪声下的动作引导视频分割，并探索多种噪声学习策略。
3. 实验分析了不同噪声类型的影响，并提出并行掩码头机制（PMHM）以提升模型在掩码噪声下的鲁棒性。

## 📝 摘要（中文）

具身智能依赖于精确分割交互中的物体。基于动作的视频物体分割通过将分割与动作语义联系起来来解决这个问题，但它依赖于大规模标注和提示，这些标注和提示成本高昂、不一致且容易出现多模态噪声，例如不精确的掩码和指代歧义。目前，这一挑战尚未被探索。在这项工作中，我们迈出了第一步，研究了标签噪声下的基于动作的视频物体分割，重点关注两个来源：文本提示噪声（类别翻转和类别内的名词替换）和掩码标注噪声（扰动的对象边界以模仿不精确的监督）。我们的贡献有三方面。首先，我们为基于动作的视频物体分割任务引入了两种类型的标签噪声。其次，我们构建了第一个标签噪声下的基于动作的视频物体分割基准ActiSeg-NL，并将六种标签噪声学习策略应用于此设置，并建立了在文本、边界和混合噪声下评估它们的协议。第三，我们提供了一个综合分析，将噪声类型与失败模式和鲁棒性增益联系起来，并引入了一种并行掩码头机制（PMHM）来解决掩码标注噪声。定性评估进一步揭示了特征性的失败模式，包括边界泄漏和边界扰动下的错误定位，以及文本翻转下的偶尔身份替换。我们的比较分析表明，不同的学习策略表现出不同的鲁棒性特征，受前景-背景权衡的支配，其中一些策略实现了平衡的性能，而另一些策略则以牺牲背景精度为代价优先考虑前景精度。已建立的基准和源代码将在https://github.com/mylwx/ActiSeg-NL上公开发布。

## 🔬 方法详解

**问题定义**：现有的基于动作的视频物体分割方法依赖于大规模且高质量的标注数据。然而，在实际应用中，获取精确的标注成本高昂，并且标注数据不可避免地会受到噪声的影响，例如文本提示的错误（类别翻转、名词替换）以及掩码边界的不准确。这些噪声会严重影响模型的性能和泛化能力。因此，论文旨在研究在标签噪声下，如何提升基于动作的视频物体分割的鲁棒性。

**核心思路**：论文的核心思路是构建一个包含不同类型标签噪声的基准数据集，并探索不同的噪声学习策略，以提高模型在噪声环境下的鲁棒性。此外，针对掩码标注噪声，论文提出了一个并行掩码头机制（PMHM），旨在更好地处理不精确的掩码边界。

**技术框架**：整体框架包含以下几个主要部分：1) 数据集构建：构建包含文本提示噪声和掩码标注噪声的ActiSeg-NL基准数据集。2) 模型训练：将现有的视频物体分割模型应用于ActiSeg-NL数据集，并采用不同的噪声学习策略进行训练。3) 并行掩码头机制（PMHM）：针对掩码标注噪声，设计PMHM来提升模型性能。4) 评估：在ActiSeg-NL数据集上评估不同模型和策略的性能，分析噪声类型对模型的影响。

**关键创新**：论文的主要创新点在于：1) 首次研究了标签噪声下的基于动作的视频物体分割问题。2) 构建了ActiSeg-NL基准数据集，包含文本提示噪声和掩码标注噪声。3) 提出了并行掩码头机制（PMHM），用于处理掩码标注噪声。与现有方法相比，该论文更关注实际应用中存在的噪声问题，并尝试通过噪声学习策略和特定的网络结构来提高模型的鲁棒性。

**关键设计**：1) 文本提示噪声：通过类别翻转和类别内名词替换来模拟文本提示的错误。2) 掩码标注噪声：通过扰动对象边界来模拟不精确的掩码标注。3) 并行掩码头机制（PMHM）：使用多个并行的掩码头，每个掩码头负责预测不同尺度的掩码，然后将这些掩码进行融合，以提高对不精确边界的鲁棒性。4) 损失函数：实验中使用了多种损失函数，包括交叉熵损失、Dice损失等，并探索了不同的噪声学习策略，例如标签平滑、MixUp等。

## 📊 实验亮点

实验结果表明，不同的噪声学习策略在ActiSeg-NL基准上表现出不同的鲁棒性特征。一些策略在前景和背景精度之间取得了平衡，而另一些策略则更侧重于提高前景精度，但牺牲了背景精度。此外，提出的并行掩码头机制（PMHM）在掩码标注噪声下显著提升了模型的性能，表明其能够有效处理不精确的掩码边界。

## 🎯 应用场景

该研究成果可应用于机器人导航、自动驾驶、智能监控等领域。通过提高模型在噪声环境下的鲁棒性，可以使具身智能系统更好地理解和响应真实世界的复杂场景，从而提升其在实际应用中的可靠性和安全性。未来的研究可以进一步探索更复杂的噪声类型和更有效的噪声学习策略。

## 📄 摘要（原文）

> Embodied intelligence relies on accurately segmenting objects actively involved in interactions. Action-based video object segmentation addresses this by linking segmentation with action semantics, but it depends on large-scale annotations and prompts that are costly, inconsistent, and prone to multimodal noise such as imprecise masks and referential ambiguity. To date, this challenge remains unexplored. In this work, we take the first step by studying action-based video object segmentation under label noise, focusing on two sources: textual prompt noise (category flips and within-category noun substitutions) and mask annotation noise (perturbed object boundaries to mimic imprecise supervision). Our contributions are threefold. First, we introduce two types of label noises for the action-based video object segmentation task. Second, we build up the first action-based video object segmentation under a label noise benchmark ActiSeg-NL and adapt six label-noise learning strategies to this setting, and establish protocols for evaluating them under textual, boundary, and mixed noise. Third, we provide a comprehensive analysis linking noise types to failure modes and robustness gains, and we introduce a Parallel Mask Head Mechanism (PMHM) to address mask annotation noise. Qualitative evaluations further reveal characteristic failure modes, including boundary leakage and mislocalization under boundary perturbations, as well as occasional identity substitutions under textual flips. Our comparative analysis reveals that different learning strategies exhibit distinct robustness profiles, governed by a foreground-background trade-off where some achieve balanced performance while others prioritize foreground accuracy at the cost of background precision. The established benchmark and source code will be made publicly available at https://github.com/mylwx/ActiSeg-NL.

