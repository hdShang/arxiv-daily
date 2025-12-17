---
layout: default
title: Signature Forgery Detection: Improving Cross-Dataset Generalization
---

# Signature Forgery Detection: Improving Cross-Dataset Generalization

**arXiv**: [2510.17724v1](https://arxiv.org/abs/2510.17724) | [PDF](https://arxiv.org/pdf/2510.17724.pdf)

**作者**: Matheus Ramos Parracho

---

## 💡 一句话要点

**研究特征学习策略以提升签名伪造检测的跨数据集泛化能力**

**关键词**: `签名伪造检测` `跨数据集泛化` `特征学习` `离线签名验证` `壳预处理`

## 📋 核心要点

1. 核心问题：离线签名验证模型在跨数据集时泛化性能差，受手写风格和采集协议变化影响。
2. 方法要点：开发两种实验流程，基于原始图像和壳预处理，探索特征学习策略。
3. 实验或效果：原始图像模型性能更高，壳预处理模型显示未来改进潜力。

## 📄 摘要（原文）

> Automated signature verification is a critical biometric technique used in
> banking, identity authentication, and legal documentation. Despite the notable
> progress achieved by deep learning methods, most approaches in offline
> signature verification still struggle to generalize across datasets, as
> variations in handwriting styles and acquisition protocols often degrade
> performance. This study investigates feature learning strategies for signature
> forgery detection, focusing on improving cross-dataset generalization -- that
> is, model robustness when trained on one dataset and tested on another. Using
> three public benchmarks -- CEDAR, ICDAR, and GPDS Synthetic -- two experimental
> pipelines were developed: one based on raw signature images and another
> employing a preprocessing method referred to as shell preprocessing. Several
> behavioral patterns were identified and analyzed; however, no definitive
> superiority between the two approaches was established. The results show that
> the raw-image model achieved higher performance across benchmarks, while the
> shell-based model demonstrated promising potential for future refinement toward
> robust, cross-domain signature verification.

