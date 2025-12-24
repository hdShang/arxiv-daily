---
layout: default
title: "MedKGent: A Large Language Model Agent Framework for Constructing Temporally Evolving Medical Knowledge Graph"
---

# MedKGent: A Large Language Model Agent Framework for Constructing Temporally Evolving Medical Knowledge Graph

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.12393" class="toolbar-btn" target="_blank">📄 arXiv: 2508.12393v2</a>
  <a href="https://arxiv.org/pdf/2508.12393.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.12393v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.12393v2', 'MedKGent: A Large Language Model Agent Framework for Constructing Temporally Evolving Medical Knowledge Graph')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Duzhen Zhang, Zixiao Wang, Zhong-Zhi Li, Yahan Yu, Shuncheng Jia, Jiahua Dong, Haotian Xu, Xing Wu, Yingying Zhang, Tielin Zhang, Jie Yang, Xiuying Chen, Le Song

**分类**: cs.CL, cs.AI

**发布日期**: 2025-08-17 (更新: 2025-08-19)

---

## 💡 一句话要点

**提出MedKGent框架以构建动态演变的医学知识图谱**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `医学知识图谱` `动态演变` `大型语言模型` `知识提取` `药物再利用` `自动化推理` `时间序列分析`

## 📋 核心要点

1. 现有医学知识图谱构建方法依赖于监督学习，缺乏对动态知识的适应性。
2. MedKGent框架通过两个代理逐日增量构建动态演变的医学知识图谱，解决了知识的时间动态问题。
3. 实验结果显示，MedKGent在医学问答基准上显著提升了性能，准确率接近90%。

## 📝 摘要（中文）

随着医学文献的快速扩展，结构化和整合领域知识的挑战日益增加。知识图谱（KGs）提供了一种有效的解决方案，但现有构建方法往往依赖于监督管道，缺乏广泛的适应性，或简单地聚合大型语言模型（LLMs）的输出，忽视了知识的时间动态和上下文不确定性。为了解决这些问题，本文提出了MedKGent，一个用于构建动态演变医学KG的LLM代理框架。该框架利用1975年至2023年间超过1000万篇PubMed摘要，通过细粒度的日时间序列模拟生物医学知识的出现。MedKGent通过两个专门的代理逐日增量构建KG，最终生成包含156,275个实体和2,971,384个关系三元组的知识图谱。

## 🔬 方法详解

**问题定义**：现有医学知识图谱构建方法往往依赖于静态数据和监督学习，无法有效处理生物医学知识的动态演变和上下文不确定性。

**核心思路**：MedKGent框架通过引入两个专门的代理，逐日增量构建知识图谱，利用时间序列数据捕捉知识的演变。

**技术框架**：框架包括Extractor Agent和Constructor Agent。Extractor Agent负责识别知识三元组并通过采样估计分配置信度分数，Constructor Agent则根据置信度和时间戳逐步整合三元组。

**关键创新**：MedKGent的创新在于其动态构建知识图谱的能力，能够处理时间变化和上下文不确定性，区别于传统静态聚合方法。

**关键设计**：Extractor Agent使用基于采样的估计方法来过滤低置信度的提取结果，Constructor Agent则根据置信度和时间戳来整合知识，确保知识的重复性和冲突解决。

## 📊 实验亮点

实验结果表明，MedKGent在七个医学问答基准上显著提升了性能，相较于未增强的基线，准确率接近90%，并且在专家评估中显示出强一致性。这表明该框架在实际应用中的有效性和可靠性。

## 🎯 应用场景

该研究的潜在应用领域包括医学文献的自动化分析、药物再利用研究以及临床决策支持。MedKGent能够为研究人员和临床医生提供更为准确和动态的知识支持，提升医学研究和实践的效率。

## 📄 摘要（原文）

> The rapid expansion of medical literature presents growing challenges for structuring and integrating domain knowledge at scale. Knowledge Graphs (KGs) offer a promising solution by enabling efficient retrieval, automated reasoning, and knowledge discovery. However, current KG construction methods often rely on supervised pipelines with limited generalizability or naively aggregate outputs from Large Language Models (LLMs), treating biomedical corpora as static and ignoring the temporal dynamics and contextual uncertainty of evolving knowledge. To address these limitations, we introduce MedKGent, a LLM agent framework for constructing temporally evolving medical KGs. Leveraging over 10 million PubMed abstracts published between 1975 and 2023, we simulate the emergence of biomedical knowledge via a fine-grained daily time series. MedKGent incrementally builds the KG in a day-by-day manner using two specialized agents powered by the Qwen2.5-32B-Instruct model. The Extractor Agent identifies knowledge triples and assigns confidence scores via sampling-based estimation, which are used to filter low-confidence extractions and inform downstream processing. The Constructor Agent incrementally integrates the retained triples into a temporally evolving graph, guided by confidence scores and timestamps to reinforce recurring knowledge and resolve conflicts. The resulting KG contains 156,275 entities and 2,971,384 relational triples. Quality assessments by two SOTA LLMs and three domain experts demonstrate an accuracy approaching 90%, with strong inter-rater agreement. To evaluate downstream utility, we conduct RAG across seven medical question answering benchmarks using five leading LLMs, consistently observing significant improvements over non-augmented baselines. Case studies further demonstrate the KG's value in literature-based drug repurposing via confidence-aware causal inference.

