---
layout: default
title: Compression then Matching: An Efficient Pre-training Paradigm for Multimodal Embedding
---

# Compression then Matching: An Efficient Pre-training Paradigm for Multimodal Embedding

**arXiv**: [2511.08480v1](https://arxiv.org/abs/2511.08480) | [PDF](https://arxiv.org/pdf/2511.08480.pdf)

**作者**: Da Li, Yuxiao Luo, Keping Bi, Jiafeng Guo, Wei Yuan, Biao Yang, Yan Wang, Fan Yang, Tingting Gao, Guorui Zhou

---

## 💡 一句话要点

**提出CoMa预训练范式以高效优化多模态嵌入模型**

**关键词**: `多模态嵌入` `预训练范式` `对比学习` `压缩训练` `跨模态检索`

## 📋 核心要点

1. 核心问题：多模态嵌入需平衡语义完整性与下游任务判别性
2. 方法要点：通过压缩预训练阶段解耦语义理解与对比学习优化
3. 实验或效果：在MMEB基准上实现SOTA，提升效率与效果

## 📄 摘要（原文）

> Vision-language models advance multimodal representation learning by acquiring transferable semantic embeddings, thereby substantially enhancing performance across a range of vision-language tasks, including cross-modal retrieval, clustering, and classification. An effective embedding is expected to comprehensively preserve the semantic content of the input while simultaneously emphasizing features that are discriminative for downstream tasks. Recent approaches demonstrate that VLMs can be adapted into competitive embedding models via large-scale contrastive learning, enabling the simultaneous optimization of two complementary objectives. We argue that the two aforementioned objectives can be decoupled: a comprehensive understanding of the input facilitates the embedding model in achieving superior performance in downstream tasks via contrastive learning. In this paper, we propose CoMa, a compressed pre-training phase, which serves as a warm-up stage for contrastive learning. Experiments demonstrate that with only a small amount of pre-training data, we can transform a VLM into a competitive embedding model. CoMa achieves new state-of-the-art results among VLMs of comparable size on the MMEB, realizing optimization in both efficiency and effectiveness.

