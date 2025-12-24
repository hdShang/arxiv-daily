---
layout: default
title: "SiLVERScore: Semantically-Aware Embeddings for Sign Language Generation Evaluation"
---

# SiLVERScore: Semantically-Aware Embeddings for Sign Language Generation Evaluation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.03791" class="toolbar-btn" target="_blank">📄 arXiv: 2509.03791v1</a>
  <a href="https://arxiv.org/pdf/2509.03791.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.03791v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.03791v1', 'SiLVERScore: Semantically-Aware Embeddings for Sign Language Generation Evaluation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Saki Imai, Mert İnan, Anthony Sicilia, Malihe Alikhani

**分类**: cs.CL, cs.AI

**发布日期**: 2025-09-04

---

## 💡 一句话要点

**提出SiLVERScore，用于语义感知的、基于嵌入的、手语生成评估方法。**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `手语生成` `评估指标` `语义嵌入` `多模态学习` `自然语言处理`

## 📋 核心要点

1. 现有手语生成评估方法依赖回译，忽略了手语的多模态特性，且误差来源难以定位。
2. SiLVERScore在联合嵌入空间中评估手语生成，实现语义感知的评估，提升鲁棒性。
3. 实验表明，SiLVERScore在区分正确和随机配对方面表现出色，显著优于传统指标。

## 📝 摘要（中文）

手语生成评估通常通过回译实现，即先将生成的手语识别回文本，然后使用基于文本的指标与参考文本进行比较。然而，这种两步评估流程引入了歧义：它不仅无法捕捉手语的多模态特性（如面部表情、空间语法和韵律），而且难以确定评估误差来自手语生成模型还是用于评估的翻译系统。本文提出了SiLVERScore，一种新颖的、语义感知的、基于嵌入的评估指标，它在联合嵌入空间中评估手语生成。我们的贡献包括：(1) 识别现有指标的局限性，(2) 引入用于语义感知评估的SiLVERScore，(3) 证明其对语义和韵律变化的鲁棒性，以及 (4) 探索跨数据集的泛化挑战。在PHOENIX-14T和CSL-Daily数据集上，SiLVERScore在区分正确和随机配对方面几乎达到完美的区分度（ROC AUC = 0.99，重叠 < 7%），大大优于传统指标。

## 🔬 方法详解

**问题定义**：现有手语生成评估方法主要依赖于回译，即将生成的手语序列翻译回文本，然后使用文本相似度指标（如BLEU）进行评估。这种方法存在两个主要问题：一是忽略了手语本身的多模态特性，例如面部表情、身体姿态和空间关系等，这些信息在回译过程中会丢失；二是评估结果受到回译系统性能的限制，难以区分是手语生成模型的问题还是回译系统的问题。

**核心思路**：SiLVERScore的核心思路是在一个共享的嵌入空间中直接比较生成的手语和参考手语，而无需进行回译。通过学习一个能够捕捉手语语义信息的嵌入空间，SiLVERScore可以直接衡量生成手语和参考手语在语义上的相似度。这种方法能够更好地反映手语的真实质量，并且避免了回译系统带来的误差。

**技术框架**：SiLVERScore的整体框架包括以下几个主要步骤：1) 使用预训练的手语表征模型（例如，基于Transformer的模型）提取生成手语和参考手语的特征向量；2) 将提取的特征向量映射到一个共享的嵌入空间，该嵌入空间旨在捕捉手语的语义信息；3) 计算生成手语和参考手语在嵌入空间中的相似度得分，该得分即为SiLVERScore。

**关键创新**：SiLVERScore的关键创新在于它提出了一种直接在嵌入空间中评估手语生成质量的方法，避免了传统回译方法的局限性。通过学习一个语义感知的嵌入空间，SiLVERScore能够更好地捕捉手语的多模态特性，并且对语义和韵律上的变化具有更强的鲁棒性。

**关键设计**：SiLVERScore的关键设计包括：1) 使用预训练的手语表征模型，例如基于Transformer的模型，以获得高质量的手语特征向量；2) 设计合适的损失函数，例如对比损失或三元组损失，以学习一个能够区分语义相似和不相似的手语对的嵌入空间；3) 探索不同的相似度度量方法，例如余弦相似度或欧氏距离，以衡量生成手语和参考手语在嵌入空间中的相似度。

## 📊 实验亮点

SiLVERScore在PHOENIX-14T和CSL-Daily数据集上取得了显著的性能提升。实验结果表明，SiLVERScore在区分正确和随机配对方面几乎达到完美的区分度（ROC AUC = 0.99，重叠 < 7%），大大优于传统的基于回译的评估指标。这表明SiLVERScore能够更准确地评估手语生成模型的质量。

## 🎯 应用场景

SiLVERScore可广泛应用于手语生成模型的评估和优化，辅助模型训练和性能提升。它还可用于比较不同手语生成模型的优劣，推动手语翻译和人机交互领域的发展。此外，该方法可以扩展到其他多模态生成任务的评估中，具有重要的研究价值和应用前景。

## 📄 摘要（原文）

> Evaluating sign language generation is often done through back-translation, where generated signs are first recognized back to text and then compared to a reference using text-based metrics. However, this two-step evaluation pipeline introduces ambiguity: it not only fails to capture the multimodal nature of sign language-such as facial expressions, spatial grammar, and prosody-but also makes it hard to pinpoint whether evaluation errors come from sign generation model or the translation system used to assess it. In this work, we propose SiLVERScore, a novel semantically-aware embedding-based evaluation metric that assesses sign language generation in a joint embedding space. Our contributions include: (1) identifying limitations of existing metrics, (2) introducing SiLVERScore for semantically-aware evaluation, (3) demonstrating its robustness to semantic and prosodic variations, and (4) exploring generalization challenges across datasets. On PHOENIX-14T and CSL-Daily datasets, SiLVERScore achieves near-perfect discrimination between correct and random pairs (ROC AUC = 0.99, overlap < 7%), substantially outperforming traditional metrics.

