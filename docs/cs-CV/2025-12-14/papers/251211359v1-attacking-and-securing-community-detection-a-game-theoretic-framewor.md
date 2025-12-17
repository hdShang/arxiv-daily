---
layout: default
title: Attacking and Securing Community Detection: A Game-Theoretic Framework
---

# Attacking and Securing Community Detection: A Game-Theoretic Framework

**arXiv**: [2512.11359v1](https://arxiv.org/abs/2512.11359) | [PDF](https://arxiv.org/pdf/2512.11359.pdf)

**作者**: Yifan Niu, Aochuan Chen, Tingyang Xu, Jia Li

---

## 💡 一句话要点

**提出CD-GAME博弈框架，攻击与防御社区检测以保护隐私和增强鲁棒性。**

**关键词**: `社区检测` `对抗攻击` `博弈论` `隐私保护` `鲁棒性增强`

## 📋 核心要点

1. 扩展对抗图概念至社区检测，提出新攻击与防御技术。
2. 构建CD-GAME博弈框架模拟攻击者与防御者交互，动态更新策略至纳什均衡。
3. 实验显示方法显著优于基线，揭示交互场景中攻击策略的演变。

## 📄 摘要（原文）

> It has been demonstrated that adversarial graphs, i.e., graphs with imperceptible perturbations, can cause deep graph models to fail on classification tasks. In this work, we extend the concept of adversarial graphs to the community detection problem, which is more challenging. We propose novel attack and defense techniques for community detection problem, with the objective of hiding targeted individuals from detection models and enhancing the robustness of community detection models, respectively. These techniques have many applications in real-world scenarios, for example, protecting personal privacy in social networks and understanding camouflage patterns in transaction networks. To simulate interactive attack and defense behaviors, we further propose a game-theoretic framework, called CD-GAME. One player is a graph attacker, while the other player is a Rayleigh Quotient defender. The CD-GAME models the mutual influence and feedback mechanisms between the attacker and the defender, revealing the dynamic evolutionary process of the game. Both players dynamically update their strategies until they reach the Nash equilibrium. Extensive experiments demonstrate the effectiveness of our proposed attack and defense methods, and both outperform existing baselines by a significant margin. Furthermore, CD-GAME provides valuable insights for understanding interactive attack and defense scenarios in community detection problems. We found that in traditional single-step attack or defense, attacker tends to employ strategies that are most effective, but are easily detected and countered by defender. When the interactive game reaches a Nash equilibrium, attacker adopts more imperceptible strategies that can still achieve satisfactory attack effectiveness even after defense.

