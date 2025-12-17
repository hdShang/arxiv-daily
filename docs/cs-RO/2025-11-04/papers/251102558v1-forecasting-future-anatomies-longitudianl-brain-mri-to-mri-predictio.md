---
layout: default
title: Forecasting Future Anatomies: Longitudianl Brain Mri-to-Mri Prediction
---

# Forecasting Future Anatomies: Longitudianl Brain Mri-to-Mri Prediction

**arXiv**: [2511.02558v1](https://arxiv.org/abs/2511.02558) | [PDF](https://arxiv.org/pdf/2511.02558.pdf)

**作者**: Ali Farki, Elaheh Moradi, Deepika Koundal, Jussi Tohka

---

## 💡 一句话要点

**提出深度学习模型以预测未来脑部MRI，应用于神经退行性疾病研究**

**关键词**: `脑部MRI预测` `深度学习架构` `神经退行性疾病` `纵向数据分析` `图像到图像预测`

## 📋 核心要点

1. 核心问题：从基线MRI预测未来脑部状态，以研究阿尔茨海默病等神经退行性疾病
2. 方法要点：评估五种深度学习架构，包括UNet和ODE-UNet，用于图像到图像预测
3. 实验或效果：在ADNI和AIBL数据集上实现高保真预测，并展示跨队列泛化能力

## 📄 摘要（原文）

> Predicting future brain state from a baseline magnetic resonance image (MRI)
> is a central challenge in neuroimaging and has important implications for
> studying neurodegenerative diseases such as Alzheimer's disease (AD). Most
> existing approaches predict future cognitive scores or clinical outcomes, such
> as conversion from mild cognitive impairment to dementia. Instead, here we
> investigate longitudinal MRI image-to-image prediction that forecasts a
> participant's entire brain MRI several years into the future, intrinsically
> modeling complex, spatially distributed neurodegenerative patterns. We
> implement and evaluate five deep learning architectures (UNet, U2-Net, UNETR,
> Time-Embedding UNet, and ODE-UNet) on two longitudinal cohorts (ADNI and AIBL).
> Predicted follow-up MRIs are directly compared with the actual follow-up scans
> using metrics that capture global similarity and local differences. The best
> performing models achieve high-fidelity predictions, and all models generalize
> well to an independent external dataset, demonstrating robust cross-cohort
> performance. Our results indicate that deep learning can reliably predict
> participant-specific brain MRI at the voxel level, offering new opportunities
> for individualized prognosis.

