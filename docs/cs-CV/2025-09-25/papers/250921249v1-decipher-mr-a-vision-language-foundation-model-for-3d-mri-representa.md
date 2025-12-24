---
layout: default
title: "Decipher-MR: A Vision-Language Foundation Model for 3D MRI Representations"
---

# Decipher-MR: A Vision-Language Foundation Model for 3D MRI Representations

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.21249" class="toolbar-btn" target="_blank">📄 arXiv: 2509.21249v1</a>
  <a href="https://arxiv.org/pdf/2509.21249.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.21249v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.21249v1', 'Decipher-MR: A Vision-Language Foundation Model for 3D MRI Representations')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Zhijian Yang, Noel DSouza, Istvan Megyeri, Xiaojian Xu, Amin Honarmandi Shandiz, Farzin Haddadpour, Krisztian Koos, Laszlo Rusko, Emanuele Valeriano, Bharadwaj Swaninathan, Lei Wu, Parminder Bhatia, Taha Kass-Hout, Erhan Bas

**分类**: cs.CV, cs.AI, cs.LG

**发布日期**: 2025-09-25

---

## 💡 一句话要点

**Decipher-MR：用于3D MRI表征的视觉-语言基础模型**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `3D MRI` `视觉-语言模型` `医学影像分析` `自监督学习` `报告引导` `基础模型` `对比学习`

## 📋 核心要点

1. MRI数据异构性高，现有机器学习方法难以泛化，且数据量不足限制了基础模型在MRI领域的应用。
2. Decipher-MR通过大规模MRI数据上的自监督视觉学习和报告引导的文本监督，构建鲁棒且通用的3D MRI表征。
3. 实验表明，Decipher-MR在疾病分类、人口统计学预测等多个任务上优于现有模型，证明了其有效性和泛化能力。

## 📝 摘要（中文）

磁共振成像(MRI)是临床诊断和研究中至关重要的医学成像方式，但其复杂性和异质性给自动化分析带来了挑战，尤其是在可扩展和通用的机器学习应用中。虽然基础模型已经彻底改变了自然语言和视觉任务，但由于数据稀缺和狭窄的解剖学关注点，它们在MRI中的应用仍然有限。本文提出了Decipher-MR，一个3D MRI特定的视觉-语言基础模型，该模型在包含来自超过22,000项研究的200,000个MRI序列的大规模数据集上进行训练，涵盖了不同的解剖区域、序列和病理。Decipher-MR集成了自监督视觉学习和报告引导的文本监督，以构建鲁棒、通用的表征，从而能够有效地适应广泛的应用。为了以最小的计算开销实现鲁棒和多样化的临床任务，Decipher-MR支持模块化设计，该设计支持调整连接到冻结的预训练编码器的轻量级、特定于任务的解码器。按照此设置，我们在包括疾病分类、人口统计学预测、解剖定位和跨模态检索在内的各种基准上评估Decipher-MR，证明了相对于现有基础模型和特定于任务的方法的一致性能提升。我们的结果表明，Decipher-MR是基于MRI的AI的可扩展和通用基础，有助于跨临床和研究领域的高效开发。

## 🔬 方法详解

**问题定义**：论文旨在解决MRI图像分析中，现有机器学习方法泛化性差、难以适应不同解剖区域和病理的问题。现有方法通常依赖于特定任务的标注数据，难以利用大规模未标注MRI数据中的信息，并且缺乏对MRI报告文本信息的有效利用。

**核心思路**：论文的核心思路是构建一个基于视觉-语言的3D MRI基础模型，通过大规模自监督学习和报告引导的文本监督，学习到通用的MRI表征。这种方法旨在克服数据稀缺和任务特定性问题，提高模型在不同MRI分析任务中的泛化能力。

**技术框架**：Decipher-MR的技术框架包含以下主要模块：1) 3D MRI编码器：用于提取MRI图像的视觉特征。2) 文本编码器：用于提取MRI报告的文本特征。3) 自监督学习模块：利用对比学习等方法，从未标注的MRI数据中学习视觉表征。4) 报告引导的文本监督模块：利用MRI报告文本信息，指导视觉表征的学习，建立视觉和语言之间的联系。5) 任务特定解码器：用于将学习到的通用表征应用于不同的MRI分析任务。

**关键创新**：Decipher-MR的关键创新在于：1) 大规模3D MRI视觉-语言基础模型的构建，填补了该领域的空白。2) 报告引导的文本监督，有效利用了MRI报告文本信息，提高了视觉表征的质量。3) 模块化设计，支持轻量级任务特定解码器的快速部署，降低了计算成本。

**关键设计**：Decipher-MR的关键设计包括：1) 使用3D卷积神经网络作为MRI编码器，以捕捉MRI图像的三维空间信息。2) 使用Transformer模型作为文本编码器，以捕捉MRI报告文本的语义信息。3) 使用对比学习损失函数，鼓励模型学习到区分不同MRI图像的视觉表征。4) 使用文本-图像匹配损失函数，鼓励模型学习到将MRI图像和报告文本联系起来的联合表征。

## 📊 实验亮点

Decipher-MR在多个MRI分析任务上取得了显著的性能提升。例如，在疾病分类任务中，Decipher-MR的准确率超过了现有基础模型和特定任务模型。在人口统计学预测任务中，Decipher-MR的预测精度也优于其他方法。这些结果表明，Decipher-MR能够有效地学习到通用的MRI表征，并将其应用于不同的临床任务。

## 🎯 应用场景

Decipher-MR可广泛应用于医学影像分析领域，例如疾病诊断、病情评估、治疗方案制定等。该模型能够有效处理不同类型的MRI数据，并结合报告文本信息，为临床医生提供更全面、准确的诊断依据。未来，Decipher-MR有望加速医学影像AI的发展，提高医疗效率和质量。

## 📄 摘要（原文）

> Magnetic Resonance Imaging (MRI) is a critical medical imaging modality in clinical diagnosis and research, yet its complexity and heterogeneity pose challenges for automated analysis, particularly in scalable and generalizable machine learning applications. While foundation models have revolutionized natural language and vision tasks, their application to MRI remains limited due to data scarcity and narrow anatomical focus. In this work, we present Decipher-MR, a 3D MRI-specific vision-language foundation model trained on a large-scale dataset comprising 200,000 MRI series from over 22,000 studies spanning diverse anatomical regions, sequences, and pathologies. Decipher-MR integrates self-supervised vision learning with report-guided text supervision to build robust, generalizable representations, enabling effective adaptation across broad applications. To enable robust and diverse clinical tasks with minimal computational overhead, Decipher-MR supports a modular design that enables tuning of lightweight, task-specific decoders attached to a frozen pretrained encoder. Following this setting, we evaluate Decipher-MR across diverse benchmarks including disease classification, demographic prediction, anatomical localization, and cross-modal retrieval, demonstrating consistent performance gains over existing foundation models and task-specific approaches. Our results establish Decipher-MR as a scalable and versatile foundation for MRI-based AI, facilitating efficient development across clinical and research domains.

