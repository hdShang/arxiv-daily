---
layout: default
title: Cancer-Net PCa-MultiSeg: Multimodal Enhancement of Prostate Cancer Lesion Segmentation Using Synthetic Correlated Diffusion Imaging
---

# Cancer-Net PCa-MultiSeg: Multimodal Enhancement of Prostate Cancer Lesion Segmentation Using Synthetic Correlated Diffusion Imaging

**arXiv**: [2511.07816v1](https://arxiv.org/abs/2511.07816) | [PDF](https://arxiv.org/pdf/2511.07816.pdf)

**作者**: Jarett Dewbury, Chi-en Amy Tai, Alexander Wong

---

## 💡 一句话要点

**提出合成相关扩散成像以增强前列腺癌病灶分割性能**

**关键词**: `前列腺癌分割` `合成相关扩散成像` `多模态增强` `深度学习架构` `临床部署`

## 📋 核心要点

1. 当前深度学习前列腺癌病灶分割性能有限，Dice分数低至0.32或以下
2. 使用合成相关扩散成像增强标准扩散协议，无需额外扫描或架构修改
3. 在200患者数据上评估，94%配置性能提升，相对改进最高达72.5%

## 📄 摘要（原文）

> Current deep learning approaches for prostate cancer lesion segmentation achieve limited performance, with Dice scores of 0.32 or lower in large patient cohorts. To address this limitation, we investigate synthetic correlated diffusion imaging (CDI$^s$) as an enhancement to standard diffusion-based protocols. We conduct a comprehensive evaluation across six state-of-the-art segmentation architectures using 200 patients with co-registered CDI$^s$, diffusion-weighted imaging (DWI) and apparent diffusion coefficient (ADC) sequences. We demonstrate that CDI$^s$ integration reliably enhances or preserves segmentation performance in 94% of evaluated configurations, with individual architectures achieving up to 72.5% statistically significant relative improvement over baseline modalities. CDI$^s$ + DWI emerges as the safest enhancement pathway, achieving significant improvements in half of evaluated architectures with zero instances of degradation. Since CDI$^s$ derives from existing DWI acquisitions without requiring additional scan time or architectural modifications, it enables immediate deployment in clinical workflows. Our results establish validated integration pathways for CDI$^s$ as a practical drop-in enhancement for PCa lesion segmentation tasks across diverse deep learning architectures.

