---
layout: default
title: Optimal Perturbation Budget Allocation for Data Poisoning in Offline Reinforcement Learning
---

# Optimal Perturbation Budget Allocation for Data Poisoning in Offline Reinforcement Learning

**arXiv**: [2512.08485v1](https://arxiv.org/abs/2512.08485) | [PDF](https://arxiv.org/pdf/2512.08485.pdf)

**作者**: Junnan Qiu, Jie Li

---

## 💡 一句话要点

**提出全局预算分配攻击策略，以优化离线强化学习中的数据投毒扰动分配**

**关键词**: `离线强化学习` `数据投毒攻击` `全局预算分配` `TD误差` `扰动优化` `防御规避`

## 📋 核心要点

1. 离线强化学习易受数据投毒攻击，现有方法采用均匀扰动效率低且隐蔽性差
2. 基于TD误差影响理论，将攻击建模为全局资源分配问题，推导出闭式解分配扰动幅度
3. 在D4RL基准测试中，以最小扰动实现高达80%性能下降，并规避先进防御检测

## 📄 摘要（原文）

> Offline Reinforcement Learning (RL) enables policy optimization from static datasets but is inherently vulnerable to data poisoning attacks. Existing attack strategies typically rely on locally uniform perturbations, which treat all samples indiscriminately. This approach is inefficient, as it wastes the perturbation budget on low-impact samples, and lacks stealthiness due to significant statistical deviations. In this paper, we propose a novel Global Budget Allocation attack strategy. Leveraging the theoretical insight that a sample's influence on value function convergence is proportional to its Temporal Difference (TD) error, we formulate the attack as a global resource allocation problem. We derive a closed-form solution where perturbation magnitudes are assigned proportional to the TD-error sensitivity under a global L2 constraint. Empirical results on D4RL benchmarks demonstrate that our method significantly outperforms baseline strategies, achieving up to 80% performance degradation with minimal perturbations that evade detection by state-of-the-art statistical and spectral defenses.

