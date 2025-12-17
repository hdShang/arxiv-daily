---
layout: default
title: DAPO: Design Structure-Aware Pass Ordering in High-Level Synthesis with Graph Contrastive and Reinforcement Learning
---

# DAPO: Design Structure-Aware Pass Ordering in High-Level Synthesis with Graph Contrastive and Reinforcement Learning

**arXiv**: [2512.11342v1](https://arxiv.org/abs/2512.11342) | [PDF](https://arxiv.org/pdf/2512.11342.pdf)

**作者**: Jinming Ge, Linfeng Du, Likith Anaparty, Shangkun Li, Tingyuan Liang, Afzal Ahmad, Vivek Chaturvedi, Sharad Sinha, Zhiyao Xie, Jiang Xu, Wei Zhang

---

## 💡 一句话要点

**提出DAPO框架，通过图对比和强化学习实现设计结构感知的HLS优化策略定制。**

**关键词**: `高层次综合` `图对比学习` `强化学习` `硬件优化` `FPGA加速器`

## 📋 核心要点

1. 现有HLS工具依赖固定优化策略，缺乏针对特定设计的语义理解和硬件指标估计能力。
2. DAPO从控制流和数据流图提取语义，利用对比学习生成嵌入，结合分析模型指导强化学习代理。
3. 在经典HLS设计上评估，平均比Vitis HLS加速2.36倍。

## 📄 摘要（原文）

> High-Level Synthesis (HLS) tools are widely adopted in FPGA-based domain-specific accelerator design. However, existing tools rely on fixed optimization strategies inherited from software compilations, limiting their effectiveness. Tailoring optimization strategies to specific designs requires deep semantic understanding, accurate hardware metric estimation, and advanced search algorithms -- capabilities that current approaches lack.
>   We propose DAPO, a design structure-aware pass ordering framework that extracts program semantics from control and data flow graphs, employs contrastive learning to generate rich embeddings, and leverages an analytical model for accurate hardware metric estimation. These components jointly guide a reinforcement learning agent to discover design-specific optimization strategies. Evaluations on classic HLS designs demonstrate that our end-to-end flow delivers a 2.36 speedup over Vitis HLS on average.

