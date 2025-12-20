---
layout: default
title: Feature-Selective Representation Misdirection for Machine Unlearning
---

# Feature-Selective Representation Misdirection for Machine Unlearning

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.16297" class="toolbar-btn" target="_blank">📄 arXiv: 2512.16297v1</a>
  <a href="https://arxiv.org/pdf/2512.16297.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.16297v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.16297v1', 'Feature-Selective Representation Misdirection for Machine Unlearning')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Taozhao Chen, Linghan Huang, Kim-Kwang Raymond Choo, Huaming Chen

**分类**: cs.LG, cs.AI

**发布日期**: 2025-12-18

---

## 💡 一句话要点

**提出选择性表征误导(SRMU)框架，用于解决LLM中知识遗忘难题，兼顾安全与效用。**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `机器遗忘` `大型语言模型` `表征学习` `激活编辑` `知识移除`

## 📋 核心要点

1. 现有机器遗忘方法在遗忘数据和保留数据高度纠缠时表现不佳，容易导致模型效用下降或无法保证安全性。
2. SRMU通过激活编辑，有选择性地对模型表征进行扰动，抑制有害信息，同时保留有益信息，实现更精准的知识遗忘。
3. 实验表明，SRMU在低/高纠缠场景下均优于现有方法，在20-30%数据重叠时仍有效，且效用损失最小。

## 📝 摘要（中文）

随着大型语言模型（LLM）在安全关键和受监管领域得到越来越多的应用，模型中保留的敏感或违禁知识带来了越来越大的风险，包括隐私泄露、不符合法规以及潜在的滥用等等。近期的研究表明，机器遗忘可以帮助确保已部署的模型符合不断变化的法律、安全和治理要求。然而，当前的遗忘技术假设遗忘数据集和保留数据集之间存在清晰的分离，这在具有高度纠缠分布的实际操作环境中是具有挑战性的。在这种情况下，基于扰动的方法通常会降低模型的通用效用或无法确保安全性。为了解决这个问题，我们提出了一种用于遗忘的选择性表征误导（SRMU），这是一种新颖的、有原则的激活编辑框架，它强制执行特征感知和方向控制的扰动。与不加区分的模型权重扰动不同，SRMU采用具有激活重要性图的结构化误导向量。目标是允许SRMU选择性地抑制有害表征，同时保持对良性表征的效用。在广泛使用的WMDP基准上，针对低纠缠和高纠缠配置进行了实验。实验结果表明，SRMU提供了最先进的遗忘性能，同时效用损失最小，并且在现有基线崩溃的20-30％重叠下仍然有效。SRMU为基于LLM的新兴应用中的安全驱动模型治理、隐私合规性和受控知识移除提供了坚实的基础。我们在https://figshare.com/s/d5931192a8824de26aff发布了复制包。

## 🔬 方法详解

**问题定义**：论文旨在解决大型语言模型（LLM）中知识遗忘的问题，特别是当需要遗忘的数据与需要保留的数据高度纠缠时。现有的遗忘方法，如基于扰动的方法，要么会降低模型的整体性能（效用），要么无法有效地移除有害知识，从而无法满足安全和合规性要求。

**核心思路**：SRMU的核心思路是选择性地修改模型内部的表征，使其不再包含需要遗忘的信息，同时尽可能地保留模型在其他任务上的性能。通过激活编辑的方式，对模型中的激活值进行有方向性的扰动，从而实现对特定特征的抑制或增强。

**技术框架**：SRMU框架主要包含以下几个步骤：1) **激活重要性图生成**：评估模型中每个激活值对于特定任务的重要性。2) **误导向量生成**：根据激活重要性图，生成一个结构化的误导向量，用于指导激活值的修改方向和幅度。3) **激活编辑**：将误导向量应用于模型的激活值，从而实现对模型表征的修改。

**关键创新**：SRMU的关键创新在于其选择性和方向性的扰动方式。与传统的对模型权重进行全局扰动的方法不同，SRMU能够根据激活值的重要性，有选择性地对模型表征进行修改，从而在实现知识遗忘的同时，尽可能地保留模型的整体性能。此外，SRMU还通过误导向量的设计，实现了对扰动方向的控制，从而能够更有效地抑制有害信息。

**关键设计**：SRMU的关键设计包括：1) **激活重要性评估方法**：如何准确地评估每个激活值对于特定任务的重要性，是SRMU的关键。论文中可能采用了某种梯度或注意力机制来评估激活值的重要性。2) **误导向量的生成方式**：误导向量的结构和生成方式直接影响了SRMU的遗忘效果和性能保留能力。论文中可能采用了某种优化算法或启发式方法来生成误导向量。3) **激活编辑的具体实现**：如何将误导向量应用于模型的激活值，也是SRMU的关键。论文中可能采用了某种加权平均或线性组合的方式来实现激活编辑。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.16297v1/img/overviewSRMU.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.16297v1/img/combinationablation.png" alt="fig_1" loading="lazy">
</figure>
</div>

## 📊 实验亮点

实验结果表明，SRMU在WMDP基准测试中取得了最先进的遗忘性能，同时保持了最小的效用损失。在高数据纠缠场景下（20-30%重叠），SRMU仍然有效，而现有的基线方法则失效。这些结果表明，SRMU是一种鲁棒且有效的知识遗忘方法。

## 🎯 应用场景

SRMU技术可应用于各种需要知识遗忘的场景，例如：1)保护用户隐私，移除模型中包含的个人敏感信息；2)遵守法律法规，移除模型中包含的违禁内容；3)模型安全治理，移除模型中存在的偏见或有害知识。该技术有助于提升LLM在安全关键领域的应用，并促进负责任的AI发展。

## 📄 摘要（原文）

> As large language models (LLMs) are increasingly adopted in safety-critical and regulated sectors, the retention of sensitive or prohibited knowledge introduces escalating risks, ranging from privacy leakage to regulatory non-compliance to to potential misuse, and so on. Recent studies suggest that machine unlearning can help ensure deployed models comply with evolving legal, safety, and governance requirements. However, current unlearning techniques assume clean separation between forget and retain datasets, which is challenging in operational settings characterized by highly entangled distributions. In such scenarios, perturbation-based methods often degrade general model utility or fail to ensure safety. To address this, we propose Selective Representation Misdirection for Unlearning (SRMU), a novel principled activation-editing framework that enforces feature-aware and directionally controlled perturbations. Unlike indiscriminate model weights perturbations, SRMU employs a structured misdirection vector with an activation importance map. The goal is to allow SRMU selectively suppresses harmful representations while preserving the utility on benign ones. Experiments are conducted on the widely used WMDP benchmark across low- and high-entanglement configurations. Empirical results reveal that SRMU delivers state-of-the-art unlearning performance with minimal utility losses, and remains effective under 20-30\% overlap where existing baselines collapse. SRMU provides a robust foundation for safety-driven model governance, privacy compliance, and controlled knowledge removal in the emerging LLM-based applications. We release the replication package at https://figshare.com/s/d5931192a8824de26aff.

