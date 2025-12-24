---
layout: default
title: "MGT-Prism: Enhancing Domain Generalization for Machine-Generated Text Detection via Spectral Alignment"
---

# MGT-Prism: Enhancing Domain Generalization for Machine-Generated Text Detection via Spectral Alignment

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.13768" class="toolbar-btn" target="_blank">📄 arXiv: 2508.13768v2</a>
  <a href="https://arxiv.org/pdf/2508.13768.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.13768v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.13768v2', 'MGT-Prism: Enhancing Domain Generalization for Machine-Generated Text Detection via Spectral Alignment')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Shengchao Liu, Xiaoming Liu, Chengzhengxu Li, Zhaohan Zhang, Guoxin Ma, Yu Lan, Shuai Xiao

**分类**: cs.CL

**发布日期**: 2025-08-19 (更新: 2025-08-24)

---

## 💡 一句话要点

**提出MGT-Prism以解决机器生成文本检测的领域泛化问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `机器生成文本` `领域泛化` `频域分析` `动态谱对齐` `文本检测`

## 📋 核心要点

1. 现有的机器生成文本检测方法在不同领域间的泛化能力较差，难以应对领域偏移带来的挑战。
2. 论文提出MGT-Prism，通过频域分析文本表示，设计低频域过滤模块和动态谱对齐策略以提升领域泛化能力。
3. 实验结果显示，MGT-Prism在11个测试数据集上平均提高了0.90%的准确率和0.92%的F1分数，表现优于现有方法。

## 📝 摘要（中文）

大型语言模型在生成流畅且连贯的文本方面表现出越来越强的能力，这些文本与人类的写作风格高度相似。然而，现有的机器生成文本（MGT）检测器在同一领域训练和测试时表现良好，但在未见领域的泛化能力较差，主要由于不同来源数据之间的领域偏移。本文提出MGT-Prism，从频域的角度出发，旨在改善MGT检测的领域泛化能力。通过分析文本在频域中的表示，观察到不同领域间存在一致的谱模式，而MGT与人类写作文本（HWT）之间在幅度上存在显著差异。基于这一观察，设计了低频域过滤模块和动态谱对齐策略，以提取任务特定且领域不变的特征，从而提升检测器在领域泛化中的表现。大量实验表明，MGT-Prism在11个测试数据集上平均提高了0.90%的准确率和0.92%的F1分数，超越了现有的最先进基线。

## 🔬 方法详解

**问题定义**：本文旨在解决机器生成文本检测在不同领域间的泛化能力不足的问题。现有方法在同一领域内表现良好，但在面对领域偏移时效果显著下降。

**核心思路**：论文的核心思路是通过频域分析文本表示，发现不同领域间存在一致的谱模式，而MGT与HWT在幅度上有显著差异。基于此，设计了低频域过滤模块以去除对领域偏移敏感的特征，并引入动态谱对齐策略以提取领域不变的特征。

**技术框架**：MGT-Prism的整体架构包括两个主要模块：低频域过滤模块和动态谱对齐模块。前者用于过滤掉受领域影响的特征，后者则用于对齐不同领域的频谱特征，以增强模型的泛化能力。

**关键创新**：MGT-Prism的关键创新在于从频域的角度出发，利用谱模式的稳定性和幅度的差异性来设计检测器，显著提升了领域泛化能力。这一方法与传统的基于文本内容的检测方法有本质区别。

**关键设计**：在设计中，低频域过滤模块采用了特定的频率范围来筛选特征，动态谱对齐策略则使用了自适应算法来调整不同领域间的频谱特征。此外，损失函数的设计也考虑了领域不变性，以进一步提升模型的性能。

## 📊 实验亮点

实验结果表明，MGT-Prism在11个测试数据集上平均提高了0.90%的准确率和0.92%的F1分数，超越了当前最先进的基线方法。这一显著提升证明了其在领域泛化能力上的有效性。

## 🎯 应用场景

该研究的潜在应用领域包括社交媒体内容监测、学术不端检测以及自动化内容审核等。通过提升机器生成文本的检测能力，MGT-Prism能够有效防止虚假信息的传播，维护信息的真实性和可靠性。未来，该方法有望在更广泛的文本生成和检测任务中发挥重要作用。

## 📄 摘要（原文）

> Large Language Models have shown growing ability to generate fluent and coherent texts that are highly similar to the writing style of humans. Current detectors for Machine-Generated Text (MGT) perform well when they are trained and tested in the same domain but generalize poorly to unseen domains, due to domain shift between data from different sources. In this work, we propose MGT-Prism, an MGT detection method from the perspective of the frequency domain for better domain generalization. Our key insight stems from analyzing text representations in the frequency domain, where we observe consistent spectral patterns across diverse domains, while significant discrepancies in magnitude emerge between MGT and human-written texts (HWTs). The observation initiates the design of a low frequency domain filtering module for filtering out the document-level features that are sensitive to domain shift, and a dynamic spectrum alignment strategy to extract the task-specific and domain-invariant features for improving the detector's performance in domain generalization. Extensive experiments demonstrate that MGT-Prism outperforms state-of-the-art baselines by an average of 0.90% in accuracy and 0.92% in F1 score on 11 test datasets across three domain-generalization scenarios.

