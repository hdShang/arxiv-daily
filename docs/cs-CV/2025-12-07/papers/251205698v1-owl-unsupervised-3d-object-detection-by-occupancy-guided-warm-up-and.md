---
layout: default
title: OWL: Unsupervised 3D Object Detection by Occupancy Guided Warm-up and Large Model Priors Reasoning
---

# OWL: Unsupervised 3D Object Detection by Occupancy Guided Warm-up and Large Model Priors Reasoning

**arXiv**: [2512.05698v1](https://arxiv.org/abs/2512.05698) | [PDF](https://arxiv.org/pdf/2512.05698.pdf)

**作者**: Xusheng Guo, Wanfa Zhang, Shijia Zhao, Qiming Xia, Xiaolong Xie, Mingming Wang, Hai Wu, Chenglu Wen

---

## 💡 一句话要点

**提出OWL方法，通过占用引导预热和大模型先验推理解决无监督3D目标检测中伪标签误导与优化挑战。**

**关键词**: `无监督3D目标检测` `占用引导预热` `大模型先验推理` `伪标签优化` `自动驾驶`

## 📋 核心要点

1. 核心问题：无监督3D目标检测中初始伪标签错误易误导网络优化，且有效过滤与精炼伪标签是难题。
2. 方法要点：采用占用引导预热策略初始化骨干网络权重，结合实例提示推理模块利用大模型先验评估伪标签质量。
3. 实验或效果：在Waymo和KITTI数据集上超越现有无监督方法超过15.0% mAP，验证了方法的有效性。

## 📄 摘要（原文）

> Unsupervised 3D object detection leverages heuristic algorithms to discover potential objects, offering a promising route to reduce annotation costs in autonomous driving. Existing approaches mainly generate pseudo labels and refine them through self-training iterations. However, these pseudo-labels are often incorrect at the beginning of training, resulting in misleading the optimization process. Moreover, effectively filtering and refining them remains a critical challenge. In this paper, we propose OWL for unsupervised 3D object detection by occupancy guided warm-up and large-model priors reasoning. OWL first employs an Occupancy Guided Warm-up (OGW) strategy to initialize the backbone weight with spatial perception capabilities, mitigating the interference of incorrect pseudo-labels on network convergence. Furthermore, OWL introduces an Instance-Cued Reasoning (ICR) module that leverages the prior knowledge of large models to assess pseudo-label quality, enabling precise filtering and refinement. Finally, we design a Weight-adapted Self-training (WAS) strategy to dynamically re-weight pseudo-labels, improving the performance through self-training. Extensive experiments on Waymo Open Dataset (WOD) and KITTI demonstrate that OWL outperforms state-of-the-art unsupervised methods by over 15.0% mAP, revealing the effectiveness of our method.

