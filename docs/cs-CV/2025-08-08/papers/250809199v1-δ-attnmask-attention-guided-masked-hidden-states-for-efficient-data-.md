---
layout: default
title: "$Δ$-AttnMask: Attention-Guided Masked Hidden States for Efficient Data Selection and Augmentation"
---

# $Δ$-AttnMask: Attention-Guided Masked Hidden States for Efficient Data Selection and Augmentation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.09199" class="toolbar-btn" target="_blank">📄 arXiv: 2508.09199v1</a>
  <a href="https://arxiv.org/pdf/2508.09199.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.09199v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.09199v1', '$Δ$-AttnMask: Attention-Guided Masked Hidden States for Efficient Data Selection and Augmentation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Jucheng Hu, Suorong Yang, Dongzhan Zhou

**分类**: cs.CV, cs.AI, cs.CL

**发布日期**: 2025-08-08

---

## 💡 一句话要点

**提出$Δ$-AttnMask以解决视觉指令微调中的数据选择问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `视觉指令微调` `多模态数据` `样本质量评估` `注意力机制` `数据选择` `模型无关` `训练加速`

## 📋 核心要点

1. 现有的视觉指令微调方法在数据选择上面临挑战，尤其是在多模态数据的质量和对齐性方面。
2. 本文提出的$Δ$-AttnMask通过注意力引导的掩蔽方法，评估样本质量，避免了对额外标签和模型的依赖。
3. 实验结果显示，$Δ$-AttnMask在多个VLM和数据集上表现出色，仅用20%数据即可实现5倍的训练加速和10.1%的准确率提升。

## 📝 摘要（中文）

视觉指令微调（VIF）对后训练的视觉-语言模型（VLMs）至关重要。与单模态指令微调不同，VIF需要多模态数据以实现视觉和文本的联合理解，因此对数据的需求更大。尽管数据选择对性能影响重大，但这一领域仍未得到充分研究。本文提出$Δ$-AttnMask框架，通过对模型隐藏状态的注意力引导掩蔽量化样本质量，能够在不需要领域标签、辅助模型或额外训练的情况下，评估图像-文本对的质量。实验表明，$Δ$-AttnMask在仅使用20%数据的情况下，训练速度提升5倍，并在整体准确率上超越全数据集基线10.1%。

## 🔬 方法详解

**问题定义**：本文旨在解决视觉指令微调（VIF）中数据选择的效率和质量问题。现有方法在处理多模态数据时，往往需要大量高质量的标注数据，导致数据选择过程复杂且低效。

**核心思路**：$Δ$-AttnMask通过对模型隐藏状态进行注意力引导的掩蔽，量化样本质量。这种方法能够在不依赖额外标签或辅助模型的情况下，直接评估图像-文本对的质量。

**技术框架**：该框架的整体流程包括：首先计算模型的隐藏状态，然后根据注意力权重进行掩蔽，最后通过比较原始状态与掩蔽状态之间的损失差异来评估样本质量。

**关键创新**：$Δ$-AttnMask的主要创新在于其无监督的样本质量评估机制，利用注意力机制直接从模型内部获取信息，避免了传统方法对外部标签和模型的依赖。

**关键设计**：在设计中，$Δ$-AttnMask采用了基于注意力权重的掩蔽策略，损失函数通过计算原始状态与掩蔽状态的差异来实现样本质量的量化，确保了方法的高效性和准确性。

## 📊 实验亮点

实验结果表明，$Δ$-AttnMask在多个视觉-语言模型和数据集上均表现出色，仅使用20%的数据便实现了5倍的训练加速，并在整体准确率上超越全数据集基线10.1%。这一显著提升展示了其在数据选择和效率方面的优势。

## 🎯 应用场景

$Δ$-AttnMask的设计具有广泛的应用潜力，尤其在需要高效数据选择和增强的多模态学习任务中，如图像描述生成、视觉问答和跨模态检索等领域。其高效性和准确性将推动相关领域的研究和应用发展。

## 📄 摘要（原文）

> Visual Instruction Finetuning (VIF) is pivotal for post-training Vision-Language Models (VLMs). Unlike unimodal instruction finetuning in plain-text large language models, which mainly requires instruction datasets to enable model instruction-following ability, VIF also requires multimodal data to enable joint visual and textual understanding; therefore, it typically requires more data. Consequently, VIF imposes stricter data selection challenges: the method must scale efficiently to handle larger data demands while ensuring the quality of both visual and textual content, as well as their alignment. Despite its critical impact on performance, data selection for VIF remains an understudied area. In this paper, we propose $Δ$-AttnMask. This data-efficient framework quantifies sample quality through attention-guided masking of the model's hidden states, jointly evaluating image-text pairs without requiring domain labels, auxiliary models, or extra training. By computing loss differences ($Δ$) between the original states and states masked using high-attention regions, $Δ$-AttnMask intrinsically assesses sample quality. Experiments across multiple VLMs and datasets show that $Δ$-AttnMask achieves state-of-the-art performance with just 20% of data, accelerating training by 5x while surpassing full-dataset baselines by +10.1% in overall accuracy. Its model-agnostic and data-agnostic design ensures broad applicability across modalities and architectures.

