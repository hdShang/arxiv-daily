---
layout: default
title: NavForesee: A Unified Vision-Language World Model for Hierarchical Planning and Dual-Horizon Navigation Prediction
---

# NavForesee: A Unified Vision-Language World Model for Hierarchical Planning and Dual-Horizon Navigation Prediction

**arXiv**: [2512.01550v1](https://arxiv.org/abs/2512.01550) | [PDF](https://arxiv.org/pdf/2512.01550.pdf)

**作者**: Fei Liu, Shichao Xie, Minghua Luo, Zedong Chu, Junjun Hu, Xiaolong Wu, Mu Xu

---

## 💡 一句话要点

**提出NavForesee统一视觉语言世界模型，以解决长视野任务中基于自然语言指令的导航规划与预测挑战。**

**关键词**: `视觉语言模型` `长视野导航` `世界模型预测` `任务规划` `自然语言指令` `感知-规划-行动循环`

## 📋 核心要点

1. 核心问题：现有智能体在未知环境中进行长视野导航时，规划能力不足，导致高失败率。
2. 方法要点：NavForesee将高层语言规划与生成式世界模型预测统一于单一框架，实现任务分解、进度跟踪和双视野预测。
3. 实验或效果：在R2R-CE和RxR-CE基准测试中，NavForesee在复杂场景下表现出高度竞争力。

## 📄 摘要（原文）

> Embodied navigation for long-horizon tasks, guided by complex natural language instructions, remains a formidable challenge in artificial intelligence. Existing agents often struggle with robust long-term planning about unseen environments, leading to high failure rates. To address these limitations, we introduce NavForesee, a novel Vision-Language Model (VLM) that unifies high-level language planning and predictive world model imagination within a single, unified framework. Our approach empowers a single VLM to concurrently perform planning and predictive foresight. Conditioned on the full instruction and historical observations, the model is trained to understand the navigation instructions by decomposing the task, tracking its progress, and formulating the subsequent sub-goal. Simultaneously, it functions as a generative world model, providing crucial foresight by predicting short-term environmental dynamics and long-term navigation milestones. The VLM's structured plan guides its targeted prediction, while the imagined future provides rich context to inform the navigation actions, creating a powerful internal feedback loop of perception-planning/prediction-action. We demonstrate through extensive experiments on the R2R-CE and RxR-CE benchmark that NavForesee achieves highly competitive performance in complex scenarios. Our work highlights the immense potential of fusing explicit language planning with implicit spatiotemporal prediction, paving the way for more intelligent and capable embodied agents.

