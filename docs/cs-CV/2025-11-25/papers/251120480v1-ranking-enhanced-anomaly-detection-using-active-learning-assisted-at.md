---
layout: default
title: Ranking-Enhanced Anomaly Detection Using Active Learning-Assisted Attention Adversarial Dual AutoEncoders
---

# Ranking-Enhanced Anomaly Detection Using Active Learning-Assisted Attention Adversarial Dual AutoEncoders

**arXiv**: [2511.20480v1](https://arxiv.org/abs/2511.20480) | [PDF](https://arxiv.org/pdf/2511.20480.pdf)

**作者**: Sidahmed Benabderrahmane, James Cheney, Talal Rahwan

---

## 💡 一句话要点

**提出基于主动学习和注意力对抗双自编码器的异常检测方法以应对高级持续性威胁**

**关键词**: `异常检测` `主动学习` `自编码器` `高级持续性威胁` `不平衡数据` `注意力机制`

## 📋 核心要点

1. 高级持续性威胁检测面临标签数据稀缺和隐蔽攻击的挑战
2. 采用无监督自编码器结合主动学习，通过选择性查询提升检测精度
3. 在DARPA不平衡数据集上验证，显著提高检测率并优于现有方法

## 📄 摘要（原文）

> Advanced Persistent Threats (APTs) pose a significant challenge in cybersecurity due to their stealthy and long-term nature. Modern supervised learning methods require extensive labeled data, which is often scarce in real-world cybersecurity environments. In this paper, we propose an innovative approach that leverages AutoEncoders for unsupervised anomaly detection, augmented by active learning to iteratively improve the detection of APT anomalies. By selectively querying an oracle for labels on uncertain or ambiguous samples, we minimize labeling costs while improving detection rates, enabling the model to improve its detection accuracy with minimal data while reducing the need for extensive manual labeling. We provide a detailed formulation of the proposed Attention Adversarial Dual AutoEncoder-based anomaly detection framework and show how the active learning loop iteratively enhances the model. The framework is evaluated on real-world imbalanced provenance trace databases produced by the DARPA Transparent Computing program, where APT-like attacks constitute as little as 0.004\% of the data. The datasets span multiple operating systems, including Android, Linux, BSD, and Windows, and cover two attack scenarios. The results have shown significant improvements in detection rates during active learning and better performance compared to other existing approaches.

