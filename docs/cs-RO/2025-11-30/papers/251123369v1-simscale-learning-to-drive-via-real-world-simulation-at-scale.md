---
layout: default
title: SimScale: Learning to Drive via Real-World Simulation at Scale
---

# SimScale: Learning to Drive via Real-World Simulation at Scale

**arXiv**: [2511.23369v1](https://arxiv.org/abs/2511.23369) | [PDF](https://arxiv.org/pdf/2511.23369.pdf)

**作者**: Haochen Tian, Tianyu Li, Haochen Liu, Jiazhi Yang, Yihang Qiu, Guang Li, Junli Wang, Yinfeng Gao, Zhang Zhang, Liang Wang, Hangjun Ye, Tieniu Tan, Long Chen, Hongyang Li

---

## 💡 一句话要点

**提出SimScale框架，通过大规模真实世界模拟增强自动驾驶决策的鲁棒性和泛化能力。**

**关键词**: `自动驾驶模拟` `神经渲染` `伪专家轨迹` `协同训练` `数据增强` `规划方法`

## 📋 核心要点

1. 核心问题：真实驾驶数据缺乏多样性和安全关键场景，限制自动驾驶系统决策学习。
2. 方法要点：利用神经渲染和反应式环境生成高保真模拟数据，并设计伪专家轨迹提供动作监督。
3. 实验或效果：在真实基准测试中，通过协同训练显著提升规划方法性能，且仅增加模拟数据即可平滑扩展。

## 📄 摘要（原文）

> Achieving fully autonomous driving systems requires learning rational decisions in a wide span of scenarios, including safety-critical and out-of-distribution ones. However, such cases are underrepresented in real-world corpus collected by human experts. To complement for the lack of data diversity, we introduce a novel and scalable simulation framework capable of synthesizing massive unseen states upon existing driving logs. Our pipeline utilizes advanced neural rendering with a reactive environment to generate high-fidelity multi-view observations controlled by the perturbed ego trajectory. Furthermore, we develop a pseudo-expert trajectory generation mechanism for these newly simulated states to provide action supervision. Upon the synthesized data, we find that a simple co-training strategy on both real-world and simulated samples can lead to significant improvements in both robustness and generalization for various planning methods on challenging real-world benchmarks, up to +6.8 EPDMS on navhard and +2.9 on navtest. More importantly, such policy improvement scales smoothly by increasing simulation data only, even without extra real-world data streaming in. We further reveal several crucial findings of such a sim-real learning system, which we term SimScale, including the design of pseudo-experts and the scaling properties for different policy architectures. Our simulation data and code would be released.

