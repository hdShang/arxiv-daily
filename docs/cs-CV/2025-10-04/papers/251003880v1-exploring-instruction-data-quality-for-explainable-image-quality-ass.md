---
layout: default
title: Exploring Instruction Data Quality for Explainable Image Quality Assessment
---

# Exploring Instruction Data Quality for Explainable Image Quality Assessment

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2510.03880" class="toolbar-btn" target="_blank">📄 arXiv: 2510.03880v1</a>
  <a href="https://arxiv.org/pdf/2510.03880.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.03880v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2510.03880v1', 'Exploring Instruction Data Quality for Explainable Image Quality Assessment')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yunhao Li, Sijing Wu, Huiyu Duan, Yucheng Zhu, Qi Jia, Guangtao Zhai

**分类**: cs.CV

**发布日期**: 2025-10-04

---

## 💡 一句话要点

**针对可解释图像质量评估，提出基于聚类的数据选择方法IQA-Select，提升数据效率。**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `图像质量评估` `可解释性` `指令调优` `数据选择` `聚类分析`

## 📋 核心要点

1. 现有可解释图像质量评估方法依赖大规模指令调优数据，计算成本高昂且数据存在冗余。
2. 论文提出基于聚类的数据选择框架IQA-Select，旨在选择最具代表性的数据子集进行微调，提高数据效率。
3. 实验表明，IQA-Select仅使用10%的数据即可达到甚至超过全量数据微调的性能，显著降低计算成本。

## 📝 摘要（中文）

近年来，随着多模态大型语言模型（MLLM）的快速发展，可解释图像质量评估（IQA）逐渐流行，其目标是提供与图像质量相关的描述和答案。为了实现这一目标，目前的方法试图构建大规模指令调优数据集，以赋予MLLM质量感知能力，遵循著名的缩放定律。然而，大量的指令调优数据可能导致巨大的计算成本和冗余数据，进而损害模型的性能。为了解决这个问题，本文挑战了缩放定律，并系统地研究了指令调优数据集的数据质量在可解释IQA中的作用。使用强大的预训练MLLM，我们首先研究了使用不同大小的指令调优数据进行微调后模型性能的变化。我们发现，使用适当的比例随机选择数据集的子集，甚至可以比使用整个指令调优数据集进行训练获得更好的结果，这表明当前可解释IQA指令调优数据的冗余性。除了随机抽样子集外，我们还提出了一个基于聚类的数据选择框架，包括三个阶段：聚类特征提取、聚类配额分配和聚类抽样策略。然后，我们系统地分析了每个阶段的选择，并提出了一种简单而有效的数据选择方法IQA-Select，用于可解释IQA。实验结果表明，IQA-Select仅使用10%的选定数据，即可在Q-Bench和AesBench中分别达到完整微调的102.1%和103.7%的性能，从而显著降低计算成本，同时获得更好的性能。

## 🔬 方法详解

**问题定义**：现有可解释图像质量评估方法依赖于大规模的指令调优数据集来训练多模态大型语言模型(MLLM)，以使其具备质量感知能力。然而，这种方法存在两个主要痛点：一是计算成本高昂，训练大规模数据集需要大量的计算资源；二是数据集中存在冗余，并非所有数据都对模型性能提升有贡献。因此，如何高效地利用数据，在保证性能的前提下减少计算成本，是本文要解决的核心问题。

**核心思路**：论文的核心思路是挑战传统的“缩放定律”，即并非数据越多越好，而是数据质量更重要。通过选择最具代表性的数据子集进行训练，可以减少冗余，提高训练效率，甚至提升模型性能。论文提出了一种基于聚类的数据选择框架，旨在从原始数据集中选择一个高质量的子集。

**技术框架**：IQA-Select框架包含三个主要阶段：
1. **聚类特征提取**：首先，从指令数据中提取特征，用于后续的聚类分析。具体实现方式未知，但目标是获得能够代表数据特征的向量表示。
2. **聚类配额分配**：根据每个簇的重要性，为每个簇分配不同的数据选择配额。重要性高的簇分配更多的配额，以保证其代表性。
3. **聚类抽样策略**：在每个簇内，根据一定的策略选择数据样本。具体策略未知，但目标是选择最具代表性的样本。

**关键创新**：该方法最重要的创新点在于，它打破了可解释IQA领域对大规模数据的盲目依赖，转而关注数据质量。通过聚类分析，能够识别并选择最具代表性的数据子集，从而在保证甚至提升模型性能的同时，显著降低计算成本。与随机抽样相比，聚类方法能够更好地保留数据的多样性，避免信息损失。

**关键设计**：论文的关键设计在于三个阶段的具体实现方式，包括特征提取方法、聚类算法的选择、簇重要性的评估标准以及簇内抽样策略。论文提到对每个阶段的选择进行了系统分析，并最终提出了一种简单但有效的IQA-Select方法。具体的参数设置、损失函数、网络结构等技术细节在摘要中没有提及，属于未知信息。

## 📊 实验亮点

实验结果表明，IQA-Select仅使用10%的选定数据，即可在Q-Bench和AesBench两个基准数据集上分别达到完整微调的102.1%和103.7%的性能。这意味着在显著降低计算成本的同时，模型性能甚至有所提升。这一结果充分证明了IQA-Select方法的有效性和优越性，挑战了可解释IQA领域对大规模数据的盲目依赖。

## 🎯 应用场景

该研究成果可广泛应用于图像质量评估相关的领域，例如图像增强、图像压缩、图像传输等。通过减少训练数据量，可以降低模型训练的成本和时间，加速算法的开发和部署。此外，该方法还可以应用于其他需要大规模数据训练的任务中，提高数据利用效率，降低计算资源消耗。未来，该研究可以进一步探索更高效的数据选择策略，提升模型性能。

## 📄 摘要（原文）

> In recent years, with the rapid development of powerful multimodal large language models (MLLMs), explainable image quality assessment (IQA) has gradually become popular, aiming at providing quality-related descriptions and answers of images. To achieve this goal, recent methods seek to construct a large-scale instruction tuning dataset to empower the MLLM with quality perception ability following the well-known scaling law. However, a large amount of instruction tuning data may cause substantial computational costs and redundant data, which in turn will cause harm to the performance of the model. To cope with this problem, in this paper, we challenge the scaling law and systematically investigate the role of data quality of the instruction tuning dataset for explainable IQA. Using a powerful pre-trained MLLM, we first investigate the changes in model performance after fine-tuning with different sizes of instruction tuning data. We find that selecting a subset of the data set randomly using an appropriate ratio can even lead to better results than training with the entire instruction tuning dataset, demonstrating the redundancy of current explainable IQA instruction tuning data. Beyond randomly sampling a subset, we propose a clustering-based data selection framework with three stages: clustering feature extraction, cluster quota allocation, and cluster sampling strategy. Then we systematically analyze the choices of each stage and propose a simple but efficient data selection method IQA-Select for explainable IQA. The experimental results demonstrate that IQA-Select can achieve 102.1% and 103.7% performance of full fine-tuning using only 10% selected data in Q-Bench and AesBench respectively, significantly reducing computational costs while achieving better performance.

