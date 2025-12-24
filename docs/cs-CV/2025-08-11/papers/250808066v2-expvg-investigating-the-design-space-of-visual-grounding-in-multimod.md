---
layout: default
title: "ExpVG: Investigating the Design Space of Visual Grounding in Multimodal Large Language Model"
---

# ExpVG: Investigating the Design Space of Visual Grounding in Multimodal Large Language Model

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.08066" class="toolbar-btn" target="_blank">📄 arXiv: 2508.08066v2</a>
  <a href="https://arxiv.org/pdf/2508.08066.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.08066v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.08066v2', 'ExpVG: Investigating the Design Space of Visual Grounding in Multimodal Large Language Model')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Weitai Kang, Weiming Zhuang, Zhizhong Li, Yan Yan, Lingjuan Lyu

**分类**: cs.CV, cs.AI, cs.CL, cs.LG

**发布日期**: 2025-08-11 (更新: 2025-08-19)

**备注**: 8 pages for the main paper

---

## 💡 一句话要点

**提出ExpVG以系统研究多模态大语言模型中的视觉定位问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多模态大语言模型` `视觉定位` `LLaVA-1.5` `消融研究` `设计选择` `性能提升`

## 📋 核心要点

1. 现有的多模态大语言模型在视觉定位任务中存在设计选择不一致和缺乏系统验证的问题。
2. 本文通过对不同视觉定位范式的探索和对基础数据设计的消融研究，提出了一种系统化的研究方法。
3. 实验结果表明，优化后的模型在RefCOCO/+/g数据集上分别提升了+5.6% / +6.9% / +7.0%的性能。

## 📝 摘要（中文）

多模态大语言模型（MLLMs）在细粒度多模态能力方面的研究日益重要，尤其是在视觉定位（VG）问题上。现有方法在微调MLLMs以解决VG时，采用了不同的设计选择，缺乏系统验证。为此，本文对影响MLLMs VG性能的多种设计选择进行了全面研究，使用LLaVA-1.5进行分析，探索不同的视觉定位范式，并通过消融研究优化VG任务的微调设计。最终，研究结果显示在RefCOCO/+/g上分别提升了+5.6% / +6.9% / +7.0%。

## 🔬 方法详解

**问题定义**：本文旨在解决多模态大语言模型在视觉定位任务中设计选择不一致和缺乏系统验证的问题。现有方法往往没有系统性地评估不同设计对性能的影响，导致效果不稳定。

**核心思路**：论文通过对不同视觉定位范式的探索，识别出最有效的设计，并通过消融研究优化微调过程，以提高模型在视觉定位任务中的表现。

**技术框架**：研究使用LLaVA-1.5作为基础模型，分析不同的视觉定位设计选择，主要包括视觉信息的处理方式和数据集的构建。整个流程包括设计选择的评估、消融实验的实施以及性能的比较。

**关键创新**：最重要的创新在于系统性地分析了多种设计选择对视觉定位性能的影响，填补了现有研究中的空白，并为后续研究提供了实证依据。

**关键设计**：在微调过程中，采用了针对视觉定位任务的特定损失函数和数据增强策略，确保模型能够更好地理解和处理视觉信息。

## 📊 实验亮点

实验结果显示，优化后的模型在RefCOCO/+/g数据集上分别提升了+5.6% / +6.9% / +7.0%的性能，相较于LLaVA-1.5模型，展现了显著的改进，验证了所提出设计选择的有效性。

## 🎯 应用场景

该研究的潜在应用领域包括智能助手、自动驾驶、机器人视觉等，能够帮助这些系统更准确地理解和处理视觉信息。未来，随着多模态大语言模型的进一步发展，该研究的成果有望推动更复杂的视觉理解任务的实现。

## 📄 摘要（原文）

> Fine-grained multimodal capability in Multimodal Large Language Models (MLLMs) has emerged as a critical research direction, particularly for tackling the visual grounding (VG) problem. Despite the strong performance achieved by existing approaches, they often employ disparate design choices when fine-tuning MLLMs for VG, lacking systematic verification to support these designs. To bridge this gap, this paper presents a comprehensive study of various design choices that impact the VG performance of MLLMs. We conduct our analysis using LLaVA-1.5, which has been widely adopted in prior empirical studies of MLLMs. While more recent models exist, we follow this convention to ensure our findings remain broadly applicable and extendable to other architectures. We cover two key aspects: (1) exploring different visual grounding paradigms in MLLMs, identifying the most effective design, and providing our insights; and (2) conducting ablation studies on the design of grounding data to optimize MLLMs' fine-tuning for the VG task. Finally, our findings contribute to a stronger MLLM for VG, achieving improvements of +5.6% / +6.9% / +7.0% on RefCOCO/+/g over the LLaVA-1.5.

