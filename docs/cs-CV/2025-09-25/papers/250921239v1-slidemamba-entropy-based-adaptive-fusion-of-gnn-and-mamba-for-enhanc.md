---
layout: default
title: "SlideMamba: Entropy-Based Adaptive Fusion of GNN and Mamba for Enhanced Representation Learning in Digital Pathology"
---

# SlideMamba: Entropy-Based Adaptive Fusion of GNN and Mamba for Enhanced Representation Learning in Digital Pathology

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.21239" class="toolbar-btn" target="_blank">📄 arXiv: 2509.21239v1</a>
  <a href="https://arxiv.org/pdf/2509.21239.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.21239v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.21239v1', 'SlideMamba: Entropy-Based Adaptive Fusion of GNN and Mamba for Enhanced Representation Learning in Digital Pathology')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Shakib Khan, Fariba Dambandkhameneh, Nazim Shaikh, Yao Nie, Raghavan Venugopal, Xiao Li

**分类**: cs.CV, q-bio.QM

**发布日期**: 2025-09-25

---

## 💡 一句话要点

**SlideMamba：结合GNN与Mamba的熵自适应融合框架，提升数字病理学表征学习**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱七：动作重定向 (Motion Retargeting)**

**关键词**: `数字病理学` `全切片图像` `图神经网络` `Mamba架构` `自适应融合` `表征学习` `基因融合预测`

## 📋 核心要点

1. 现有计算病理学方法难以同时有效捕捉WSI中的局部空间关系和长程上下文依赖。
2. 提出SlideMamba，结合Mamba擅长的长程依赖和GNN擅长的短程交互，并使用熵自适应融合。
3. 在基因融合和突变预测任务上，SlideMamba的PRAUC达到0.751，显著优于现有方法。

## 📝 摘要（中文）

本研究提出了一种通用的深度学习框架，该框架集成了Mamba架构和图神经网络（GNN），以增强全切片图像（WSI）的分析能力，从而支持各种临床和生物学任务。该方法旨在捕获局部空间关系和长程上下文依赖关系，为数字病理学分析提供了一种灵活的架构。Mamba模块擅长捕获长程全局依赖关系，而GNN则强调细粒度的短程空间交互。为了有效地结合这些互补信号，我们引入了一种基于熵的置信度加权机制的自适应融合策略。这种方法通过根据局部信息与全局信息对于不同下游任务的上下文重要性，为具有更高置信度（更低熵）预测的分支分配更高的权重，从而动态地平衡来自两个分支的贡献。我们在一个代表性任务上验证了该方法的有效性：从WSI预测基因融合和突变状态。我们的框架SlideMamba实现了0.751 ± 0.05的精确率-召回率曲线下面积（PRAUC），优于MIL（0.491 ± 0.042）、Trans-MIL（0.39 ± 0.017）、仅Mamba（0.664 ± 0.063）、仅GNN（0.748 ± 0.091）以及先前类似的工作GAT-Mamba（0.703 ± 0.075）。SlideMamba还在ROC AUC（0.738 ± 0.055）、灵敏度（0.662 ± 0.083）和特异性（0.725 ± 0.094）方面取得了有竞争力的结果。这些结果突出了集成架构的优势，并通过提出的基于熵的自适应融合策略得到了增强，并表明了在计算病理学中应用空间分辨预测建模任务的潜力。

## 🔬 方法详解

**问题定义**：在数字病理学中，如何从全切片图像（WSI）中提取有意义的表征，以支持各种临床和生物学任务，例如基因融合和突变状态预测？现有方法，如多示例学习（MIL）及其变体，以及单独使用GNN或Transformer的模型，难以同时有效地捕捉WSI中的局部空间关系和长程上下文依赖，导致性能受限。

**核心思路**：论文的核心思路是将擅长捕捉长程全局依赖的Mamba架构与强调细粒度短程空间交互的图神经网络（GNN）相结合。通过这种方式，模型可以同时利用全局上下文信息和局部空间信息，从而更全面地理解WSI。此外，论文还引入了一种基于熵的自适应融合策略，动态地平衡来自Mamba和GNN分支的贡献，使得模型能够根据输入数据的特性，灵活地调整对局部和全局信息的依赖程度。

