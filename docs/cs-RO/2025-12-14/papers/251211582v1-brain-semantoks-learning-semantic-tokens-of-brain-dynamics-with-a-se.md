---
layout: default
title: Brain-Semantoks: Learning Semantic Tokens of Brain Dynamics with a Self-Distilled Foundation Model
---

# Brain-Semantoks: Learning Semantic Tokens of Brain Dynamics with a Self-Distilled Foundation Model

**arXiv**: [2512.11582v1](https://arxiv.org/abs/2512.11582) | [PDF](https://arxiv.org/pdf/2512.11582.pdf)

**作者**: Sam Gijsen, Marc-Andre Schulz, Kerstin Ritter

---

## 💡 一句话要点

**提出Brain-Semantoks框架以学习脑功能磁共振成像时间序列的抽象表示，提升下游任务性能。**

**关键词**: `功能磁共振成像` `自监督学习` `语义分词器` `自蒸馏` `脑动力学` `基础模型`

## 📋 核心要点

1. 当前fMRI基础模型常基于小区域掩码重建训练，导致表示对噪声敏感，需大量微调。
2. 引入语义分词器聚合区域信号为功能网络令牌，结合自蒸馏目标增强时间稳定性。
3. 学习表示在线性探针下实现强下游任务性能，缩放分析显示无标签数据提升分布外性能。

## 📄 摘要（原文）

> The development of foundation models for functional magnetic resonance imaging (fMRI) time series holds significant promise for predicting phenotypes related to disease and cognition. Current models, however, are often trained using a mask-and-reconstruct objective on small brain regions. This focus on low-level information leads to representations that are sensitive to noise and temporal fluctuations, necessitating extensive fine-tuning for downstream tasks. We introduce Brain-Semantoks, a self-supervised framework designed specifically to learn abstract representations of brain dynamics. Its architecture is built on two core innovations: a semantic tokenizer that aggregates noisy regional signals into robust tokens representing functional networks, and a self-distillation objective that enforces representational stability across time. We show that this objective is stabilized through a novel training curriculum, ensuring the model robustly learns meaningful features from low signal-to-noise time series. We demonstrate that learned representations enable strong performance on a variety of downstream tasks even when only using a linear probe. Furthermore, we provide comprehensive scaling analyses indicating more unlabeled data reliably results in out-of-distribution performance gains without domain adaptation.

