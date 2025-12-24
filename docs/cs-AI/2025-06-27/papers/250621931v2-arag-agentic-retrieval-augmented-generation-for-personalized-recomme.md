---
layout: default
title: "ARAG: Agentic Retrieval Augmented Generation for Personalized Recommendation"
---

# ARAG: Agentic Retrieval Augmented Generation for Personalized Recommendation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.21931" class="toolbar-btn" target="_blank">📄 arXiv: 2506.21931v2</a>
  <a href="https://arxiv.org/pdf/2506.21931.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.21931v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.21931v2', 'ARAG: Agentic Retrieval Augmented Generation for Personalized Recommendation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Reza Yousefi Maragheh, Pratheek Vadla, Priyank Gupta, Kai Zhao, Aysenur Inan, Kehui Yao, Jianpeng Xu, Praveen Kanumala, Jason Cho, Sushant Kumar

**分类**: cs.IR, cs.AI, cs.CL, cs.MA

**发布日期**: 2025-06-27 (更新: 2025-08-11)

---

## 💡 一句话要点

**提出ARAG框架以解决个性化推荐中的用户偏好捕捉问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `个性化推荐` `检索增强生成` `多智能体系统` `用户偏好理解` `自然语言推理` `上下文总结` `推荐排序`

## 📋 核心要点

1. 现有的RAG方法依赖静态检索，无法动态捕捉用户的细微偏好，导致推荐效果不佳。
2. ARAG框架通过引入多智能体协作机制，利用四个专门的智能体来理解用户偏好并生成推荐。
3. 实验结果表明，ARAG在多个数据集上显著优于标准RAG和基于时效性的基线，提升效果显著。

## 📝 摘要（中文）

检索增强生成（RAG）在推荐系统中展现出潜力，但现有方法多依赖静态检索启发式，未能有效捕捉动态推荐场景中的用户偏好。本文提出ARAG，一个集成多智能体协作机制的个性化推荐框架，利用四个专门的基于大语言模型的智能体，分别负责用户理解、自然语言推理、上下文总结和项目排序。通过在三个数据集上的评估，ARAG在NDCG@5和Hit@5上分别提升了42.1%和35.5%，显示出智能体推理在检索增强推荐中的有效性。

## 🔬 方法详解

**问题定义**：本文旨在解决现有RAG方法在个性化推荐中无法动态捕捉用户偏好的问题，导致推荐效果不理想。

**核心思路**：ARAG框架通过引入多智能体协作机制，利用不同智能体分别处理用户理解、语义推理、上下文总结和推荐排序，从而提升推荐的个性化和准确性。

**技术框架**：ARAG的整体架构包括四个主要模块：用户理解智能体、自然语言推理智能体、上下文总结智能体和项目排序智能体，形成一个协同工作流程。

**关键创新**：ARAG的核心创新在于将智能体推理机制整合到检索增强推荐中，显著提升了对用户动态偏好的捕捉能力，与传统静态检索方法形成鲜明对比。

**关键设计**：在设计中，ARAG使用了特定的损失函数来优化智能体之间的协作，同时在网络结构上采用了基于大语言模型的架构，以确保对用户意图的准确理解和推荐的相关性。

## 📊 实验亮点

ARAG在三个数据集上的实验结果显示，NDCG@5提升了42.1%，Hit@5提升了35.5%，显著优于标准RAG和基于时效性的基线，验证了智能体推理在个性化推荐中的有效性和优势。

## 🎯 应用场景

ARAG框架在个性化推荐系统中具有广泛的应用潜力，能够为电商、社交媒体和内容推荐等领域提供更为精准的用户体验。通过动态捕捉用户偏好，ARAG能够提升用户满意度和平台的转化率，具有重要的实际价值和未来影响。

## 📄 摘要（原文）

> Retrieval-Augmented Generation (RAG) has shown promise in enhancing recommendation systems by incorporating external context into large language model prompts. However, existing RAG-based approaches often rely on static retrieval heuristics and fail to capture nuanced user preferences in dynamic recommendation scenarios. In this work, we introduce ARAG, an Agentic Retrieval-Augmented Generation framework for Personalized Recommendation, which integrates a multi-agent collaboration mechanism into the RAG pipeline. To better understand the long-term and session behavior of the user, ARAG leverages four specialized LLM-based agents: a User Understanding Agent that summarizes user preferences from long-term and session contexts, a Natural Language Inference (NLI) Agent that evaluates semantic alignment between candidate items retrieved by RAG and inferred intent, a context summary agent that summarizes the findings of NLI agent, and an Item Ranker Agent that generates a ranked list of recommendations based on contextual fit. We evaluate ARAG accross three datasets. Experimental results demonstrate that ARAG significantly outperforms standard RAG and recency-based baselines, achieving up to 42.1% improvement in NDCG@5 and 35.5% in Hit@5. We also, conduct an ablation study to analyse the effect by different components of ARAG. Our findings highlight the effectiveness of integrating agentic reasoning into retrieval-augmented recommendation and provide new directions for LLM-based personalization.

