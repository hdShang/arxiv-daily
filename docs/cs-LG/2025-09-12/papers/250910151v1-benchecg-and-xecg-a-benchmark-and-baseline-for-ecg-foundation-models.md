---
layout: default
title: "BenchECG and xECG: a benchmark and baseline for ECG foundation models"
---

# BenchECG and xECG: a benchmark and baseline for ECG foundation models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.10151" class="toolbar-btn" target="_blank">📄 arXiv: 2509.10151v1</a>
  <a href="https://arxiv.org/pdf/2509.10151.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.10151v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.10151v1', 'BenchECG and xECG: a benchmark and baseline for ECG foundation models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Riccardo Lunelli, Angus Nicolson, Samuel Martin Pröll, Sebastian Johannes Reinstadler, Axel Bauer, Clemens Dlaska

**分类**: cs.LG, cs.AI

**发布日期**: 2025-09-12

**备注**: 32 pages, 4 figures, 22 tables

---

## 💡 一句话要点

**BenchECG：心电图（ECG）基础模型的标准化评测基准与xECG基线模型**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `心电图` `ECG` `基础模型` `自监督学习` `循环神经网络` `基准测试` `医疗诊断`

## 📋 核心要点

1. 现有ECG基础模型研究缺乏统一的评估标准，数据集和任务选择不一致，导致模型性能难以公平比较。
2. 论文提出BenchECG基准，包含全面的公开ECG数据集和多样化任务，旨在标准化ECG模型评估流程。
3. 论文同时提出xECG模型，基于xLSTM和SimDINOv2自监督学习，在BenchECG上取得了最佳性能，为未来研究提供基线。

## 📝 摘要（中文）

心电图(ECG)成本低廉、应用广泛，非常适合深度学习。 近年来，人们对开发ECG基础模型的兴趣日益浓厚，这些模型可以泛化到不同的下游任务。 然而，一直缺乏一致的评估：先前的工作通常使用狭窄的任务选择和不一致的数据集，阻碍了公平的比较。 在这里，我们引入BenchECG，这是一个标准化的基准，包含一套全面的公开ECG数据集和多功能的任务。 我们还提出了xECG，一个基于xLSTM的循环模型，使用SimDINOv2自监督学习进行训练，与公开的state-of-the-art模型相比，它实现了最佳的BenchECG分数。 特别是，xECG是唯一一个在所有数据集和任务上表现强劲的公开模型。 通过标准化评估，BenchECG能够进行严格的比较，并旨在加速ECG表征学习的进展。 xECG实现了优于早期方法的结果，为未来的ECG基础模型定义了一个新的基线。

## 🔬 方法详解

**问题定义**：现有ECG基础模型研究缺乏统一的评估标准，不同研究使用的数据集和任务差异大，导致模型性能无法公平比较。这阻碍了ECG表征学习的进展，难以确定哪些模型真正具有泛化能力。

**核心思路**：论文的核心思路是构建一个标准化的ECG评估基准BenchECG，并提供一个高性能的基线模型xECG。BenchECG通过提供统一的数据集和任务，使得不同ECG模型可以在相同的条件下进行评估和比较。xECG则作为一个性能标杆，为未来的模型提供参考。

**技术框架**：整体框架包含两个主要部分：BenchECG基准和xECG模型。BenchECG基准包括多个公开的ECG数据集和一系列预定义的任务，涵盖了不同的ECG分析场景。xECG模型是一个基于xLSTM的循环神经网络，使用SimDINOv2自监督学习方法进行预训练，然后在下游任务上进行微调。

**关键创新**：论文的关键创新在于提出了BenchECG基准，这是首个专门为ECG基础模型设计的标准化评估平台。此外，xECG模型在BenchECG上的优异表现也证明了xLSTM和SimDINOv2在ECG表征学习中的有效性。

**关键设计**：xECG模型使用了xLSTM作为其核心循环单元，xLSTM相比于传统的LSTM具有更强的长期依赖建模能力。SimDINOv2自监督学习方法用于预训练xECG模型，使其能够学习到ECG信号的通用表征。在下游任务上，使用交叉熵损失函数进行微调。

## 📊 实验亮点

xECG模型在BenchECG基准上取得了最佳性能，超越了现有的公开模型。具体而言，xECG在多个ECG数据集和任务上均表现出色，证明了其强大的泛化能力。作为首个在BenchECG上表现优异的公开模型，xECG为未来的ECG基础模型研究设定了新的基线。

## 🎯 应用场景

该研究成果可应用于心血管疾病的自动诊断、风险预测和个性化治疗。标准化的BenchECG基准能够加速ECG基础模型的研究和开发，推动相关技术在临床实践中的应用。高质量的ECG表征学习模型可以提升远程医疗、可穿戴设备等场景下的心电监测能力。

## 📄 摘要（原文）

> Electrocardiograms (ECGs) are inexpensive, widely used, and well-suited to deep learning. Recently, interest has grown in developing foundation models for ECGs - models that generalise across diverse downstream tasks. However, consistent evaluation has been lacking: prior work often uses narrow task selections and inconsistent datasets, hindering fair comparison. Here, we introduce BenchECG, a standardised benchmark comprising a comprehensive suite of publicly available ECG datasets and versatile tasks. We also propose xECG, an xLSTM-based recurrent model trained with SimDINOv2 self-supervised learning, which achieves the best BenchECG score compared to publicly available state-of-the-art models. In particular, xECG is the only publicly available model to perform strongly on all datasets and tasks. By standardising evaluation, BenchECG enables rigorous comparison and aims to accelerate progress in ECG representation learning. xECG achieves superior performance over earlier approaches, defining a new baseline for future ECG foundation models.

