---
layout: default
title: SCU-CGAN: Enhancing Fire Detection through Synthetic Fire Image Generation and Dataset Augmentation
---

# SCU-CGAN: Enhancing Fire Detection through Synthetic Fire Image Generation and Dataset Augmentation

**arXiv**: [2512.08362v1](https://arxiv.org/abs/2512.08362) | [PDF](https://arxiv.org/pdf/2512.08362.pdf)

**作者**: Ju-Young Kim, Ji-Hong Park, Gun-Woo Kim

---

## 💡 一句话要点

**提出SCU-CGAN模型以增强火灾检测，通过合成火灾图像进行数据集增强。**

**关键词**: `火灾检测` `图像生成` `数据集增强` `生成对抗网络` `计算机视觉`

## 📋 核心要点

1. 火灾检测模型性能受限于数据集不足，影响早期预警效果。
2. SCU-CGAN集成U-Net、CBAM和额外判别器，从非火图像生成逼真火灾图像。
3. 实验显示生成图像质量提升，增强数据集显著提高检测模型准确率，如YOLOv5 nano的mAP@0.5:0.95增加56.5%。

## 📄 摘要（原文）

> Fire has long been linked to human life, causing severe disasters and losses. Early detection is crucial, and with the rise of home IoT technologies, household fire detection systems have emerged. However, the lack of sufficient fire datasets limits the performance of detection models. We propose the SCU-CGAN model, which integrates U-Net, CBAM, and an additional discriminator to generate realistic fire images from nonfire images. We evaluate the image quality and confirm that SCU-CGAN outperforms existing models. Specifically, SCU-CGAN achieved a 41.5% improvement in KID score compared to CycleGAN, demonstrating the superior quality of the generated fire images. Furthermore, experiments demonstrate that the augmented dataset significantly improves the accuracy of fire detection models without altering their structure. For the YOLOv5 nano model, the most notable improvement was observed in the mAP@0.5:0.95 metric, which increased by 56.5%, highlighting the effectiveness of the proposed approach.

