---
layout: default
title: AD-R1: Closed-Loop Reinforcement Learning for End-to-End Autonomous Driving with Impartial World Models
---

# AD-R1: Closed-Loop Reinforcement Learning for End-to-End Autonomous Driving with Impartial World Models

**arXiv**: [2511.20325v1](https://arxiv.org/abs/2511.20325) | [PDF](https://arxiv.org/pdf/2511.20325.pdf)

**作者**: Tianyi Yan, Tao Tang, Xingtai Gui, Yongkang Li, Jiasen Zhesng, Weiyao Huang, Lingdong Kong, Wencheng Han, Xia Zhou, Xueyang Zhang, Yifei Zhan, Kun Zhan, Cheng-zhong Xu, Jianbing Shen

---

## 💡 一句话要点

**提出基于公正世界模型的闭环强化学习框架，以提升端到端自动驾驶的安全性**

**关键词**: `端到端自动驾驶` `强化学习` `世界模型` `反事实合成` `安全评估` `闭环控制`

## 📋 核心要点

1. 核心问题：强化学习在自动驾驶中因世界模型存在乐观偏见，难以处理长尾安全事件
2. 方法要点：使用反事实合成生成碰撞和越野事件数据，训练公正世界模型作为内部批评器
3. 实验或效果：在风险预见基准测试中显著提升失败预测能力，减少模拟中的安全违规

## 📄 摘要（原文）

> End-to-end models for autonomous driving hold the promise of learning complex behaviors directly from sensor data, but face critical challenges in safety and handling long-tail events. Reinforcement Learning (RL) offers a promising path to overcome these limitations, yet its success in autonomous driving has been elusive. We identify a fundamental flaw hindering this progress: a deep seated optimistic bias in the world models used for RL. To address this, we introduce a framework for post-training policy refinement built around an Impartial World Model. Our primary contribution is to teach this model to be honest about danger. We achieve this with a novel data synthesis pipeline, Counterfactual Synthesis, which systematically generates a rich curriculum of plausible collisions and off-road events. This transforms the model from a passive scene completer into a veridical forecaster that remains faithful to the causal link between actions and outcomes. We then integrate this Impartial World Model into our closed-loop RL framework, where it serves as an internal critic. During refinement, the agent queries the critic to ``dream" of the outcomes for candidate actions. We demonstrate through extensive experiments, including on a new Risk Foreseeing Benchmark, that our model significantly outperforms baselines in predicting failures. Consequently, when used as a critic, it enables a substantial reduction in safety violations in challenging simulations, proving that teaching a model to dream of danger is a critical step towards building truly safe and intelligent autonomous agents.

