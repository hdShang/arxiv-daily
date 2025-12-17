---
layout: default
title: ParaGate: Parasitic-Driven Domain Adaptation Transfer Learning for Netlist Performance Prediction
---

# ParaGate: Parasitic-Driven Domain Adaptation Transfer Learning for Netlist Performance Prediction

**arXiv**: [2511.23340v1](https://arxiv.org/abs/2511.23340) | [PDF](https://arxiv.org/pdf/2511.23340.pdf)

**作者**: Bin Sun, Jingyi Zhou, Jianan Mu, Zhiteng Chao, Tianmeng Yang, Ziyue Xu, Jing Ye, Huawei Li

---

## 💡 一句话要点

**提出ParaGate框架，通过寄生参数驱动的域适应迁移学习，从网表预测布局级性能以指导早期优化。**

**关键词**: `电子设计自动化` `迁移学习` `性能预测` `寄生参数` `时序分析` `全局优化`

## 📋 核心要点

1. 传统EDA流程中，布局级性能指标仅在布局布线后获得，阻碍早期全局优化。
2. ParaGate采用三步框架：预测寄生参数、依赖EDA工具进行时序分析、基于子图特征全局校准。
3. 实验显示，ParaGate在少量微调数据下实现强泛化，如到达时间R2从0.119提升至0.897。

## 📄 摘要（原文）

> In traditional EDA flows, layout-level performance metrics are only obtainable after placement and routing, hindering global optimization at earlier stages. Although some neural-network-based solutions predict layout-level performance directly from netlists, they often face generalization challenges due to the black-box heuristics of commercial placement-and-routing tools, which create disparate data across designs. To this end, we propose ParaGate, a three-step cross-stage prediction framework that infers layout-level timing and power from netlists. First, we propose a two-phase transfer-learning approach to predict parasitic parameters, pre-training on mid-scale circuits and fine-tuning on larger ones to capture extreme conditions. Next, we rely on EDA tools for timing analysis, offloading the long-path numerical reasoning. Finally, ParaGate performs global calibration using subgraph features. Experiments show that ParaGate achieves strong generalization with minimal fine-tuning data: on openE906, its arrival-time R2 from 0.119 to 0.897. These results demonstrate that ParaGate could provide guidance for global optimization in the synthesis and placement stages.

