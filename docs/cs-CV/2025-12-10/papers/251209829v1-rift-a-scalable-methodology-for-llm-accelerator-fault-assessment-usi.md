---
layout: default
title: RIFT: A Scalable Methodology for LLM Accelerator Fault Assessment using Reinforcement Learning
---

# RIFT: A Scalable Methodology for LLM Accelerator Fault Assessment using Reinforcement Learning

**arXiv**: [2512.09829v1](https://arxiv.org/abs/2512.09829) | [PDF](https://arxiv.org/pdf/2512.09829.pdf)

**作者**: Khurram Khalil, Muhammad Mahad Khaliq, Khaza Anuarul Hoque

---

## 💡 一句话要点

**提出RIFT框架，利用强化学习自动化发现最小高影响故障场景，以解决AI加速器故障评估的可扩展性问题。**

**关键词**: `AI加速器故障评估` `强化学习引导` `最小高影响测试` `混合敏感度分析` `可扩展框架` `硬件保护策略`

## 📋 核心要点

1. 核心问题：现代AI加速器规模巨大，传统故障评估方法计算成本高且关键故障模式覆盖差。
2. 方法要点：将最坏故障搜索转化为序列决策问题，结合混合敏感度分析和强化学习生成最小高影响测试套件。
3. 实验或效果：在十亿参数LLM工作负载上，RIFT比进化方法快2.2倍，测试向量量比随机注入减少99%以上，故障覆盖更优。

## 📄 摘要（原文）

> The massive scale of modern AI accelerators presents critical challenges to traditional fault assessment methodologies, which face prohibitive computational costs and provide poor coverage of critical failure modes. This paper introduces RIFT (Reinforcement Learning-guided Intelligent Fault Targeting), a scalable framework that automates the discovery of minimal, high-impact fault scenarios for efficient design-time fault assessment. RIFT transforms the complex search for worst-case faults into a sequential decision-making problem, combining hybrid sensitivity analysis for search space pruning with reinforcement learning to intelligently generate minimal, high-impact test suites. Evaluated on billion-parameter Large Language Model (LLM) workloads using NVIDIA A100 GPUs, RIFT achieves a \textbf{2.2$\times$} fault assessment speedup over evolutionary methods and reduces the required test vector volume by over \textbf{99\%} compared to random fault injection, all while achieving \textbf{superior fault coverage}. The proposed framework also provides actionable data to enable intelligent hardware protection strategies, demonstrating that RIFT-guided selective error correction code provides a \textbf{12.8$\times$} improvement in \textbf{cost-effectiveness} (coverage per unit area) compared to uniform triple modular redundancy protection. RIFT automatically generates UVM-compliant verification artifacts, ensuring its findings are directly actionable and integrable into commercial RTL verification workflows.

