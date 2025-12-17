---
layout: default
title: Abstract 3D Perception for Spatial Intelligence in Vision-Language Models
---

# Abstract 3D Perception for Spatial Intelligence in Vision-Language Models

**arXiv**: [2511.10946v1](https://arxiv.org/abs/2511.10946) | [PDF](https://arxiv.org/pdf/2511.10946.pdf)

**作者**: Yifan Liu, Fangneng Zhan, Kaichen Zhou, Yilun Du, Paul Pu Liang, Hanspeter Pfister

---

## 💡 一句话要点

**提出SandboxVLM框架以增强视觉语言模型的三维空间智能**

**关键词**: `三维感知` `视觉语言模型` `空间智能` `抽象边界框` `零样本学习` `模态鸿沟`

## 📋 核心要点

1. 核心问题：视觉语言模型在3D任务中存在模态鸿沟，导致从2D输入中检索3D信息效率低下
2. 方法要点：利用抽象边界框编码几何结构和物理运动，设计多阶段3D感知管道
3. 实验或效果：在零样本设置下，SAT Real基准上性能提升8.3%，无需额外训练

## 📄 摘要（原文）

> Vision-language models (VLMs) struggle with 3D-related tasks such as spatial cognition and physical understanding, which are crucial for real-world applications like robotics and embodied agents. We attribute this to a modality gap between the 3D tasks and the 2D training of VLM, which led to inefficient retrieval of 3D information from 2D input. To bridge this gap, we introduce SandboxVLM, a simple yet effective framework that leverages abstract bounding boxes to encode geometric structure and physical kinematics for VLM. Specifically, we design a 3D Sandbox reconstruction and perception pipeline comprising four stages: generating multi-view priors with abstract control, proxy elevation, multi-view voting and clustering, and 3D-aware reasoning. Evaluated in zero-shot settings across multiple benchmarks and VLM backbones, our approach consistently improves spatial intelligence, achieving an 8.3\% gain on SAT Real compared with baseline methods for instance. These results demonstrate that equipping VLMs with a 3D abstraction substantially enhances their 3D reasoning ability without additional training, suggesting new possibilities for general-purpose embodied intelligence.

