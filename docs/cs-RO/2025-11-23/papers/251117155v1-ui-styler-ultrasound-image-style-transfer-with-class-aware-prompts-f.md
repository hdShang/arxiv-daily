---
layout: default
title: UI-Styler: Ultrasound Image Style Transfer with Class-Aware Prompts for Cross-Device Diagnosis Using a Frozen Black-Box Inference Network
---

# UI-Styler: Ultrasound Image Style Transfer with Class-Aware Prompts for Cross-Device Diagnosis Using a Frozen Black-Box Inference Network

**arXiv**: [2511.17155v1](https://arxiv.org/abs/2511.17155) | [PDF](https://arxiv.org/pdf/2511.17155.pdf)

**作者**: Nhat-Tuong Do-Tran, Ngoc-Hoang-Lam Le, Ching-Chun Huang

---

## 💡 一句话要点

**提出UI-Styler框架，通过类感知提示解决超声图像跨设备诊断中的域偏移问题。**

**关键词**: `超声图像风格迁移` `跨设备诊断` `类感知提示` `域适应` `黑盒推理网络`

## 📋 核心要点

1. 超声图像因设备差异导致域偏移，降低黑盒推理模型性能。
2. 采用模式匹配和类感知提示策略，实现纹理转移和语义对齐。
3. 实验显示在分类和分割任务中优于现有方法，提升分布距离和下游性能。

## 📄 摘要（原文）

> The appearance of ultrasound images varies across acquisition devices, causing domain shifts that degrade the performance of fixed black-box downstream inference models when reused. To mitigate this issue, it is practical to develop unpaired image translation (UIT) methods that effectively align the statistical distributions between source and target domains, particularly under the constraint of a reused inference-blackbox setting. However, existing UIT approaches often overlook class-specific semantic alignment during domain adaptation, resulting in misaligned content-class mappings that can impair diagnostic accuracy. To address this limitation, we propose UI-Styler, a novel ultrasound-specific, class-aware image style transfer framework. UI-Styler leverages a pattern-matching mechanism to transfer texture patterns embedded in the target images onto source images while preserving the source structural content. In addition, we introduce a class-aware prompting strategy guided by pseudo labels of the target domain, which enforces accurate semantic alignment with diagnostic categories. Extensive experiments on ultrasound cross-device tasks demonstrate that UI-Styler consistently outperforms existing UIT methods, achieving state-of-the-art performance in distribution distance and downstream tasks, such as classification and segmentation.

