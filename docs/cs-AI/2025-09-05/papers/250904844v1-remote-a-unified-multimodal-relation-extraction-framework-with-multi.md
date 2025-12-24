---
layout: default
title: "REMOTE: A Unified Multimodal Relation Extraction Framework with Multilevel Optimal Transport and Mixture-of-Experts"
---

# REMOTE: A Unified Multimodal Relation Extraction Framework with Multilevel Optimal Transport and Mixture-of-Experts

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.04844" class="toolbar-btn" target="_blank">📄 arXiv: 2509.04844v1</a>
  <a href="https://arxiv.org/pdf/2509.04844.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.04844v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.04844v1', 'REMOTE: A Unified Multimodal Relation Extraction Framework with Multilevel Optimal Transport and Mixture-of-Experts')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Xinkui Lin, Yongxiu Xu, Minghao Tang, Shilong Zhang, Hongbo Xu, Hao Xu, Yubin Wang

**分类**: cs.MM, cs.AI, cs.IR

**发布日期**: 2025-09-05

**备注**: ACM MM 2025

**DOI**: [10.1145/3746027.3754868](https://doi.org/10.1145/3746027.3754868)

**🔗 代码/项目**: [GITHUB](https://github.com/Nikol-coder/REMOTE)

---

## 💡 一句话要点

**提出REMOTE框架，通过多层最优传输和混合专家模型实现统一的多模态关系抽取。**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多模态关系抽取` `混合专家模型` `最优传输` `知识图谱` `跨模态融合` `多层特征融合` `统一框架`

## 📋 核心要点

1. 现有MRE方法局限于提取单一关系类型，无法有效处理复杂场景，且跨模态交互建模不足。
2. REMOTE框架利用混合专家机制动态选择模态信息，并采用多层最优传输融合低层特征。
3. 实验结果表明，REMOTE在多个数据集上取得了SOTA性能，验证了其有效性。

## 📝 摘要（中文）

多模态关系抽取(MRE)是知识图谱和多媒体领域中的关键任务，在多模态知识图谱构建中起着至关重要的作用。然而，现有的方法通常仅限于提取单一类型的关系三元组，限制了它们提取指定类型之外的三元组的能力。直接组合这些方法无法捕捉动态的跨模态交互，并引入了显著的计算冗余。因此，我们提出了一种新颖的统一多模态关系抽取框架，该框架具有多层最优传输和混合专家模型，称为REMOTE，它可以同时提取文本实体和视觉对象之间的模内和模间关系。为了动态地为不同类型的关系三元组选择最佳交互特征，我们引入了混合专家机制，确保利用最相关的模态信息。此外，考虑到现有编码器中多层顺序编码的固有属性通常会导致低层信息的丢失，我们采用多层最优传输融合模块来保留低层特征，同时保持多层编码，从而产生更具表现力的表示。相应地，我们还创建了一个统一多模态关系抽取(UMRE)数据集，以评估我们框架的有效性，该数据集包含头实体和尾实体可以来自文本或图像的各种情况。大量的实验表明，REMOTE有效地提取了各种类型的关系三元组，并在另外两个公共MRE数据集上几乎所有指标上都实现了最先进的性能。

## 🔬 方法详解

**问题定义**：现有的多模态关系抽取方法主要存在两个痛点。一是只能抽取预定义类型的关系三元组，泛化能力不足。二是无法有效捕捉文本和图像之间动态的跨模态交互，导致信息利用不充分。此外，现有编码器中的多层顺序编码容易丢失低层信息，影响最终的表示效果。

**核心思路**：REMOTE框架的核心思路是利用混合专家模型动态选择不同模态的信息，并采用多层最优传输融合模块保留低层特征，从而实现更全面、更准确的关系抽取。通过混合专家模型，框架可以根据不同的关系类型自适应地选择最相关的模态信息，避免了冗余信息的干扰。多层最优传输融合模块则可以有效地保留低层特征，弥补了传统编码器的不足。

**技术框架**：REMOTE框架主要包含以下几个模块：1) 多模态特征编码器：用于提取文本和图像的特征表示。2) 混合专家模型：用于动态选择不同模态的信息。3) 多层最优传输融合模块：用于融合不同层次的特征表示。4) 关系分类器：用于预测实体之间的关系类型。整体流程是，首先通过多模态特征编码器提取文本和图像的特征，然后利用混合专家模型选择最相关的模态信息，接着通过多层最优传输融合模块融合不同层次的特征，最后通过关系分类器预测实体之间的关系类型。

**关键创新**：REMOTE框架的关键创新在于以下两点：1) 提出了混合专家模型，可以动态选择不同模态的信息，从而更好地适应不同的关系类型。2) 采用了多层最优传输融合模块，可以有效地保留低层特征，弥补了传统编码器的不足。与现有方法相比，REMOTE框架能够更全面、更准确地抽取关系，具有更强的泛化能力。

**关键设计**：在混合专家模型中，使用了多个专家网络，每个专家网络负责处理一种模态的信息。通过门控机制，可以根据不同的关系类型动态地选择不同的专家网络。在多层最优传输融合模块中，使用了最优传输算法来对齐不同层次的特征表示。损失函数包括关系分类损失和最优传输损失，用于优化模型的参数。

## 📊 实验亮点

REMOTE框架在两个公开MRE数据集上取得了SOTA性能，证明了其有效性。具体而言，在UMRE数据集上，REMOTE框架在多个指标上都取得了显著的提升。实验结果表明，REMOTE框架能够有效地提取各种类型的关系三元组，并且具有较强的泛化能力。

## 🎯 应用场景

REMOTE框架可应用于多模态知识图谱构建、智能问答、图像检索等领域。例如，在多模态知识图谱构建中，可以利用REMOTE框架自动抽取文本和图像中的实体关系，从而丰富知识图谱的内容。在智能问答中，可以利用REMOTE框架理解用户的问题，并从知识图谱中找到答案。在图像检索中，可以利用REMOTE框架对图像进行语义分析，从而提高检索的准确率。

## 📄 摘要（原文）

> Multimodal relation extraction (MRE) is a crucial task in the fields of Knowledge Graph and Multimedia, playing a pivotal role in multimodal knowledge graph construction. However, existing methods are typically limited to extracting a single type of relational triplet, which restricts their ability to extract triplets beyond the specified types. Directly combining these methods fails to capture dynamic cross-modal interactions and introduces significant computational redundancy. Therefore, we propose a novel \textit{unified multimodal Relation Extraction framework with Multilevel Optimal Transport and mixture-of-Experts}, termed REMOTE, which can simultaneously extract intra-modal and inter-modal relations between textual entities and visual objects. To dynamically select optimal interaction features for different types of relational triplets, we introduce mixture-of-experts mechanism, ensuring the most relevant modality information is utilized. Additionally, considering that the inherent property of multilayer sequential encoding in existing encoders often leads to the loss of low-level information, we adopt a multilevel optimal transport fusion module to preserve low-level features while maintaining multilayer encoding, yielding more expressive representations. Correspondingly, we also create a Unified Multimodal Relation Extraction (UMRE) dataset to evaluate the effectiveness of our framework, encompassing diverse cases where the head and tail entities can originate from either text or image. Extensive experiments show that REMOTE effectively extracts various types of relational triplets and achieves state-of-the-art performanc on almost all metrics across two other public MRE datasets. We release our resources at https://github.com/Nikol-coder/REMOTE.

