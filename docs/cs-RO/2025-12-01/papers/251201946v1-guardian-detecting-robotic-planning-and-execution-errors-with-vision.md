---
layout: default
title: Guardian: Detecting Robotic Planning and Execution Errors with Vision-Language Models
---

# Guardian: Detecting Robotic Planning and Execution Errors with Vision-Language Models

**arXiv**: [2512.01946v1](https://arxiv.org/abs/2512.01946) | [PDF](https://arxiv.org/pdf/2512.01946.pdf)

**作者**: Paul Pacaud, Ricardo Garcia, Shizhe Chen, Cordelia Schmid

---

## 💡 一句话要点

**提出自动机器人失败合成方法以解决视觉语言模型在失败检测中的数据稀缺问题**

**关键词**: `机器人失败检测` `视觉语言模型` `数据合成` `多视图图像` `失败基准` `自动扰动`

## 📋 核心要点

1. 核心问题：机器人操作中失败检测数据稀缺，限制视觉语言模型的准确性和泛化能力
2. 方法要点：通过程序化扰动成功轨迹，自动生成多样化的规划和执行失败数据
3. 实验或效果：构建三个新基准，训练Guardian模型在仿真和真实机器人中提升任务成功率

## 📄 摘要（原文）

> Robust robotic manipulation requires reliable failure detection and recovery. Although current Vision-Language Models (VLMs) show promise, their accuracy and generalization are limited by the scarcity of failure data. To address this data gap, we propose an automatic robot failure synthesis approach that procedurally perturbs successful trajectories to generate diverse planning and execution failures. This method produces not only binary classification labels but also fine-grained failure categories and step-by-step reasoning traces in both simulation and the real world. With it, we construct three new failure detection benchmarks: RLBench-Fail, BridgeDataV2-Fail, and UR5-Fail, substantially expanding the diversity and scale of existing failure datasets. We then train Guardian, a VLM with multi-view images for detailed failure reasoning and detection. Guardian achieves state-of-the-art performance on both existing and newly introduced benchmarks. It also effectively improves task success rates when integrated into a state-of-the-art manipulation system in simulation and real robots, demonstrating the impact of our generated failure data.

