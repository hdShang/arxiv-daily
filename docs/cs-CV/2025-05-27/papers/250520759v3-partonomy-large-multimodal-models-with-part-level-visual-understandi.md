---
layout: default
title: "PARTONOMY: Large Multimodal Models with Part-Level Visual Understanding"
---

# PARTONOMY: Large Multimodal Models with Part-Level Visual Understanding

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.20759" class="toolbar-btn" target="_blank">📄 arXiv: 2505.20759v3</a>
  <a href="https://arxiv.org/pdf/2505.20759.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.20759v3" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.20759v3', 'PARTONOMY: Large Multimodal Models with Part-Level Visual Understanding')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Ansel Blume, Jeonghwan Kim, Hyeonjeong Ha, Elen Chatikyan, Xiaomeng Jin, Khanh Duy Nguyen, Nanyun Peng, Kai-Wei Chang, Derek Hoiem, Heng Ji

**分类**: cs.CV, cs.AI

**发布日期**: 2025-05-27 (更新: 2025-10-26)

**备注**: NeurIPS 2025 Spotlight; project page: https://wjdghks950.github.io/partonomy.github.io/

---

## 💡 一句话要点

**提出PARTONOMY以解决大规模多模态模型的部件识别问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多模态模型` `部件识别` `视觉理解` `细粒度推理` `PLUM模型` `数据集构建` `反馈机制`

## 📋 核心要点

1. 现有的大规模多模态模型在部件识别和定位方面存在显著不足，无法有效进行细粒度推理。
2. 本文提出PARTONOMY基准，构建了一个包含丰富部件和物体标签的数据集，并提出PLUM模型以改进部件定位能力。
3. 实验结果显示，PLUM在推理分割、视觉问答和视觉幻觉基准上超越了现有的分割LMM，展现出显著的性能提升。

## 📝 摘要（中文）

现实世界中的物体由独特的、特定于物体的部件组成。识别这些部件对于进行细粒度的组合推理至关重要，但现有的大规模多模态模型（LMMs）在这一看似简单的任务上表现不佳。本文提出了PARTONOMY，一个旨在进行像素级部件定位的LMM基准。PARTONOMY基于现有的部件数据集和我们自己严格注释的图像集构建，涵盖862个部件标签和534个物体标签。与现有数据集不同，PARTONOMY使用专业概念，并挑战模型比较物体的部件、考虑部件与整体的关系，并用视觉分割来证明文本预测的合理性。实验表明，当前最先进的LMMs在部件定位能力上存在显著不足。为了解决这些问题，本文提出了PLUM，一个新的分割LMM，采用跨度标记而非分割标记，并在反馈循环中依赖于先前的预测。

## 🔬 方法详解

**问题定义**：本文旨在解决大规模多模态模型在部件识别和定位方面的不足，现有方法在处理细粒度推理时表现不佳，尤其是在部件与整体关系的理解上存在缺陷。

**核心思路**：论文提出了PARTONOMY基准，利用丰富的部件和物体标签来训练模型，并设计了PLUM模型，通过跨度标记替代分割标记，增强模型的部件定位能力。

**技术框架**：PLUM模型的整体架构包括输入图像的特征提取、部件定位的跨度标记处理，以及基于先前预测的反馈循环机制，确保模型在推理过程中能够利用历史信息。

**关键创新**：PLUM的主要创新在于采用跨度标记而非传统的分割标记，避免了在预训练阶段未见过的标记引起的分布偏移，同时通过反馈机制提升了模型的预测准确性。

**关键设计**：PLUM模型在训练过程中使用了新的损失函数，强调部件与整体的关系，并通过多层次的特征融合来增强模型的表现，确保在细粒度推理任务中具备更强的能力。

## 📊 实验亮点

实验结果显示，预训练的PLUM在推理分割、视觉问答和视觉幻觉基准上显著优于现有的分割LMM，尤其在推理分割任务中，PLUM的表现提升幅度达到了显著的水平，展示了其在部件定位能力上的优势。

## 🎯 应用场景

该研究的潜在应用领域包括智能监控、自动驾驶、机器人视觉等，能够帮助系统更好地理解和处理复杂场景中的物体和部件关系。未来，随着模型性能的提升，可能会推动更广泛的视觉理解任务的进展。

## 📄 摘要（原文）

> Real-world objects are composed of distinctive, object-specific parts. Identifying these parts is key to performing fine-grained, compositional reasoning-yet, large multimodal models (LMMs) struggle to perform this seemingly straightforward task. In this work, we introduce PARTONOMY, an LMM benchmark designed for pixel-level part grounding. We construct PARTONOMY from existing part datasets and our own rigorously annotated set of images, encompassing 862 part labels and 534 object labels for evaluation. Unlike existing datasets that simply ask models to identify generic parts, PARTONOMY uses specialized concepts (e.g., agricultural airplane), and challenges models to compare objects' parts, consider part-whole relationships, and justify textual predictions with visual segmentations. Our experiments demonstrate significant limitations in state-of-the-art LMMs (e.g., LISA-13B achieves only 5.9% gIoU), highlighting a critical gap in their part grounding abilities. We note that existing segmentation-enabled LMMs (segmenting LMMs) have two key architectural shortcomings: they use special [SEG] tokens not seen during pretraining which induce distribution shift, and they discard predicted segmentations instead of using past predictions to guide future ones. To address these deficiencies, we train several part-centric LMMs and propose PLUM, a novel segmenting LMM that uses span tagging instead of segmentation tokens and that conditions on prior predictions in a feedback loop. We find that pretrained PLUM outperforms existing segmenting LMMs on reasoning segmentation, VQA, and visual hallucination benchmarks. In addition, PLUM finetuned on our proposed Explanatory Part Segmentation task is competitive with segmenting LMMs trained on significantly more segmentation data. Our work opens up new avenues towards enabling fine-grained, grounded visual understanding in LMMs.

