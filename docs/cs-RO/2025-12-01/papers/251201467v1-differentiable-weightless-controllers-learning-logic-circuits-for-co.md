---
layout: default
title: Differentiable Weightless Controllers: Learning Logic Circuits for Continuous Control
---

# Differentiable Weightless Controllers: Learning Logic Circuits for Continuous Control

**arXiv**: [2512.01467v1](https://arxiv.org/abs/2512.01467) | [PDF](https://arxiv.org/pdf/2512.01467.pdf)

**作者**: Fabian Kresse, Christoph H. Lampert

---

## 💡 一句话要点

**提出可微分无权重控制器，将连续控制策略表示为离散逻辑电路以降低延迟与能耗。**

**关键词**: `连续控制` `逻辑电路` `可微分架构` `FPGA部署` `稀疏连接` `能效优化`

## 📋 核心要点

1. 研究连续控制策略能否用离散逻辑电路替代连续神经网络表示与学习。
2. 引入可微分无权重控制器，通过温度计编码输入、稀疏布尔查找表层和轻量动作头实现端到端梯度训练。
3. 在MuJoCo基准测试中性能与基于权重的策略相当，并可直接编译为低延迟、低能耗的FPGA电路。

## 📄 摘要（原文）

> We investigate whether continuous-control policies can be represented and learned as discrete logic circuits instead of continuous neural networks. We introduce Differentiable Weightless Controllers (DWCs), a symbolic-differentiable architecture that maps real-valued observations to actions using thermometer-encoded inputs, sparsely connected boolean lookup-table layers, and lightweight action heads. DWCs can be trained end-to-end by gradient-based techniques, yet compile directly into FPGA-compatible circuits with few- or even single-clock-cycle latency and nanojoule-level energy cost per action. Across five MuJoCo benchmarks, including high-dimensional Humanoid, DWCs achieve returns competitive with weight-based policies (full precision or quantized neural networks), matching performance on four tasks and isolating network capacity as the key limiting factor on HalfCheetah. Furthermore, DWCs exhibit structurally sparse and interpretable connectivity patterns, enabling a direct inspection of which input thresholds influence control decisions.

