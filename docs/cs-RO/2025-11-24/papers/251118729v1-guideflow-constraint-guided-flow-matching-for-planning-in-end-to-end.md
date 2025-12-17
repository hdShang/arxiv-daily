---
layout: default
title: GuideFlow: Constraint-Guided Flow Matching for Planning in End-to-End Autonomous Driving
---

# GuideFlow: Constraint-Guided Flow Matching for Planning in End-to-End Autonomous Driving

**arXiv**: [2511.18729v1](https://arxiv.org/abs/2511.18729) | [PDF](https://arxiv.org/pdf/2511.18729.pdf)

**作者**: Lin Liu, Caiyan Jia, Guanyi Yu, Ziying Song, JunQiao Li, Feiyang Jia, Peiliang Wu, Xiaoshuai Hao, Yandan Luo

---

## 💡 一句话要点

**提出GuideFlow框架，通过约束引导流匹配解决端到端自动驾驶规划中的多模态轨迹生成问题**

**关键词**: `自动驾驶规划` `流匹配` `约束引导生成` `多模态轨迹` `端到端学习`

## 📋 核心要点

1. 核心问题：模仿式端到端规划器易出现多模态轨迹模式坍塌，生成式规划器难以直接整合安全与物理约束
2. 方法要点：在流匹配生成过程中直接施加显式约束，结合能量模型增强自主优化能力
3. 实验或效果：在多个驾驶基准测试中验证有效性，NavSim测试中达到SOTA性能

## 📄 摘要（原文）

> Driving planning is a critical component of end-to-end (E2E) autonomous driving. However, prevailing Imitative E2E Planners often suffer from multimodal trajectory mode collapse, failing to produce diverse trajectory proposals. Meanwhile, Generative E2E Planners struggle to incorporate crucial safety and physical constraints directly into the generative process, necessitating an additional optimization stage to refine their outputs. In this paper, we propose \textit{\textbf{GuideFlow}}, a novel planning framework that leverages Constrained Flow Matching. Concretely, \textit{\textbf{GuideFlow}} explicitly models the flow matching process, which inherently mitigates mode collapse and allows for flexible guidance from various conditioning signals. Our core contribution lies in directly enforcing explicit constraints within the flow matching generation process, rather than relying on implicit constraint encoding. Crucially, \textit{\textbf{GuideFlow}} unifies the training of the flow matching with the Energy-Based Model (EBM) to enhance the model's autonomous optimization capability to robustly satisfy physical constraints. Secondly, \textit{\textbf{GuideFlow}} parameterizes driving aggressiveness as a control signal during generation, enabling precise manipulation of trajectory style. Extensive evaluations on major driving benchmarks (Bench2Drive, NuScenes, NavSim and ADV-NuScenes) validate the effectiveness of \textit{\textbf{GuideFlow}}. Notably, on the NavSim test hard split (Navhard), \textit{\textbf{GuideFlow}} achieved SOTA with an EPDMS score of 43.0. The code will be released.

