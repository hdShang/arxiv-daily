---
layout: default
title: Distilling Cross-Modal Knowledge via Feature Disentanglement
---

# Distilling Cross-Modal Knowledge via Feature Disentanglement

**arXiv**: [2511.19887v1](https://arxiv.org/abs/2511.19887) | [PDF](https://arxiv.org/pdf/2511.19887.pdf)

**作者**: Junhong Liu, Yuan Zhang, Tao Huang, Wenchao Xu, Renyu Yang

---

## 💡 一句话要点

**提出频率解耦跨模态知识蒸馏以解决跨模态表示不一致问题**

**关键词**: `知识蒸馏` `跨模态学习` `特征解耦` `频域分析` `表示对齐`

## 📋 核心要点

1. 跨模态知识蒸馏中表示不一致导致知识迁移困难
2. 利用频域特征解耦，低频强对齐、高频松对齐，并引入尺度一致性损失
3. 在多个基准数据集上显著优于传统和先进跨模态蒸馏方法

## 📄 摘要（原文）

> Knowledge distillation (KD) has proven highly effective for compressing large models and enhancing the performance of smaller ones. However, its effectiveness diminishes in cross-modal scenarios, such as vision-to-language distillation, where inconsistencies in representation across modalities lead to difficult knowledge transfer. To address this challenge, we propose frequency-decoupled cross-modal knowledge distillation, a method designed to decouple and balance knowledge transfer across modalities by leveraging frequency-domain features. We observed that low-frequency features exhibit high consistency across different modalities, whereas high-frequency features demonstrate extremely low cross-modal similarity. Accordingly, we apply distinct losses to these features: enforcing strong alignment in the low-frequency domain and introducing relaxed alignment for high-frequency features. We also propose a scale consistency loss to address distributional shifts between modalities, and employ a shared classifier to unify feature spaces. Extensive experiments across multiple benchmark datasets show our method substantially outperforms traditional KD and state-of-the-art cross-modal KD approaches. Code is available at https://github.com/Johumliu/FD-CMKD.

