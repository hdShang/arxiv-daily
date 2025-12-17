---
layout: default
title: MaxShapley: Towards Incentive-compatible Generative Search with Fair Context Attribution
---

# MaxShapley: Towards Incentive-compatible Generative Search with Fair Context Attribution

**arXiv**: [2512.05958v1](https://arxiv.org/abs/2512.05958) | [PDF](https://arxiv.org/pdf/2512.05958.pdf)

**作者**: Sara Patel, Mingxun Zhou, Giulia Fanti

---

## 💡 一句话要点

**提出MaxShapley算法，为基于检索增强生成的搜索系统实现高效公平的内容贡献度分配**

**关键词**: `生成式搜索` `贡献度分配` `Shapley值` `检索增强生成` `激励机制` `多跳问答`

## 📋 核心要点

1. 核心问题：生成式搜索需公平分配内容提供者贡献，传统Shapley值计算成本过高
2. 方法要点：利用可分解的最大和效用函数，将计算复杂度从指数级降至线性级
3. 实验效果：在三个多跳问答数据集上，以少量资源消耗达到与精确Shapley值相当的分配质量

## 📄 摘要（原文）

> Generative search engines based on large language models (LLMs) are replacing traditional search, fundamentally changing how information providers are compensated. To sustain this ecosystem, we need fair mechanisms to attribute and compensate content providers based on their contributions to generated answers. We introduce MaxShapley, an efficient algorithm for fair attribution in generative search pipelines that use retrieval-augmented generation (RAG). MaxShapley is a special case of the celebrated Shapley value; it leverages a decomposable max-sum utility function to compute attributions with linear computation in the number of documents, as opposed to the exponential cost of Shapley values. We evaluate MaxShapley on three multi-hop QA datasets (HotPotQA, MuSiQUE, MS MARCO); MaxShapley achieves comparable attribution quality to exact Shapley computation, while consuming a fraction of its tokens--for instance, it gives up to an 8x reduction in resource consumption over prior state-of-the-art methods at the same attribution accuracy.

