---
layout: default
title: Why Text Prevails: Vision May Undermine Multimodal Medical Decision Making
---

# Why Text Prevails: Vision May Undermine Multimodal Medical Decision Making

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.13747" class="toolbar-btn" target="_blank">📄 arXiv: 2512.13747</a>
  <a href="https://arxiv.org/pdf/2512.13747.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.13747" onclick="toggleFavorite(this, '2512.13747', 'Why Text Prevails: Vision May Undermine Multimodal Medical Decision Making')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Siyuan Dai, Lunxiao Li, Kun Zhao, Eardi Lila, Paul K. Crane, Heng Huang, Dongkuan Xu, Haoteng Tang, Liang Zhan

**分类**: cs.CV, cs.AI

**发布日期**: 2025-12-18

---

## 💡 一句话要点

**研究表明：在医学决策中，文本信息优于视觉信息，多模态融合可能适得其反**

🎯 **匹配领域**: **支柱四：生成式动作 (Generative Motion)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `医学决策` `多模态学习` `视觉语言模型` `文本信息` `阿尔茨海默病` `胸部X光片` `MIMIC-CXR`

## 📋 核心要点

1. 现有MLLMs在生物医学决策任务中表现不佳，尤其是在视觉信息微妙或复杂的场景下，面临挑战。
2. 研究核心在于分析文本、视觉以及多模态信息在医学决策中的作用，并探索提升多模态性能的策略。
3. 实验结果表明，文本信息在医学决策中起主导作用，多模态融合效果不佳，并提出了三种改进策略。

## 📝 摘要（中文）

随着大型语言模型（LLMs）的快速发展，先进的多模态大型语言模型（MLLMs）在视觉-语言任务中展现了令人印象深刻的零样本能力。然而，在生物医学领域，即使是最先进的MLLMs在基本的医学决策（MDM）任务中也表现不佳。本研究通过两个具有挑战性的数据集来调查这一局限性：（1）三阶段阿尔茨海默病（AD）分类（正常、轻度认知障碍、痴呆），其中类别差异在视觉上很微妙；（2）MIMIC-CXR胸部X光片分类，包含14种非互斥的疾病。实证研究表明，仅文本推理始终优于仅视觉或视觉-文本设置，多模态输入通常比仅文本表现更差。为了缓解这个问题，我们探索了三种策略：（1）使用带有原因注释的示例进行上下文学习；（2）视觉描述后进行仅文本推理；（3）使用分类监督对视觉塔进行少量样本微调。这些发现表明，当前的MLLMs缺乏扎实的视觉理解，并为改善医疗保健中的多模态决策提供了有希望的方向。

## 🔬 方法详解

**问题定义**：论文旨在解决多模态大型语言模型（MLLMs）在医学决策（MDM）任务中表现不佳的问题，尤其是在视觉信息不明显或容易产生歧义的情况下。现有方法过度依赖视觉信息，导致性能下降，未能充分利用文本信息的优势。

**核心思路**：论文的核心思路是揭示文本信息在医学决策中的主导地位，并探索如何更好地利用文本信息来提升多模态模型的性能。通过对比文本、视觉和多模态输入在不同医学数据集上的表现，验证文本信息的重要性，并提出相应的改进策略。

**技术框架**：整体框架包括数据准备、模型选择、实验设计和结果分析四个主要部分。首先，选择两个具有挑战性的医学数据集：阿尔茨海默病（AD）分类和MIMIC-CXR胸部X光片分类。然后，使用现有的MLLMs作为基线模型，并设计不同的输入模式（仅文本、仅视觉、多模态）。最后，通过实验对比不同输入模式下的性能，并分析结果。

**关键创新**：论文的关键创新在于揭示了在医学决策任务中，文本信息的重要性超过视觉信息，并且多模态融合可能适得其反。这一发现挑战了传统的视觉-语言模型的设计理念，并为未来的研究提供了新的方向。

**关键设计**：论文的关键设计包括：(1) 使用reason-annotated exemplars进行上下文学习，以提升模型的推理能力；(2) 使用视觉描述模型生成文本描述，然后进行文本推理，以缓解视觉信息的不足；(3) 使用少量样本对视觉塔进行微调，以提升视觉特征的表达能力。这些设计旨在更好地利用文本信息，并提升多模态模型的性能。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.13747/fig.png" alt="fig_0" loading="lazy">
</figure>
</div>

## 📊 实验亮点

实验结果表明，在阿尔茨海默病分类和MIMIC-CXR胸部X光片分类任务中，仅文本推理的性能始终优于仅视觉或视觉-文本设置。多模态输入甚至可能比仅文本表现更差。通过提出的三种改进策略，可以在一定程度上提升多模态模型的性能，但仍有很大的提升空间。

## 🎯 应用场景

该研究成果可应用于辅助医生进行疾病诊断和治疗决策，尤其是在影像学诊断方面。通过优化多模态模型的性能，可以提高诊断的准确性和效率，减少误诊和漏诊的风险。未来的研究可以进一步探索如何更好地融合文本和视觉信息，开发更智能、更可靠的医学决策支持系统。

## 📄 摘要（原文）

> With the rapid progress of large language models (LLMs), advanced multimodal large language models (MLLMs) have demonstrated impressive zero-shot capabilities on vision-language tasks. In the biomedical domain, however, even state-of-the-art MLLMs struggle with basic Medical Decision Making (MDM) tasks. We investigate this limitation using two challenging datasets: (1) three-stage Alzheimer's disease (AD) classification (normal, mild cognitive impairment, dementia), where category differences are visually subtle, and (2) MIMIC-CXR chest radiograph classification with 14 non-mutually exclusive conditions. Our empirical study shows that text-only reasoning consistently outperforms vision-only or vision-text settings, with multimodal inputs often performing worse than text alone. To mitigate this, we explore three strategies: (1) in-context learning with reason-annotated exemplars, (2) vision captioning followed by text-only inference, and (3) few-shot fine-tuning of the vision tower with classification supervision. These findings reveal that current MLLMs lack grounded visual understanding and point to promising directions for improving multimodal decision making in healthcare.

