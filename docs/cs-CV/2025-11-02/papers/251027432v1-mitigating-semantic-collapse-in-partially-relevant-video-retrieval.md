---
layout: default
title: Mitigating Semantic Collapse in Partially Relevant Video Retrieval
---

# Mitigating Semantic Collapse in Partially Relevant Video Retrieval

**arXiv**: [2510.27432v1](https://arxiv.org/abs/2510.27432) | [PDF](https://arxiv.org/pdf/2510.27432.pdf)

**作者**: WonJun Moon, MinSeok Jung, Gilhan Park, Tae-Young Kim, Cheol-Ho Cho, Woojin Jun, Jae-Pil Heo

---

## 💡 一句话要点

**提出文本相关保留学习和跨分支视频对齐方法，以缓解部分相关视频检索中的语义坍缩问题。**

**关键词**: `部分相关视频检索` `语义坍缩` `文本相关保留学习` `跨分支视频对齐` `层次视频表示` `对比学习`

## 📋 核心要点

1. 核心问题：现有方法忽略视频内和跨视频的语义变化，导致嵌入空间语义坍缩，限制检索性能。
2. 方法要点：引入文本相关保留学习保持查询语义关系，并使用跨分支视频对齐解耦层次视频表示。
3. 实验或效果：在PRVR基准测试中，框架有效防止语义坍缩，显著提升检索准确率。

## 📄 摘要（原文）

> Partially Relevant Video Retrieval (PRVR) seeks videos where only part of the
> content matches a text query. Existing methods treat every annotated text-video
> pair as a positive and all others as negatives, ignoring the rich semantic
> variation both within a single video and across different videos. Consequently,
> embeddings of both queries and their corresponding video-clip segments for
> distinct events within the same video collapse together, while embeddings of
> semantically similar queries and segments from different videos are driven
> apart. This limits retrieval performance when videos contain multiple, diverse
> events. This paper addresses the aforementioned problems, termed as semantic
> collapse, in both the text and video embedding spaces. We first introduce Text
> Correlation Preservation Learning, which preserves the semantic relationships
> encoded by the foundation model across text queries. To address collapse in
> video embeddings, we propose Cross-Branch Video Alignment (CBVA), a contrastive
> alignment method that disentangles hierarchical video representations across
> temporal scales. Subsequently, we introduce order-preserving token merging and
> adaptive CBVA to enhance alignment by producing video segments that are
> internally coherent yet mutually distinctive. Extensive experiments on PRVR
> benchmarks demonstrate that our framework effectively prevents semantic
> collapse and substantially improves retrieval accuracy.

