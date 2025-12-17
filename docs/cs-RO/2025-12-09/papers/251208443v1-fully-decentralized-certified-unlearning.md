---
layout: default
title: Fully Decentralized Certified Unlearning
---

# Fully Decentralized Certified Unlearning

**arXiv**: [2512.08443v1](https://arxiv.org/abs/2512.08443) | [PDF](https://arxiv.org/pdf/2512.08443.pdf)

**作者**: Hithem Lamri, Michail Maniatakos

---

## 💡 一句话要点

**提出RR-DU方法以解决去中心化网络中认证遗忘的核心挑战**

**关键词**: `认证遗忘` `去中心化网络` `差分隐私` `随机游走` `梯度优化` `图像分类`

## 📋 核心要点

1. 研究去中心化网络中的认证遗忘问题，填补无协调器场景的空白
2. 基于随机游走结合梯度上升/下降、子采样高斯噪声和信任区域投影
3. 在图像基准上实现高测试精度，遗忘准确率降至随机猜测水平

## 📄 摘要（原文）

> Machine unlearning (MU) seeks to remove the influence of specified data from a trained model in response to privacy requests or data poisoning. While certified unlearning has been analyzed in centralized and server-orchestrated federated settings (via guarantees analogous to differential privacy, DP), the decentralized setting -- where peers communicate without a coordinator remains underexplored. We study certified unlearning in decentralized networks with fixed topologies and propose RR-DU, a random-walk procedure that performs one projected gradient ascent step on the forget set at the unlearning client and a geometrically distributed number of projected descent steps on the retained data elsewhere, combined with subsampled Gaussian noise and projection onto a trust region around the original model. We provide (i) convergence guarantees in the convex case and stationarity guarantees in the nonconvex case, (ii) $(\varepsilon,δ)$ network-unlearning certificates on client views via subsampled Gaussian $Rényi$ DP (RDP) with segment-level subsampling, and (iii) deletion-capacity bounds that scale with the forget-to-local data ratio and quantify the effect of decentralization (network mixing and randomized subsampling) on the privacy--utility trade-off. Empirically, on image benchmarks (MNIST, CIFAR-10), RR-DU matches a given $(\varepsilon,δ)$ while achieving higher test accuracy than decentralized DP baselines and reducing forget accuracy to random guessing ($\approx 10\%$).

