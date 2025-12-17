---
layout: default
title: Think, Remember, Navigate: Zero-Shot Object-Goal Navigation with VLM-Powered Reasoning
---

# Think, Remember, Navigate: Zero-Shot Object-Goal Navigation with VLM-Powered Reasoning

**arXiv**: [2511.08942v1](https://arxiv.org/abs/2511.08942) | [PDF](https://arxiv.org/pdf/2511.08942.pdf)

**作者**: Mobin Habibpour, Fatemeh Afghah

---

## 💡 一句话要点

**提出VLM驱动推理框架以提升零样本目标导航效率**

**关键词**: `零样本目标导航` `视觉语言模型` `推理规划` `空间感知增强` `机器人导航`

## 📋 核心要点

1. 现有方法未充分利用VLM推理能力，导致导航效率低下
2. 采用结构化思维链提示、动态动作历史和障碍地图解释增强VLM规划
3. 在HM3D等基准测试中，轨迹更直接高效，优于现有方法

## 📄 摘要（原文）

> While Vision-Language Models (VLMs) are set to transform robotic navigation, existing methods often underutilize their reasoning capabilities. To unlock the full potential of VLMs in robotics, we shift their role from passive observers to active strategists in the navigation process. Our framework outsources high-level planning to a VLM, which leverages its contextual understanding to guide a frontier-based exploration agent. This intelligent guidance is achieved through a trio of techniques: structured chain-of-thought prompting that elicits logical, step-by-step reasoning; dynamic inclusion of the agent's recent action history to prevent getting stuck in loops; and a novel capability that enables the VLM to interpret top-down obstacle maps alongside first-person views, thereby enhancing spatial awareness. When tested on challenging benchmarks like HM3D, Gibson, and MP3D, this method produces exceptionally direct and logical trajectories, marking a substantial improvement in navigation efficiency over existing approaches and charting a path toward more capable embodied agents.

