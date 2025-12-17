---
layout: default
title: Nav-$R^2$ Dual-Relation Reasoning for Generalizable Open-Vocabulary Object-Goal Navigation
---

# Nav-$R^2$ Dual-Relation Reasoning for Generalizable Open-Vocabulary Object-Goal Navigation

**arXiv**: [2512.02400v1](https://arxiv.org/abs/2512.02400) | [PDF](https://arxiv.org/pdf/2512.02400.pdf)

**作者**: Wentao Xiang, Haokang Zhang, Tianhang Yang, Zedong Chu, Ruihang Chu, Shichao Xie, Yujian Yuan, Jian Sun, Zhining Gu, Junjie Wang, Xiaolong Wu, Mu Xu, Yujiu Yang

---

## 💡 一句话要点

**提出Nav-R^2框架，通过双关系推理解决开放词汇对象目标导航中未见对象定位问题。**

**关键词**: `开放词汇导航` `对象目标导航` `双关系推理` `思维链推理` `相似性感知记忆` `未见对象定位`

## 📋 核心要点

1. 核心问题：开放词汇对象目标导航中，现有方法决策不透明且对未见对象定位成功率低。
2. 方法要点：显式建模目标-环境和环境-动作双关系，结合结构化思维链推理与相似性感知记忆。
3. 实验或效果：在未见对象定位上达到最先进性能，避免过拟合，保持实时推理速度。

## 📄 摘要（原文）

> Object-goal navigation in open-vocabulary settings requires agents to locate novel objects in unseen environments, yet existing approaches suffer from opaque decision-making processes and low success rate on locating unseen objects. To address these challenges, we propose Nav-$R^2$, a framework that explicitly models two critical types of relationships, target-environment modeling and environment-action planning, through structured Chain-of-Thought (CoT) reasoning coupled with a Similarity-Aware Memory. We construct a Nav$R^2$-CoT dataset that teaches the model to perceive the environment, focus on target-related objects in the surrounding context and finally make future action plans. Our SA-Mem preserves the most target-relevant and current observation-relevant features from both temporal and semantic perspectives by compressing video frames and fusing historical observations, while introducing no additional parameters. Compared to previous methods, Nav-R^2 achieves state-of-the-art performance in localizing unseen objects through a streamlined and efficient pipeline, avoiding overfitting to seen object categories while maintaining real-time inference at 2Hz. Resources will be made publicly available at \href{https://github.com/AMAP-EAI/Nav-R2}{github link}.

