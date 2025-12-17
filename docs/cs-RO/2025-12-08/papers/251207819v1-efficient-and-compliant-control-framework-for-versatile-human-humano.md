---
layout: default
title: Efficient and Compliant Control Framework for Versatile Human-Humanoid Collaborative Transportation
---

# Efficient and Compliant Control Framework for Versatile Human-Humanoid Collaborative Transportation

**arXiv**: [2512.07819v1](https://arxiv.org/abs/2512.07819) | [PDF](https://arxiv.org/pdf/2512.07819.pdf)

**作者**: Shubham S. Kumbhar, Abhijeet M. Kulkarni, Panagiotis Artemiadis

---

## 💡 一句话要点

**提出高效合规控制框架，实现人形机器人与人类协作搬运任务**

**关键词**: `人形机器人控制` `协作搬运` `动态规划` `全身控制` `刚度调制` `人机交互`

## 📋 核心要点

1. 核心问题：人形机器人需在协作搬运中支持平移和旋转运动，确保动态可行性和合规性。
2. 方法要点：结合I-LIP规划器、QP全身控制器和刚度调制，生成并执行动态可行的步态计划。
3. 实验或效果：在Digit人形平台上验证，提出效率指标量化协作质量，展示平移、转向等行为。

## 📄 摘要（原文）

> We present a control framework that enables humanoid robots to perform collaborative transportation tasks with a human partner. The framework supports both translational and rotational motions, which are fundamental to co-transport scenarios. It comprises three components: a high-level planner, a low-level controller, and a stiffness modulation mechanism. At the planning level, we introduce the Interaction Linear Inverted Pendulum (I-LIP), which, combined with an admittance model and an MPC formulation, generates dynamically feasible footstep plans. These are executed by a QP-based whole-body controller that accounts for the coupled humanoid-object dynamics. Stiffness modulation regulates robot-object interaction, ensuring convergence to the desired relative configuration defined by the distance between the object and the robot's center of mass. We validate the effectiveness of the framework through real-world experiments conducted on the Digit humanoid platform. To quantify collaboration quality, we propose an efficiency metric that captures both task performance and inter-agent coordination. We show that this metric highlights the role of compliance in collaborative tasks and offers insights into desirable trajectory characteristics across both high- and low-level control layers. Finally, we showcase experimental results on collaborative behaviors, including translation, turning, and combined motions such as semi circular trajectories, representative of naturally occurring co-transportation tasks.

