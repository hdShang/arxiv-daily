---
layout: default
title: Solving Semi-Supervised Few-Shot Learning from an Auto-Annotation Perspective
---

# Solving Semi-Supervised Few-Shot Learning from an Auto-Annotation Perspective

**arXiv**: [2512.10244v1](https://arxiv.org/abs/2512.10244) | [PDF](https://arxiv.org/pdf/2512.10244.pdf)

**作者**: Tian Liu, Anwesha Basu, James Caverlee, Shu Kong

---

## 💡 一句话要点

**提出SWIFT方法以解决半监督少样本学习中视觉语言模型微调效果不佳的问题**

**关键词**: `半监督少样本学习` `视觉语言模型微调` `伪标签置信度提升` `温度调优` `阶段式微调`

## 📋 核心要点

1. 核心问题：现有半监督少样本学习方法忽视开源视觉语言模型，导致微调时未标记数据利用率和监督信号弱
2. 方法要点：通过分类器初始化和温度调优提升伪标签置信度，并设计阶段式微调策略SWIFT以有效利用任务相关数据
3. 实验或效果：在五个基准测试中，SWIFT超越现有方法约5个准确点，甚至媲美监督学习

## 📄 摘要（原文）

> Semi-supervised few-shot learning (SSFSL) formulates real-world applications like ''auto-annotation'', as it aims to learn a model over a few labeled and abundant unlabeled examples to annotate the unlabeled ones. Despite the availability of powerful open-source Vision-Language Models (VLMs) and their pretraining data, the SSFSL literature largely neglects these open-source resources. In contrast, the related area few-shot learning (FSL) has already exploited them to boost performance. Arguably, to achieve auto-annotation in the real world, SSFSL should leverage such open-source resources. To this end, we start by applying established SSL methods to finetune a VLM. Counterintuitively, they significantly underperform FSL baselines. Our in-depth analysis reveals the root cause: VLMs produce rather ''flat'' distributions of softmax probabilities. This results in zero utilization of unlabeled data and weak supervision signals. We address this issue with embarrassingly simple techniques: classifier initialization and temperature tuning. They jointly increase the confidence scores of pseudo-labels, improving the utilization rate of unlabeled data, and strengthening supervision signals. Building on this, we propose: Stage-Wise Finetuning with Temperature Tuning (SWIFT), which enables existing SSL methods to effectively finetune a VLM on limited labeled data, abundant unlabeled data, and task-relevant but noisy data retrieved from the VLM's pretraining set. Extensive experiments on five SSFSL benchmarks show that SWIFT outperforms recent FSL and SSL methods by $\sim$5 accuracy points. SWIFT even rivals supervised learning, which finetunes VLMs with the unlabeled data being labeled with ground truth!

