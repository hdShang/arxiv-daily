---
layout: default
title: RegionRAG: Region-level Retrieval-Augumented Generation for Visually-Rich Documents
---

# RegionRAG: Region-level Retrieval-Augumented Generation for Visually-Rich Documents

**arXiv**: [2510.27261v1](https://arxiv.org/abs/2510.27261) | [PDF](https://arxiv.org/pdf/2510.27261.pdf)

**作者**: Yinglu Li, Zhiying Lu, Zhihang Liu, Chuanbin Liu, Hongtao Xie

---

## 💡 一句话要点

**提出RegionRAG框架，通过区域级检索增强生成解决视觉丰富文档中冗余内容问题**

**关键词**: `区域级检索` `检索增强生成` `视觉文档理解` `混合监督训练` `动态补丁分组`

## 📋 核心要点

1. 核心问题：文档级检索引入大量无关视觉内容，稀释关键信息并降低性能
2. 方法要点：训练时混合监督定位相关区域，推理时动态分组补丁为语义区域
3. 实验效果：在六个基准上实现SOTA，检索精度平均提升10.02%，问答精度提升3.56%

## 📄 摘要（原文）

> Multi-modal Retrieval-Augmented Generation (RAG) has become a critical method
> for empowering LLMs by leveraging candidate visual documents. However, current
> methods consider the entire document as the basic retrieval unit, introducing
> substantial irrelevant visual content in two ways: 1) Relevant documents often
> contain large regions unrelated to the query, diluting the focus on salient
> information; 2) Retrieving multiple documents to increase recall further
> introduces redundant and irrelevant documents. These redundant contexts
> distract the model's attention and further degrade the performance. To address
> this challenge, we propose \modelname, a novel framework that shifts the
> retrieval paradigm from the document level to the region level. During
> training, we design a hybrid supervision strategy from both labeled data and
> unlabeled data to pinpoint relevant patches. During inference, we propose a
> dynamic pipeline that intelligently groups salient patches into complete
> semantic regions. By delegating the task of identifying relevant regions to the
> retriever, \modelname enables the generator to focus solely on concise visual
> content relevant to queries, improving both efficiency and accuracy.
> Experiments on six benchmarks demonstrate that RegionRAG achieves
> state-of-the-art performance. Improves retrieval accuracy by 10.02\% in R@1 on
> average and increases question answering accuracy by 3.56\% while using only
> 71.42\% visual tokens compared to prior methods. The code will be available at
> https://github.com/Aeryn666/RegionRAG.

