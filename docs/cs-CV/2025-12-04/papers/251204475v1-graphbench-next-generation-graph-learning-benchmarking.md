---
layout: default
title: GraphBench: Next-generation graph learning benchmarking
---

# GraphBench: Next-generation graph learning benchmarking

**arXiv**: [2512.04475v1](https://arxiv.org/abs/2512.04475) | [PDF](https://arxiv.org/pdf/2512.04475.pdf)

**作者**: Timo Stoll, Chendi Qian, Ben Finkelshtein, Ali Parviz, Darius Weber, Fabrizio Frasca, Hadar Shavit, Antoine Siraudin, Arman Mielke, Marie Anastacio, Erik Müller, Maya Bechler-Speicher, Michael Bronstein, Mikhail Galkin, Holger Hoos, Mathias Niepert, Bryan Perozzi, Jan Tönshoff, Christopher Morris

---

## 💡 一句话要点

**提出GraphBench以解决图学习基准测试碎片化问题，提供跨领域标准化评估**

**关键词**: `图学习基准测试` `标准化评估协议` `跨领域数据集` `消息传递神经网络` `图Transformer模型` `超参数调优框架`

## 📋 核心要点

1. 核心问题：图学习基准测试碎片化，数据集和评估协议不一致，阻碍可复现性和进展
2. 方法要点：GraphBench提供全面基准套件，覆盖节点、边、图和生成任务，包含标准化评估协议和超参数调优框架
3. 实验或效果：使用消息传递神经网络和图Transformer模型进行基准测试，建立参考性能基线

## 📄 摘要（原文）

> Machine learning on graphs has recently achieved impressive progress in various domains, including molecular property prediction and chip design. However, benchmarking practices remain fragmented, often relying on narrow, task-specific datasets and inconsistent evaluation protocols, which hampers reproducibility and broader progress. To address this, we introduce GraphBench, a comprehensive benchmarking suite that spans diverse domains and prediction tasks, including node-level, edge-level, graph-level, and generative settings. GraphBench provides standardized evaluation protocols -- with consistent dataset splits and performance metrics that account for out-of-distribution generalization -- as well as a unified hyperparameter tuning framework. Additionally, we benchmark GraphBench using message-passing neural networks and graph transformer models, providing principled baselines and establishing a reference performance. See www.graphbench.io for further details.

