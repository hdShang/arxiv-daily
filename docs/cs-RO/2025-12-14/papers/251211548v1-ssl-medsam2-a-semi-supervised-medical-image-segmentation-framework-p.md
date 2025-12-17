---
layout: default
title: SSL-MedSAM2: A Semi-supervised Medical Image Segmentation Framework Powered by Few-shot Learning of SAM2
---

# SSL-MedSAM2: A Semi-supervised Medical Image Segmentation Framework Powered by Few-shot Learning of SAM2

**arXiv**: [2512.11548v1](https://arxiv.org/abs/2512.11548) | [PDF](https://arxiv.org/pdf/2512.11548.pdf)

**作者**: Zhendi Gong, Xin Chen

---

## 💡 一句话要点

**提出SSL-MedSAM2半监督医学图像分割框架，结合SAM2少样本学习与nnUNet迭代训练以降低标注成本。**

**关键词**: `半监督学习` `医学图像分割` `少样本学习` `伪标签生成` `SAM2` `nnUNet`

## 📋 核心要点

1. 核心问题：医学图像标注耗时，全监督方法依赖大规模标注数据，限制临床应用。
2. 方法要点：基于SAM2的免训练少样本分支生成伪标签，结合nnUNet迭代分支进行伪标签精炼。
3. 实验或效果：在CARE-LiSeg挑战中，GED4和T1 MRI测试集Dice分数分别为0.9710和0.9648，表现优异。

## 📄 摘要（原文）

> Despite the success of deep learning based models in medical image segmentation, most state-of-the-art (SOTA) methods perform fully-supervised learning, which commonly rely on large scale annotated training datasets. However, medical image annotation is highly time-consuming, hindering its clinical applications. Semi-supervised learning (SSL) has been emerged as an appealing strategy in training with limited annotations, largely reducing the labelling cost. We propose a novel SSL framework SSL-MedSAM2, which contains a training-free few-shot learning branch TFFS-MedSAM2 based on the pretrained large foundation model Segment Anything Model 2 (SAM2) for pseudo label generation, and an iterative fully-supervised learning branch FSL-nnUNet based on nnUNet for pseudo label refinement. The results on MICCAI2025 challenge CARE-LiSeg (Liver Segmentation) demonstrate an outstanding performance of SSL-MedSAM2 among other methods. The average dice scores on the test set in GED4 and T1 MRI are 0.9710 and 0.9648 respectively, and the Hausdorff distances are 20.07 and 21.97 respectively. The code is available via https://github.com/naisops/SSL-MedSAM2/tree/main.

