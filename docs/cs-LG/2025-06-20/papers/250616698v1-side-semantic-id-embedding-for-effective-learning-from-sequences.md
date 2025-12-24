---
layout: default
title: "SIDE: Semantic ID Embedding for effective learning from sequences"
---

# SIDE: Semantic ID Embedding for effective learning from sequences

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.16698" class="toolbar-btn" target="_blank">📄 arXiv: 2506.16698v1</a>
  <a href="https://arxiv.org/pdf/2506.16698.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.16698v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.16698v1', 'SIDE: Semantic ID Embedding for effective learning from sequences')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Dinesh Ramasamy, Shakti Kumar, Chris Cadonic, Jiaxin Yang, Sohini Roychowdhury, Esam Abdel Rhman, Srihari Reddy

**分类**: cs.LG

**发布日期**: 2025-06-20

**备注**: 7 pages, 4 images, 6 tables

**期刊**: KDD workshop, 2025

---

## 💡 一句话要点

**提出SIDE方法以解决序列推荐系统中的嵌入规模问题**

🎯 **匹配领域**: **支柱四：生成式动作 (Generative Motion)**

**关键词**: `序列推荐` `语义ID` `向量量化` `多任务学习` `广告推荐` `实时预测`

## 📋 核心要点

1. 现有的推荐系统在处理大规模用户历史数据时，嵌入的存储和推理成本高，难以实时应用。
2. 本文提出了一种基于向量量化的SID方法，通过融合多种内容嵌入，简化了嵌入的使用。
3. 在大规模工业广告推荐系统中，应用该方法实现了2.4倍的归一化熵增益和3倍的数据占用减少。

## 📝 摘要（中文）

基于序列的推荐模型在工业广告推荐系统中处于领先地位，通常处理的用户历史或序列长度在O(10^3)到O(10^4)事件之间。尽管在预训练模型中添加嵌入是可行的，但在实时预测模型中，由于存储和推理成本，整合这些嵌入面临挑战。为了解决这一问题，本文提出了一种新方法，通过向推荐模型注入紧凑的语义ID（SID）来替代大量嵌入。该方法引入了多任务VQ-VAE框架、无参数的SID到嵌入转换技术，以及一种新的量化方法，显著提高了工业广告推荐系统的性能。

## 🔬 方法详解

**问题定义**：现有的序列推荐系统在处理大规模用户历史数据时，嵌入的存储和推理成本高，导致实时预测的效率低下。

**核心思路**：本文提出了一种新颖的方法，通过引入紧凑的语义ID（SID）来替代传统的多个嵌入，从而降低存储需求和提高推理速度。

**技术框架**：整体架构包括一个多任务VQ-VAE框架，称为VQ融合，能够将多个内容嵌入和分类预测融合为一个单一的SID。同时，采用无参数的SID到嵌入转换技术，简化了模型的复杂性。

**关键创新**：本文的主要创新在于引入了DISCRETE-PCA（DPCA）量化方法，增强了残差量化技术的效果，并且通过无参数的SID转换消除了对大型查找表的需求。

**关键设计**：在模型设计中，采用了多任务学习的策略，优化了损失函数以提高SID的表达能力，并通过实验验证了两种内容嵌入集合的有效性。整体架构的设计旨在实现高效的实时推荐。

## 📊 实验亮点

在实验中，提出的方法在大规模工业广告推荐系统中实现了2.4倍的归一化熵增益，相比传统的SID方法，数据占用减少了3倍。这些结果表明，SIDE方法在性能和效率上均有显著提升，具有较强的实际应用价值。

## 🎯 应用场景

该研究的潜在应用领域包括广告推荐、个性化内容推荐和用户行为分析等。通过优化嵌入的使用，能够显著提升推荐系统的实时性和准确性，进而提高用户体验和商业价值。未来，该方法可能在更多的序列数据处理场景中得到应用，推动相关领域的发展。

## 📄 摘要（原文）

> Sequence-based recommendations models are driving the state-of-the-art for industrial ad-recommendation systems. Such systems typically deal with user histories or sequence lengths ranging in the order of O(10^3) to O(10^4) events. While adding embeddings at this scale is manageable in pre-trained models, incorporating them into real-time prediction models is challenging due to both storage and inference costs. To address this scaling challenge, we propose a novel approach that leverages vector quantization (VQ) to inject a compact Semantic ID (SID) as input to the recommendation models instead of a collection of embeddings. Our method builds on recent works of SIDs by introducing three key innovations: (i) a multi-task VQ-VAE framework, called VQ fusion that fuses multiple content embeddings and categorical predictions into a single Semantic ID; (ii) a parameter-free, highly granular SID-to-embedding conversion technique, called SIDE, that is validated with two content embedding collections, thereby eliminating the need for a large parameterized lookup table; and (iii) a novel quantization method called Discrete-PCA (DPCA) which generalizes and enhances residual quantization techniques. The proposed enhancements when applied to a large-scale industrial ads-recommendation system achieves 2.4X improvement in normalized entropy (NE) gain and 3X reduction in data footprint compared to traditional SID methods.

