---
layout: default
title: Unimedvl: Unifying Medical Multimodal Understanding And Generation Through Observation-Knowledge-Analysis
---

# Unimedvl: Unifying Medical Multimodal Understanding And Generation Through Observation-Knowledge-Analysis

**arXiv**: [2510.15710v1](https://arxiv.org/abs/2510.15710) | [PDF](https://arxiv.org/pdf/2510.15710.pdf)

**作者**: Junzhi Ning, Wei Li, Cheng Tang, Jiashi Lin, Chenglong Ma, Chaoyang Zhang, Jiyao Liu, Ying Chen, Shujian Gao, Lihao Liu, Yuandong Pu, Huihui Xu, Chenhui Gou, Ziyan Huang, Yi Xin, Qi Qin, Zhongying Deng, Diping Song, Bin Fu, Guang Yang, Yuanfeng Ji, Tianbin Li, Yanzhou Su, Jin Ye, Shixiang Tang, Ming Hu, Junjun He

---

## 💡 一句话要点

**提出UniMedVL统一框架，解决医学多模态理解与生成分离问题。**

**关键词**: `医学多模态理解` `医学图像生成` `统一模型架构` `渐进式课程学习` `Observation-Knowledge-Analysis` `双向知识共享`

## 📋 核心要点

1. 核心问题：现有医学AI系统将图像理解与生成任务分离，导致数据表示和特征整合不足。
2. 方法要点：基于Observation-Knowledge-Analysis范式，构建数据集并采用渐进式课程学习。
3. 实验或效果：在五个理解基准上表现优异，在八个生成模态中匹配专业模型质量。

## 📄 摘要（原文）

> Medical diagnostic applications require models that can process multimodal
> medical inputs (images, patient histories, lab results) and generate diverse
> outputs including both textual reports and visual content (annotations,
> segmentation masks, and images). Despite this need, existing medical AI systems
> disrupt this unified process: medical image understanding models interpret
> images but cannot generate visual outputs, while medical image generation
> models synthesize images but cannot provide textual explanations. This leads to
> gaps in data representation, feature integration, and task-level multimodal
> capabilities. To this end, we propose a multi-level framework that draws
> inspiration from diagnostic workflows through the
> Observation-Knowledge-Analysis (OKA) paradigm. Specifically, at the observation
> level, we construct UniMed-5M, a dataset comprising over 5.6M samples that
> reformat diverse unimodal data into multimodal pairs for foundational
> observation. At the knowledge level, we propose Progressive Curriculum Learning
> that systematically introduces medical multimodal knowledge. At the analysis
> level, we introduce UniMedVL, the first medical unified multimodal model for
> the simultaneous analysis of image understanding and generation tasks within a
> single architecture. UniMedVL achieves superior performance on five medical
> image understanding benchmarks, while matching specialized models in generation
> quality across eight medical imaging modalities. Crucially, our unified
> architecture enables bidirectional knowledge sharing: generation tasks enhance
> visual understanding features, demonstrating that integrating traditionally
> separate capabilities within a single medical framework unlocks improvements
> across diverse medical vision-language tasks. Code is available at
> https://github.com/uni-medical/UniMedVL.

