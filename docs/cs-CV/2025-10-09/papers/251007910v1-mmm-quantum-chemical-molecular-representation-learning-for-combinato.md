---
layout: default
title: MMM: Quantum-Chemical Molecular Representation Learning for Combinatorial Drug Recommendation
---

# MMM: Quantum-Chemical Molecular Representation Learning for Combinatorial Drug Recommendation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2510.07910" class="toolbar-btn" target="_blank">📄 arXiv: 2510.07910v1</a>
  <a href="https://arxiv.org/pdf/2510.07910.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.07910v1" onclick="toggleFavorite(this, '2510.07910v1', 'MMM: Quantum-Chemical Molecular Representation Learning for Combinatorial Drug Recommendation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Chongmyung Kwon, Yujin Kim, Seoeun Park, Yunji Lee, Charmgil Hong

**分类**: cs.LG, cs.AI, cs.CV

**发布日期**: 2025-10-09

**备注**: Medical Image Computing and Computer-Assisted Intervention (MICCAI) Predictive Intelligence in Medicine Workshop (MICCAI PRIME) 2025; 13 pages

---

## 💡 一句话要点

**MMM：利用量子化学分子表示学习进行组合药物推荐，提升DDI预测。**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `药物推荐` `药物-药物相互作用` `量子化学` `分子表示学习` `图神经网络`

## 📋 核心要点

1. 现有药物推荐方法依赖简化的药物结构表示，无法充分捕捉分子结合亲和力和反应性，导致DDI预测不准确。
2. MMM框架将三维量子化学信息（ELF）融入药物表示学习，结合全局电子特性和局部子结构相互作用，更全面地描述药物。
3. 实验表明，MMM在DDI预测的F1分数、Jaccard指数和DDI率上显著优于GNN基线模型，提升了药物推荐的安全性。

## 📝 摘要（中文）

药物推荐是基于机器学习的临床决策支持系统中的一项关键任务。然而，联合处方药物之间药物-药物相互作用（DDI）的风险仍然是一个重大挑战。以往的研究使用图神经网络（GNN）来表示药物结构，但其简化的离散形式无法完全捕捉分子结合亲和力和反应性。因此，我们提出了基于分子电子局域化函数（ELF）图的多模态DDI预测（MMM），这是一个将三维（3D）量子化学信息整合到药物表示学习中的新框架。它使用ELF生成3D电子密度图。为了捕捉治疗相关性和相互作用风险，MMM结合了编码全局电子特性的ELF衍生特征与模拟局部子结构相互作用的二分图编码器。这种设计能够学习药物分子的互补特征。我们在MIMIC-III数据集（250种药物，442个子结构）中评估了MMM，并将其与多个基线模型进行了比较。特别是，与基于GNN的SafeDrug模型相比，在F1分数（p = 0.0387）、Jaccard指数（p = 0.0112）和DDI率（p = 0.0386）方面表现出统计学上的显著改进。这些结果证明了基于ELF的3D表示在提高预测准确性和支持临床实践中更安全的组合药物处方的潜力。

## 🔬 方法详解

**问题定义**：论文旨在解决药物推荐中药物-药物相互作用（DDI）预测不准确的问题。现有方法，特别是基于图神经网络（GNN）的方法，通常使用简化的药物结构表示，忽略了药物分子的三维结构和电子特性，无法充分捕捉分子间的结合亲和力和反应性，导致DDI预测的准确性受限。

**核心思路**：论文的核心思路是将三维量子化学信息融入药物表示学习中，利用分子电子局域化函数（ELF）生成药物分子的三维电子密度图，从而更全面地描述药物分子的特性。通过结合全局电子特性和局部子结构相互作用，模型能够学习药物分子的互补特征，提高DDI预测的准确性。

**技术框架**：MMM框架包含以下主要模块：1) **ELF特征提取**：利用量子化学计算生成药物分子的三维电子密度图，并从中提取全局电子特性。2) **二分图编码器**：构建药物分子子结构之间的二分图，利用图神经网络学习局部子结构相互作用。3) **多模态融合**：将ELF特征和二分图编码器的输出进行融合，得到药物分子的综合表示。4) **DDI预测**：利用药物分子的综合表示进行DDI预测。

**关键创新**：最重要的技术创新点在于将三维量子化学信息（ELF）引入药物表示学习。与现有方法相比，MMM能够更全面地描述药物分子的特性，捕捉分子间的结合亲和力和反应性，从而提高DDI预测的准确性。此外，结合全局电子特性和局部子结构相互作用的多模态融合方法也是一个创新点。

**关键设计**：论文的关键设计包括：1) 使用ELF生成三维电子密度图，并从中提取全局电子特性。具体如何提取未知。2) 构建药物分子子结构之间的二分图，并使用图神经网络学习局部子结构相互作用。具体GNN结构未知。3) 使用某种融合方法（具体方法未知）将ELF特征和二分图编码器的输出进行融合。4) 使用某种分类器（具体类型未知）进行DDI预测。损失函数未知。

## 📊 实验亮点

实验结果表明，MMM在MIMIC-III数据集上显著优于基于GNN的SafeDrug模型，在F1分数上提升了统计显著的水平（p = 0.0387），Jaccard指数（p = 0.0112）和DDI率（p = 0.0386）也得到了显著改善。这些结果验证了基于ELF的3D表示在提高DDI预测准确性方面的有效性。

## 🎯 应用场景

该研究成果可应用于临床决策支持系统，辅助医生进行更安全的组合药物处方。通过提高DDI预测的准确性，降低药物不良反应的风险，改善患者的治疗效果。未来，该方法可以扩展到其他药物相关的预测任务，例如药物靶点预测、药物毒性预测等。

## 📄 摘要（原文）

> Drug recommendation is an essential task in machine learning-based clinical decision support systems. However, the risk of drug-drug interactions (DDI) between co-prescribed medications remains a significant challenge. Previous studies have used graph neural networks (GNNs) to represent drug structures. Regardless, their simplified discrete forms cannot fully capture the molecular binding affinity and reactivity. Therefore, we propose Multimodal DDI Prediction with Molecular Electron Localization Function (ELF) Maps (MMM), a novel framework that integrates three-dimensional (3D) quantum-chemical information into drug representation learning. It generates 3D electron density maps using the ELF. To capture both therapeutic relevance and interaction risks, MMM combines ELF-derived features that encode global electronic properties with a bipartite graph encoder that models local substructure interactions. This design enables learning complementary characteristics of drug molecules. We evaluate MMM in the MIMIC-III dataset (250 drugs, 442 substructures), comparing it with several baseline models. In particular, a comparison with the GNN-based SafeDrug model demonstrates statistically significant improvements in the F1-score (p = 0.0387), Jaccard (p = 0.0112), and the DDI rate (p = 0.0386). These results demonstrate the potential of ELF-based 3D representations to enhance prediction accuracy and support safer combinatorial drug prescribing in clinical practice.

