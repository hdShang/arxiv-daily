---
layout: default
title: TARA Test-by-Adaptive-Ranks for Quantum Anomaly Detection with Conformal Prediction Guarantees
---

# TARA Test-by-Adaptive-Ranks for Quantum Anomaly Detection with Conformal Prediction Guarantees

**arXiv**: [2512.04016v1](https://arxiv.org/abs/2512.04016) | [PDF](https://arxiv.org/pdf/2512.04016.pdf)

**作者**: Davut Emre Tasar, Ceren Ocal Tasar

---

## 💡 一句话要点

**提出TARA框架，结合保形预测与序贯鞅测试，为量子异常检测提供分布无关的统计保证。**

**关键词**: `量子异常检测` `保形预测` `序贯鞅测试` `量子密钥分发` `分布无关保证` `跨平台验证`

## 📋 核心要点

1. 核心问题：量子密钥分发安全认证在有限样本和对抗场景下缺乏严格统计保证。
2. 方法要点：TARA-k基于Kolmogorov-Smirnov校准，TARA-m使用投注鞅进行流式检测，控制I类错误。
3. 实验效果：在IBM和IonQ量子处理器上验证，安全裕度超过经典CHSH界限36%，揭示校准方法影响性能。

## 📄 摘要（原文）

> Quantum key distribution (QKD) security fundamentally relies on the ability to distinguish genuine quantum correlations from classical eavesdropper simulations, yet existing certification methods lack rigorous statistical guarantees under finite-sample conditions and adversarial scenarios. We introduce TARA (Test by Adaptive Ranks), a novel framework combining conformal prediction with sequential martingale testing for quantum anomaly detection that provides distribution-free validity guarantees. TARA offers two complementary approaches. TARA k, based on Kolmogorov Smirnov calibration against local hidden variable (LHV) null distributions, achieving ROC AUC = 0.96 for quantum-classical discrimination. And TARA-m, employing betting martingales for streaming detection with anytime valid type I error control that enables real time monitoring of quantum channels. We establish theoretical guarantees proving that under (context conditional) exchangeability, conformal p-values remain uniformly distributed even for strongly contextual quantum data, confirming that quantum contextuality does not break conformal prediction validity a result with implications beyond quantum certification to any application of distribution-free methods to nonclassical data. Extensive validation on both IBM Torino (superconducting, CHSH = 2.725) and IonQ Forte Enterprise (trapped ion, CHSH = 2.716) quantum processors demonstrates cross-platform robustness, achieving 36% security margins above the classical CHSH bound of 2. Critically, our framework reveals a methodological concern affecting quantum certification more broadly: same-distribution calibration can inflate detection performance by up to 44 percentage points compared to proper cross-distribution calibration, suggesting that prior quantum certification studies using standard train test splits may have systematically overestimated adversarial robustness.

