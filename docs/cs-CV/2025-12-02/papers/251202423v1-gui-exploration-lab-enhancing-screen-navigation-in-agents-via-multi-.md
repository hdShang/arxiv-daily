---
layout: default
title: GUI Exploration Lab: Enhancing Screen Navigation in Agents via Multi-Turn Reinforcement Learning
---

# GUI Exploration Lab: Enhancing Screen Navigation in Agents via Multi-Turn Reinforcement Learning

**arXiv**: [2512.02423v1](https://arxiv.org/abs/2512.02423) | [PDF](https://arxiv.org/pdf/2512.02423.pdf)

**作者**: Haolong Yan, Yeqing Shen, Xin Huang, Jia Wang, Kaijun Tan, Zhixuan Liang, Hongxin Li, Zheng Ge, Osamu Yoshie, Si Li, Xiangyu Zhang, Daxin Jiang

---

## 💡 一句话要点

**提出GUI Exploration Lab模拟环境引擎，通过多轮强化学习增强GUI代理的屏幕导航能力**

**关键词**: `GUI代理导航` `模拟环境引擎` `多轮强化学习` `屏幕导航` `监督微调` `基准测试`

## 📋 核心要点

1. 核心问题：真实GUI环境复杂且专有，缺乏全面环境信息，阻碍代理导航能力的系统研究和基准测试
2. 方法要点：构建灵活可定义的模拟环境引擎，结合监督微调、单轮和多轮强化学习分阶段训练代理
3. 实验或效果：在静态和交互基准上验证方法，多轮强化学习通过探索策略提升导航性能，并推广到真实场景

## 📄 摘要（原文）

> With the rapid development of Large Vision Language Models, the focus of Graphical User Interface (GUI) agent tasks shifts from single-screen tasks to complex screen navigation challenges. However, real-world GUI environments, such as PC software and mobile Apps, are often complex and proprietary, making it difficult to obtain the comprehensive environment information needed for agent training and evaluation. This limitation hinders systematic investigation and benchmarking of agent navigation capabilities. To address this limitation, we introduce GUI Exploration Lab, a simulation environment engine for GUI agent navigation research that enables flexible definition and composition of screens, icons, and navigation graphs, while providing full access to environment information for comprehensive agent training and evaluation. Through extensive experiments, we find that supervised fine-tuning enables effective memorization of fundamental knowledge, serving as a crucial foundation for subsequent training. Building on this, single-turn reinforcement learning further enhances generalization to unseen scenarios. Finally, multi-turn reinforcement learning encourages the development of exploration strategies through interactive trial and error, leading to further improvements in screen navigation performance. We validate our methods on both static and interactive benchmarks, demonstrating that our findings generalize effectively to real-world scenarios. These findings demonstrate the advantages of reinforcement learning approaches in GUI navigation and offer practical guidance for building more capable and generalizable GUI agents.

