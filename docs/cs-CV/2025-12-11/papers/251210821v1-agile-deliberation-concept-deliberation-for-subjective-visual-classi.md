---
layout: default
title: Agile Deliberation: Concept Deliberation for Subjective Visual Classification
---

# Agile Deliberation: Concept Deliberation for Subjective Visual Classification

**arXiv**: [2512.10821v1](https://arxiv.org/abs/2512.10821) | [PDF](https://arxiv.org/pdf/2512.10821.pdf)

**作者**: Leijie Wang, Otilia Stretcu, Wei Qiao, Thomas Denby, Krishnamurthy Viswanathan, Enming Luo, Chun-Ta Lu, Tushar Dogra, Ranjay Krishna, Ariel Fuxman

---

## 💡 一句话要点

**提出Agile Deliberation框架，通过概念审议支持主观视觉分类中用户概念的迭代精炼。**

**关键词**: `主观视觉分类` `概念审议` `人机交互框架` `内容审核` `迭代精炼` `边界案例`

## 📋 核心要点

1. 核心问题：用户常以模糊概念开始，需迭代精炼以提供高质量监督，现有方法假设概念清晰稳定。
2. 方法要点：系统分概念范围界定和概念迭代两阶段，利用边界案例促进用户反思与反馈。
3. 实验或效果：通过18次用户会话评估，F1分数比自动分解基线高7.5%，认知负担更低。

## 📄 摘要（原文）

> From content moderation to content curation, applications requiring vision classifiers for visual concepts are rapidly expanding. Existing human-in-the-loop approaches typically assume users begin with a clear, stable concept understanding to be able to provide high-quality supervision. In reality, users often start with a vague idea and must iteratively refine it through "concept deliberation", a practice we uncovered through structured interviews with content moderation experts. We operationalize the common strategies in deliberation used by real content moderators into a human-in-the-loop framework called "Agile Deliberation" that explicitly supports evolving and subjective concepts. The system supports users in defining the concept for themselves by exposing them to borderline cases. The system does this with two deliberation stages: (1) concept scoping, which decomposes the initial concept into a structured hierarchy of sub-concepts, and (2) concept iteration, which surfaces semantically borderline examples for user reflection and feedback to iteratively align an image classifier with the user's evolving intent. Since concept deliberation is inherently subjective and interactive, we painstakingly evaluate the framework through 18 user sessions, each 1.5h long, rather than standard benchmarking datasets. We find that Agile Deliberation achieves 7.5% higher F1 scores than automated decomposition baselines and more than 3% higher than manual deliberation, while participants reported clearer conceptual understanding and lower cognitive effort.

