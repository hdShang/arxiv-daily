---
layout: default
title: "EAGLE: Efficient Alignment of Generalized Latent Embeddings for Multimodal Survival Prediction with Interpretable Attribution Analysis"
---

# EAGLE: Efficient Alignment of Generalized Latent Embeddings for Multimodal Survival Prediction with Interpretable Attribution Analysis

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.22446" class="toolbar-btn" target="_blank">📄 arXiv: 2506.22446v1</a>
  <a href="https://arxiv.org/pdf/2506.22446.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.22446v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.22446v1', 'EAGLE: Efficient Alignment of Generalized Latent Embeddings for Multimodal Survival Prediction with Interpretable Attribution Analysis')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Aakash Tripathi, Asim Waqas, Matthew B. Schabath, Yasin Yilmaz, Ghulam Rasool

**分类**: cs.LG, cs.AI

**发布日期**: 2025-06-12

---

## 💡 一句话要点

**提出EAGLE以解决多模态癌症生存预测中的融合与可解释性问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多模态融合` `生存预测` `深度学习` `可解释性` `癌症研究` `注意力机制` `归因分析`

## 📋 核心要点

1. 现有多模态癌症生存预测方法存在融合策略简单、计算需求高和缺乏可解释性等问题，限制了其临床应用。
2. EAGLE通过动态跨模态注意力机制和全面的归因分析，提供了一种高效的多模态融合解决方案，提升了预测准确性和可解释性。
3. 在911名患者的实验中，EAGLE实现了99.96%的维度减少，并在生存预测中显著提高了风险分层的临床意义。

## 📝 摘要（中文）

准确的癌症生存预测需要整合多种数据模态，以反映影像、临床参数和文本报告之间的复杂关系。然而，现有的多模态方法存在融合策略简单、计算需求庞大和缺乏可解释性等问题，限制了其临床应用。本文提出EAGLE（高效对齐广义潜在嵌入），通过基于注意力的多模态融合和全面的归因分析来解决这些局限性。EAGLE引入了四项关键创新：动态跨模态注意力机制、99.96%的维度减少、三种互补的归因方法以及统一的管道，能够无缝适应不同癌症类型。我们在911名患者中评估了EAGLE，结果显示高风险患者更依赖不良影像特征，而低风险患者则表现出模态贡献的平衡。

## 🔬 方法详解

**问题定义**：本文旨在解决多模态癌症生存预测中的融合策略简单、计算需求高和缺乏可解释性的问题。现有方法往往无法有效整合影像、临床参数和文本数据，导致预测性能不足。

**核心思路**：EAGLE的核心思路是通过动态跨模态注意力机制，学习模态之间的层次关系，并结合多种归因方法，提升模型的可解释性和预测性能。这样的设计使得模型能够在不同模态之间灵活调整权重，从而更好地反映患者的真实情况。

**技术框架**：EAGLE的整体架构包括数据预处理、动态跨模态注意力机制、维度减少模块和归因分析模块。首先对输入数据进行预处理，然后通过注意力机制对不同模态进行加权融合，接着进行维度减少，最后进行患者级别的归因分析。

**关键创新**：EAGLE的四项关键创新包括动态跨模态注意力机制、99.96%的维度减少、三种互补的归因方法以及统一的适应管道。这些创新使得EAGLE在多模态生存预测中具备更高的效率和可解释性，与现有方法相比具有显著优势。

**关键设计**：在模型设计中，EAGLE采用了自适应注意力权重计算，结合了交叉熵损失函数和L2正则化，确保模型在训练过程中能够有效学习到不同模态的重要性。此外，归因分析模块通过SHAP、LIME等方法提供了患者级别的可解释性，增强了临床应用的信任度。

## 📊 实验亮点

在911名患者的实验中，EAGLE实现了99.96%的维度减少，同时在生存预测中显著提高了风险分层的临床意义，GBM患者的中位生存期差异达到4倍，NSCLC患者则达到5倍。这些结果表明EAGLE在多模态生存预测中具有优越的性能和临床应用价值。

## 🎯 应用场景

EAGLE的研究成果在癌症生存预测领域具有广泛的应用潜力，能够为临床医生提供更为准确的风险评估和个性化治疗方案。通过提升模型的可解释性，EAGLE有助于增强医生对自动化预测结果的信任，从而推动人工智能在医疗领域的实际应用。未来，该方法还可扩展至其他疾病的生存预测和风险评估中。

## 📄 摘要（原文）

> Accurate cancer survival prediction requires integration of diverse data modalities that reflect the complex interplay between imaging, clinical parameters, and textual reports. However, existing multimodal approaches suffer from simplistic fusion strategies, massive computational requirements, and lack of interpretability-critical barriers to clinical adoption. We present EAGLE (Efficient Alignment of Generalized Latent Embeddings), a novel deep learning framework that addresses these limitations through attention-based multimodal fusion with comprehensive attribution analysis. EAGLE introduces four key innovations: (1) dynamic cross-modal attention mechanisms that learn hierarchical relationships between modalities, (2) massive dimensionality reduction (99.96%) while maintaining predictive performance, (3) three complementary attribution methods providing patient-level interpretability, and (4) a unified pipeline enabling seamless adaptation across cancer types. We evaluated EAGLE on 911 patients across three distinct malignancies: glioblastoma (GBM, n=160), intraductal papillary mucinous neoplasms (IPMN, n=171), and non-small cell lung cancer (NSCLC, n=580). Patient-level analysis showed high-risk individuals relied more heavily on adverse imaging features, while low-risk patients demonstrated balanced modality contributions. Risk stratification identified clinically meaningful groups with 4-fold (GBM) to 5-fold (NSCLC) differences in median survival, directly informing treatment intensity decisions. By combining state-of-the-art performance with clinical interpretability, EAGLE bridges the gap between advanced AI capabilities and practical healthcare deployment, offering a scalable solution for multimodal survival prediction that enhances both prognostic accuracy and physician trust in automated predictions.

