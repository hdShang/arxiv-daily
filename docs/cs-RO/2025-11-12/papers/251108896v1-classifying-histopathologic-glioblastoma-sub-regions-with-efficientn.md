---
layout: default
title: Classifying Histopathologic Glioblastoma Sub-regions with EfficientNet
---

# Classifying Histopathologic Glioblastoma Sub-regions with EfficientNet

**arXiv**: [2511.08896v1](https://arxiv.org/abs/2511.08896) | [PDF](https://arxiv.org/pdf/2511.08896.pdf)

**作者**: Sanyukta Adap, Ujjwal Baid, Spyridon Bakas

---

## 💡 一句话要点

**提出基于EfficientNet的深度学习方法，用于分类胶质母细胞瘤组织病理学子区域。**

**关键词**: `胶质母细胞瘤分类` `组织病理学图像` `EfficientNet` `深度学习` `BraTS-Path数据集`

## 📋 核心要点

1. 核心问题：胶质母细胞瘤组织病理学子区域的自动分类，以辅助疾病形态学理解。
2. 方法要点：采用EfficientNet变体（如B1和B4）构建四步深度学习框架。
3. 实验或效果：在BraTS-Path数据集上，训练集F1达0.98，但验证和测试集F1约0.55，显示泛化挑战。

## 📄 摘要（原文）

> Glioblastoma (GBM) is the most common aggressive, fast-growing brain tumor, with a grim prognosis. Despite clinical diagnostic advancements, there have not been any substantial improvements to patient prognosis. Histopathological assessment of excised tumors is the first line of clinical diagnostic routine. We hypothesize that automated, robust, and accurate identification of distinct histological sub-regions within GBM could contribute to morphologically understanding this disease at scale. In this study, we designed a four-step deep learning approach to classify six (6) histopathological regions and quantitatively evaluated it on the BraTS-Path 2024 challenge dataset, which includes digitized Hematoxylin \& Eosin (H\&E) stained GBM tissue sections annotated for six distinct regions. We used the challenge's publicly available training dataset to develop and evaluate the effectiveness of several variants of EfficientNet architectures (i.e., B0, B1, B2, B3, B4). EfficientNet-B1 and EfficientNet-B4 achieved the best performance, achieving an F1 score of 0.98 in a 5-fold cross-validation configuration using the BraTS-Path training set. The quantitative performance evaluation of our proposed approach with EfficientNet-B1 on the BraTS-Path hold-out validation data and the final hidden testing data yielded F1 scores of 0.546 and 0.517, respectively, for the associated 6-class classification task. The difference in the performance on training, validation, and testing data highlights the challenge of developing models that generalize well to new data, which is crucial for clinical applications. The source code of the proposed approach can be found at the GitHub repository of Indiana University Division of Computational Pathology: https://github.com/IUCompPath/brats-path-2024-enet.

