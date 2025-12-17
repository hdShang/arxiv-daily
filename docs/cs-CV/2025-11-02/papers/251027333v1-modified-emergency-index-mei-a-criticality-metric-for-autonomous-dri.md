---
layout: default
title: Modified-Emergency Index (MEI): A Criticality Metric for Autonomous Driving in Lateral Conflict
---

# Modified-Emergency Index (MEI): A Criticality Metric for Autonomous Driving in Lateral Conflict

**arXiv**: [2510.27333v1](https://arxiv.org/abs/2510.27333) | [PDF](https://arxiv.org/pdf/2510.27333.pdf)

**作者**: Hao Cheng, Yanbo Jiang, Qingyuan Shi, Qingwen Meng, Keyu Chen, Wenhao Yu, Jianqiang Wang, Sifa Zheng

---

## 💡 一句话要点

**提出改进紧急指数以量化自动驾驶横向冲突中的规避努力**

**关键词**: `自动驾驶安全` `关键性指标` `横向冲突` `风险评估` `规避努力` `公开数据集`

## 📋 核心要点

1. 现有关键性指标主要针对纵向冲突，难以准确评估横向冲突风险
2. MEI优化了规避动作可用时间估计，提升风险量化精度
3. 在公开数据集上验证，MEI在关键性量化和风险演化捕捉方面优于ACT和PET

## 📄 摘要（原文）

> Effective, reliable, and efficient evaluation of autonomous driving safety is
> essential to demonstrate its trustworthiness. Criticality metrics provide an
> objective means of assessing safety. However, as existing metrics primarily
> target longitudinal conflicts, accurately quantifying the risks of lateral
> conflicts - prevalent in urban settings - remains challenging. This paper
> proposes the Modified-Emergency Index (MEI), a metric designed to quantify
> evasive effort in lateral conflicts. Compared to the original Emergency Index
> (EI), MEI refines the estimation of the time available for evasive maneuvers,
> enabling more precise risk quantification. We validate MEI on a public lateral
> conflict dataset based on Argoverse-2, from which we extract over 1,500
> high-quality AV conflict cases, including more than 500 critical events. MEI is
> then compared with the well-established ACT and the widely used PET metrics.
> Results show that MEI consistently outperforms them in accurately quantifying
> criticality and capturing risk evolution. Overall, these findings highlight MEI
> as a promising metric for evaluating urban conflicts and enhancing the safety
> assessment framework for autonomous driving. The open-source implementation is
> available at https://github.com/AutoChengh/MEI.

