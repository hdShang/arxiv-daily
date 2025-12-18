---
layout: default
title: Don't Just Chase "Highlighted Tokens" in MLLMs: Revisiting Visual Holistic Context Retention
---

# Don't Just Chase "Highlighted Tokens" in MLLMs: Revisiting Visual Holistic Context Retention

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2510.02912" class="toolbar-btn" target="_blank">📄 arXiv: 2510.02912v2</a>
  <a href="https://arxiv.org/pdf/2510.02912.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.02912v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2510.02912v2', 'Don\'t Just Chase &quot;Highlighted Tokens&quot; in MLLMs: Revisiting Visual Holistic Context Retention')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Xin Zou, Di Lu, Yizhou Wang, Yibo Yan, Yuanhuiyi Lyu, Xu Zheng, Linfeng Zhang, Xuming Hu

**分类**: cs.CV

**发布日期**: 2025-10-03 (更新: 2025-10-10)

**备注**: Accepted by NeurIPS 2025 main

---

## 💡 一句话要点

**HoloV：一种视觉token剪枝框架，通过全局上下文保留提升多模态大语言模型效率。**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多模态大语言模型` `视觉token剪枝` `全局上下文` `模型效率` `LLaVA1.5`

## 📋 核心要点

1. 现有MLLM的token剪枝方法倾向于保留语义相似的tokens，导致高剪枝率下性能下降。
2. HoloV通过自适应地在不同空间区域分配剪枝预算，确保保留tokens捕获全局视觉上下文。
3. 实验表明，HoloV在各种任务和模型上优于SOTA方法，实现了更好的效率-精度平衡。

## 📝 摘要（中文）

多模态大语言模型(MLLM)由于依赖大量的视觉tokens而面临巨大的计算开销。为了缓解这个问题，最近的研究探索了token剪枝，通常使用文本-视觉交叉注意力或[	exttt{CLS}]注意力来评估和丢弃冗余的视觉tokens。本文指出，这种以注意力为先的剪枝方法存在一个关键限制，即它们倾向于保留语义相似的tokens，导致在高剪枝率下性能显著下降。为此，我们提出了HoloV，一个简单而有效的、即插即用的视觉token剪枝框架，用于高效推理。与以往的以注意力为先的方案不同，HoloV从整体的角度重新思考token保留。通过自适应地在不同的空间裁剪区域分配剪枝预算，HoloV确保保留的tokens捕获全局视觉上下文，而不是孤立的显著特征。这种策略最大限度地减少了表征崩溃，并在高强度剪枝下保持了任务相关的信息。实验结果表明，与SOTA方法相比，我们的HoloV在各种任务、MLLM架构和剪枝率下都取得了优异的性能。例如，配备HoloV的LLaVA1.5在剪枝88.9%的视觉tokens后，仍能保持原始性能的95.8%，实现了卓越的效率-精度权衡。

## 🔬 方法详解

**问题定义**：论文旨在解决多模态大语言模型（MLLM）中视觉token数量庞大导致的计算开销问题。现有的token剪枝方法，如基于注意力机制的方法，往往会保留语义相似的token，在高剪枝率下造成严重的性能下降，无法有效提取全局视觉信息。

**核心思路**：HoloV的核心思路是从全局视角出发进行token剪枝，避免只关注局部显著特征。通过在不同的空间区域自适应地分配剪枝预算，确保保留的token能够捕捉到图像的整体上下文信息，从而减少信息损失，维持模型性能。

**技术框架**：HoloV是一个即插即用的视觉token剪枝框架，可以应用于各种MLLM架构。其主要流程包括：1) 将输入图像划分为多个空间区域（crops）；2) 根据每个区域的重要性自适应地分配剪枝预算；3) 根据分配的预算，对每个区域内的token进行剪枝；4) 将保留的token输入到MLLM中进行后续处理。

**关键创新**：HoloV的关键创新在于其全局上下文保留的剪枝策略。与以往基于注意力机制的局部剪枝方法不同，HoloV考虑了图像的整体结构和不同区域之间的关系，从而能够更有效地保留任务相关的视觉信息。这种全局视角避免了模型过度关注局部显著特征，从而在高剪枝率下也能保持较好的性能。

**关键设计**：HoloV的关键设计包括：1) 自适应剪枝预算分配策略：根据每个空间区域的重要性（例如，基于注意力得分或区域内的信息熵）动态调整剪枝预算。2) 空间区域划分策略：采用不同的划分方式（例如，均匀划分、基于显著性划分）来适应不同的图像和任务。3) 剪枝准则：可以使用不同的剪枝准则（例如，基于注意力得分、token的L1范数）来选择要删除的token。

## 📊 实验亮点

实验结果表明，HoloV在各种任务、MLLM架构和剪枝率下都优于SOTA方法。例如，配备HoloV的LLaVA1.5在剪枝88.9%的视觉tokens后，仍能保持原始性能的95.8%，实现了卓越的效率-精度权衡。这表明HoloV能够有效地减少计算开销，同时保持模型的性能。

## 🎯 应用场景

HoloV可应用于各种需要处理图像输入的多模态大语言模型，尤其是在资源受限的场景下，如移动设备、边缘计算等。通过减少视觉token的数量，HoloV可以显著降低计算成本和内存占用，提高模型的推理速度，从而扩展MLLM的应用范围。

## 📄 摘要（原文）

> Despite their powerful capabilities, Multimodal Large Language Models (MLLMs) suffer from considerable computational overhead due to their reliance on massive visual tokens. Recent studies have explored token pruning to alleviate this problem, which typically uses text-vision cross-attention or [\texttt{CLS}] attention to assess and discard redundant visual tokens. In this work, we identify a critical limitation of such attention-first pruning approaches, i.e., they tend to preserve semantically similar tokens, resulting in pronounced performance drops under high pruning ratios. To this end, we propose {HoloV}, a simple yet effective, plug-and-play visual token pruning framework for efficient inference. Distinct from previous attention-first schemes, HoloV rethinks token retention from a holistic perspective. By adaptively distributing the pruning budget across different spatial crops, HoloV ensures that the retained tokens capture the global visual context rather than isolated salient features. This strategy minimizes representational collapse and maintains task-relevant information even under aggressive pruning. Experimental results demonstrate that our HoloV achieves superior performance across various tasks, MLLM architectures, and pruning ratios compared to SOTA methods. For instance, LLaVA1.5 equipped with HoloV preserves 95.8\% of the original performance after pruning 88.9\% of visual tokens, achieving superior efficiency-accuracy trade-offs.

