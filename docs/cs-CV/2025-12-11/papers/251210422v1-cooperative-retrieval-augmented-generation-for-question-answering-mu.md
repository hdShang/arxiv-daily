---
layout: default
title: Cooperative Retrieval-Augmented Generation for Question Answering: Mutual Information Exchange and Ranking by Contrasting Layers
---

# Cooperative Retrieval-Augmented Generation for Question Answering: Mutual Information Exchange and Ranking by Contrasting Layers

**arXiv**: [2512.10422v1](https://arxiv.org/abs/2512.10422) | [PDF](https://arxiv.org/pdf/2512.10422.pdf)

**作者**: Youmin Ko, Sungjong Seo, Hyunjoon Kim

---

## 💡 一句话要点

**提出CoopRAG框架，通过检索器与LLM协同及层间对比排序，提升问答任务中检索与生成的准确性。**

**关键词**: `检索增强生成` `多跳问答` `协同学习` `层间对比` `推理链重建` `文档重排`

## 📋 核心要点

1. 针对现有RAG方法在简单和多跳问答中易出现错误检索和幻觉的问题。
2. 采用问题分解、推理链掩码、文档检索与层间对比重排、LLM填充重建的协同机制。
3. 实验表明在多个数据集上检索和问答性能优于现有方法，代码已开源。

## 📄 摘要（原文）

> Since large language models (LLMs) have a tendency to generate factually inaccurate output, retrieval-augmented generation (RAG) has gained significant attention as a key means to mitigate this downside of harnessing only LLMs. However, existing RAG methods for simple and multi-hop question answering (QA) are still prone to incorrect retrievals and hallucinations. To address these limitations, we propose CoopRAG, a novel RAG framework for the question answering task in which a retriever and an LLM work cooperatively with each other by exchanging informative knowledge, and the earlier and later layers of the retriever model work cooperatively with each other to accurately rank the retrieved documents relevant to a given query. In this framework, we (i) unroll a question into sub-questions and a reasoning chain in which uncertain positions are masked, (ii) retrieve the documents relevant to the question augmented with the sub-questions and the reasoning chain, (iii) rerank the documents by contrasting layers of the retriever, and (iv) reconstruct the reasoning chain by filling the masked positions via the LLM. Our experiments demonstrate that CoopRAG consistently outperforms state-of-the-art QA methods on three multi-hop QA datasets as well as a simple QA dataset in terms of both the retrieval and QA performances. Our code is available.\footnote{https://github.com/meaningful96/CoopRAG}

