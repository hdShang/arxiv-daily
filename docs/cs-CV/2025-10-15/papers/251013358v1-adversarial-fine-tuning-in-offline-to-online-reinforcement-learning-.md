---
layout: default
title: Adversarial Fine-tuning in Offline-to-Online Reinforcement Learning for Robust Robot Control
---

# Adversarial Fine-tuning in Offline-to-Online Reinforcement Learning for Robust Robot Control

**arXiv**: [2510.13358v1](https://arxiv.org/abs/2510.13358) | [PDF](https://arxiv.org/pdf/2510.13358.pdf)

**作者**: Shingo Ayabe, Hiroshi Kera, Kazuhiko Kawamoto

---

## 💡 一句话要点

**提出对抗性微调框架以增强离线强化学习在机器人控制中的鲁棒性**

**关键词**: `离线强化学习` `对抗性微调` `机器人控制` `鲁棒性增强` `自适应课程`

## 📋 核心要点

1. 离线强化学习策略在动作空间扰动下脆弱，影响机器人控制稳定性
2. 采用离线训练后在线对抗微调，注入扰动诱导补偿行为提升韧性
3. 实验显示方法优于离线基线，收敛更快，自适应课程策略保持性能

## 📄 摘要（原文）

> Offline reinforcement learning enables sample-efficient policy acquisition
> without risky online interaction, yet policies trained on static datasets
> remain brittle under action-space perturbations such as actuator faults. This
> study introduces an offline-to-online framework that trains policies on clean
> data and then performs adversarial fine-tuning, where perturbations are
> injected into executed actions to induce compensatory behavior and improve
> resilience. A performance-aware curriculum further adjusts the perturbation
> probability during training via an exponential-moving-average signal, balancing
> robustness and stability throughout the learning process. Experiments on
> continuous-control locomotion tasks demonstrate that the proposed method
> consistently improves robustness over offline-only baselines and converges
> faster than training from scratch. Matching the fine-tuning and evaluation
> conditions yields the strongest robustness to action-space perturbations, while
> the adaptive curriculum strategy mitigates the degradation of nominal
> performance observed with the linear curriculum strategy. Overall, the results
> show that adversarial fine-tuning enables adaptive and robust control under
> uncertain environments, bridging the gap between offline efficiency and online
> adaptability.

