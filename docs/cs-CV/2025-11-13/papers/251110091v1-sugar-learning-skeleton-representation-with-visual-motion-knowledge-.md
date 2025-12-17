---
layout: default
title: SUGAR: Learning Skeleton Representation with Visual-Motion Knowledge for Action Recognition
---

# SUGAR: Learning Skeleton Representation with Visual-Motion Knowledge for Action Recognition

**arXiv**: [2511.10091v1](https://arxiv.org/abs/2511.10091) | [PDF](https://arxiv.org/pdf/2511.10091.pdf)

**作者**: Qilang Ye, Yu Zhou, Lian He, Jie Zhang, Xuanming Guo, Jiayu Zhang, Mingkui Tan, Weicheng Xie, Yue Sun, Tao Tan, Xiaochen Yuan, Ghada Khoriba, Zitong Yu

---

## 💡 一句话要点

**提出SUGAR方法，结合视觉-运动知识学习骨架表示以进行动作识别**

**关键词**: `骨架动作识别` `视觉-运动知识` `大语言模型` `零样本学习` `时序建模`

## 📋 核心要点

1. 核心问题：如何让大语言模型理解骨架数据并区分不同动作
2. 方法要点：利用视频模型生成视觉-运动知识，监督骨架学习生成离散表示
3. 实验或效果：在多个基准测试中验证有效性，零样本场景下优于线性方法

## 📄 摘要（原文）

> Large Language Models (LLMs) hold rich implicit knowledge and powerful transferability. In this paper, we explore the combination of LLMs with the human skeleton to perform action classification and description. However, when treating LLM as a recognizer, two questions arise: 1) How can LLMs understand skeleton? 2) How can LLMs distinguish among actions? To address these problems, we introduce a novel paradigm named learning Skeleton representation with visUal-motion knowledGe for Action Recognition (SUGAR). In our pipeline, we first utilize off-the-shelf large-scale video models as a knowledge base to generate visual, motion information related to actions. Then, we propose to supervise skeleton learning through this prior knowledge to yield discrete representations. Finally, we use the LLM with untouched pre-training weights to understand these representations and generate the desired action targets and descriptions. Notably, we present a Temporal Query Projection (TQP) module to continuously model the skeleton signals with long sequences. Experiments on several skeleton-based action classification benchmarks demonstrate the efficacy of our SUGAR. Moreover, experiments on zero-shot scenarios show that SUGAR is more versatile than linear-based methods.

