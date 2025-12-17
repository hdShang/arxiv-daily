---
layout: default
title: Differentially Private and Federated Structure Learning in Bayesian Networks
---

# Differentially Private and Federated Structure Learning in Bayesian Networks

**arXiv**: [2512.01708v1](https://arxiv.org/abs/2512.01708) | [PDF](https://arxiv.org/pdf/2512.01708.pdf)

**作者**: Ghita Fassy El Fehri, Aurélien Bellet, Philippe Bastien

---

## 💡 一句话要点

**提出Fed-Sparse-BNSL方法，以解决贝叶斯网络结构学习中的隐私保护和通信效率问题。**

**关键词**: `贝叶斯网络结构学习` `差分隐私` `联邦学习` `通信效率` `线性高斯模型` `贪婪算法`

## 📋 核心要点

1. 核心问题：从去中心化数据学习贝叶斯网络结构时，需确保隐私保证并避免通信成本随维度增长。
2. 方法要点：结合差分隐私和贪婪更新，针对每个参与者仅处理少量相关边，高效利用隐私预算并降低通信开销。
3. 实验或效果：在合成和真实数据集上，实现接近非隐私基线的效用，同时提供更强的隐私和通信效率。

## 📄 摘要（原文）

> Learning the structure of a Bayesian network from decentralized data poses two major challenges: (i) ensuring rigorous privacy guarantees for participants, and (ii) avoiding communication costs that scale poorly with dimensionality. In this work, we introduce Fed-Sparse-BNSL, a novel federated method for learning linear Gaussian Bayesian network structures that addresses both challenges. By combining differential privacy with greedy updates that target only a few relevant edges per participant, Fed-Sparse-BNSL efficiently uses the privacy budget while keeping communication costs low. Our careful algorithmic design preserves model identifiability and enables accurate structure estimation. Experiments on synthetic and real datasets demonstrate that Fed-Sparse-BNSL achieves utility close to non-private baselines while offering substantially stronger privacy and communication efficiency.

