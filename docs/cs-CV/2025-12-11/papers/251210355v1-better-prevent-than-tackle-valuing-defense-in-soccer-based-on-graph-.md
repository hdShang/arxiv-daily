---
layout: default
title: Better Prevent than Tackle: Valuing Defense in Soccer Based on Graph Neural Networks
---

# Better Prevent than Tackle: Valuing Defense in Soccer Based on Graph Neural Networks

**arXiv**: [2512.10355v1](https://arxiv.org/abs/2512.10355) | [PDF](https://arxiv.org/pdf/2512.10355.pdf)

**作者**: Hyunsung Kim, Sangwoo Seo, Hoyoung Choi, Tom Boomstra, Jinsung Yoon, Chanyoung Park

---

## 💡 一句话要点

**提出DEFCON框架，基于图神经网络量化足球防守贡献，解决现有方法忽视预防性防守的问题。**

**关键词**: `足球防守评估` `图神经网络` `预期控球价值` `球员贡献量化` `图注意力网络`

## 📋 核心要点

1. 核心问题：现有足球防守评估方法主要关注抢断等有球动作，难以衡量预防性防守的贡献。
2. 方法要点：利用图注意力网络估计进攻选项的成功概率和预期价值，并分配防守责任，计算预期控球价值变化。
3. 实验或效果：在Eredivisie数据上训练和评估，球员积分与市场估值呈强正相关，并展示多种应用场景。

## 📄 摘要（原文）

> Evaluating defensive performance in soccer remains challenging, as effective defending is often expressed not through visible on-ball actions such as interceptions and tackles, but through preventing dangerous opportunities before they arise. Existing approaches have largely focused on valuing on-ball actions, leaving much of defenders' true impact unmeasured. To address this gap, we propose DEFCON (DEFensive CONtribution evaluator), a comprehensive framework that quantifies player-level defensive contributions for every attacking situation in soccer. Leveraging Graph Attention Networks, DEFCON estimates the success probability and expected value of each attacking option, along with each defender's responsibility for stopping it. These components yield an Expected Possession Value (EPV) for the attacking team before and after each action, and DEFCON assigns positive or negative credits to defenders according to whether they reduced or increased the opponent's EPV. Trained on 2023-24 and evaluated on 2024-25 Eredivisie event and tracking data, DEFCON's aggregated player credits exhibit strong positive correlations with market valuations. Finally, we showcase several practical applications, including in-game timelines of defensive contributions, spatial analyses across pitch zones, and pairwise summaries of attacker-defender interactions.

