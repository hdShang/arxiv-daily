---
layout: default
title: LUCID: Learning-Enabled Uncertainty-Aware Certification of Stochastic Dynamical Systems
---

# LUCID: Learning-Enabled Uncertainty-Aware Certification of Stochastic Dynamical Systems

**arXiv**: [2512.11750v1](https://arxiv.org/abs/2512.11750) | [PDF](https://arxiv.org/pdf/2512.11750.pdf)

**作者**: Ernesto Casablanca, Oliver Schön, Paolo Zuliani, Sadegh Soudjani

---

## 💡 一句话要点

**提出LUCID以解决黑盒随机动态系统的安全验证问题**

**关键词**: `随机动态系统` `安全验证` `控制屏障证书` `RKHS嵌入` `傅里叶核展开` `线性规划`

## 📋 核心要点

1. 核心问题：传统形式化验证工具难以处理嵌入不透明AI组件和复杂随机动态的系统
2. 方法要点：基于数据驱动学习控制屏障证书，利用RKHS嵌入和傅里叶核展开将非凸优化转化为线性规划
3. 实验或效果：在挑战性基准测试中展示其提供形式化安全保证的能力

## 📄 摘要（原文）

> Ensuring the safety of AI-enabled systems, particularly in high-stakes domains such as autonomous driving and healthcare, has become increasingly critical. Traditional formal verification tools fall short when faced with systems that embed both opaque, black-box AI components and complex stochastic dynamics. To address these challenges, we introduce LUCID (Learning-enabled Uncertainty-aware Certification of stochastIc Dynamical systems), a verification engine for certifying safety of black-box stochastic dynamical systems from a finite dataset of random state transitions. As such, LUCID is the first known tool capable of establishing quantified safety guarantees for such systems. Thanks to its modular architecture and extensive documentation, LUCID is designed for easy extensibility. LUCID employs a data-driven methodology rooted in control barrier certificates, which are learned directly from system transition data, to ensure formal safety guarantees. We use conditional mean embeddings to embed data into a reproducing kernel Hilbert space (RKHS), where an RKHS ambiguity set is constructed that can be inflated to robustify the result to out-of-distribution behavior. A key innovation within LUCID is its use of a finite Fourier kernel expansion to reformulate a semi-infinite non-convex optimization problem into a tractable linear program. The resulting spectral barrier allows us to leverage the fast Fourier transform to generate the relaxed problem efficiently, offering a scalable yet distributionally robust framework for verifying safety. LUCID thus offers a robust and efficient verification framework, able to handle the complexities of modern black-box systems while providing formal guarantees of safety. These unique capabilities are demonstrated on challenging benchmarks.

