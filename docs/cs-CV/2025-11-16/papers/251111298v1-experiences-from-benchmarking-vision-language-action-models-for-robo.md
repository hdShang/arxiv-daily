---
layout: default
title: Experiences from Benchmarking Vision-Language-Action Models for Robotic Manipulation
---

# Experiences from Benchmarking Vision-Language-Action Models for Robotic Manipulation

**arXiv**: [2511.11298v1](https://arxiv.org/abs/2511.11298) | [PDF](https://arxiv.org/pdf/2511.11298.pdf)

**作者**: Yihao Zhang, Yuankai Qi, Xi Zheng

---

## 💡 一句话要点

**基准测试四种视觉-语言-动作模型在机器人操作中的性能与适应性**

**关键词**: `视觉-语言-动作模型` `机器人操作基准测试` `分布外适应性` `标准化评估框架` `模型性能比较`

## 📋 核心要点

1. 核心问题：视觉-语言-动作模型在机器人操作中缺乏系统性评估与跨模型比较。
2. 方法要点：建立标准化评估框架，测量准确性、效率和适应性等维度。
3. 实验或效果：π_0在分布外场景适应性最佳，ACT在分布内稳定性最高。

## 📄 摘要（原文）

> Foundation models applied in robotics, particularly \textbf{Vision--Language--Action (VLA)} models, hold great promise for achieving general-purpose manipulation. Yet, systematic real-world evaluations and cross-model comparisons remain scarce. This paper reports our \textbf{empirical experiences} from benchmarking four representative VLAs -- \textbf{ACT}, \textbf{OpenVLA--OFT}, \textbf{RDT-1B}, and \boldmath{$π_0$} -- across four manipulation tasks conducted in both simulation and on the \textbf{ALOHA Mobile} platform. We establish a \textbf{standardized evaluation framework} that measures performance along three key dimensions: (1) \textit{accuracy and efficiency} (success rate and time-to-success), (2) \textit{adaptability} across in-distribution, spatial out-of-distribution, and instance-plus-spatial out-of-distribution settings, and (3) \textit{language instruction-following accuracy}. Through this process, we observe that \boldmath{$π_0$} demonstrates superior adaptability in out-of-distribution scenarios, while \textbf{ACT} provides the highest stability in-distribution. Further analysis highlights differences in computational demands, data-scaling behavior, and recurring failure modes such as near-miss grasps, premature releases, and long-horizon state drift. These findings reveal practical trade-offs among VLA model architectures in balancing precision, generalization, and deployment cost, offering actionable insights for selecting and deploying VLAs in real-world robotic manipulation tasks.

