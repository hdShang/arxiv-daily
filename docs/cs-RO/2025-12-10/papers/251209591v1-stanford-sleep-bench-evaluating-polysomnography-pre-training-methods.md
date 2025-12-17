---
layout: default
title: Stanford Sleep Bench: Evaluating Polysomnography Pre-training Methods for Sleep Foundation Models
---

# Stanford Sleep Bench: Evaluating Polysomnography Pre-training Methods for Sleep Foundation Models

**arXiv**: [2512.09591v1](https://arxiv.org/abs/2512.09591) | [PDF](https://arxiv.org/pdf/2512.09591.pdf)

**作者**: Magnus Ruud Kjaer, Rahul Thapa, Gauri Ganjoo, Hyatt Moore, Poul Joergen Jennum, Brandon M. Westover, James Zou, Emmanuel Mignot, Bryan He, Andreas Brink-Kjaer

---

## 💡 一句话要点

**提出Stanford Sleep Bench数据集与基准，以评估多导睡眠图自监督预训练方法在睡眠基础模型中的应用。**

**关键词**: `多导睡眠图` `自监督学习` `睡眠基础模型` `临床预测` `对比学习` `数据集基准`

## 📋 核心要点

1. 核心问题：睡眠基础模型发展受限，缺乏共享数据集和系统评估自监督学习方法。
2. 方法要点：引入大规模多导睡眠图数据集，包含17,467条记录和13个临床任务。
3. 实验或效果：对比学习在疾病和死亡率预测任务中表现显著优于其他方法，收敛更快。

## 📄 摘要（原文）

> Polysomnography (PSG), the gold standard test for sleep analysis, generates vast amounts of multimodal clinical data, presenting an opportunity to leverage self-supervised representation learning (SSRL) for pre-training foundation models to enhance sleep analysis. However, progress in sleep foundation models is hindered by two key limitations: (1) the lack of a shared dataset and benchmark with diverse tasks for training and evaluation, and (2) the absence of a systematic evaluation of SSRL approaches across sleep-related tasks. To address these gaps, we introduce Stanford Sleep Bench, a large-scale PSG dataset comprising 17,467 recordings totaling over 163,000 hours from a major sleep clinic, including 13 clinical disease prediction tasks alongside canonical sleep-related tasks such as sleep staging, apnea diagnosis, and age estimation. We systematically evaluate SSRL pre-training methods on Stanford Sleep Bench, assessing downstream performance across four tasks: sleep staging, apnea diagnosis, age estimation, and disease and mortality prediction. Our results show that multiple pretraining methods achieve comparable performance for sleep staging, apnea diagnosis, and age estimation. However, for mortality and disease prediction, contrastive learning significantly outperforms other approaches while also converging faster during pretraining. To facilitate reproducibility and advance sleep research, we will release Stanford Sleep Bench along with pretrained model weights, training pipelines, and evaluation code.

