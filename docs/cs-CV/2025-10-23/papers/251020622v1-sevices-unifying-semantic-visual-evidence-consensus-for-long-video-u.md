---
layout: default
title: SeViCES: Unifying Semantic-Visual Evidence Consensus for Long Video Understanding
---

# SeViCES: Unifying Semantic-Visual Evidence Consensus for Long Video Understanding

**arXiv**: [2510.20622v1](https://arxiv.org/abs/2510.20622) | [PDF](https://arxiv.org/pdf/2510.20622.pdf)

**作者**: Yuan Sheng, Yanbin Hao, Chenxu Li, Shuo Wang, Xiangnan He

---

## 💡 一句话要点

**提出SeViCES框架以解决长视频理解中的证据选择问题**

**关键词**: `长视频理解` `证据选择` `语义视觉共识` `训练无关框架` `多模态融合`

## 📋 核心要点

1. 核心问题：长视频内容复杂分散，现有方法忽略时序依赖或依赖单模态证据
2. 方法要点：训练无关框架，结合语义分支和视觉分支进行共识帧选择
3. 实验或效果：在基准测试中准确性和鲁棒性优于先进方法

## 📄 摘要（原文）

> Long video understanding remains challenging due to its complex, diverse, and
> temporally scattered content. Although video large language models (Video-LLMs)
> can process videos lasting tens of minutes, applying them to truly long
> sequences is computationally prohibitive and often leads to unfocused or
> inconsistent reasoning. A promising solution is to select only the most
> informative frames, yet existing approaches typically ignore temporal
> dependencies or rely on unimodal evidence, limiting their ability to provide
> complete and query-relevant context. We propose a Semantic-Visual Consensus
> Evidence Selection (SeViCES) framework for effective and reliable long video
> understanding. SeViCES is training-free and model-agnostic, and introduces two
> key components. The Semantic-Visual Consensus Frame Selection (SVCFS) module
> selects frames through (1) a temporal-aware semantic branch that leverages LLM
> reasoning over captions, and (2) a cluster-guided visual branch that aligns
> embeddings with semantic scores via mutual information. The Answer Consensus
> Refinement (ACR) module further resolves inconsistencies between semantic- and
> visual-based predictions by fusing evidence and constraining the answer space.
> Extensive experiments on long video understanding benchmarks show that SeViCES
> consistently outperforms state-of-the-art methods in both accuracy and
> robustness, demonstrating the importance of consensus-driven evidence selection
> for Video-LLMs.

