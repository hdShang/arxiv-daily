---
layout: default
title: Noisy Quantum Learning Theory
---

# Noisy Quantum Learning Theory

**arXiv**: [2512.10929v1](https://arxiv.org/abs/2512.10929) | [PDF](https://arxiv.org/pdf/2512.10929.pdf)

**作者**: Jordan Cotler, Weiyuan Gong, Ishaan Kannan

---

## 💡 一句话要点

**提出噪声量子学习理论框架，分析噪声对量子学习优势的影响与恢复条件。**

**关键词**: `量子学习理论` `噪声量子计算` `复杂度类` `纯度测试` `影子层析` `噪声鲁棒性`

## 📋 核心要点

1. 核心问题：噪声如何影响量子设备的学习能力，特别是理想无噪声学习者的指数优势。
2. 方法要点：引入NBQP复杂度类，研究噪声下的oracle分离和具体学习任务如纯度测试。
3. 实验或效果：发现噪声可消除指数优势，但在特定结构下可恢复量子学习优势。

## 📄 摘要（原文）

> We develop a framework for learning from noisy quantum experiments, focusing on fault-tolerant devices accessing uncharacterized systems through noisy couplings. Our starting point is the complexity class $\textsf{NBQP}$ ("noisy BQP"), modeling noisy fault-tolerant quantum computers that cannot, in general, error-correct the oracle systems they query. Using this class, we show that for natural oracle problems, noise can eliminate exponential quantum learning advantages of ideal noiseless learners while preserving a superpolynomial gap between NISQ and fault-tolerant devices. Beyond oracle separations, we study concrete noisy learning tasks. For purity testing, the exponential two-copy advantage collapses under a single application of local depolarizing noise. Nevertheless, we identify a setting motivated by AdS/CFT in which noise-resilient structure restores a quantum learning advantage in a noisy regime. We then analyze noisy Pauli shadow tomography, deriving lower bounds that characterize how instance size, quantum memory, and noise control sample complexity, and design algorithms with parametrically similar scalings. Together, our results show that the Bell-basis and SWAP-test primitives underlying most exponential quantum learning advantages are fundamentally fragile to noise unless the experimental system has latent noise-robust structure. Thus, realizing meaningful quantum advantages in future experiments will require understanding how noise-robust physical properties interface with available algorithmic techniques.

