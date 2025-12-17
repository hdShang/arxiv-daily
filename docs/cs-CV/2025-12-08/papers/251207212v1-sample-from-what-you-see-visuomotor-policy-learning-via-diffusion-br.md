---
layout: default
title: Sample from What You See: Visuomotor Policy Learning via Diffusion Bridge with Observation-Embedded Stochastic Differential Equation
---

# Sample from What You See: Visuomotor Policy Learning via Diffusion Bridge with Observation-Embedded Stochastic Differential Equation

**arXiv**: [2512.07212v1](https://arxiv.org/abs/2512.07212) | [PDF](https://arxiv.org/pdf/2512.07212.pdf)

**作者**: Zhaoyang Liu, Mokai Pan, Zhongyi Wang, Kaizhen Zhu, Haotao Lu, Jingya Wang, Ye Shi

---

## 💡 一句话要点

**提出BridgePolicy，通过扩散桥嵌入观测的随机微分方程，以提升机器人视觉运动策略的精确性和可靠性。**

**关键词**: `扩散模型模仿学习` `视觉运动策略` `随机微分方程` `多模态融合` `机器人控制`

## 📋 核心要点

1. 现有扩散模型模仿学习将观测作为去噪网络的高层条件输入，而非融入扩散过程的随机动态，导致采样从随机高斯噪声开始，感知与控制耦合弱。
2. BridgePolicy通过扩散桥公式将观测嵌入随机微分方程，构建观测信息轨迹，使采样从丰富先验开始，改善控制性能。
3. 在52个模拟任务和5个真实世界任务中，BridgePolicy优于现有生成策略，未知具体基准名称。

## 📄 摘要（原文）

> Imitation learning with diffusion models has advanced robotic control by capturing multi-modal action distributions. However, existing approaches typically treat observations as high-level conditioning inputs to the denoising network, rather than integrating them into the stochastic dynamics of the diffusion process itself. As a result, sampling must begin from random Gaussian noise, weakening the coupling between perception and control and often yielding suboptimal performance. We introduce BridgePolicy, a generative visuomotor policy that explicitly embeds observations within the stochastic differential equation via a diffusion-bridge formulation. By constructing an observation-informed trajectory, BridgePolicy enables sampling to start from a rich, informative prior rather than random noise, substantially improving precision and reliability in control. A key challenge is that classical diffusion bridges connect distributions with matched dimensionality, whereas robotic observations are heterogeneous and multi-modal and do not naturally align with the action space. To address this, we design a multi-modal fusion module and a semantic aligner that unify visual and state inputs and align observation and action representations, making the bridge applicable to heterogeneous robot data. Extensive experiments across 52 simulation tasks on three benchmarks and five real-world tasks demonstrate that BridgePolicy consistently outperforms state-of-the-art generative policies.

