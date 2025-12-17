---
layout: default
title: MobiAct: Efficient MAV Action Recognition Using MobileNetV4 with Contrastive Learning and Knowledge Distillation
---

# MobiAct: Efficient MAV Action Recognition Using MobileNetV4 with Contrastive Learning and Knowledge Distillation

**arXiv**: [2510.19273v1](https://arxiv.org/abs/2510.19273) | [PDF](https://arxiv.org/pdf/2510.19273.pdf)

**作者**: Zhang Nengbo, Ho Hann Woei

---

## 💡 一句话要点

**提出MobiAct框架，使用MobileNetV4与知识蒸馏，实现高效MAV动作识别。**

**关键词**: `MAV动作识别` `知识蒸馏` `MobileNetV4` `轻量级模型` `对比学习` `注意力机制`

## 📋 核心要点

1. 核心问题：现有MAV动作识别模型计算量大，不适合资源受限平台。
2. 方法要点：采用MobileNetV4骨干，结合阶段正交知识蒸馏和无参数注意力机制。
3. 实验效果：在自收集数据集上平均准确率92.12%，能耗低且解码速度快。

## 📄 摘要（原文）

> Accurate and efficient recognition of Micro Air Vehicle (MAV) motion is
> essential for enabling real-time perception and coordination in autonomous
> aerial swarm. However, most existing approaches rely on large, computationally
> intensive models that are unsuitable for resource-limited MAV platforms, which
> results in a trade-off between recognition accuracy and inference speed. To
> address these challenges, this paper proposes a lightweight MAV action
> recognition framework, MobiAct, designed to achieve high accuracy with low
> computational cost. Specifically, MobiAct adopts MobileNetV4 as the backbone
> network and introduces a Stage-wise Orthogonal Knowledge Distillation (SOKD)
> strategy to effectively transfer MAV motion features from a teacher network
> (ResNet18) to a student network, thereby enhancing knowledge transfer
> efficiency. Furthermore, a parameter-free attention mechanism is integrated
> into the architecture to improve recognition accuracy without increasing model
> complexity. In addition, a hybrid loss training strategy is developed to
> combine multiple loss objectives, which ensures stable and robust optimization
> during training. Experimental results demonstrate that the proposed MobiAct
> achieves low-energy and low-computation MAV action recognition, while
> maintaining the fastest action decoding speed among compared methods. Across
> all three self-collected datasets, MobiAct achieves an average recognition
> accuracy of 92.12%, while consuming only 136.16 pJ of energy and processing
> recognition at a rate of 8.84 actions per second. Notably, MobiAct decodes
> actions up to 2 times faster than the leading method, with highly comparable
> recognition accuracy, highlighting its superior efficiency in MAV action
> recognition.

