---
layout: default
title: Collaborative Reconstruction and Repair for Multi-class Industrial Anomaly Detection
---

# Collaborative Reconstruction and Repair for Multi-class Industrial Anomaly Detection

**arXiv**: [2512.11401v1](https://arxiv.org/abs/2512.11401) | [PDF](https://arxiv.org/pdf/2512.11401.pdf)

**作者**: Qishan Wang, Haofeng Wang, Shuyong Gao, Jia Guo, Li Xiong, Jiaqi Li, Dengxuan Bai, Wenqiang Zhang

---

## 💡 一句话要点

**提出协作重建与修复框架以解决多类工业异常检测中的身份映射问题**

**关键词**: `工业异常检测` `多类统一框架` `协作重建与修复` `身份映射问题` `特征掩码` `异常定位`

## 📋 核心要点

1. 核心问题：多类统一框架下重建网络易发生身份映射，导致异常检测失败。
2. 方法要点：通过重建正常样本并修复合成异常，结合特征掩码和分割网络优化表示差异。
3. 实验或效果：在工业数据集上验证有效缓解身份映射，实现先进检测性能。

## 📄 摘要（原文）

> Industrial anomaly detection is a challenging open-set task that aims to identify unknown anomalous patterns deviating from normal data distribution. To avoid the significant memory consumption and limited generalizability brought by building separate models per class, we focus on developing a unified framework for multi-class anomaly detection. However, under this challenging setting, conventional reconstruction-based networks often suffer from an identity mapping problem, where they directly replicate input features regardless of whether they are normal or anomalous, resulting in detection failures. To address this issue, this study proposes a novel framework termed Collaborative Reconstruction and Repair (CRR), which transforms the reconstruction to repairation. First, we optimize the decoder to reconstruct normal samples while repairing synthesized anomalies. Consequently, it generates distinct representations for anomalous regions and similar representations for normal areas compared to the encoder's output. Second, we implement feature-level random masking to ensure that the representations from decoder contain sufficient local information. Finally, to minimize detection errors arising from the discrepancies between feature representations from the encoder and decoder, we train a segmentation network supervised by synthetic anomaly masks, thereby enhancing localization performance. Extensive experiments on industrial datasets that CRR effectively mitigates the identity mapping issue and achieves state-of-the-art performance in multi-class industrial anomaly detection.

