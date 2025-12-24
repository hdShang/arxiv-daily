---
layout: default
title: Distilling to Hybrid Attention Models via KL-Guided Layer Selection
---

# Distilling to Hybrid Attention Models via KL-Guided Layer Selection

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.20569" class="toolbar-btn" target="_blank">📄 arXiv: 2512.20569v1</a>
  <a href="https://arxiv.org/pdf/2512.20569.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.20569v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.20569v1', 'Distilling to Hybrid Attention Models via KL-Guided Layer Selection')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yanhong Li, Songlin Yang, Shawn Tan, Mayank Mishra, Rameswar Panda, Jiawei Zhou, Yoon Kim

**分类**: cs.CL, cs.AI

**发布日期**: 2025-12-23

---

## 💡 一句话要点

**提出基于KL散度引导的层选择方法，用于将Softmax注意力Transformer蒸馏为混合注意力模型。**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `Transformer蒸馏` `混合注意力模型` `层选择` `KL散度` `模型压缩`

## 📋 核心要点

1. 现有方法在将Softmax注意力Transformer蒸馏为混合架构时，层选择策略效率低或依赖特定数据集。
2. 论文提出基于KL散度引导的层选择方法，通过层重要性得分确定线性注意力层的位置。
3. 实验表明，该方法优于均匀交错等现有层选择策略，能更有效地提升推理效率。

## 📝 摘要（中文）

本文提出了一种简单高效的层选择方法，用于将预训练的Softmax注意力Transformer蒸馏为更高效的混合架构，该架构交替使用Softmax和线性注意力层。这种方法旨在提高LLM的推理效率，而无需从头开始进行昂贵的预训练。该方法使用从少量通用文本数据训练中获得的层重要性得分来确定要转换为线性注意力变体的层。在选定层之后，我们使用最近的蒸馏流程（RADLADS），该流程包括注意力权重转移、隐藏状态对齐、基于KL散度的分布匹配，以及少量的微调。实验表明，该方法比现有的层选择方法更有效，包括基于固定比例均匀交错线性注意力的启发式方法，以及依赖于专门诊断数据集的更复杂的方法。

## 🔬 方法详解

**问题定义**：论文旨在解决如何高效地将预训练的Softmax注意力Transformer模型蒸馏成混合注意力模型的问题。现有方法，如均匀交错线性注意力层或依赖特定诊断数据集的方法，在层选择方面效率较低或泛化性不足，无法充分利用线性注意力的优势来加速推理。

**核心思路**：核心思路是利用少量通用文本数据训练得到的层重要性得分来指导层选择过程。通过评估每一层的重要性，选择性地将重要性较低的层转换为线性注意力层，从而在保持模型性能的同时，降低计算复杂度。这种方法避免了对特定数据集的依赖，提高了泛化能力。

**技术框架**：整体框架包括两个主要阶段：层选择阶段和蒸馏阶段。在层选择阶段，首先使用少量通用文本数据训练原始的Softmax注意力Transformer模型，然后计算每一层的层重要性得分。基于这些得分，选择一部分层转换为线性注意力层。在蒸馏阶段，使用RADLADS流程，包括注意力权重转移、隐藏状态对齐、基于KL散度的分布匹配，以及少量的微调，将原始模型的知识迁移到混合注意力模型。

**关键创新**：最重要的技术创新点在于提出了一种基于KL散度引导的层选择方法。与现有方法相比，该方法不需要专门的诊断数据集，而是利用通用文本数据来评估层的重要性，从而更准确地确定哪些层可以安全地转换为线性注意力层，而不会显著降低模型性能。

**关键设计**：关键设计包括：1) 使用KL散度来衡量原始模型和蒸馏模型在每一层的输出分布之间的差异，从而指导蒸馏过程。2) 使用RADLADS流程进行蒸馏，该流程包括注意力权重转移、隐藏状态对齐和分布匹配，以确保蒸馏后的模型能够尽可能地保留原始模型的知识。3) 使用少量微调来进一步优化蒸馏后的模型。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.20569v1/x1.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.20569v1/x2.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.20569v1/x3.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

该论文提出的方法在层选择方面优于现有的均匀交错等策略。实验结果表明，使用该方法蒸馏得到的混合注意力模型在保持性能的同时，显著降低了计算复杂度，提高了推理效率。具体的性能数据和提升幅度在论文中进行了详细的展示和对比。

## 🎯 应用场景

该研究成果可广泛应用于自然语言处理领域，尤其是在需要部署大规模语言模型的场景中，如智能客服、机器翻译、文本生成等。通过将大型Softmax注意力Transformer模型蒸馏为更高效的混合注意力模型，可以显著降低推理成本，提高响应速度，从而更好地满足实际应用的需求。此外，该方法还可以应用于其他类型的Transformer模型，具有一定的通用性。

## 📄 摘要（原文）

> Distilling pretrained softmax attention Transformers into more efficient hybrid architectures that interleave softmax and linear attention layers is a promising approach for improving the inference efficiency of LLMs without requiring expensive pretraining from scratch. A critical factor in the conversion process is layer selection, i.e., deciding on which layers to convert to linear attention variants. This paper describes a simple and efficient recipe for layer selection that uses layer importance scores derived from a small amount of training on generic text data. Once the layers have been selected we use a recent pipeline for the distillation process itself \citep[RADLADS;][]{goldstein2025radlads}, which consists of attention weight transfer, hidden state alignment, KL-based distribution matching, followed by a small amount of finetuning. We find that this approach is more effective than existing approaches for layer selection, including heuristics that uniformly interleave linear attentions based on a fixed ratio, as well as more involved approaches that rely on specialized diagnostic datasets.

