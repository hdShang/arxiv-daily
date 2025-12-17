---
layout: default
title: Tackling Snow-Induced Challenges: Safe Autonomous Lane-Keeping with Robust Reinforcement Learning
---

# Tackling Snow-Induced Challenges: Safe Autonomous Lane-Keeping with Robust Reinforcement Learning

**arXiv**: [2512.12987v1](https://arxiv.org/abs/2512.12987) | [PDF](https://arxiv.org/pdf/2512.12987.pdf)

**作者**: Amin Jalal Aghdasian, Farzaneh Abdollahi, Ali Kamali Iglie

---

## 💡 一句话要点

**提出两种动作鲁棒强化学习算法以解决自动驾驶车辆在雪天路况下的车道保持问题。**

**关键词**: `自动驾驶车道保持` `雪天路况鲁棒性` `深度强化学习` `动作鲁棒算法` `端到端决策` `注意力机制`

## 📋 核心要点

1. 核心问题：雪天路况导致车道线识别困难、车辆打滑，影响自动驾驶车道保持系统的安全性和稳定性。
2. 方法要点：开发AR-RDPG和AR-CADPG两种算法，前者结合去噪网络和预训练DCNN提取车道线，后者集成CNN和注意力机制实现端到端决策。
3. 实验或效果：在CARLA模拟器中训练和验证，并在基于Jetson Nano的真实车辆上测试，AR-CADPG在路径跟踪精度和鲁棒性上表现更优。

## 📄 摘要（原文）

> This paper proposes two new algorithms for the lane keeping system (LKS) in autonomous vehicles (AVs) operating under snowy road conditions. These algorithms use deep reinforcement learning (DRL) to handle uncertainties and slippage. They include Action-Robust Recurrent Deep Deterministic Policy Gradient (AR-RDPG) and end-to-end Action-Robust convolutional neural network Attention Deterministic Policy Gradient (AR-CADPG), two action-robust approaches for decision-making. In the AR-RDPG method, within the perception layer, camera images are first denoised using multi-scale neural networks. Then, the centerline coefficients are extracted by a pre-trained deep convolutional neural network (DCNN). These coefficients, concatenated with the driving characteristics, are used as input to the control layer. The AR-CADPG method presents an end-to-end approach in which a convolutional neural network (CNN) and an attention mechanism are integrated within a DRL framework. Both methods are first trained in the CARLA simulator and validated under various snowy scenarios. Real-world experiments on a Jetson Nano-based autonomous vehicle confirm the feasibility and stability of the learned policies. Among the two models, the AR-CADPG approach demonstrates superior path-tracking accuracy and robustness, highlighting the effectiveness of combining temporal memory, adversarial resilience, and attention mechanisms in AVs.

