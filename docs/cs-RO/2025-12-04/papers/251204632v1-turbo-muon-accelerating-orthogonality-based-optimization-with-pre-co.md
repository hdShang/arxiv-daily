---
layout: default
title: Turbo-Muon: Accelerating Orthogonality-Based Optimization with Pre-Conditioning
---

# Turbo-Muon: Accelerating Orthogonality-Based Optimization with Pre-Conditioning

**arXiv**: [2512.04632v1](https://arxiv.org/abs/2512.04632) | [PDF](https://arxiv.org/pdf/2512.04632.pdf)

**作者**: Thibaut Boissin, Thomas Massena, Franck Mamalet, Mathieu Serrurier

---

## 💡 一句话要点

**提出预条件化方法以加速基于正交性的优化器中的牛顿-舒尔茨近似收敛**

**关键词**: `正交性优化` `牛顿-舒尔茨近似` `预条件化` `训练加速` `计算效率` `深度学习优化`

## 📋 核心要点

1. 基于正交性的优化器如Muon依赖昂贵的梯度正交化步骤，牛顿-舒尔茨近似需数十次矩阵乘法
2. 引入预条件化程序加速牛顿-舒尔茨收敛，降低计算成本，开销可忽略
3. 实验显示牛顿-舒尔茨近似加速达2.8倍，端到端训练运行时提升5-10%，模型性能保持或提升

## 📄 摘要（原文）

> Orthogonality-based optimizers, such as Muon, have recently shown strong performance across large-scale training and community-driven efficiency challenges. However, these methods rely on a costly gradient orthogonalization step. Even efficient iterative approximations such as Newton-Schulz remain expensive, typically requiring dozens of matrix multiplications to converge. We introduce a preconditioning procedure that accelerates Newton-Schulz convergence and reduces its computational cost. We evaluate its impact and show that the overhead of our preconditioning can be made negligible. Furthermore, the faster convergence it enables allows us to remove one iteration out of the usual five without degrading approximation quality. Our publicly available implementation achieves up to a 2.8x speedup in the Newton-Schulz approximation. We also show that this has a direct impact on end-to-end training runtime with 5-10% improvement in realistic training scenarios across two efficiency-focused tasks. On challenging language or vision tasks, we validate that our method maintains equal or superior model performance while improving runtime. Crucially, these improvements require no hyperparameter tuning and can be adopted as a simple drop-in replacement. Our code is publicly available on github.

