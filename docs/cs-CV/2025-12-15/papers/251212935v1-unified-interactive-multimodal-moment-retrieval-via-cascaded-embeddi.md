---
layout: default
title: Unified Interactive Multimodal Moment Retrieval via Cascaded Embedding-Reranking and Temporal-Aware Score Fusion
---

# Unified Interactive Multimodal Moment Retrieval via Cascaded Embedding-Reranking and Temporal-Aware Score Fusion

**arXiv**: [2512.12935v1](https://arxiv.org/abs/2512.12935) | [PDF](https://arxiv.org/pdf/2512.12935.pdf)

**作者**: Toan Le Ngo Thanh, Phat Ha Huu, Tan Nguyen Dang Duy, Thong Nguyen Le Minh, Anh Nguyen Nhu Tinh

---

## 💡 一句话要点

**提出统一交互式多模态时刻检索系统，通过级联嵌入-重排序和时序感知评分融合解决跨模态噪声和模糊查询问题。**

**关键词**: `多模态时刻检索` `时序建模` `查询分解` `嵌入融合` `交互式搜索` `视频理解`

## 📋 核心要点

1. 核心问题：现有方法面临固定权重融合策略失效、时序建模难以捕捉连贯事件序列、需手动模态选择降低可用性。
2. 方法要点：采用级联双嵌入管道结合BEIT-3和SigLIP进行广泛检索，BLIP-2重排序优化；时序感知评分机制通过波束搜索施加指数衰减惩罚；Agent引导查询分解自动解释模糊查询并自适应融合分数。
3. 实验或效果：系统有效处理模糊查询，检索时序连贯序列，动态适应融合策略，提升交互式时刻搜索能力。

## 📄 摘要（原文）

> The exponential growth of video content has created an urgent need for efficient multimodal moment retrieval systems. However, existing approaches face three critical challenges: (1) fixed-weight fusion strategies fail across cross modal noise and ambiguous queries, (2) temporal modeling struggles to capture coherent event sequences while penalizing unrealistic gaps, and (3) systems require manual modality selection, reducing usability. We propose a unified multimodal moment retrieval system with three key innovations. First, a cascaded dual-embedding pipeline combines BEIT-3 and SigLIP for broad retrieval, refined by BLIP-2 based reranking to balance recall and precision. Second, a temporal-aware scoring mechanism applies exponential decay penalties to large temporal gaps via beam search, constructing coherent event sequences rather than isolated frames. Third, Agent-guided query decomposition (GPT-4o) automatically interprets ambiguous queries, decomposes them into modality specific sub-queries (visual/OCR/ASR), and performs adaptive score fusion eliminating manual modality selection. Qualitative analysis demonstrates that our system effectively handles ambiguous queries, retrieves temporally coherent sequences, and dynamically adapts fusion strategies, advancing interactive moment search capabilities.

