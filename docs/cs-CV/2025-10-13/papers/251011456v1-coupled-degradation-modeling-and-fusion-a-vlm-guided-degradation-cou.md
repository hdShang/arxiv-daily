---
layout: default
title: Coupled Degradation Modeling and Fusion: A VLM-Guided Degradation-Coupled Network for Degradation-Aware Infrared and Visible Image Fusion
---

# Coupled Degradation Modeling and Fusion: A VLM-Guided Degradation-Coupled Network for Degradation-Aware Infrared and Visible Image Fusion

**arXiv**: [2510.11456v1](https://arxiv.org/abs/2510.11456) | [PDF](https://arxiv.org/pdf/2510.11456.pdf)

**作者**: Tianpei Zhang, Jufeng Zhao, Yiming Zhu, Guangmang Cui

---

## 💡 一句话要点

**提出VGDCFusion网络，耦合退化建模与图像融合以处理退化红外和可见光图像**

**关键词**: `红外和可见光图像融合` `退化建模` `视觉语言模型` `退化感知` `特征融合`

## 📋 核心要点

1. 现有红外和可见光图像融合方法假设高质量输入，处理退化图像时性能下降
2. 使用VLM引导退化感知，SPDCE和JPDCF模块耦合退化抑制与特征提取融合
3. 实验表明VGDCFusion在多种退化场景下优于现有方法，代码已开源

## 📄 摘要（原文）

> Existing Infrared and Visible Image Fusion (IVIF) methods typically assume
> high-quality inputs. However, when handing degraded images, these methods
> heavily rely on manually switching between different pre-processing techniques.
> This decoupling of degradation handling and image fusion leads to significant
> performance degradation. In this paper, we propose a novel VLM-Guided
> Degradation-Coupled Fusion network (VGDCFusion), which tightly couples
> degradation modeling with the fusion process and leverages vision-language
> models (VLMs) for degradation-aware perception and guided suppression.
> Specifically, the proposed Specific-Prompt Degradation-Coupled Extractor
> (SPDCE) enables modality-specific degradation awareness and establishes a joint
> modeling of degradation suppression and intra-modal feature extraction. In
> parallel, the Joint-Prompt Degradation-Coupled Fusion (JPDCF) facilitates
> cross-modal degradation perception and couples residual degradation filtering
> with complementary cross-modal feature fusion. Extensive experiments
> demonstrate that our VGDCFusion significantly outperforms existing
> state-of-the-art fusion approaches under various degraded image scenarios. Our
> code is available at https://github.com/Lmmh058/VGDCFusion.

