---
layout: default
title: Point to Span: Zero-Shot Moment Retrieval for Navigating Unseen Hour-Long Videos
---

# Point to Span: Zero-Shot Moment Retrieval for Navigating Unseen Hour-Long Videos

**arXiv**: [2512.10363v1](https://arxiv.org/abs/2512.10363) | [PDF](https://arxiv.org/pdf/2512.10363.pdf)

**作者**: Mingyu Jeon, Jisoo Yang, Sungjin Han, Jinkwon Hwang, Sunjae Yoon, Jonghee Kim, Junyeoung Kim

---

## 💡 一句话要点

**提出Point-to-Span框架以解决零样本长视频时刻检索中的搜索爆炸和验证成本高问题**

**关键词**: `零样本学习` `长视频理解` `时刻检索` `自适应跨度生成` `查询分解` `训练免费框架`

## 📋 核心要点

1. 核心问题：零样本长视频时刻检索面临搜索阶段候选爆炸和验证阶段高成本VLM依赖的挑战
2. 方法要点：通过自适应跨度生成器防止候选爆炸，并利用查询分解进行低成本候选精炼
3. 实验或效果：在MAD数据集上超越监督方法，如R5@0.1指标提升3.7%

## 📄 摘要（原文）

> Zero-shot Long Video Moment Retrieval (ZLVMR) is the task of identifying temporal segments in hour-long videos using a natural language query without task-specific training. The core technical challenge of LVMR stems from the computational infeasibility of processing entire lengthy videos in a single pass. This limitation has established a 'Search-then-Refine' approach, where candidates are rapidly narrowed down, and only those portions are analyzed, as the dominant paradigm for LVMR. However, existing approaches to this paradigm face severe limitations. Conventional supervised learning suffers from limited scalability and poor generalization, despite substantial resource consumption. Yet, existing zero-shot methods also fail, facing a dual challenge: (1) their heuristic strategies cause a 'search' phase candidate explosion, and (2) the 'refine' phase, which is vulnerable to semantic discrepancy, requires high-cost VLMs for verification, incurring significant computational overhead. We propose \textbf{P}oint-\textbf{to}-\textbf{S}pan (P2S), a novel training-free framework to overcome this challenge of inefficient 'search' and costly 'refine' phases. P2S overcomes these challenges with two key innovations: an 'Adaptive Span Generator' to prevent the search phase candidate explosion, and 'Query Decomposition' to refine candidates without relying on high-cost VLM verification. To our knowledge, P2S is the first zero-shot framework capable of temporal grounding in hour-long videos, outperforming supervised state-of-the-art methods by a significant margin (e.g., +3.7\% on R5@0.1 on MAD).

