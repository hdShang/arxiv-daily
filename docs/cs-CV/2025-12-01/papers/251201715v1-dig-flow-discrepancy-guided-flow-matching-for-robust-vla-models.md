---
layout: default
title: DiG-Flow: Discrepancy-Guided Flow Matching for Robust VLA Models
---

# DiG-Flow: Discrepancy-Guided Flow Matching for Robust VLA Models

**arXiv**: [2512.01715v1](https://arxiv.org/abs/2512.01715) | [PDF](https://arxiv.org/pdf/2512.01715.pdf)

**作者**: Wanpeng Zhang, Ye Wang, Hao Luo, Haoqi Yuan, Yicheng Feng, Sipeng Zheng, Qin Jin, Zongqing Lu

---

## 💡 一句话要点

**提出DiG-Flow框架，通过几何正则化增强视觉-语言-动作模型的鲁棒性。**

**关键词**: `视觉-语言-动作模型` `流匹配` `几何正则化` `分布差异` `鲁棒性增强` `多步任务`

## 📋 核心要点

1. 核心问题：VLA模型在分布偏移和多步任务中性能下降，表示学习不鲁棒。
2. 方法要点：利用观测与动作嵌入的分布差异作为几何信号，通过单调函数调制权重并应用残差更新。
3. 实验或效果：理论保证训练目标下降和推理收敛，实验显示在复杂任务和有限数据下性能提升显著。

## 📄 摘要（原文）

> Vision-Language-Action (VLA) models trained with flow matching have demonstrated impressive capabilities on robotic manipulation tasks. However, their performance often degrades under distribution shift and on complex multi-step tasks, suggesting that the learned representations may not robustly capture task-relevant semantics. We introduce DiG-Flow, a principled framework that enhances VLA robustness through geometric regularization. Our key insight is that the distributional discrepancy between observation and action embeddings provides a meaningful geometric signal: lower transport cost indicates compatible representations, while higher cost suggests potential misalignment. DiG-Flow computes a discrepancy measure between empirical distributions of observation and action embeddings, maps it to a modulation weight via a monotone function, and applies residual updates to the observation embeddings before flow matching. Crucially, this intervention operates at the representation level without modifying the flow matching path or target vector field. We provide theoretical guarantees showing that discrepancy-guided training provably decreases the training objective, and that guided inference refinement converges with contraction. Empirically, DiG-Flow integrates into existing VLA architectures with negligible overhead and consistently improves performance, with particularly pronounced gains on complex multi-step tasks and under limited training data.

