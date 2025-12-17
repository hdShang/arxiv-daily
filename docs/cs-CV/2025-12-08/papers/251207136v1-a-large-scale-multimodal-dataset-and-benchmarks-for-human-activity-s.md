---
layout: default
title: A Large-Scale Multimodal Dataset and Benchmarks for Human Activity Scene Understanding and Reasoning
---

# A Large-Scale Multimodal Dataset and Benchmarks for Human Activity Scene Understanding and Reasoning

**arXiv**: [2512.07136v1](https://arxiv.org/abs/2512.07136) | [PDF](https://arxiv.org/pdf/2512.07136.pdf)

**作者**: Siyang Jiang, Mu Yuan, Xiang Ji, Bufang Yang, Zeyu Liu, Lilin Xu, Yang Li, Yuting He, Liran Dong, Wenrui Lu, Zhenyu Yan, Xiaofan Jiang, Wei Gao, Hongkai Chen, Guoliang Xing

---

## 💡 一句话要点

**提出大规模多模态数据集CUHK-X与基准套件，以支持人类活动理解与推理任务。**

**关键词**: `多模态数据集` `人类活动理解` `人类活动推理` `大规模视觉语言模型` `基准评估` `非RGB模态`

## 📋 核心要点

1. 核心问题：现有数据集缺乏非RGB模态的大规模文本描述资源，限制LVLMs在人类活动理解与推理中的应用。
2. 方法要点：采用基于提示的场景创建方法，利用LLMs生成逻辑连贯的活动序列，并通过人工验证提升描述一致性。
3. 实验或效果：在HAR、HAU和HARn任务上平均准确率分别为76.52%、40.76%和70.25%。

## 📄 摘要（原文）

> Multimodal human action recognition (HAR) leverages complementary sensors for activity classification. Beyond recognition, recent advances in large language models (LLMs) enable detailed descriptions and causal reasoning, motivating new tasks: human action understanding (HAU) and human action reasoning (HARn). However, most LLMs, especially large vision language models (LVLMs), struggle with non-RGB modalities such as depth, IMU, and mmWave due to the lack of large-scale data-caption resources. Existing HAR datasets mainly provide coarse data-label annotations, which are insufficient to capture fine-grained action dynamics needed for HAU and HARn. We consider two ground-truth pair types: (1) data label (discrete category) and (2) data caption (textual description). Naively generating captions from labels often lacks logical and spatiotemporal consistency. We introduce CUHK-X, a large-scale multimodal dataset and benchmark suite for HAR, HAU, and HARn. CUHK-X contains 58,445 samples covering 40 actions performed by 30 participants across two indoor environments. To improve caption consistency, we propose a prompt-based scene creation method that leverages LLMs to generate logically connected activity sequences, followed by human validation. CUHK-X includes three benchmarks with six evaluation tasks. Experiments report average accuracies of 76.52% (HAR), 40.76% (HAU), and 70.25% (HARn). CUHK-X aims to enable the community to apply and develop data-intensive learning methods for robust, multimodal human activity analysis. Project page and code: https://openaiotlab.github.io/CUHK-X/ and https://github.com/openaiotlab/CUHK-X.

