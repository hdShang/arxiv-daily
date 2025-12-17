---
layout: default
title: Collaborative Attention and Consistent-Guided Fusion of MRI and PET for Alzheimer's Disease Diagnosis
---

# Collaborative Attention and Consistent-Guided Fusion of MRI and PET for Alzheimer's Disease Diagnosis

**arXiv**: [2511.02228v1](https://arxiv.org/abs/2511.02228) | [PDF](https://arxiv.org/pdf/2511.02228.pdf)

**作者**: Delin Ma, Menghui Zhou, Jun Qi, Yun Yang, Po Yang

---

## 💡 一句话要点

**提出协作注意与一致性引导融合框架，用于MRI和PET的阿尔茨海默病诊断**

**关键词**: `阿尔茨海默病诊断` `多模态融合` `协作注意机制` `一致性引导` `MRI和PET` `神经影像分析`

## 📋 核心要点

1. 现有方法忽视模态特定特征，且模态分布差异导致表示偏差和噪声
2. 引入可学习参数表示块、共享与独立编码器，以及一致性引导机制
3. 在ADNI数据集上实验，诊断性能优于现有融合策略

## 📄 摘要（原文）

> Alzheimer's disease (AD) is the most prevalent form of dementia, and its
> early diagnosis is essential for slowing disease progression. Recent studies on
> multimodal neuroimaging fusion using MRI and PET have achieved promising
> results by integrating multi-scale complementary features. However, most
> existing approaches primarily emphasize cross-modal complementarity while
> overlooking the diagnostic importance of modality-specific features. In
> addition, the inherent distributional differences between modalities often lead
> to biased and noisy representations, degrading classification performance. To
> address these challenges, we propose a Collaborative Attention and
> Consistent-Guided Fusion framework for MRI and PET based AD diagnosis. The
> proposed model introduces a learnable parameter representation (LPR) block to
> compensate for missing modality information, followed by a shared encoder and
> modality-independent encoders to preserve both shared and specific
> representations. Furthermore, a consistency-guided mechanism is employed to
> explicitly align the latent distributions across modalities. Experimental
> results on the ADNI dataset demonstrate that our method achieves superior
> diagnostic performance compared with existing fusion strategies.

