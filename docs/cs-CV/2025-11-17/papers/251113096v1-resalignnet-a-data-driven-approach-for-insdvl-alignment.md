---
layout: default
title: ResAlignNet: A Data-Driven Approach for INS/DVL Alignment
---

# ResAlignNet: A Data-Driven Approach for INS/DVL Alignment

**arXiv**: [2511.13096v1](https://arxiv.org/abs/2511.13096) | [PDF](https://arxiv.org/pdf/2511.13096.pdf)

**作者**: Guy Damari, Itzik Klein

---

## 💡 一句话要点

**提出ResAlignNet数据驱动方法以解决水下自主航行器INS/DVL传感器对齐问题**

**关键词**: `传感器对齐` `数据驱动方法` `水下导航` `Sim2Real迁移` `神经网络优化`

## 📋 核心要点

1. 标准模型对齐方法收敛慢、依赖特定运动模式，限制操作灵活性
2. 使用1D ResNet-18架构，将对齐问题转化为神经网络优化，无需外部辅助
3. 实验显示25秒数据实现0.8°精度，收敛时间减少65%，支持Sim2Real迁移

## 📄 摘要（原文）

> Autonomous underwater vehicles rely on precise navigation systems that combine the inertial navigation system and the Doppler velocity log for successful missions in challenging environments where satellite navigation is unavailable. The effectiveness of this integration critically depends on accurate alignment between the sensor reference frames. Standard model-based alignment methods between these sensor systems suffer from lengthy convergence times, dependence on prescribed motion patterns, and reliance on external aiding sensors, significantly limiting operational flexibility. To address these limitations, this paper presents ResAlignNet, a data-driven approach using the 1D ResNet-18 architecture that transforms the alignment problem into deep neural network optimization, operating as an in-situ solution that requires only sensors on board without external positioning aids or complex vehicle maneuvers, while achieving rapid convergence in seconds. Additionally, the approach demonstrates the learning capabilities of Sim2Real transfer, enabling training in synthetic data while deploying in operational sensor measurements. Experimental validation using the Snapir autonomous underwater vehicle demonstrates that ResAlignNet achieves alignment accuracy within 0.8° using only 25 seconds of data collection, representing a 65\% reduction in convergence time compared to standard velocity-based methods. The trajectory-independent solution eliminates motion pattern requirements and enables immediate vehicle deployment without lengthy pre-mission procedures, advancing underwater navigation capabilities through robust sensor-agnostic alignment that scales across different operational scenarios and sensor specifications.

