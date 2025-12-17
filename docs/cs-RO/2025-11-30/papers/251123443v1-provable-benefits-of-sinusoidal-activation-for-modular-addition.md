---
layout: default
title: Provable Benefits of Sinusoidal Activation for Modular Addition
---

# Provable Benefits of Sinusoidal Activation for Modular Addition

**arXiv**: [2511.23443v1](https://arxiv.org/abs/2511.23443) | [PDF](https://arxiv.org/pdf/2511.23443.pdf)

**作者**: Tianlong Huang, Zhiyuan Li

---

## 💡 一句话要点

**证明正弦激活在模加法学习中的优势，包括表达能力和泛化性能**

**关键词**: `激活函数` `模加法学习` `神经网络表达能力` `泛化理论` `正弦网络` `两层神经网络`

## 📋 核心要点

1. 研究两层神经网络中激活函数对模加法学习的影响，揭示正弦与ReLU的表达能力差异
2. 提出正弦网络的Natarajan维泛化界，获得接近最优的样本复杂度，并推导过参数化下的宽度无关泛化
3. 实验验证正弦网络在泛化和长度外推上优于ReLU网络，支持理论结果

## 📄 摘要（原文）

> This paper studies the role of activation functions in learning modular addition with two-layer neural networks. We first establish a sharp expressivity gap: sine MLPs admit width-$2$ exact realizations for any fixed length $m$ and, with bias, width-$2$ exact realizations uniformly over all lengths. In contrast, the width of ReLU networks must scale linearly with $m$ to interpolate, and they cannot simultaneously fit two lengths with different residues modulo $p$. We then provide a novel Natarajan-dimension generalization bound for sine networks, yielding nearly optimal sample complexity $\widetilde{\mathcal{O}}(p)$ for ERM over constant-width sine networks. We also derive width-independent, margin-based generalization for sine networks in the overparametrized regime and validate it. Empirically, sine networks generalize consistently better than ReLU networks across regimes and exhibit strong length extrapolation.

