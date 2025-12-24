---
layout: default
title: "VGR: Visual Grounded Reasoning"
---

# VGR: Visual Grounded Reasoning

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.11991" class="toolbar-btn" target="_blank">📄 arXiv: 2506.11991v2</a>
  <a href="https://arxiv.org/pdf/2506.11991.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.11991v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.11991v2', 'VGR: Visual Grounded Reasoning')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Jiacong Wang, Zijian Kang, Haochen Wang, Haiyong Jiang, Jiawen Li, Bohong Wu, Ya Wang, Jiao Ran, Xiao Liang, Chao Feng, Jun Xiao

**分类**: cs.CV, cs.AI, cs.CL

**发布日期**: 2025-06-13 (更新: 2025-06-16)

**备注**: 9 pages, 4 figures

---

## 💡 一句话要点

**提出VGR以解决多模态推理中的语言偏见问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多模态推理` `视觉感知` `语言模型` `图像理解` `深度学习` `推理机制` `区域检测`

## 📋 核心要点

1. 现有多模态推理方法主要依赖语言推理，导致语言偏见，且难以处理复杂的视觉推理任务。
2. VGR通过检测图像中的相关区域并结合视觉信息进行推理，提升了模型的多模态理解能力。
3. 在LLaVA-NeXT-7B基线模型上，VGR在多个基准测试中表现优异，显著提高了推理性能。

## 📝 摘要（中文）

在多模态链式推理领域，现有方法主要依赖于纯语言空间的推理，导致语言偏见，并且局限于数学或科学领域。为了解决这些局限性，本文提出了一种新颖的多模态大语言模型VGR，具备增强的细粒度视觉感知能力。VGR首先检测相关区域以帮助解决问题，然后基于回放的图像区域提供精确答案。实验表明，VGR在多模态基准测试中表现优异，相较于基线模型，显著提高了性能。

## 🔬 方法详解

**问题定义**：本文旨在解决现有多模态推理方法在语言空间推理中存在的偏见和局限性，特别是在处理复杂视觉推理任务时的不足。

**核心思路**：VGR的核心思路是通过检测图像中的相关区域，结合视觉信息与语言推理，提供更为准确的答案。这种设计使得模型能够更全面地理解图像细节，从而提升推理能力。

**技术框架**：VGR的整体架构包括两个主要阶段：首先是区域检测阶段，模型选择与问题相关的边界框；其次是回放阶段，将选定的图像区域整合进推理过程中，增强多模态理解。

**关键创新**：VGR的主要创新在于引入了视觉区域的回放机制，使得模型在推理时不仅依赖语言信息，还能有效利用图像信息。这一设计与传统方法的本质区别在于其多模态融合的深度。

**关键设计**：在模型设计中，VGR使用了一个大规模的SFT数据集，包含视觉基础和语言推理混合的数据。此外，模型在图像令牌数量上仅使用基线的30%，但在多个基准测试中取得了显著的性能提升。

## 📊 实验亮点

VGR在LLaVA-NeXT-7B基线模型上表现出色，在MMStar、AI2D和ChartQA等多模态基准测试中分别提高了4.1、7.1和12.9的分数，且仅使用了30%的图像令牌数量，显示出其在效率和效果上的显著优势。

## 🎯 应用场景

VGR的研究成果在多个领域具有广泛的应用潜力，包括智能问答系统、自动图像描述生成、以及复杂视觉推理任务等。通过提升模型的多模态理解能力，VGR能够为实际应用提供更为准确和全面的解决方案，推动人工智能在视觉理解方面的进步。

## 📄 摘要（原文）

> In the field of multimodal chain-of-thought (CoT) reasoning, existing approaches predominantly rely on reasoning on pure language space, which inherently suffers from language bias and is largely confined to math or science domains. This narrow focus limits their ability to handle complex visual reasoning tasks that demand comprehensive understanding of image details. To address these limitations, this paper introduces VGR, a novel reasoning multimodal large language model (MLLM) with enhanced fine-grained visual perception capabilities. Unlike traditional MLLMs that answer the question or reasoning solely on the language space, our VGR first detects relevant regions that may help to solve problems, and then provides precise answers based on replayed image regions. To achieve this, we conduct a large-scale SFT dataset called VGR -SFT that contains reasoning data with mixed vision grounding and language deduction. The inference pipeline of VGR allows the model to choose bounding boxes for visual reference and a replay stage is introduced to integrates the corresponding regions into the reasoning process, enhancing multimodel comprehension. Experiments on the LLaVA-NeXT-7B baseline show that VGR achieves superior performance on multi-modal benchmarks requiring comprehensive image detail understanding. Compared to the baseline, VGR uses only 30\% of the image token count while delivering scores of +4.1 on MMStar, +7.1 on AI2D, and a +12.9 improvement on ChartQA.

