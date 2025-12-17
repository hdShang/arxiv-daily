---
layout: default
title: ReMatch: Boosting Representation through Matching for Multimodal Retrieval
---

# ReMatch: Boosting Representation through Matching for Multimodal Retrieval

**arXiv**: [2511.19278v1](https://arxiv.org/abs/2511.19278) | [PDF](https://arxiv.org/pdf/2511.19278.pdf)

**作者**: Qianying Liu, Xiao Liang, Zhiqiang Zhang, Yibo Chen, Xu Tang, Zhongfei Qing, Fengfan Zhou, Yao Hu, Paul Henderson

---

## 💡 一句话要点

**提出ReMatch框架，利用MLLM的生成能力增强多模态检索性能。**

**关键词**: `多模态检索` `生成匹配` `零样本泛化` `MLLM训练` `嵌入增强`

## 📋 核心要点

1. 核心问题：现有方法将MLLM仅用作编码器，忽略其生成特性，导致推理能力利用不足。
2. 方法要点：端到端训练嵌入MLLM，结合聊天式生成匹配阶段，提供实例级判别监督。
3. 实验效果：在MMEB基准上实现新SOTA，零样本泛化在五个数据集上表现优异。

## 📄 摘要（原文）

> We present ReMatch, a framework that leverages the generative strength of MLLMs for multimodal retrieval. Previous approaches treated an MLLM as a simple encoder, ignoring its generative nature, and under-utilising its compositional reasoning and world knowledge. We instead train the embedding MLLM end-to-end with a chat-style generative matching stage. The matching stage uses the same MLLM to autoregressively decide relevance from multi-view inputs, including both raw data and its own projected embeddings for each query and document. It provides instance-wise discrimination supervision that complements a standard contrastive loss, offering stronger gradients on hard negatives and preserving the compositional strengths of the original MLLM. To obtain semantically richer multimodal embeddings, we use multiple learnable tokens to augment each input, generating fine-grained contextual, mutually orthogonal embeddings with low inference cost. Leveraging our established high-performance baseline,we assemble the ideas mentioned above into a powerful training recipe and achieve a new state-of-the-art on the Massive Multimodal Embedding Benchmark (MMEB). Our experiments show particularly strong zero-shot generalization results on five datasets, highlighting the robustness and transferability of ReMatch.

