---
layout: default
title: Bridging Streaming Continual Learning via In-Context Large Tabular Models
---

# Bridging Streaming Continual Learning via In-Context Large Tabular Models

**arXiv**: [2512.11668v1](https://arxiv.org/abs/2512.11668) | [PDF](https://arxiv.org/pdf/2512.11668.pdf)

**作者**: Afonso Lourenço, João Gama, Eric P. Xing, Goreti Marreiros

---

## 💡 一句话要点

**提出基于大上下文表格模型的流式持续学习框架，以桥接流学习与持续学习**

**关键词**: `流式持续学习` `大上下文表格模型` `概念漂移` `灾难性遗忘` `数据压缩` `经验回放`

## 📋 核心要点

1. 核心问题：流式场景中模型需连续学习，但现有研究孤立处理流学习与持续学习，缺乏算法重叠
2. 方法要点：利用大上下文表格模型，将无界流数据实时压缩为紧凑摘要，平衡可塑性与稳定性
3. 实验或效果：通过分布匹配和压缩原则，实现数据选择，控制内存大小并避免冗余

## 📄 摘要（原文）

> In streaming scenarios, models must learn continuously, adapting to concept drifts without erasing previously acquired knowledge. However, existing research communities address these challenges in isolation. Continual Learning (CL) focuses on long-term retention and mitigating catastrophic forgetting, often without strict real-time constraints. Stream Learning (SL) emphasizes rapid, efficient adaptation to high-frequency data streams, but typically neglects forgetting. Recent efforts have tried to combine these paradigms, yet no clear algorithmic overlap exists. We argue that large in-context tabular models (LTMs) provide a natural bridge for Streaming Continual Learning (SCL). In our view, unbounded streams should be summarized on-the-fly into compact sketches that can be consumed by LTMs. This recovers the classical SL motivation of compressing massive streams with fixed-size guarantees, while simultaneously aligning with the experience-replay desiderata of CL. To clarify this bridge, we show how the SL and CL communities implicitly adopt a divide-to-conquer strategy to manage the tension between plasticity (performing well on the current distribution) and stability (retaining past knowledge), while also imposing a minimal complexity constraint that motivates diversification (avoiding redundancy in what is stored) and retrieval (re-prioritizing past information when needed). Within this perspective, we propose structuring SCL with LTMs around two core principles of data selection for in-context learning: (1) distribution matching, which balances plasticity and stability, and (2) distribution compression, which controls memory size through diversification and retrieval mechanisms.

