---
layout: default
title: MindDrive: An All-in-One Framework Bridging World Models and Vision-Language Model for End-to-End Autonomous Driving
---

# MindDrive: An All-in-One Framework Bridging World Models and Vision-Language Model for End-to-End Autonomous Driving

**arXiv**: [2512.04441v1](https://arxiv.org/abs/2512.04441) | [PDF](https://arxiv.org/pdf/2512.04441.pdf)

**作者**: Bin Suna, Yaoguang Caob, Yan Wanga, Rui Wanga, Jiachen Shanga, Xiejie Fenga, Jiayi Lu, Jia Shi, Shichun Yang, Xiaoyu Yane, Ziying Song

---

## 💡 一句话要点

**提出MindDrive框架，通过整合世界模型与视觉语言模型，实现端到端自动驾驶中的高质量轨迹生成与决策推理。**

**关键词**: `端到端自动驾驶` `轨迹生成` `决策推理` `世界模型` `视觉语言模型` `多目标评估`

## 📋 核心要点

1. 核心问题：端到端自动驾驶中，现有方法在轨迹生成与决策推理间存在割裂，难以兼顾高质量轨迹和全面评估。
2. 方法要点：基于世界动作模型进行未来感知轨迹生成，并利用视觉语言模型进行多目标评估，形成结构化推理范式。
3. 实验或效果：在NAVSIM基准测试中实现最优性能，显著提升安全性、合规性和泛化能力。

## 📄 摘要（原文）

> End-to-End autonomous driving (E2E-AD) has emerged as a new paradigm, where trajectory planning plays a crucial role. Existing studies mainly follow two directions: trajectory generation oriented, which focuses on producing high-quality trajectories with simple decision mechanisms, and trajectory selection oriented, which performs multi-dimensional evaluation to select the best trajectory yet lacks sufficient generative capability. In this work, we propose MindDrive, a harmonized framework that integrates high-quality trajectory generation with comprehensive decision reasoning. It establishes a structured reasoning paradigm of "context simulation - candidate generation - multi-objective trade-off". In particular, the proposed Future-aware Trajectory Generator (FaTG), based on a World Action Model (WaM), performs ego-conditioned "what-if" simulations to predict potential future scenes and generate foresighted trajectory candidates. Building upon this, the VLM-oriented Evaluator (VLoE) leverages the reasoning capability of a large vision-language model to conduct multi-objective evaluations across safety, comfort, and efficiency dimensions, leading to reasoned and human-aligned decision making. Extensive experiments on the NAVSIM-v1 and NAVSIM-v2 benchmarks demonstrate that MindDrive achieves state-of-the-art performance across multi-dimensional driving metrics, significantly enhancing safety, compliance, and generalization. This work provides a promising path toward interpretable and cognitively guided autonomous driving.

