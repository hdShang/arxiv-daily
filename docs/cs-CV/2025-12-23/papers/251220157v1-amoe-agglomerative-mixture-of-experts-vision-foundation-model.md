---
layout: default
title: AMoE: Agglomerative Mixture-of-Experts Vision Foundation Model
---

# AMoE: Agglomerative Mixture-of-Experts Vision Foundation Model

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.20157" class="toolbar-btn" target="_blank">📄 arXiv: 2512.20157v1</a>
  <a href="https://arxiv.org/pdf/2512.20157.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.20157v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.20157v1', 'AMoE: Agglomerative Mixture-of-Experts Vision Foundation Model')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Sofian Chaybouti, Sanath Narayan, Yasser Dahou, Phúc H. Lê Khac, Ankit Singh, Ngoc Dung Huynh, Wamiq Reyaz Para, Hilde Kuehne, Hakim Hacid

**分类**: cs.CV

**发布日期**: 2025-12-23

**备注**: 17 pages, 8 figures, 11 tables

---

## 💡 一句话要点

**提出AMoE，一种高效的Agglomerative Mixture-of-Experts视觉基础模型，通过多教师蒸馏实现。**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `视觉基础模型` `多教师蒸馏` `知识蒸馏` `混合专家模型` `数据采样` `表征学习`

## 📋 核心要点

1. 现有的视觉基础模型训练方法计算成本高昂，且对多教师蒸馏的学习动态和数据效率研究不足。
2. AMoE通过非对称关系知识蒸馏、token平衡批处理和分层聚类采样等技术，提升多教师蒸馏的效率。
3. 实验表明，AMoE在2亿图像语料库OpenLVD200M上表现出卓越的效率，并发布了该数据集和蒸馏模型。

## 📝 摘要（中文）

本文系统研究了视觉基础模型的多教师蒸馏方法，并确定了在较低计算成本下进行训练的关键因素。我们提出了Agglomerative Mixture-of-Experts视觉基础模型（AMoE），它同时从SigLIP2和DINOv3中提取知识到一个混合专家学生模型中。我们证明了：（1）我们的非对称关系知识蒸馏损失保留了每个教师的几何属性，同时实现了有效的知识转移；（2）token平衡批处理将不同分辨率的图像打包成具有统一token预算的序列，稳定了跨分辨率的表示学习，且不牺牲性能；（3）训练数据的分层聚类和采样（通常用于自监督学习）显著提高了多教师蒸馏的样本效率，优于随机采样。通过结合这些发现，我们创建了OpenLVD200M，一个2亿图像语料库，展示了多教师蒸馏的卓越效率。我们发布了OpenLVD200M和蒸馏模型。

## 🔬 方法详解

**问题定义**：现有的视觉基础模型训练，特别是基于多教师蒸馏的方法，面临着计算资源需求高、数据利用率低的问题。如何降低训练成本，同时保证甚至提升模型性能，是本文要解决的核心问题。现有方法在知识迁移过程中可能无法充分保留各个教师模型的优势，且对不同分辨率图像的处理不够高效。

**核心思路**：本文的核心思路是通过一种高效的多教师蒸馏框架，将多个预训练视觉模型的知识整合到一个轻量级的混合专家模型中。通过精心设计的损失函数、数据采样策略和批处理方法，优化知识迁移过程，提高数据利用率，从而降低训练成本。

**技术框架**：AMoE的整体框架包括以下几个主要模块：1) 多教师模型（SigLIP2和DINOv3）；2) 混合专家学生模型；3) 非对称关系知识蒸馏损失；4) token平衡批处理；5) 分层聚类采样。首先，利用分层聚类采样从训练数据集中选择具有代表性的样本。然后，将不同分辨率的图像通过token平衡批处理构建统一token预算的序列。接着，利用非对称关系知识蒸馏损失，将多教师模型的知识迁移到混合专家学生模型中。

**关键创新**：本文的关键创新在于以下三个方面：1) 提出了非对称关系知识蒸馏损失，能够更好地保留各个教师模型的几何属性，实现更有效的知识迁移；2) 引入了token平衡批处理，解决了不同分辨率图像在训练过程中带来的不稳定性问题；3) 将分层聚类采样应用于多教师蒸馏，显著提高了样本效率。

**关键设计**：非对称关系知识蒸馏损失的设计考虑了不同教师模型之间的差异，通过不对称的方式保留各自的优势。Token平衡批处理通过调整不同分辨率图像的数量，使得每个批次的token数量保持一致，从而稳定训练过程。分层聚类采样通过对训练数据进行聚类，并从每个簇中选择代表性样本，减少了数据冗余，提高了训练效率。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.20157v1/x1.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.20157v1/x2.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.20157v1/x3.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

AMoE在OpenLVD200M数据集上进行了实验，结果表明，通过结合非对称关系知识蒸馏、token平衡批处理和分层聚类采样，AMoE能够以更高的效率进行多教师蒸馏。相比于随机采样，分层聚类采样显著提高了样本效率。具体性能数据和对比基线将在论文中详细展示。

## 🎯 应用场景

AMoE具有广泛的应用前景，可用于图像分类、目标检测、图像分割等多种视觉任务。通过高效的多教师蒸馏，可以降低训练成本，加速模型部署，并为资源受限的设备提供高性能的视觉模型。该研究成果有助于推动视觉基础模型在实际场景中的应用。

## 📄 摘要（原文）

> Vision foundation models trained via multi-teacher distillation offer a promising path toward unified visual representations, yet the learning dynamics and data efficiency of such approaches remain underexplored. In this paper, we systematically study multi-teacher distillation for vision foundation models and identify key factors that enable training at lower computational cost. We introduce Agglomerative Mixture-of-Experts Vision Foundation Models (AMoE), which distill knowledge from SigLIP2 and DINOv3 simultaneously into a Mixture-of-Experts student. We show that (1) our Asymmetric Relation-Knowledge Distillation loss preserves the geometric properties of each teacher while enabling effective knowledge transfer, (2) token-balanced batching that packs varying-resolution images into sequences with uniform token budgets stabilizes representation learning across resolutions without sacrificing performance, and (3) hierarchical clustering and sampling of training data--typically reserved for self-supervised learning--substantially improves sample efficiency over random sampling for multi-teacher distillation. By combining these findings, we curate OpenLVD200M, a 200M-image corpus that demonstrates superior efficiency for multi-teacher distillation. Instantiated in a Mixture-of-Experts. We release OpenLVD200M and distilled models.

