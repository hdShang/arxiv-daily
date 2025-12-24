---
layout: default
title: "KGAlign: Joint Semantic-Structural Knowledge Encoding for Multimodal Fake News Detection"
---

# KGAlign: Joint Semantic-Structural Knowledge Encoding for Multimodal Fake News Detection

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.14714" class="toolbar-btn" target="_blank">📄 arXiv: 2505.14714v2</a>
  <a href="https://arxiv.org/pdf/2505.14714.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.14714v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.14714v2', 'KGAlign: Joint Semantic-Structural Knowledge Encoding for Multimodal Fake News Detection')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Tuan-Vinh La, Minh-Hieu Nguyen, Minh-Son Dao

**分类**: cs.CV, cs.AI, cs.CL

**发布日期**: 2025-05-18 (更新: 2025-10-17)

**备注**: Withdrawn by the authors due to lack of explicit agreement from all co-authors to post this version publicly on arXiv

**🔗 代码/项目**: [GITHUB](https://github.com/latuanvinh1998/KGAlign)

---

## 💡 一句话要点

**提出KGAlign以解决多模态假新闻检测中的知识编码问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `假新闻检测` `多模态融合` `知识图谱` `视觉特征提取` `文本编码` `Transformer分类器` `实体选择` `语义理解`

## 📋 核心要点

1. 现有假新闻检测方法存在局限，主要集中于全局图像上下文，忽视了局部细节和外部知识的整合。
2. 提出KGAlign框架，通过自下而上的注意力机制和知识图谱增强多模态特征融合，实现更深层次的语义理解。
3. 实验结果显示，KGAlign在假新闻检测任务中表现优异，超越了多种基线方法，验证了其有效性。

## 📝 摘要（中文）

假新闻检测仍然是一个具有挑战性的问题，因其涉及文本虚假信息、操控图像和外部知识推理的复杂交互。现有方法在验证真实性和跨模态一致性方面取得了一定成果，但仍面临两个主要挑战：一是现有方法往往只考虑全局图像上下文，而忽视局部对象级细节；二是未能结合外部知识和实体关系以实现更深层次的语义理解。为此，本文提出了一种新颖的多模态假新闻检测框架，整合视觉、文本和基于知识的表示。我们的方案利用自下而上的注意力机制捕捉细粒度对象细节，使用CLIP进行全局图像语义编码，并通过RoBERTa进行上下文感知的文本编码。我们进一步通过知识图谱检索和自适应选择相关实体来增强知识利用。实验结果表明，我们的模型在假新闻检测中优于近期方法，展示了邻居选择机制和多模态融合的有效性。

## 🔬 方法详解

**问题定义**：本文旨在解决多模态假新闻检测中的知识编码问题，现有方法未能充分利用局部对象信息和外部知识，导致检测效果不佳。

**核心思路**：KGAlign框架通过整合视觉、文本和知识表示，利用自下而上的注意力机制捕捉细粒度信息，并结合知识图谱进行实体选择，以实现更深层次的语义理解。

**技术框架**：整体架构包括三个主要模块：视觉特征提取（使用CLIP）、文本特征编码（使用RoBERTa）和知识图谱的实体选择，最后通过Transformer分类器进行假新闻的真实性预测。

**关键创新**：最重要的创新在于引入了知识驱动的多模态推理，通过显式的实体选择和NLI引导的过滤，将假新闻检测从特征融合转向语义基础的验证。

**关键设计**：在模型设计中，采用了自下而上的注意力机制以捕捉细粒度对象信息，并通过知识图谱进行动态实体选择，确保模型能够有效利用外部知识。

## 📊 实验亮点

实验结果表明，KGAlign在假新闻检测任务中显著优于多种基线方法，具体性能提升达到X%（具体数据未知），验证了邻居选择机制和多模态融合的有效性，展示了其在实际应用中的潜力。

## 🎯 应用场景

该研究的潜在应用领域包括社交媒体监测、新闻验证平台和信息传播分析等。通过提高假新闻检测的准确性，KGAlign能够有效减少虚假信息的传播，增强公众对信息的信任度，具有重要的社会价值和实际影响。

## 📄 摘要（原文）

> Fake news detection remains a challenging problem due to the complex interplay between textual misinformation, manipulated images, and external knowledge reasoning. While existing approaches have achieved notable results in verifying veracity and cross-modal consistency, two key challenges persist: (1) Existing methods often consider only the global image context while neglecting local object-level details, and (2) they fail to incorporate external knowledge and entity relationships for deeper semantic understanding. To address these challenges, we propose a novel multi-modal fake news detection framework that integrates visual, textual, and knowledge-based representations. Our approach leverages bottom-up attention to capture fine-grained object details, CLIP for global image semantics, and RoBERTa for context-aware text encoding. We further enhance knowledge utilization by retrieving and adaptively selecting relevant entities from a knowledge graph. The fused multi-modal features are processed through a Transformer-based classifier to predict news veracity. Experimental results demonstrate that our model outperforms recent approaches, showcasing the effectiveness of neighbor selection mechanism and multi-modal fusion for fake news detection. Our proposal introduces a new paradigm: knowledge-grounded multimodal reasoning. By integrating explicit entity-level selection and NLI-guided filtering, we shift fake news detection from feature fusion to semantically grounded verification. For reproducibility and further research, the source code is publicly at \href{https://github.com/latuanvinh1998/KGAlign}{github.com/latuanvinh1998/KGAlign}.

