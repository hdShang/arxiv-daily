---
layout: default
title: Rethinking Expert Trajectory Utilization in LLM Post-training
---

# Rethinking Expert Trajectory Utilization in LLM Post-training

**arXiv**: [2512.11470v1](https://arxiv.org/abs/2512.11470) | [PDF](https://arxiv.org/pdf/2512.11470.pdf)

**作者**: Bowen Ding, Yuhan Chen, Jiayang Lv, Jiyao Yuan, Qi Zhu, Shuangshuang Tian, Dantong Zhu, Futing Wang, Heyuan Deng, Fei Mi, Lifeng Shang, Tao Lin

---

## 💡 一句话要点

**提出塑性-上限框架以优化大语言模型后训练中专家轨迹的利用**

**关键词**: `大语言模型后训练` `专家轨迹利用` `塑性-上限框架` `SFT-then-RL` `缩放指南` `性能优化`

## 📋 核心要点

1. 核心问题：专家轨迹在后训练中的最佳利用机制未解决，影响SFT与RL的整合效果。
2. 方法要点：通过塑性-上限框架理论分析，分解性能为基础SFT表现与后续RL塑性。
3. 实验或效果：基准测试确立顺序SFT-then-RL为优标准，提供数据规模和轨迹难度的缩放指南。

## 📄 摘要（原文）

> While effective post-training integrates Supervised Fine-Tuning (SFT) and Reinforcement Learning (RL), the optimal mechanism for utilizing expert trajectories remains unresolved. We propose the Plasticity-Ceiling Framework to theoretically ground this landscape, decomposing performance into foundational SFT performance and the subsequent RL plasticity. Through extensive benchmarking, we establish the Sequential SFT-then-RL pipeline as the superior standard, overcoming the stability deficits of synchronized approaches. Furthermore, we derive precise scaling guidelines: (1) Transitioning to RL at the SFT Stable or Mild Overfitting Sub-phase maximizes the final ceiling by securing foundational SFT performance without compromising RL plasticity; (2) Refuting ``Less is More'' in the context of SFT-then-RL scaling, we demonstrate that Data Scale determines the primary post-training potential, while Trajectory Difficulty acts as a performance multiplier; and (3) Identifying that the Minimum SFT Validation Loss serves as a robust indicator for selecting the expert trajectories that maximize the final performance ceiling. Our findings provide actionable guidelines for maximizing the value extracted from expert trajectories.

