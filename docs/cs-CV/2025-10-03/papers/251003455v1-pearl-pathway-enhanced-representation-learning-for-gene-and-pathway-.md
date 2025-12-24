---
layout: default
title: "PEaRL: Pathway-Enhanced Representation Learning for Gene and Pathway Expression Prediction from Histology"
---

# PEaRL: Pathway-Enhanced Representation Learning for Gene and Pathway Expression Prediction from Histology

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2510.03455" class="toolbar-btn" target="_blank">📄 arXiv: 2510.03455v1</a>
  <a href="https://arxiv.org/pdf/2510.03455.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.03455v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2510.03455v1', 'PEaRL: Pathway-Enhanced Representation Learning for Gene and Pathway Expression Prediction from Histology')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Sejuti Majumder, Saarthak Kapse, Moinak Bhattacharya, Xuan Xu, Alisa Yurovsky, Prateek Prasanna

**分类**: cs.CV

**发布日期**: 2025-10-03

---

## 💡 一句话要点

**PEaRL：通过通路增强表示学习，从组织学图像预测基因和通路表达**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `空间转录组学` `组织病理学` `多模态学习` `通路分析` `对比学习`

## 📋 核心要点

1. 现有方法依赖少量高变异基因，限制了预测范围，忽略了塑造组织表型的协同生物学程序。
2. PEaRL通过通路激活得分表示转录组学，利用Transformer编码通路信号，并通过对比学习对齐组织学特征。
3. 实验表明，PEaRL在基因和通路水平的表达预测方面均优于现有方法，Pearson相关系数分别提高了高达58.9%和20.4%。

## 📝 摘要（中文）

本研究提出PEaRL（Pathway Enhanced Representation Learning），一个多模态框架，旨在整合组织病理学和空间转录组学，从而将组织形态与分子功能联系起来。PEaRL通过ssGSEA计算通路激活得分来表示转录组学信息。该方法利用Transformer编码生物学上一致的通路信号，并通过对比学习将其与组织学特征对齐，从而降低维度、提高可解释性并加强跨模态对应关系。在三个癌症空间转录组学数据集（乳腺癌、皮肤癌和淋巴结癌）上的实验结果表明，PEaRL始终优于现有方法，在基因和通路水平的表达预测方面均实现了更高的准确率（Pearson相关系数分别提高了高达58.9%和20.4%）。这些结果表明，基于通路的转录组表示能够产生更具生物学意义且更易于解释的多模态模型，从而推动计算病理学超越基因水平的嵌入。

## 🔬 方法详解

**问题定义**：现有方法在整合组织病理学和空间转录组学时，主要依赖于少量高变异基因，这限制了预测的范围，并且忽略了组织表型是由多个协同作用的生物学通路共同决定的事实。因此，如何更全面、更准确地利用空间转录组学数据，并将其与组织学图像有效整合，是一个亟待解决的问题。

**核心思路**：PEaRL的核心思路是将基因表达信息转化为通路激活得分，从而将基因层面的信息聚合到通路层面，减少了数据的维度，并提高了生物学意义。通过关注通路，模型能够捕捉到基因之间的协同作用，从而更准确地预测基因和通路的表达。同时，利用对比学习，将组织学特征和通路激活得分对齐，从而建立跨模态的联系。

**技术框架**：PEaRL框架主要包含以下几个模块：1) 利用ssGSEA算法计算每个样本的通路激活得分；2) 使用Transformer模型对通路激活得分进行编码，得到通路表示；3) 从组织学图像中提取视觉特征；4) 利用对比学习，将通路表示和视觉特征对齐，学习一个共享的嵌入空间；5) 利用学习到的嵌入空间，预测基因和通路的表达。

**关键创新**：PEaRL的关键创新在于：1) 使用通路激活得分来表示转录组学信息，从而捕捉基因之间的协同作用；2) 利用Transformer模型对通路激活得分进行编码，从而学习到更具生物学意义的通路表示；3) 利用对比学习，将通路表示和视觉特征对齐，从而建立跨模态的联系。与现有方法相比，PEaRL能够更全面、更准确地利用空间转录组学数据，并将其与组织学图像有效整合。

**关键设计**：PEaRL的关键设计包括：1) 使用ssGSEA算法计算通路激活得分，该算法能够有效地评估每个样本中通路的激活程度；2) 使用Transformer模型对通路激活得分进行编码，Transformer模型具有强大的序列建模能力，能够捕捉通路之间的依赖关系；3) 使用对比学习，将通路表示和视觉特征对齐，对比学习的目标是使相似的样本在嵌入空间中更接近，而不相似的样本更远离。损失函数采用InfoNCE损失。

## 📊 实验亮点

PEaRL在三个癌症空间转录组学数据集（乳腺癌、皮肤癌和淋巴结癌）上进行了评估，实验结果表明，PEaRL始终优于现有方法。在基因水平的表达预测方面，PEaRL的Pearson相关系数比现有方法提高了高达58.9%。在通路水平的表达预测方面，PEaRL的Pearson相关系数比现有方法提高了高达20.4%。这些结果表明，PEaRL能够更准确地预测基因和通路的表达。

## 🎯 应用场景

PEaRL具有广泛的应用前景，可用于癌症诊断、预后预测和治疗方案选择。通过整合组织病理学和空间转录组学信息，PEaRL能够更准确地预测基因和通路的表达，从而帮助医生更好地了解肿瘤的生物学特性，并制定更有效的治疗方案。此外，PEaRL还可以用于药物研发，通过预测药物对基因和通路的影响，加速药物的开发过程。

## 📄 摘要（原文）

> Integrating histopathology with spatial transcriptomics (ST) provides a powerful opportunity to link tissue morphology with molecular function. Yet most existing multimodal approaches rely on a small set of highly variable genes, which limits predictive scope and overlooks the coordinated biological programs that shape tissue phenotypes. We present PEaRL (Pathway Enhanced Representation Learning), a multimodal framework that represents transcriptomics through pathway activation scores computed with ssGSEA. By encoding biologically coherent pathway signals with a transformer and aligning them with histology features via contrastive learning, PEaRL reduces dimensionality, improves interpretability, and strengthens cross-modal correspondence. Across three cancer ST datasets (breast, skin, and lymph node), PEaRL consistently outperforms SOTA methods, yielding higher accuracy for both gene- and pathway-level expression prediction (up to 58.9 percent and 20.4 percent increase in Pearson correlation coefficient compared to SOTA). These results demonstrate that grounding transcriptomic representation in pathways produces more biologically faithful and interpretable multimodal models, advancing computational pathology beyond gene-level embeddings.

