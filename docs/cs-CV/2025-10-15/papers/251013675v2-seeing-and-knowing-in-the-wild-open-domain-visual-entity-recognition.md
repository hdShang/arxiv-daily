---
layout: default
title: Seeing and Knowing in the Wild: Open-domain Visual Entity Recognition with Large-scale Knowledge Graphs via Contrastive Learning
---

# Seeing and Knowing in the Wild: Open-domain Visual Entity Recognition with Large-scale Knowledge Graphs via Contrastive Learning

<div class="paper-toolbar">
  <div class="toolbar-left">
    <a href="https://arxiv.org/abs/2510.13675" target="_blank" class="toolbar-btn">arXiv: 2510.13675v2</a>
    <a href="https://arxiv.org/pdf/2510.13675.pdf" target="_blank" class="toolbar-btn">PDF</a>
  </div>
  <div class="toolbar-right">
    <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.13675v2" 
            onclick="toggleFavorite(this, '2510.13675v2', 'Seeing and Knowing in the Wild: Open-domain Visual Entity Recognition with Large-scale Knowledge Graphs via Contrastive Learning')" title="收藏">
      ☆ 收藏
    </button>
    <button class="toolbar-btn share-btn" onclick="copyLink()" title="复制链接">
      🔗 分享
    </button>
  </div>
</div>


**作者**: Hongkuan Zhou, Lavdim Halilaj, Sebastian Monka, Stefan Schmid, Yuqicheng Zhu, Jingcheng Wu, Nadeem Nazer, Steffen Staab

**分类**: cs.CV, cs.LG

**发布日期**: 2025-10-15 (更新: 2025-11-18)

**备注**: Accepted by AAAI2026

---

## 💡 一句话要点

**提出知识引导对比学习框架以解决开放域视觉实体识别问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `开放域识别` `对比学习` `知识图谱` `视觉实体识别` `零样本学习` `Wikidata` `长尾分布` `多模态学习`

## 📋 核心要点

1. 核心问题：现有方法在开放域视觉实体识别中面临有限监督和高视觉歧义的挑战，导致对未见实体的识别困难。
2. 方法要点：提出的KnowCoL框架通过将图像和文本描述映射到共享语义空间，利用结构化知识进行零样本实体识别。
3. 实验或效果：在OVEN基准上，最小模型在未见实体的准确率上提高了10.5%，且模型体积仅为现有方法的1/35。

## 📝 摘要（中文）

开放域视觉实体识别旨在识别和链接图像中描绘的实体与现实世界概念，如Wikidata中的概念。与传统的固定标签分类任务不同，该任务在开放集条件下进行，训练期间大多数目标实体是未见的，并且表现出长尾分布。这使得任务在有限监督、高视觉歧义和语义消歧的需求下变得极具挑战性。本文提出了一种知识引导对比学习（KnowCoL）框架，将图像和文本描述结合到一个由Wikidata结构信息支撑的共享语义空间中。通过将视觉和文本输入抽象到概念层面，模型利用实体描述、类型层次和关系上下文来支持零样本实体识别。实验表明，使用视觉、文本和结构知识显著提高了准确性，尤其是对于稀有和未见实体。

## 🔬 方法详解

**问题定义**：本文解决开放域视觉实体识别问题，现有方法在面对未见实体时准确性不足，且在有限监督和高视觉歧义的情况下表现不佳。

**核心思路**：提出知识引导对比学习（KnowCoL）框架，通过将图像和文本描述映射到一个共享的语义空间，利用Wikidata的结构化信息来支持零样本实体识别。这样的设计旨在增强模型对未见实体的识别能力。

**技术框架**：KnowCoL框架包括图像输入、文本描述和结构化知识三个主要模块。首先，图像和文本通过对比学习进行特征提取，然后映射到共享的语义空间中，最后利用结构化知识进行实体识别。

**关键创新**：该研究的创新点在于结合视觉、文本和结构知识进行对比学习，显著提升了对稀有和未见实体的识别能力，与传统方法相比，能够在开放集条件下更有效地进行实体识别。

**关键设计**：模型采用了对比损失函数，优化了图像和文本特征的相似性，同时利用Wikidata中的实体描述和类型层次进行知识引导，确保模型在面对未见实体时仍能保持较高的准确性。

## 📊 实验亮点

实验结果表明，使用视觉、文本和结构知识的组合显著提高了模型的准确性。最小模型在未见实体的准确率上提高了10.5%，且模型体积仅为现有最优方法的1/35，展示了高效的性能提升。

## 🎯 应用场景

该研究的潜在应用领域包括图像搜索、社交媒体内容分析和自动标注系统等。通过提高开放域视觉实体识别的准确性，可以在多种实际场景中实现更智能的信息检索和内容理解，未来可能对人机交互和智能推荐系统产生深远影响。

## 📄 摘要（原文）

> Open-domain visual entity recognition aims to identify and link entities depicted in images to a vast and evolving set of real-world concepts, such as those found in Wikidata. Unlike conventional classification tasks with fixed label sets, it operates under open-set conditions, where most target entities are unseen during training and exhibit long-tail distributions. This makes the task inherently challenging due to limited supervision, high visual ambiguity, and the need for semantic disambiguation. We propose a Knowledge-guided Contrastive Learning (KnowCoL) framework that combines both images and text descriptions into a shared semantic space grounded by structured information from Wikidata. By abstracting visual and textual inputs to a conceptual level, the model leverages entity descriptions, type hierarchies, and relational context to support zero-shot entity recognition. We evaluate our approach on the OVEN benchmark, a large-scale open-domain visual recognition dataset with Wikidata IDs as the label space. Our experiments show that using visual, textual, and structured knowledge greatly improves accuracy, especially for rare and unseen entities. Our smallest model improves the accuracy on unseen entities by 10.5% compared to the state-of-the-art, despite being 35 times smaller.

