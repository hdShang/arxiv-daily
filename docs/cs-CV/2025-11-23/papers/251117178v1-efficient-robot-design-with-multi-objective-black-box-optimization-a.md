---
layout: default
title: Efficient Robot Design with Multi-Objective Black-Box Optimization and Large Language Models
---

# Efficient Robot Design with Multi-Objective Black-Box Optimization and Large Language Models

**arXiv**: [2511.17178v1](https://arxiv.org/abs/2511.17178) | [PDF](https://arxiv.org/pdf/2511.17178.pdf)

**作者**: Kento Kawaharazuka, Yoshiki Obinata, Naoaki Kanazawa, Haoyu Jia, Kei Okada

---

## 💡 一句话要点

**提出结合大语言模型与黑盒优化的方法以提升机器人设计效率**

**关键词**: `机器人设计优化` `黑盒优化` `大语言模型` `多目标优化` `采样效率`

## 📋 核心要点

1. 核心问题：黑盒优化采样效率低，难以处理复杂结构或离散值。
2. 方法要点：并行使用黑盒优化和大语言模型采样，提供问题设置与反馈。
3. 实验或效果：该方法能更高效探索设计解，但存在未知局限性。

## 📄 摘要（原文）

> Various methods for robot design optimization have been developed so far. These methods are diverse, ranging from numerical optimization to black-box optimization. While numerical optimization is fast, it is not suitable for cases involving complex structures or discrete values, leading to frequent use of black-box optimization instead. However, black-box optimization suffers from low sampling efficiency and takes considerable sampling iterations to obtain good solutions. In this study, we propose a method to enhance the efficiency of robot body design based on black-box optimization by utilizing large language models (LLMs). In parallel with the sampling process based on black-box optimization, sampling is performed using LLMs, which are provided with problem settings and extensive feedback. We demonstrate that this method enables more efficient exploration of design solutions and discuss its characteristics and limitations.

