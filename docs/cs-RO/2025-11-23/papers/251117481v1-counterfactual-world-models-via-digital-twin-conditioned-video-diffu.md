---
layout: default
title: Counterfactual World Models via Digital Twin-conditioned Video Diffusion
---

# Counterfactual World Models via Digital Twin-conditioned Video Diffusion

**arXiv**: [2511.17481v1](https://arxiv.org/abs/2511.17481) | [PDF](https://arxiv.org/pdf/2511.17481.pdf)

**作者**: Yiqing Shen, Aiza Maksutova, Chenjia Li, Mathias Unberath

---

## 💡 一句话要点

**提出CWMDT框架，通过数字孪生和视频扩散模型实现反事实世界建模**

**关键词**: `反事实世界模型` `数字孪生` `视频扩散模型` `大语言模型` `场景干预` `视频生成`

## 📋 核心要点

1. 核心问题：传统世界模型无法处理反事实查询，如对象移除等假设性干预。
2. 方法要点：构建数字孪生编码场景结构，利用大语言模型推理干预传播，并条件视频扩散生成序列。
3. 实验或效果：在两个基准测试中达到最先进性能，验证数字孪生作为控制信号的有效性。

## 📄 摘要（原文）

> World models learn to predict the temporal evolution of visual observations given a control signal, potentially enabling agents to reason about environments through forward simulation. Because of the focus on forward simulation, current world models generate predictions based on factual observations. For many emerging applications, such as comprehensive evaluations of physical AI behavior under varying conditions, the ability of world models to answer counterfactual queries, such as "what would happen if this object was removed?", is of increasing importance. We formalize counterfactual world models that additionally take interventions as explicit inputs, predicting temporal sequences under hypothetical modifications to observed scene properties. Traditional world models operate directly on entangled pixel-space representations where object properties and relationships cannot be selectively modified. This modeling choice prevents targeted interventions on specific scene properties. We introduce CWMDT, a framework to overcome those limitations, turning standard video diffusion models into effective counterfactual world models. First, CWMDT constructs digital twins of observed scenes to explicitly encode objects and their relationships, represented as structured text. Second, CWMDT applies large language models to reason over these representations and predict how a counterfactual intervention propagates through time to alter the observed scene. Third, CWMDT conditions a video diffusion model with the modified representation to generate counterfactual visual sequences. Evaluations on two benchmarks show that the CWMDT approach achieves state-of-the-art performance, suggesting that alternative representations of videos, such as the digital twins considered here, offer powerful control signals for video forward simulation-based world models.

