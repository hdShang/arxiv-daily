---
layout: default
title: CoIDO: Efficient Data Selection for Visual Instruction Tuning via Coupled Importance-Diversity Optimization
---

# CoIDO: Efficient Data Selection for Visual Instruction Tuning via Coupled Importance-Diversity Optimization

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2510.17847" class="toolbar-btn" target="_blank">📄 arXiv: 2510.17847v1</a>
  <a href="https://arxiv.org/pdf/2510.17847.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.17847v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2510.17847v1', 'CoIDO: Efficient Data Selection for Visual Instruction Tuning via Coupled Importance-Diversity Optimization')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yichen Yan, Ming Zhong, Qi Zhu, Xiaoling Gu, Jinpeng Chen, Huan Li

**分类**: cs.CV

**发布日期**: 2025-10-11

**备注**: 22 pages, 8 figures, 39th Conference on Neural Information Processing Systems (NeurIPS 2025)

---

## 💡 一句话要点

**CoIDO：通过耦合重要性-多样性优化实现视觉指令调优的高效数据选择**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `视觉指令调优` `数据选择` `多模态学习` `重要性采样` `多样性优化` `轻量级模型` `计算效率`

## 📋 核心要点

1. 现有视觉指令调优方法在大规模数据集上训练成本高昂，且数据选择方法通常计算开销大，重要性和多样性处理分离。
2. CoIDO通过联合优化数据重要性和多样性，并采用轻量级评分器在小样本上学习数据分布，降低计算成本。
3. 实验表明，CoIDO仅使用20%的数据进行训练，并选择20%的数据进行指令调优，即可达到全量数据微调性能的98.2%。

## 📝 摘要（中文）

多模态大型语言模型（MLLMs）严重依赖指令调优来对齐视觉和语言能力，但大规模数据集的训练计算成本仍然是一个主要瓶颈。现有的数据选择方法旨在通过选择重要且多样化的子集来缓解这个问题，但它们通常存在两个关键缺陷：处理整个数据集带来的高计算开销，以及由于对重要性和多样性的单独处理而导致的数据选择次优。我们引入了CoIDO，这是一种新颖的双目标框架，它联合优化数据重要性和多样性，以克服这些挑战。与现有方法需要对整个数据集进行昂贵评估不同，CoIDO采用轻量级插件评分器。该评分器仅在少量随机数据样本上训练，以学习候选集的分布，从而大大降低了计算需求。通过利用基于同方差不确定性的公式，CoIDO在训练期间有效地平衡了重要性和多样性，从而实现高效且可扩展的数据选择。在我们的实验中，我们仅使用20%的随机抽样数据训练了CoIDO评分器。训练完成后，CoIDO被应用于整个数据集，以选择20%的子集进行指令调优。在广泛使用的LLaVA-1.5-7B模型上，针对十个下游任务，这个选定的子集平均实现了完整数据微调性能的98.2%。

## 🔬 方法详解

**问题定义**：论文旨在解决视觉指令调优中，使用大规模数据集进行训练时计算成本过高的问题。现有数据选择方法通常需要处理整个数据集，计算开销大，并且将数据的重要性和多样性分开考虑，导致选择的数据子集并非最优。

**核心思路**：CoIDO的核心思路是联合优化数据的重要性和多样性，并在一个轻量级的框架下实现高效的数据选择。通过训练一个轻量级的评分器，使其能够从小样本数据中学习到整个数据集的分布，从而避免对整个数据集进行昂贵的评估。

**技术框架**：CoIDO包含两个主要阶段：1) 训练轻量级评分器：从原始数据集中随机抽取一小部分样本，用于训练一个评分器，该评分器能够评估数据的重要性和多样性。2) 数据选择：使用训练好的评分器对整个数据集进行评估，并选择一个既重要又具有多样性的数据子集用于指令调优。

**关键创新**：CoIDO的关键创新在于联合优化重要性和多样性，并使用轻量级评分器来降低计算成本。与现有方法需要处理整个数据集不同，CoIDO仅需处理一小部分样本即可学习到数据集的分布，从而实现高效的数据选择。此外，CoIDO使用基于同方差不确定性的公式来平衡重要性和多样性，从而选择更具代表性的数据子集。

**关键设计**：CoIDO使用一个轻量级的神经网络作为评分器，该网络以图像和文本指令作为输入，输出一个标量值，表示该数据样本的重要性和多样性。损失函数的设计至关重要，需要同时考虑数据的重要性和多样性。论文采用基于同方差不确定性的公式来平衡这两个目标。具体而言，损失函数可以设计为重要性损失和多样性损失的加权和，权重由同方差不确定性估计得到。

## 📊 实验亮点

实验结果表明，CoIDO仅使用20%的随机抽样数据训练评分器，并选择20%的数据子集进行指令调优，在LLaVA-1.5-7B模型上，针对十个下游任务，平均实现了完整数据微调性能的98.2%。这表明CoIDO能够在显著降低计算成本的同时，保持甚至接近全量数据训练的性能。

## 🎯 应用场景

CoIDO可应用于各种多模态大型语言模型的指令调优场景，尤其是在计算资源有限的情况下。通过高效的数据选择，CoIDO能够降低训练成本，加速模型开发周期，并提升模型在下游任务中的性能。该方法具有广泛的应用前景，例如在移动设备或边缘设备上部署多模态模型。

## 📄 摘要（原文）

> Multimodal large language models (MLLMs) rely heavily on instruction tuning to align vision and language capabilities, yet the computational cost of training on large-scale datasets remains a major bottleneck. Existing data selection methods aim to mitigate this by selecting important and diverse subsets, but they often suffer from two critical drawbacks: high computational overhead from processing the entire dataset and suboptimal data selection due to separate treatment of importance and diversity.
>   We introduce CoIDO, a novel dual-objective framework that jointly optimizes data importance and diversity to overcome these challenges. Unlike existing approaches that require costly evaluations across the whole dataset, CoIDO employs a lightweight plug-in scorer. This scorer is trained on just a small random sample of data to learn the distribution of the candidate set, drastically reducing computational demands. By leveraging a homoscedastic uncertainty-based formulation, CoIDO effectively balances importance and diversity during training, enabling efficient and scalable data selection.
>   In our experiments, we trained the CoIDO scorer using only 20 percent of randomly sampled data. Once trained, CoIDO was applied to the entire dataset to select a 20 percent subset for instruction tuning. On the widely used LLaVA-1.5-7B model across ten downstream tasks, this selected subset achieved an impressive 98.2 percent of the performance of full-data fine-tuning, on average.

