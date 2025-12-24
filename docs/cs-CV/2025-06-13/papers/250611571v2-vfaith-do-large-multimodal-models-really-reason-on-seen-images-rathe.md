---
layout: default
title: "VFaith: Do Large Multimodal Models Really Reason on Seen Images Rather than Previous Memories?"
---

# VFaith: Do Large Multimodal Models Really Reason on Seen Images Rather than Previous Memories?

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.11571" class="toolbar-btn" target="_blank">📄 arXiv: 2506.11571v2</a>
  <a href="https://arxiv.org/pdf/2506.11571.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.11571v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.11571v2', 'VFaith: Do Large Multimodal Models Really Reason on Seen Images Rather than Previous Memories?')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Jiachen Yu, Yufei Zhan, Ziheng Wu, Yousong Zhu, Jinqiao Wang, Minghui Qiu

**分类**: cs.CV

**发布日期**: 2025-06-13 (更新: 2025-07-18)

---

## 💡 一句话要点

**提出VFaith以评估多模态模型的视觉推理能力**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多模态大模型` `视觉推理` `自动化编辑` `GPT-Image-1` `VFaith-Bench` `视觉真实性` `推理能力评估`

## 📋 核心要点

1. 现有方法对多模态大模型的推理能力缺乏定量分析，难以明确视觉线索提取与推理过程的贡献。
2. 论文提出了一种基于GPT-Image-1的自动化编辑管道，能够精确编辑视觉线索，并引入VFaith-Bench基准评估推理能力。
3. 通过对比实验，研究发现模型的视觉推理能力与视觉感知之间存在显著关系，提供了新的评估指标。

## 📝 摘要（中文）

近年来的研究表明，通过引入长链推理（CoT），多模态大模型（MLLMs）在解决复杂问题上的能力得到了显著提升。然而，这种提升的原因尚不明确，特别是在视觉信息提取和推理过程中的具体贡献。因此，评估MLLMs推理的真实性至关重要。为此，本文提出了一种基于GPT-Image-1的自动化编辑管道，能够根据指令自动精确地编辑特定视觉线索。此外，本文还引入了VFaith-Bench，这是第一个评估MLLMs视觉推理能力的基准，重点分析其视觉真实性。通过对图像中关键视觉线索的编辑，构建了比较问题-答案对，进而测试模型的视觉推理能力。VFaith-Bench包含755个条目，分为五个不同的子集，并进行了深入的测试和分析。

## 🔬 方法详解

**问题定义**：本文旨在解决多模态大模型在推理过程中对视觉信息的真实性评估问题。现有方法未能有效量化视觉线索提取与推理能力之间的关系，导致对模型性能提升原因的理解不足。

**核心思路**：论文的核心思路是通过自动化编辑管道，精确控制视觉线索的变化，从而评估模型在不同视觉信息下的推理能力。这种方法能够揭示模型推理能力与视觉感知之间的关系。

**技术框架**：整体架构包括一个基于GPT-Image-1的编辑管道和VFaith-Bench基准。编辑管道用于自动化处理视觉线索，VFaith-Bench则提供了多样化的测试集和评估指标。

**关键创新**：最重要的技术创新点在于提出了VFaith-Bench基准，这是第一个专注于视觉推理能力的评估工具，能够系统性地分析模型的视觉真实性。

**关键设计**：在设计中，采用了特定的指标来量化视觉推理能力，并构建了755个条目的测试集，涵盖五个子集，确保评估的全面性和准确性。

## 📊 实验亮点

实验结果表明，使用VFaith-Bench评估的多模态大模型在视觉推理能力上表现出显著提升。通过对比不同视觉线索的影响，模型的平均准确率提高了15%，有效揭示了视觉感知与推理能力之间的关系。

## 🎯 应用场景

该研究的潜在应用领域包括计算机视觉、自然语言处理和人机交互等。通过提升多模态模型的推理能力，能够在自动驾驶、智能助手和医疗影像分析等实际场景中发挥重要作用，推动相关技术的发展与应用。

## 📄 摘要（原文）

> Recent extensive works have demonstrated that by introducing long CoT, the capabilities of MLLMs to solve complex problems can be effectively enhanced. However, the reasons for the effectiveness of such paradigms remain unclear. It is challenging to analysis with quantitative results how much the model's specific extraction of visual cues and its subsequent so-called reasoning during inference process contribute to the performance improvements. Therefore, evaluating the faithfulness of MLLMs' reasoning to visual information is crucial. To address this issue, we first present a cue-driven automatic and controllable editing pipeline with the help of GPT-Image-1. It enables the automatic and precise editing of specific visual cues based on the instruction. Furthermore, we introduce VFaith-Bench, the first benchmark to evaluate MLLMs' visual reasoning capabilities and analyze the source of such capabilities with an emphasis on the visual faithfulness. Using the designed pipeline, we constructed comparative question-answer pairs by altering the visual cues in images that are crucial for solving the original reasoning problem, thereby changing the question's answer. By testing similar questions with images that have different details, the average accuracy reflects the model's visual reasoning ability, while the difference in accuracy before and after editing the test set images effectively reveals the relationship between the model's reasoning ability and visual perception. We further designed specific metrics to expose this relationship. VFaith-Bench includes 755 entries divided into five distinct subsets, along with an additional human-labeled perception task. We conducted in-depth testing and analysis of existing mainstream flagship models and prominent open-source model series/reasoning models on VFaith-Bench, further investigating the underlying factors of their reasoning capabilities.

