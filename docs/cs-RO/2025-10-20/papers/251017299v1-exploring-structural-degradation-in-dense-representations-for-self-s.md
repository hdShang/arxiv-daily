---
layout: default
title: Exploring Structural Degradation in Dense Representations for Self-supervised Learning
---

# Exploring Structural Degradation in Dense Representations for Self-supervised Learning

**arXiv**: [2510.17299v1](https://arxiv.org/abs/2510.17299) | [PDF](https://arxiv.org/pdf/2510.17299.pdf)

**作者**: Siran Dai, Qianqian Xu, Peisong Wen, Yang Liu, Qingming Huang

---

## 💡 一句话要点

**提出DSE指标与策略以缓解自监督学习中的密集预测退化问题**

**关键词**: `自监督学习` `密集预测` `表示结构评估` `模型选择` `正则化方法`

## 📋 核心要点

1. 自监督学习中，训练时间延长可能损害密集预测任务性能，称为SDD现象
2. 引入DSE指标，结合类相关性和有效维度，无需标注评估密集表示结构
3. 实验验证模型选择和正则化策略平均提升mIoU 3.0%，有效缓解退化

## 📄 摘要（原文）

> In this work, we observe a counterintuitive phenomenon in self-supervised
> learning (SSL): longer training may impair the performance of dense prediction
> tasks (e.g., semantic segmentation). We refer to this phenomenon as
> Self-supervised Dense Degradation (SDD) and demonstrate its consistent presence
> across sixteen state-of-the-art SSL methods with various losses, architectures,
> and datasets. When the model performs suboptimally on dense tasks at the end of
> training, measuring the performance during training becomes essential. However,
> evaluating dense performance effectively without annotations remains an open
> challenge. To tackle this issue, we introduce a Dense representation Structure
> Estimator (DSE), composed of a class-relevance measure and an effective
> dimensionality measure. The proposed DSE is both theoretically grounded and
> empirically validated to be closely correlated with the downstream performance.
> Based on this metric, we introduce a straightforward yet effective model
> selection strategy and a DSE-based regularization method. Experiments on
> sixteen SSL methods across four benchmarks confirm that model selection
> improves mIoU by $3.0\%$ on average with negligible computational cost.
> Additionally, DSE regularization consistently mitigates the effects of dense
> degradation. Code is available at
> https://github.com/EldercatSAM/SSL-Degradation.

