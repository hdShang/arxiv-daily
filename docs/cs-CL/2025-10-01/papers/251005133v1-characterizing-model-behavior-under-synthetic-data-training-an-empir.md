---
layout: default
title: "Characterizing Model Behavior Under Synthetic Data Training: An Empirical Study Across Scales and Mixing Ratios"
---

# Characterizing Model Behavior Under Synthetic Data Training: An Empirical Study Across Scales and Mixing Ratios

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2510.05133" class="toolbar-btn" target="_blank">📄 arXiv: 2510.05133v1</a>
  <a href="https://arxiv.org/pdf/2510.05133.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.05133v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2510.05133v1', 'Characterizing Model Behavior Under Synthetic Data Training: An Empirical Study Across Scales and Mixing Ratios')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Y. Du, G. Wu, G. Tang, W. Wang, Q. Fan

**分类**: cs.CL

**发布日期**: 2025-10-01

**备注**: 17 pages. Technical report

---

## 💡 一句话要点

**研究合成数据比例对不同规模NLP模型行为的影响，为实际应用提供指导。**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `合成数据` `模型训练` `数据增强` `模型校准` `NLP` `大型语言模型` `模型规模`

## 📋 核心要点

1. 现有研究缺乏对合成数据比例如何影响不同规模模型行为的系统性理解，阻碍了合成数据在NLP训练中的有效应用。
2. 通过控制合成数据比例，在不同规模的Pythia模型上进行实验，评估模型性能、校准和输出特征，揭示合成数据比例与模型行为之间的关系。
3. 实验表明，模型在一定比例的合成数据下能保持性能，但超过阈值后性能下降，且模型规模和任务类型会影响模型对合成数据的鲁棒性。

## 📝 摘要（中文）

本文针对大型语言模型生成的合成数据在现代NLP训练流程中的应用，特别是其对模型性能的影响进行了深入研究。通过控制合成数据与外部数据的比例，并使用Pythia模型套件（410M-12B参数）在五个不同的任务上进行评估，研究了模型在不同比例合成数据训练下的性能、校准和输出特征。研究发现，模型在合成数据比例高达20%时仍能保持稳定性能，但超过30%后性能下降加速；较大模型（6.9B-12B）比小型模型（410M-1.4B）对合成数据更具鲁棒性；校准退化先于准确率损失，可作为早期预警信号；任务特性也很重要，推理任务在合成数据训练下比检索任务退化更快。研究结果为实际应用中合成数据的使用提供了指导，并与Shumailov等人的模型崩溃研究进行了比较。

## 🔬 方法详解

**问题定义**：论文旨在研究在NLP模型训练中使用合成数据时，合成数据与外部数据比例对模型性能、校准和输出特征的影响。现有方法缺乏对这一比例的系统性研究，导致在实际应用中难以确定合适的合成数据预算，可能导致模型性能下降甚至崩溃。

**核心思路**：论文的核心思路是通过控制合成数据与外部数据的比例，并在不同规模的NLP模型上进行实验，观察模型在不同比例下的性能表现。通过这种方式，可以揭示合成数据比例与模型行为之间的关系，为实际应用提供指导。

**技术框架**：论文采用实证研究的方法，使用Pythia模型套件（410M-12B参数）在五个不同的NLP任务上进行实验。实验流程包括：1）准备外部数据和合成数据；2）以不同的合成数据比例训练模型；3）评估模型的性能、校准和输出特征；4）分析实验结果，得出结论。

**关键创新**：论文的关键创新在于对合成数据比例与模型行为之间的关系进行了系统性的研究。通过实验，论文揭示了模型在不同比例的合成数据下的性能表现，并发现了模型规模和任务类型对模型鲁棒性的影响。此外，论文还发现校准退化先于准确率损失，可作为早期预警信号。

**关键设计**：论文的关键设计包括：1）选择Pythia模型套件作为实验对象，涵盖不同规模的模型；2）选择五个不同的NLP任务，包括推理和检索任务；3）控制合成数据比例在0-50%之间；4）使用标准评估指标评估模型性能，如准确率和校准误差。

## 📊 实验亮点

实验结果表明，模型在合成数据比例高达20%时仍能保持稳定性能，但超过30%后性能下降加速。较大模型（6.9B-12B）比小型模型（410M-1.4B）对合成数据更具鲁棒性。校准退化先于准确率损失，可作为早期预警信号。推理任务在合成数据训练下比检索任务退化更快。这些发现为实际应用中合成数据的使用提供了量化指导。

## 🎯 应用场景

该研究成果可应用于各种NLP任务中，例如指令跟随、推理和问答等。通过了解合成数据比例对模型性能的影响，开发者可以更有效地利用合成数据来增强模型的泛化能力和鲁棒性，降低数据标注成本，并为特定领域定制模型。研究结果为合成数据的使用提供了实践指导，有助于提升NLP模型的性能和效率。

## 📄 摘要（原文）

> Synthetic data generated by large language models has become integral to modern NLP training pipelines, from bootstrapping reasoning capabilities to augmenting instruction-following datasets. While recent work demonstrates successful applications maintaining high external data ratios, systematic understanding of how synthetic data proportion affects model behavior across different scales remains limited. This paper presents a controlled empirical study examining model performance, calibration, and output characteristics when trained on varying synthetic-to-external data ratios. Using the Pythia model suite (410M-12B parameters) across five diverse tasks, we evaluate models after one to three training iterations with synthetic data proportions ranging from 0-50\%. Our key findings include: models maintain stable performance with up to 20\% synthetic data, but degradation accelerates beyond 30\%; larger models (6.9B-12B) show greater robustness to synthetic data than smaller models (410M-1.4B); calibration degradation precedes accuracy loss, providing an early warning signal; and task characteristics matter, with reasoning tasks degrading faster than retrieval tasks under synthetic data training. Importantly, we find that current best practices, such as those employed in STaR and Self-Instruct systems that maintain greater than 80\% external data, operate well within safe regimes identified by our experiments. We provide practical guidance for practitioners on synthetic data budgets based on model scale and task requirements, alongside detailed comparison with concurrent work including Shumailov et al.'s model collapse findings.

