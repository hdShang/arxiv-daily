---
layout: default
title: Deep Learning-Based Regional White Matter Hyperintensity Mapping as a Robust Biomarker for Alzheimer's Disease
---

# Deep Learning-Based Regional White Matter Hyperintensity Mapping as a Robust Biomarker for Alzheimer's Disease

**arXiv**: [2511.14588v1](https://arxiv.org/abs/2511.14588) | [PDF](https://arxiv.org/pdf/2511.14588.pdf)

**作者**: Julia Machnio, Mads Nielsen, Mostafa Mehdipour Ghazi

---

## 💡 一句话要点

**提出基于深度学习的区域白质高信号映射方法，以增强阿尔茨海默病诊断。**

**关键词**: `白质高信号分割` `深度学习框架` `阿尔茨海默病诊断` `区域病变量化` `脑萎缩指标`

## 📋 核心要点

1. 核心问题：现有白质高信号分割方法忽略空间分布，仅提供全局病变负荷。
2. 方法要点：开发深度学习框架，实现稳健分割并量化解剖区域病变体积。
3. 实验或效果：区域病变体积结合脑萎缩指标，疾病分类AUC最高达0.97。

## 📄 摘要（原文）

> White matter hyperintensities (WMH) are key imaging markers in cognitive aging, Alzheimer's disease (AD), and related dementias. Although automated methods for WMH segmentation have advanced, most provide only global lesion load and overlook their spatial distribution across distinct white matter regions. We propose a deep learning framework for robust WMH segmentation and localization, evaluated across public datasets and an independent Alzheimer's Disease Neuroimaging Initiative (ADNI) cohort. Our results show that the predicted lesion loads are in line with the reference WMH estimates, confirming the robustness to variations in lesion load, acquisition, and demographics. Beyond accurate segmentation, we quantify WMH load within anatomically defined regions and combine these measures with brain structure volumes to assess diagnostic value. Regional WMH volumes consistently outperform global lesion burden for disease classification, and integration with brain atrophy metrics further improves performance, reaching area under the curve (AUC) values up to 0.97. Several spatially distinct regions, particularly within anterior white matter tracts, are reproducibly associated with diagnostic status, indicating localized vulnerability in AD. These results highlight the added value of regional WMH quantification. Incorporating localized lesion metrics alongside atrophy markers may enhance early diagnosis and stratification in neurodegenerative disorders.

