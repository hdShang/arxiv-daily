---
layout: default
title: Mitigating representation bias caused by missing pixels in methane plume detection
---

# Mitigating representation bias caused by missing pixels in methane plume detection

**arXiv**: [2510.19478v1](https://arxiv.org/abs/2510.19478) | [PDF](https://arxiv.org/pdf/2510.19478.pdf)

**作者**: Julia Wąsala, Joannes D. Maasakkers, Ilse Aben, Rochelle Schneider, Holger Hoos, Mitra Baratchi

---

## 💡 一句话要点

**提出加权重采样和插补方法以缓解甲烷羽流检测中的表示偏差**

**关键词**: `甲烷羽流检测` `表示偏差缓解` `缺失数据插补` `加权重采样` `卫星图像分析`

## 📋 核心要点

1. 卫星图像中系统缺失像素导致表示偏差，模型错误关联覆盖度与标签
2. 采用插补和加权重采样方法，强制覆盖度分箱中的类别平衡
3. 实验显示方法显著减少偏差，提升低覆盖图像中的羽流检测能力

## 📄 摘要（原文）

> Most satellite images have systematically missing pixels (i.e., missing data
> not at random (MNAR)) due to factors such as clouds. If not addressed, these
> missing pixels can lead to representation bias in automated feature extraction
> models. In this work, we show that spurious association between the label and
> the number of missing values in methane plume detection can cause the model to
> associate the coverage (i.e., the percentage of valid pixels in an image) with
> the label, subsequently under-detecting plumes in low-coverage images. We
> evaluate multiple imputation approaches to remove the dependence between the
> coverage and a label. Additionally, we propose a weighted resampling scheme
> during training that removes the association between the label and the coverage
> by enforcing class balance in each coverage bin. Our results show that both
> resampling and imputation can significantly reduce the representation bias
> without hurting balanced accuracy, precision, or recall. Finally, we evaluate
> the capability of the debiased models using these techniques in an operational
> scenario and demonstrate that the debiased models have a higher chance of
> detecting plumes in low-coverage images.

