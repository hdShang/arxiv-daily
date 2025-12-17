---
layout: default
title: GigaWorld-0: World Models as Data Engine to Empower Embodied AI
---

# GigaWorld-0: World Models as Data Engine to Empower Embodied AI

**arXiv**: [2511.19861v1](https://arxiv.org/abs/2511.19861) | [PDF](https://arxiv.org/pdf/2511.19861.pdf)

**作者**: GigaWorld Team, Angen Ye, Boyuan Wang, Chaojun Ni, Guan Huang, Guosheng Zhao, Haoyun Li, Jiagang Zhu, Kerui Li, Mengyuan Xu, Qiuping Deng, Siting Wang, Wenkang Qin, Xinze Chen, Xiaofeng Wang, Yankai Wang, Yu Cao, Yifan Chang, Yuan Xu, Yun Ye, Yang Wang, Yukun Zhou, Zhengyuan Zhang, Zhehao Dong, Zheng Zhu

---

## 💡 一句话要点

**提出GigaWorld-0世界模型框架作为数据引擎，赋能具身AI学习。**

**关键词**: `世界模型` `视频生成` `3D建模` `具身AI` `数据合成` `高效训练`

## 📋 核心要点

1. 核心问题：具身AI需要大规模、高质量交互数据，但真实数据获取成本高。
2. 方法要点：集成视频生成与3D建模组件，联合优化生成视觉逼真、物理合理的序列。
3. 实验或效果：生成数据训练VLA模型，显著提升物理机器人任务成功率和泛化能力。

## 📄 摘要（原文）

> World models are emerging as a foundational paradigm for scalable, data-efficient embodied AI. In this work, we present GigaWorld-0, a unified world model framework designed explicitly as a data engine for Vision-Language-Action (VLA) learning. GigaWorld-0 integrates two synergistic components: GigaWorld-0-Video, which leverages large-scale video generation to produce diverse, texture-rich, and temporally coherent embodied sequences under fine-grained control of appearance, camera viewpoint, and action semantics; and GigaWorld-0-3D, which combines 3D generative modeling, 3D Gaussian Splatting reconstruction, physically differentiable system identification, and executable motion planning to ensure geometric consistency and physical realism. Their joint optimization enables the scalable synthesis of embodied interaction data that is visually compelling, spatially coherent, physically plausible, and instruction-aligned. Training at scale is made feasible through our efficient GigaTrain framework, which exploits FP8-precision and sparse attention to drastically reduce memory and compute requirements. We conduct comprehensive evaluations showing that GigaWorld-0 generates high-quality, diverse, and controllable data across multiple dimensions. Critically, VLA model (e.g., GigaBrain-0) trained on GigaWorld-0-generated data achieve strong real-world performance, significantly improving generalization and task success on physical robots without any real-world interaction during training.

