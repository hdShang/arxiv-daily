---
layout: default
title: REMISVFU: Vertical Federated Unlearning via Representation Misdirection for Intermediate Output Feature
---

# REMISVFU: Vertical Federated Unlearning via Representation Misdirection for Intermediate Output Feature

**arXiv**: [2512.10348v1](https://arxiv.org/abs/2512.10348) | [PDF](https://arxiv.org/pdf/2512.10348.pdf)

**作者**: Wenhan Wu, Zhili He, Huanghuang Liang, Yili Gong, Jiawei Jiang, Chuang Hu, Dazhao Cheng

---

## 💡 一句话要点

**提出REMISVFU框架，通过表示误导实现垂直联邦学习中的快速客户端级遗忘**

**关键词**: `垂直联邦学习` `联邦遗忘` `表示误导` `客户端级遗忘` `隐私保护` `模型效用`

## 📋 核心要点

1. 针对垂直联邦学习（VFL）中数据按特征划分，现有遗忘方法无效的问题
2. 采用表示误导技术，将遗忘方编码器输出坍缩至单位球面随机锚点，切断特征与全局模型的统计关联
3. 实验显示，REMISVFU能抑制后门攻击至自然类先验水平，仅牺牲约2.5%的干净准确率

## 📄 摘要（原文）

> Data-protection regulations such as the GDPR grant every participant in a federated system a right to be forgotten. Federated unlearning has therefore emerged as a research frontier, aiming to remove a specific party's contribution from the learned model while preserving the utility of the remaining parties. However, most unlearning techniques focus on Horizontal Federated Learning (HFL), where data are partitioned by samples. In contrast, Vertical Federated Learning (VFL) allows organizations that possess complementary feature spaces to train a joint model without sharing raw data. The resulting feature-partitioned architecture renders HFL-oriented unlearning methods ineffective. In this paper, we propose REMISVFU, a plug-and-play representation misdirection framework that enables fast, client-level unlearning in splitVFL systems. When a deletion request arrives, the forgetting party collapses its encoder output to a randomly sampled anchor on the unit sphere, severing the statistical link between its features and the global model. To maintain utility for the remaining parties, the server jointly optimizes a retention loss and a forgetting loss, aligning their gradients via orthogonal projection to eliminate destructive interference. Evaluations on public benchmarks show that REMISVFU suppresses back-door attack success to the natural class-prior level and sacrifices only about 2.5% points of clean accuracy, outperforming state-of-the-art baselines.

