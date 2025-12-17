---
layout: default
title: UniMM-V2X: MoE-Enhanced Multi-Level Fusion for End-to-End Cooperative Autonomous Driving
---

# UniMM-V2X: MoE-Enhanced Multi-Level Fusion for End-to-End Cooperative Autonomous Driving

**arXiv**: [2511.09013v1](https://arxiv.org/abs/2511.09013) | [PDF](https://arxiv.org/pdf/2511.09013.pdf)

**作者**: Ziyi Song, Chen Xia, Chenbing Wang, Haibao Yu, Sheng Zhou, Zhisheng Niu

---

## 💡 一句话要点

**提出MoE增强多级融合框架以提升端到端协同自动驾驶性能**

**关键词**: `协同自动驾驶` `多级融合` `MoE架构` `BEV表示` `端到端学习` `多智能体系统`

## 📋 核心要点

1. 核心问题：单车感知与决策受限，现有多智能体方法忽视感知与下游规划对齐。
2. 方法要点：引入多级融合策略和MoE架构，动态增强BEV表示并捕捉多样运动模式。
3. 实验效果：在DAIR-V2X数据集上，感知精度提升39.7%，预测误差降低7.2%。

## 📄 摘要（原文）

> Autonomous driving holds transformative potential but remains fundamentally constrained by the limited perception and isolated decision-making with standalone intelligence. While recent multi-agent approaches introduce cooperation, they often focus merely on perception-level tasks, overlooking the alignment with downstream planning and control, or fall short in leveraging the full capacity of the recent emerging end-to-end autonomous driving. In this paper, we present UniMM-V2X, a novel end-to-end multi-agent framework that enables hierarchical cooperation across perception, prediction, and planning. At the core of our framework is a multi-level fusion strategy that unifies perception and prediction cooperation, allowing agents to share queries and reason cooperatively for consistent and safe decision-making. To adapt to diverse downstream tasks and further enhance the quality of multi-level fusion, we incorporate a Mixture-of-Experts (MoE) architecture to dynamically enhance the BEV representations. We further extend MoE into the decoder to better capture diverse motion patterns. Extensive experiments on the DAIR-V2X dataset demonstrate our approach achieves state-of-the-art (SOTA) performance with a 39.7% improvement in perception accuracy, a 7.2% reduction in prediction error, and a 33.2% improvement in planning performance compared with UniV2X, showcasing the strength of our MoE-enhanced multi-level cooperative paradigm.

