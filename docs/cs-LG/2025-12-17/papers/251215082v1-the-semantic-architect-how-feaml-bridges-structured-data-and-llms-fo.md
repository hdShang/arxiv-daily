---
layout: default
title: The Semantic Architect: How FEAML Bridges Structured Data and LLMs for Multi-Label Tasks
---

# The Semantic Architect: How FEAML Bridges Structured Data and LLMs for Multi-Label Tasks

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.15082" class="toolbar-btn" target="_blank">📄 arXiv: 2512.15082v1</a>
  <a href="https://arxiv.org/pdf/2512.15082.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.15082v1" onclick="toggleFavorite(this, '2512.15082v1', 'The Semantic Architect: How FEAML Bridges Structured Data and LLMs for Multi-Label Tasks')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Wanfu Gao, Zebin He, Jun Gao

**分类**: cs.LG

**发布日期**: 2025-12-17

---

## 💡 一句话要点

**FEAML：利用LLM桥接结构化数据与多标签任务，实现自动化特征工程**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多标签学习` `特征工程` `大型语言模型` `自动化机器学习` `代码生成`

## 📋 核心要点

1. 现有基于LLM的特征工程方法难以建模多标签学习中复杂的标签依赖关系，且缺乏针对性优化。
2. FEAML利用LLM的代码生成能力，结合元数据和标签共现矩阵，引导LLM理解数据特征与任务目标。
3. 实验结果表明，FEAML在多个多标签数据集上优于其他特征工程方法，实现了性能提升。

## 📝 摘要（中文）

现有的基于大型语言模型（LLM）的特征工程方法尚未应用于多标签学习任务。它们缺乏对复杂标签依赖关系建模的能力，并且没有针对多标签任务的特性进行专门调整。为了解决上述问题，我们提出了一种用于多标签学习的自动化特征工程方法——多标签学习的特征工程自动化（FEAML），该方法利用LLM的代码生成能力。通过利用元数据和标签共现矩阵，引导LLM理解数据特征和任务目标之间的关系，从而生成高质量的特征。新生成的特征在模型精度方面进行评估，以评估其有效性，同时使用Pearson相关系数来检测冗余。FEAML进一步将评估结果作为反馈，以驱动LLM在后续迭代中不断优化代码生成。通过将LLM与反馈机制相结合，FEAML实现了高效、可解释和自我改进的特征工程范式。在各种多标签数据集上的实验结果表明，我们的FEAML优于其他特征工程方法。

## 🔬 方法详解

**问题定义**：论文旨在解决多标签学习任务中，现有基于LLM的特征工程方法无法有效建模标签依赖关系，且缺乏针对性优化的问题。现有方法通常无法充分利用多标签数据的特性，导致特征工程的效率和效果受限。

**核心思路**：论文的核心思路是利用LLM的代码生成能力，结合多标签数据的元数据和标签共现矩阵，引导LLM理解数据特征和任务目标之间的关系，从而自动生成高质量的特征。通过反馈机制，不断优化LLM的代码生成过程，实现特征工程的自动化和自改进。

**技术框架**：FEAML的技术框架主要包含以下几个阶段：1) 数据准备：收集多标签数据集的元数据和计算标签共现矩阵。2) LLM引导：利用元数据和标签共现矩阵，引导LLM生成特征工程代码。3) 特征评估：评估新生成的特征在模型精度方面的有效性，并使用Pearson相关系数检测冗余。4) 反馈优化：将评估结果作为反馈，驱动LLM在后续迭代中不断优化代码生成。

**关键创新**：FEAML的关键创新在于将LLM的代码生成能力与多标签数据的特性相结合，实现了一种自动化、可解释和自改进的特征工程范式。与现有方法相比，FEAML能够更有效地利用多标签数据的标签依赖关系，并根据评估结果不断优化特征工程过程。

**关键设计**：论文的关键设计包括：1) 如何利用元数据和标签共现矩阵引导LLM生成特征工程代码；2) 如何设计特征评估指标，以评估特征的有效性和冗余性；3) 如何设计反馈机制，将评估结果反馈给LLM，以驱动其不断优化代码生成。具体的参数设置、损失函数和网络结构等技术细节在论文中未详细说明，属于未知信息。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.15082v1/AFT1.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.15082v1/FEAML18.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.15082v1/prompt.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

实验结果表明，FEAML在多个多标签数据集上优于其他特征工程方法。具体的性能数据和提升幅度在摘要中未给出，属于未知信息。但总体而言，FEAML展现了其在多标签特征工程方面的有效性和优越性。

## 🎯 应用场景

FEAML可应用于各种多标签分类任务，例如文本分类、图像分类、生物信息学等。该方法能够自动生成高质量的特征，提高多标签分类模型的性能，降低人工特征工程的成本。未来，FEAML有望进一步扩展到其他类型的机器学习任务，并与其他自动化机器学习技术相结合，实现更高效、更智能的机器学习流程。

## 📄 摘要（原文）

> Existing feature engineering methods based on large language models (LLMs) have not yet been applied to multi-label learning tasks. They lack the ability to model complex label dependencies and are not specifically adapted to the characteristics of multi-label tasks. To address the above issues, we propose Feature Engineering Automation for Multi-Label Learning (FEAML), an automated feature engineering method for multi-label classification which leverages the code generation capabilities of LLMs. By utilizing metadata and label co-occurrence matrices, LLMs are guided to understand the relationships between data features and task objectives, based on which high-quality features are generated. The newly generated features are evaluated in terms of model accuracy to assess their effectiveness, while Pearson correlation coefficients are used to detect redundancy. FEAML further incorporates the evaluation results as feedback to drive LLMs to continuously optimize code generation in subsequent iterations. By integrating LLMs with a feedback mechanism, FEAML realizes an efficient, interpretable and self-improving feature engineering paradigm. Empirical results on various multi-label datasets demonstrate that our FEAML outperforms other feature engineering methods.

