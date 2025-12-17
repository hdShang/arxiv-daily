---
layout: default
title: Tumor-anchored deep feature random forests for out-of-distribution detection in lung cancer segmentation
---

# Tumor-anchored deep feature random forests for out-of-distribution detection in lung cancer segmentation

**arXiv**: [2512.08216v1](https://arxiv.org/abs/2512.08216) | [PDF](https://arxiv.org/pdf/2512.08216.pdf)

**作者**: Aneesh Rangnekar, Harini Veeraraghavan

---

## 💡 一句话要点

**提出基于肿瘤锚定深度特征的随机森林框架RF-Deep，用于肺癌分割中的分布外检测。**

**关键词**: `肺癌分割` `分布外检测` `深度特征` `随机森林` `计算机断层扫描` `医学影像分析`

## 📋 核心要点

1. 核心问题：现有肺癌分割模型易受分布外输入影响，产生错误分割，威胁临床安全部署。
2. 方法要点：利用预训练编码器的层次特征，通过肿瘤锚定区域提取特征，构建轻量级随机森林进行检测。
3. 实验或效果：在近分布外和远分布外数据集上，RF-Deep的AUROC分别超过93.50%和99.00%，优于基线方法。

## 📄 摘要（原文）

> Accurate segmentation of cancerous lesions from 3D computed tomography (CT) scans is essential for automated treatment planning and response assessment. However, even state-of-the-art models combining self-supervised learning (SSL) pretrained transformers with convolutional decoders are susceptible to out-of-distribution (OOD) inputs, generating confidently incorrect tumor segmentations, posing risks for safe clinical deployment. Existing logit-based methods suffer from task-specific model biases, while architectural enhancements to explicitly detect OOD increase parameters and computational costs. Hence, we introduce a plug-and-play and lightweight post-hoc random forests-based OOD detection framework called RF-Deep that leverages deep features with limited outlier exposure. RF-Deep enhances generalization to imaging variations by repurposing the hierarchical features from the pretrained-then-finetuned backbone encoder, providing task-relevant OOD detection by extracting the features from multiple regions of interest anchored to the predicted tumor segmentations. Hence, it scales to images of varying fields-of-view. We compared RF-Deep against existing OOD detection methods using 1,916 CT scans across near-OOD (pulmonary embolism, negative COVID-19) and far-OOD (kidney cancer, healthy pancreas) datasets. RF-Deep achieved AUROC > 93.50 for the challenging near-OOD datasets and near-perfect detection (AUROC > 99.00) for the far-OOD datasets, substantially outperforming logit-based and radiomics approaches. RF-Deep maintained similar performance consistency across networks of different depths and pretraining strategies, demonstrating its effectiveness as a lightweight, architecture-agnostic approach to enhance the reliability of tumor segmentation from CT volumes.

