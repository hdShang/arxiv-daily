---
layout: default
title: How Far are Modern Trackers from UAV-Anti-UAV? A Million-Scale Benchmark and New Baseline
---

# How Far are Modern Trackers from UAV-Anti-UAV? A Million-Scale Benchmark and New Baseline

**arXiv**: [2512.07385v1](https://arxiv.org/abs/2512.07385) | [PDF](https://arxiv.org/pdf/2512.07385.pdf)

**作者**: Chunhui Zhang, Li Liu, Zhipeng Zhang, Yong Wang, Hao Wen, Xi Zhou, Shiming Ge, Yanfeng Wang

---

## 💡 一句话要点

**提出UAV-Anti-UAV任务与MambaSTS基线，以解决移动无人机平台追踪目标无人机的挑战。**

**关键词**: `无人机追踪` `多模态视觉跟踪` `时空语义学习` `Mamba模型` `长序列建模` `基准数据集`

## 📋 核心要点

1. 核心问题：现有反无人机研究忽视移动平台追踪，UAV-Anti-UAV任务面临双动态干扰。
2. 方法要点：构建百万规模数据集，提出MambaSTS方法，集成时空语义学习。
3. 实验或效果：评估50种现代跟踪算法，显示该领域有显著改进空间，验证MambaSTS有效性。

## 📄 摘要（原文）

> Unmanned Aerial Vehicles (UAVs) offer wide-ranging applications but also pose significant safety and privacy violation risks in areas like airport and infrastructure inspection, spurring the rapid development of Anti-UAV technologies in recent years. However, current Anti-UAV research primarily focuses on RGB, infrared (IR), or RGB-IR videos captured by fixed ground cameras, with little attention to tracking target UAVs from another moving UAV platform. To fill this gap, we propose a new multi-modal visual tracking task termed UAV-Anti-UAV, which involves a pursuer UAV tracking a target adversarial UAV in the video stream. Compared to existing Anti-UAV tasks, UAV-Anti-UAV is more challenging due to severe dual-dynamic disturbances caused by the rapid motion of both the capturing platform and the target. To advance research in this domain, we construct a million-scale dataset consisting of 1,810 videos, each manually annotated with bounding boxes, a language prompt, and 15 tracking attributes. Furthermore, we propose MambaSTS, a Mamba-based baseline method for UAV-Anti-UAV tracking, which enables integrated spatial-temporal-semantic learning. Specifically, we employ Mamba and Transformer models to learn global semantic and spatial features, respectively, and leverage the state space model's strength in long-sequence modeling to establish video-level long-term context via a temporal token propagation mechanism. We conduct experiments on the UAV-Anti-UAV dataset to validate the effectiveness of our method. A thorough experimental evaluation of 50 modern deep tracking algorithms demonstrates that there is still significant room for improvement in the UAV-Anti-UAV domain. The dataset and codes will be available at {\color{magenta}https://github.com/983632847/Awesome-Multimodal-Object-Tracking}.

