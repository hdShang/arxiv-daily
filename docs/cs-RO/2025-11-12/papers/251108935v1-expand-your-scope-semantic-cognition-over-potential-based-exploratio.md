---
layout: default
title: Expand Your SCOPE: Semantic Cognition over Potential-Based Exploration for Embodied Visual Navigation
---

# Expand Your SCOPE: Semantic Cognition over Potential-Based Exploration for Embodied Visual Navigation

**arXiv**: [2511.08935v1](https://arxiv.org/abs/2511.08935) | [PDF](https://arxiv.org/pdf/2511.08935.pdf)

**作者**: Ningnan Wang, Weihuang Chen, Liming Chen, Haoxuan Ji, Zhongyu Guo, Xuchong Zhang, Hongbin Sun

---

## 💡 一句话要点

**提出SCOPE框架以解决具身视觉导航中的探索与规划问题**

**关键词**: `具身视觉导航` `零样本学习` `探索潜力` `时空图` `自反思机制` `视觉语言模型`

## 📋 核心要点

1. 核心问题：现有零样本方法忽视视觉边界，影响长程规划与目标推理。
2. 方法要点：利用视觉语言模型估计探索潜力，构建时空图并集成自反思机制。
3. 实验或效果：在两项导航任务中准确率提升4.6%，改善校准与泛化能力。

## 📄 摘要（原文）

> Embodied visual navigation remains a challenging task, as agents must explore unknown environments with limited knowledge. Existing zero-shot studies have shown that incorporating memory mechanisms to support goal-directed behavior can improve long-horizon planning performance. However, they overlook visual frontier boundaries, which fundamentally dictate future trajectories and observations, and fall short of inferring the relationship between partial visual observations and navigation goals. In this paper, we propose Semantic Cognition Over Potential-based Exploration (SCOPE), a zero-shot framework that explicitly leverages frontier information to drive potential-based exploration, enabling more informed and goal-relevant decisions. SCOPE estimates exploration potential with a Vision-Language Model and organizes it into a spatio-temporal potential graph, capturing boundary dynamics to support long-horizon planning. In addition, SCOPE incorporates a self-reconsideration mechanism that revisits and refines prior decisions, enhancing reliability and reducing overconfident errors. Experimental results on two diverse embodied navigation tasks show that SCOPE outperforms state-of-the-art baselines by 4.6\% in accuracy. Further analysis demonstrates that its core components lead to improved calibration, stronger generalization, and higher decision quality.

