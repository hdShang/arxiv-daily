---
layout: default
title: Procedural Mistake Detection via Action Effect Modeling
---

# Procedural Mistake Detection via Action Effect Modeling

**arXiv**: [2512.03474v1](https://arxiv.org/abs/2512.03474) | [PDF](https://arxiv.org/pdf/2512.03474.pdf)

**作者**: Wenliang Guo, Yujiang Pu, Yu Kong

---

## 💡 一句话要点

**提出动作效果建模框架，通过联合建模动作执行与结果以提升过程性任务中的错误检测性能。**

**关键词**: `过程性错误检测` `动作效果建模` `视觉基础` `符号场景图` `单类分类`

## 📋 核心要点

1. 核心问题：现有方法忽略动作效果，导致许多错误无法检测，如对象状态或空间排列错误。
2. 方法要点：AEM框架通过概率建模，结合视觉基础和符号场景图，提取效果感知表示，并设计基于提示的检测器。
3. 实验或效果：在EgoPER和CaptainCook4D基准上，在单类分类设置下达到最先进性能，验证了联合建模的有效性。

## 📄 摘要（原文）

> Mistake detection in procedural tasks is essential for building intelligent systems that support learning and task execution. Existing approaches primarily analyze how an action is performed, while overlooking what it produces, i.e., the \textbf{action effect}. Yet many errors manifest not in the execution itself but in the resulting outcome, such as an unintended object state or incorrect spatial arrangement. To address this gap, we propose Action Effect Modeling (AEM), a unified framework that jointly captures action execution and its outcomes through a probabilistic formulation. AEM first identifies the outcome of an action by selecting the most informative effect frame based on semantic relevance and visual quality. It then extracts complementary cues from visual grounding and symbolic scene graphs, aligning them in a shared latent space to form robust effect-aware representations. To detect mistakes, we further design a prompt-based detector that incorporates task-specific prompts and aligns each action segment with its intended execution semantics. Our approach achieves state-of-the-art performance on the EgoPER and CaptainCook4D benchmarks under the challenging one-class classification (OCC) setting. These results demonstrate that modeling both execution and outcome yields more reliable mistake detection, and highlight the potential of effect-aware representations to benefit a broader range of downstream applications.

