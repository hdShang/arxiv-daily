---
layout: default
title: Benchmarking SAM2-based Trackers on FMOX
---

# Benchmarking SAM2-based Trackers on FMOX

**arXiv**: [2512.09633v1](https://arxiv.org/abs/2512.09633) | [PDF](https://arxiv.org/pdf/2512.09633.pdf)

**作者**: Senem Aktas, Charles Markham, John McDonald, Rozenn Dahyot

---

## 💡 一句话要点

**在FMOX数据集上基准测试基于SAM2的跟踪器，揭示其在快速移动对象上的性能**

**关键词**: `对象跟踪` `SAM2基准测试` `快速移动对象` `跟踪器性能评估` `计算机视觉`

## 📋 核心要点

1. 核心问题：评估基于SAM2的跟踪器在快速移动对象（FMO）数据集上的性能，以理解当前先进跟踪器的局限性。
2. 方法要点：基准测试SAM2、EfficientTAM、DAM4SAM和SAMURAI等跟踪器，使用用户提供的单模板进行对象跟踪和分割。
3. 实验或效果：DAM4SAM和SAMURAI在更具挑战性的序列上表现良好，提供了对跟踪器行为的详细洞察。

## 📄 摘要（原文）

> Several object tracking pipelines extending Segment Anything Model 2 (SAM2) have been proposed in the past year, where the approach is to follow and segment the object from a single exemplar template provided by the user on a initialization frame. We propose to benchmark these high performing trackers (SAM2, EfficientTAM, DAM4SAM and SAMURAI) on datasets containing fast moving objects (FMO) specifically designed to be challenging for tracking approaches. The goal is to understand better current limitations in state-of-the-art trackers by providing more detailed insights on the behavior of these trackers. We show that overall the trackers DAM4SAM and SAMURAI perform well on more challenging sequences.