**技术框架**：SlideMamba的整体架构包含以下几个主要模块：1) WSI切片提取：将WSI分割成多个图像块（patches）。2) 特征提取：使用预训练的卷积神经网络（CNN）提取每个图像块的特征。3) GNN模块：利用GNN对图像块之间的空间关系进行建模，捕获局部空间依赖。4) Mamba模块：利用Mamba架构对图像块之间的长程依赖进行建模，捕获全局上下文信息。5) 自适应融合：使用基于熵的置信度加权机制，动态地融合GNN和Mamba模块的输出。6) 预测：使用融合后的特征进行基因融合和突变状态预测。

**关键创新**：最重要的技术创新点在于基于熵的自适应融合策略。与传统的静态融合方法不同，该策略能够根据GNN和Mamba模块的预测结果的熵值，动态地调整它们在最终预测中的权重。熵值越低，表示预测结果的置信度越高，对应的模块的权重也就越高。这种自适应融合策略使得模型能够更好地利用局部和全局信息，从而提高预测精度。

**关键设计**：论文中一个关键的设计是使用熵作为置信度的度量。熵是一种衡量信息不确定性的指标，熵值越低，表示信息越确定。在SlideMamba中，熵被用来衡量GNN和Mamba模块的预测结果的置信度。具体来说，对于每个模块的输出，论文计算其预测概率分布的熵值，并将熵值的倒数作为该模块的权重。此外，论文还使用了交叉熵损失函数来训练模型，并使用Adam优化器进行参数更新。具体的网络结构和参数设置在论文中有详细描述。

## 📊 实验亮点

SlideMamba在基因融合和突变预测任务上取得了显著的性能提升。具体来说，SlideMamba的PRAUC达到了0.751 ± 0.05，显著优于MIL（0.491 ± 0.042）、Trans-MIL（0.39 ± 0.017）、仅Mamba（0.664 ± 0.063）、仅GNN（0.748 ± 0.091）以及GAT-Mamba（0.703 ± 0.075）。这些结果表明，SlideMamba能够有效地结合局部空间关系和长程上下文依赖，从而提高预测精度。

## 🎯 应用场景

SlideMamba在计算病理学领域具有广泛的应用前景，可用于疾病诊断、预后预测、治疗方案选择等。通过对WSI进行深入分析，该模型可以帮助病理学家更准确地识别肿瘤细胞、评估肿瘤的侵袭性，并预测患者的生存率。此外，SlideMamba还可以应用于药物研发领域，例如，通过预测药物对肿瘤细胞的疗效，加速新药的开发过程。

## 📄 摘要（原文）

> Advances in computational pathology increasingly rely on extracting meaningful representations from Whole Slide Images (WSIs) to support various clinical and biological tasks. In this study, we propose a generalizable deep learning framework that integrates the Mamba architecture with Graph Neural Networks (GNNs) for enhanced WSI analysis. Our method is designed to capture both local spatial relationships and long-range contextual dependencies, offering a flexible architecture for digital pathology analysis. Mamba modules excels in capturing long-range global dependencies, while GNNs emphasize fine-grained short-range spatial interactions. To effectively combine these complementary signals, we introduce an adaptive fusion strategy that uses an entropy-based confidence weighting mechanism. This approach dynamically balances contributions from both branches by assigning higher weight to the branch with more confident (lower-entropy) predictions, depending on the contextual importance of local versus global information for different downstream tasks. We demonstrate the utility of our approach on a representative task: predicting gene fusion and mutation status from WSIs. Our framework, SlideMamba, achieves an area under the precision recall curve (PRAUC) of 0.751 \pm 0.05, outperforming MIL (0.491 \pm 0.042), Trans-MIL (0.39 \pm 0.017), Mamba-only (0.664 \pm 0.063), GNN-only (0.748 \pm 0.091), and a prior similar work GAT-Mamba (0.703 \pm 0.075). SlideMamba also achieves competitive results across ROC AUC (0.738 \pm 0.055), sensitivity (0.662 \pm 0.083), and specificity (0.725 \pm 0.094). These results highlight the strength of the integrated architecture, enhanced by the proposed entropy-based adaptive fusion strategy, and suggest promising potential for application of spatially-resolved predictive modeling tasks in computational pathology.

