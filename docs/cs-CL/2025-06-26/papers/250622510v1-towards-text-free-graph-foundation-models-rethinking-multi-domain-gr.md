---
layout: default
title: "Towards Text-free Graph Foundation Models: Rethinking Multi-Domain Graph Contrastive Learning"
---

# Towards Text-free Graph Foundation Models: Rethinking Multi-Domain Graph Contrastive Learning

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.22510" class="toolbar-btn" target="_blank">📄 arXiv: 2506.22510v1</a>
  <a href="https://arxiv.org/pdf/2506.22510.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.22510v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.22510v1', 'Towards Text-free Graph Foundation Models: Rethinking Multi-Domain Graph Contrastive Learning')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Zihao Zhao, Xinlong Zhai, Jinyu Yang, Chuan Shi

**分类**: cs.CL, cs.AI

**发布日期**: 2025-06-26

**备注**: 16 pages, 5 figures

---

## 💡 一句话要点

**提出MDGCL以解决多领域图对比学习问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `图对比学习` `多领域迁移` `基础模型` `领域注意机制` `知识转移`

## 📋 核心要点

1. 现有的图对比学习方法未能有效处理不同领域之间的语义和属性差异，导致知识迁移效果不佳。
2. 本文提出MDGCL框架，通过对比学习策略识别领域差异，并引入领域令牌和领域注意机制以实现知识转移。
3. 在五个基准数据集上的实验表明，MDGCL在准确率和Macro-F1得分上分别提升了19.33%和19.13%，显著优于现有方法。

## 📝 摘要（中文）

基础模型在自然语言处理和计算机视觉领域取得了显著成功，主要得益于其在预训练中整合多领域知识的能力。然而，针对图数据，尤其是没有文本特征的图，现有的对比预训练策略未能有效吸收不同领域的知识。本文提出了一种新的多领域预训练和跨领域迁移框架MDGCL，通过设计对比学习策略识别领域差异，并引入领域注意机制实现细粒度知识转移。实验结果表明，该方法在五个基准数据集上显著优于现有最先进的方法，准确率和Macro-F1得分分别提升了19.33%和19.13%。

## 🔬 方法详解

**问题定义**：本文旨在解决现有图对比学习方法在多领域场景下的不足，特别是不同领域图之间的语义和属性差异导致的知识迁移效果不佳。

**核心思路**：提出MDGCL框架，通过设计对比学习策略来识别和捕捉领域差异，并引入领域令牌以编码领域级的全局信息，从而实现有效的知识转移。

**技术框架**：MDGCL框架分为预训练阶段和下游任务阶段。在预训练阶段，采用对比学习策略识别领域差异；在下游阶段，引入领域注意机制以实现细粒度的知识转移。

**关键创新**：最重要的创新在于引入领域令牌和领域注意机制，使得模型能够有效识别和利用不同领域的知识，从而克服传统方法的局限。

**关键设计**：在对比学习中，设计了特定的损失函数以优化领域差异的识别，同时在领域注意机制中设置了参数以控制不同领域知识的权重，从而实现更精细的知识转移。

## 📊 实验亮点

实验结果显示，MDGCL在五个基准数据集上表现优异，准确率提升了19.33%，Macro-F1得分提升了19.13%，显著超过了现有的最先进方法，验证了其有效性和优越性。

## 🎯 应用场景

该研究的潜在应用领域包括社交网络分析、推荐系统和其他需要处理图数据的多领域任务。通过有效的知识迁移，MDGCL能够提升模型在不同领域的表现，具有重要的实际价值和广泛的应用前景。

## 📄 摘要（原文）

> Foundation models have achieved great success in natural language processing (NLP) and computer vision (CV). Their success largely stems from the ability to integrate multi-domain knowledge in pre-training and transfer it to target domains. Considering graph data, especially graphs without textual features, is ubiquitous in real-world applications such as social networks and recommendation systems, some researchers have attempted to extend this paradigm to the graph field, aiming to construct graph foundation models. However, unlike CV and NLP, there are huge gaps among the semantics and properties of graphs in different domains, while current works still adopt traditional contrastive pre-training strategies designed in the single-domain scenario, which regard contrastive samples from different domains as equivalent. From experimental investigations, we discovered that inherent domain-specific differences prevent these strategies from effectively absorbing knowledge from different domains to generate informative representations. In this paper, we propose a novel multi-domain pre-training and cross-domain transfer framework, namely MDGCL.In the pre-training stage, we design a contrastive learning strategy to substantially recognize and capture domain differences, and introduce domain tokens to encode domain-level global information. In the downstream stage, we introduce a domain attention mechanism to enable fine-grained domain knowledge transfer. Extensive experiments on five benchmark datasets have demonstrated that our method outperforms state-of-the-art significantly, with the maximum improvement of 19.33\% on accuracy and 19.13\% on Macro-F1 score.

