---
layout: default
title: DeepSalt: Bridging Laboratory and Satellite Spectra through Domain Adaptation and Knowledge Distillation for Large-Scale Soil Salinity Estimation
---

# DeepSalt: Bridging Laboratory and Satellite Spectra through Domain Adaptation and Knowledge Distillation for Large-Scale Soil Salinity Estimation

**arXiv**: [2510.23124v1](https://arxiv.org/abs/2510.23124) | [PDF](https://arxiv.org/pdf/2510.23124.pdf)

**作者**: Rupasree Dey, Abdul Matin, Everett Lewark, Tanjim Bin Faruk, Andrei Bachinin, Sam Leuthold, M. Francesca Cotrufo, Shrideep Pallickara, Sangmi Lee Pallickara

---

## 💡 一句话要点

**提出DeepSalt框架，通过领域适应和知识蒸馏解决实验室与卫星光谱差异，实现大规模土壤盐度估计。**

**关键词**: `土壤盐度估计` `领域适应` `知识蒸馏` `光谱迁移` `深度学习` `遥感监测`

## 📋 核心要点

1. 土壤盐化影响生态系统和农业，实验室光谱精确但难扩展，卫星图像覆盖广但精度低。
2. 使用知识蒸馏和光谱适应单元，将实验室高分辨率光谱知识迁移到卫星数据。
3. 实验显示性能优于无领域适应方法，能泛化到未知区域，解释盐度方差。

## 📄 摘要（原文）

> Soil salinization poses a significant threat to both ecosystems and
> agriculture because it limits plants' ability to absorb water and, in doing so,
> reduces crop productivity. This phenomenon alters the soil's spectral
> properties, creating a measurable relationship between salinity and light
> reflectance that enables remote monitoring. While laboratory spectroscopy
> provides precise measurements, its reliance on in-situ sampling limits
> scalability to regional or global levels. Conversely, hyperspectral satellite
> imagery enables wide-area observation but lacks the fine-grained
> interpretability of laboratory instruments. To bridge this gap, we introduce
> DeepSalt, a deep-learning-based spectral transfer framework that leverages
> knowledge distillation and a novel Spectral Adaptation Unit to transfer
> high-resolution spectral insights from laboratory-based spectroscopy to
> satellite-based hyperspectral sensing. Our approach eliminates the need for
> extensive ground sampling while enabling accurate, large-scale salinity
> estimation, as demonstrated through comprehensive empirical benchmarks.
> DeepSalt achieves significant performance gains over methods without explicit
> domain adaptation, underscoring the impact of the proposed Spectral Adaptation
> Unit and the knowledge distillation strategy. The model also effectively
> generalized to unseen geographic regions, explaining a substantial portion of
> the salinity variance.

