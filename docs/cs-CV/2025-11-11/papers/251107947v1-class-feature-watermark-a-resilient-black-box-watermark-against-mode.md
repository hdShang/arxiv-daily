---
layout: default
title: Class-feature Watermark: A Resilient Black-box Watermark Against Model Extraction Attacks
---

# Class-feature Watermark: A Resilient Black-box Watermark Against Model Extraction Attacks

**arXiv**: [2511.07947v1](https://arxiv.org/abs/2511.07947) | [PDF](https://arxiv.org/pdf/2511.07947.pdf)

**作者**: Yaxin Xiao, Qingqing Ye, Zi Liang, Haoyang Li, RongHua Li, Huadi Zheng, Haibo Hu

---

## 💡 一句话要点

**提出类特征水印以增强模型提取攻击下的黑盒水印鲁棒性**

**关键词**: `模型水印` `模型提取攻击` `黑盒水印` `鲁棒性` `类特征水印` `移除攻击`

## 📋 核心要点

1. 核心问题：现有黑盒水印在序列模型提取和移除攻击下鲁棒性不足，风险被低估。
2. 方法要点：CFW利用类级伪影构建合成类，消除易受攻击的决策边界。
3. 实验效果：CFW在多种领域保持至少70.15%水印成功率，优于现有方法。

## 📄 摘要（原文）

> Machine learning models constitute valuable intellectual property, yet remain vulnerable to model extraction attacks (MEA), where adversaries replicate their functionality through black-box queries. Model watermarking counters MEAs by embedding forensic markers for ownership verification. Current black-box watermarks prioritize MEA survival through representation entanglement, yet inadequately explore resilience against sequential MEAs and removal attacks. Our study reveals that this risk is underestimated because existing removal methods are weakened by entanglement. To address this gap, we propose Watermark Removal attacK (WRK), which circumvents entanglement constraints by exploiting decision boundaries shaped by prevailing sample-level watermark artifacts. WRK effectively reduces watermark success rates by at least 88.79% across existing watermarking benchmarks.
>   For robust protection, we propose Class-Feature Watermarks (CFW), which improve resilience by leveraging class-level artifacts. CFW constructs a synthetic class using out-of-domain samples, eliminating vulnerable decision boundaries between original domain samples and their artifact-modified counterparts (watermark samples). CFW concurrently optimizes both MEA transferability and post-MEA stability. Experiments across multiple domains show that CFW consistently outperforms prior methods in resilience, maintaining a watermark success rate of at least 70.15% in extracted models even under the combined MEA and WRK distortion, while preserving the utility of protected models.

