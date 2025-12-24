---
layout: default
title: Aligning Proteins and Language: A Foundation Model for Protein Retrieval
---

# Aligning Proteins and Language: A Foundation Model for Protein Retrieval

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.08023" class="toolbar-btn" target="_blank">📄 arXiv: 2506.08023v1</a>
  <a href="https://arxiv.org/pdf/2506.08023.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.08023v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.08023v1', 'Aligning Proteins and Language: A Foundation Model for Protein Retrieval')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Qifeng Wu, Zhengzhe Liu, Han Zhu, Yizhou Zhao, Daisuke Kihara, Min Xu

**分类**: q-bio.BM, cs.AI, cs.CE, cs.CV, cs.LG

**发布日期**: 2025-05-27

**备注**: 4 pages for body, 3 pages for appendix, 11 figures. Accepted to CVPR 2025 Workshop on Multimodal Foundation Models for Biomedicine: Challenges and Opportunities(MMFM-BIOMED)

---

## 💡 一句话要点

**提出CLIP风格框架以实现蛋白质检索**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `蛋白质检索` `对比学习` `多模态模型` `结构生物学` `功能注释`

## 📋 核心要点

1. 现有方法在蛋白质结构与功能的关联性理解上存在不足，难以有效检索相似蛋白质。
2. 论文提出了一种基于对比学习的CLIP风格框架，旨在将3D蛋白质结构与功能注释进行对齐。
3. 实验结果显示，该方法在PDB和EMDB数据集上均实现了良好的零样本检索性能，验证了其有效性。

## 📝 摘要（中文）

本论文旨在从大规模蛋白质数据集中检索具有相似结构和语义的蛋白质，以促进通过结构确定方法（如冷冻电子显微镜）获得的蛋白质结构的功能解释。受近期视觉-语言模型（VLMs）进展的启发，我们提出了一种CLIP风格的框架，通过对比学习将3D蛋白质结构与功能注释对齐。为模型训练，我们构建了一个包含约20万个蛋白质-描述对的大规模数据集，具有丰富的功能描述。我们在蛋白质数据银行（PDB）和电子显微镜数据银行（EMDB）数据集上评估了模型，在领域内和更具挑战性的跨数据库检索中均表现出良好的零样本检索性能，突显了多模态基础模型在蛋白质生物学中的结构-功能理解潜力。

## 🔬 方法详解

**问题定义**：本论文旨在解决从大规模蛋白质数据集中检索相似蛋白质的具体问题。现有方法在结构与功能的关联性理解上存在不足，导致检索效果不佳。

**核心思路**：论文的核心解决思路是利用对比学习将3D蛋白质结构与其功能注释进行对齐，借鉴了视觉-语言模型的成功经验。这样的设计能够有效捕捉蛋白质的结构特征与功能描述之间的关系。

**技术框架**：整体架构包括数据预处理、模型训练和检索三个主要模块。首先，构建包含蛋白质及其功能描述的数据集；其次，采用对比学习训练模型以实现结构与功能的对齐；最后，通过检索模块进行相似蛋白质的查找。

**关键创新**：最重要的技术创新点在于提出了一个大规模的蛋白质-描述对数据集，并采用对比学习方法进行模型训练。这与现有方法的本质区别在于，能够同时考虑结构和功能信息，从而提高检索的准确性。

**关键设计**：在模型设计中，采用了特定的损失函数来优化对比学习过程，并在网络结构上进行了调整，以适应3D蛋白质结构的特征提取。

## 📊 实验亮点

实验结果表明，该方法在PDB和EMDB数据集上均实现了良好的零样本检索性能，具体表现为在跨数据库检索中，相较于基线方法，检索准确率提升了显著的百分比，验证了多模态基础模型在蛋白质生物学中的应用潜力。

## 🎯 应用场景

该研究的潜在应用领域包括生物信息学、药物发现和蛋白质工程等。通过有效检索相似蛋白质，研究人员可以更好地理解蛋白质的功能，推动新药研发和生物技术的进步。未来，该方法有望在蛋白质结构与功能的关联性研究中发挥重要作用。

## 📄 摘要（原文）

> This paper aims to retrieve proteins with similar structures and semantics from large-scale protein dataset, facilitating the functional interpretation of protein structures derived by structural determination methods like cryo-Electron Microscopy (cryo-EM). Motivated by the recent progress of vision-language models (VLMs), we propose a CLIP-style framework for aligning 3D protein structures with functional annotations using contrastive learning. For model training, we propose a large-scale dataset of approximately 200,000 protein-caption pairs with rich functional descriptors. We evaluate our model in both in-domain and more challenging cross-database retrieval on Protein Data Bank (PDB) and Electron Microscopy Data Bank (EMDB) dataset, respectively. In both cases, our approach demonstrates promising zero-shot retrieval performance, highlighting the potential of multimodal foundation models for structure-function understanding in protein biology.

