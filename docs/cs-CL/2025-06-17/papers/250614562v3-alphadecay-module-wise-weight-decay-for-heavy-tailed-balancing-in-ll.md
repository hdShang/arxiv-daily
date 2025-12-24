---
layout: default
title: "AlphaDecay: Module-wise Weight Decay for Heavy-Tailed Balancing in LLMs"
---

# AlphaDecay: Module-wise Weight Decay for Heavy-Tailed Balancing in LLMs

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.14562" class="toolbar-btn" target="_blank">📄 arXiv: 2506.14562v3</a>
  <a href="https://arxiv.org/pdf/2506.14562.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.14562v3" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.14562v3', 'AlphaDecay: Module-wise Weight Decay for Heavy-Tailed Balancing in LLMs')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Di He, Songjun Tu, Ajay Jaiswal, Li Shen, Ganzhao Yuan, Shiwei Liu, Lu Yin

**分类**: cs.CL, cs.AI, cs.LG

**发布日期**: 2025-06-17 (更新: 2025-11-05)

**🔗 代码/项目**: [GITHUB](https://github.com/hed-ucas/AlphaDecay)

---

## 💡 一句话要点

**提出AlphaDecay以解决LLMs模块间权重衰减不均问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `权重衰减` `自适应学习` `大型语言模型` `重尾自正则化` `谱特性分析` `模型训练` `性能优化`

## 📋 核心要点

1. 现有的权重衰减方法通常为每层分配统一衰减率，未能考虑模块间的结构差异和谱特性，导致性能不足。
2. 本文提出的AlphaDecay方法通过重尾自正则化理论，自适应地为每个模块分配不同的权重衰减强度，以平衡模块间的差异。
3. 在60M到1B参数规模的多项预训练任务中，AlphaDecay在困惑度和泛化能力上均优于传统的统一衰减和其他自适应衰减方法。

## 📝 摘要（中文）

权重衰减是训练大型语言模型（LLMs）的标准正则化技术。传统方法通常为每一层分配统一的衰减率，但忽视了LLMs的结构多样性及模块间的谱特性差异。本文提出了AlphaDecay，一种简单而有效的方法，能够自适应地为LLM的每个模块分配不同的权重衰减强度。该方法基于重尾自正则化（HT-SR）理论，通过分析权重相关矩阵的经验谱密度（ESD）来量化“重尾性”。表现出更明显重尾ESD的模块被分配较弱的衰减，而谱较轻尾的模块则获得较强的衰减。实验表明，AlphaDecay在不同规模的模型上均优于传统的统一衰减和其他自适应衰减基线。

## 🔬 方法详解

**问题定义**：本文旨在解决现有权重衰减方法在大型语言模型中未能考虑模块间结构多样性的问题。统一的衰减率可能导致某些模块学习效果不佳，影响整体性能。

**核心思路**：AlphaDecay通过重尾自正则化理论，分析权重相关矩阵的谱特性，自适应地为每个模块分配不同的权重衰减强度。这样可以针对不同模块的特性进行优化，提升模型的学习能力。

**技术框架**：该方法首先计算每个模块的经验谱密度（ESD），然后根据其重尾性分配权重衰减强度。具体流程包括数据预处理、谱特性分析、衰减强度分配和模型训练等阶段。

**关键创新**：AlphaDecay的创新在于其基于重尾性分析的自适应权重衰减分配，区别于传统的统一衰减方法，能够更好地适应模块间的学习差异。

**关键设计**：在实现中，论文详细描述了如何计算经验谱密度、如何量化重尾性以及如何设置不同模块的衰减强度，确保模型在训练过程中能够有效利用各模块的特性。

## 📊 实验亮点

实验结果显示，AlphaDecay在不同规模的模型上均取得了显著提升，困惑度降低，泛化能力增强。与传统的统一衰减方法相比，AlphaDecay在多个基准任务中表现出更优的性能，具体提升幅度未知。

## 🎯 应用场景

该研究的潜在应用领域包括自然语言处理、对话系统和文本生成等。通过优化大型语言模型的训练过程，AlphaDecay能够提升模型的性能和泛化能力，具有重要的实际价值和未来影响，尤其是在需要高效学习的场景中。

## 📄 摘要（原文）

> Weight decay is a standard regularization technique for training large language models (LLMs). While it is common to assign a uniform decay rate to every layer, this approach overlooks the structural diversity of LLMs and the varying spectral properties across modules. In this paper, we introduce AlphaDecay, a simple yet effective method that adaptively assigns different weight decay strengths to each module of an LLM. Our approach is guided by Heavy-Tailed Self-Regularization (HT-SR) theory, which analyzes the empirical spectral density (ESD) of weight correlation matrices to quantify "heavy-tailedness." Modules exhibiting more pronounced heavy-tailed ESDs, reflecting stronger feature learning, are assigned weaker decay, while modules with lighter-tailed spectra receive stronger decay. Our method leverages tailored weight decay assignments to balance the module-wise differences in spectral properties, leading to improved performance. Extensive pre-training tasks with various model sizes from 60M to 1B demonstrate that AlphaDecay achieves better perplexity and generalization than conventional uniform decay and other adaptive decay baselines. Our code is available at https://github.com/hed-ucas/AlphaDecay.

