---
layout: default
title: MasHeNe: A Benchmark for Head and Neck CT Mass Segmentation using Window-Enhanced Mamba with Frequency-Domain Integration
---

# MasHeNe: A Benchmark for Head and Neck CT Mass Segmentation using Window-Enhanced Mamba with Frequency-Domain Integration

**arXiv**: [2512.01563v1](https://arxiv.org/abs/2512.01563) | [PDF](https://arxiv.org/pdf/2512.01563.pdf)

**作者**: Thao Thi Phuong Dao, Tan-Cong Nguyen, Nguyen Chi Thanh, Truong Hoang Viet, Trong-Le Do, Mai-Khiem Tran, Minh-Khoi Pham, Trung-Nghia Le, Minh-Triet Tran, Thanh Dinh Le

---

## 💡 一句话要点

**提出MasHeNe数据集与WEMF模型，用于头颈部CT肿块分割，超越仅恶性病变的基准。**

**关键词**: `头颈部肿块分割` `CT图像分割` `Mamba模型` `多频注意力` `三窗增强` `医学影像数据集`

## 📋 核心要点

1. 核心问题：现有公开数据集主要关注恶性病变，忽略头颈部其他占位性病变，缺乏全面基准。
2. 方法要点：WEMF模型采用三窗增强丰富输入外观，并在U形Mamba骨干中通过多频注意力融合跳跃连接信息。
3. 实验或效果：在MasHeNe数据集上，WEMF达到最佳性能，Dice为70.45%，表明该任务仍具挑战性。

## 📄 摘要（原文）

> Head and neck masses are space-occupying lesions that can compress the airway and esophagus and may affect nerves and blood vessels. Available public datasets primarily focus on malignant lesions and often overlook other space-occupying conditions in this region. To address this gap, we introduce MasHeNe, an initial dataset of 3,779 contrast-enhanced CT slices that includes both tumors and cysts with pixel-level annotations. We also establish a benchmark using standard segmentation baselines and report common metrics to enable fair comparison. In addition, we propose the Windowing-Enhanced Mamba with Frequency integration (WEMF) model. WEMF applies tri-window enhancement to enrich the input appearance before feature extraction. It further uses multi-frequency attention to fuse information across skip connections within a U-shaped Mamba backbone. On MasHeNe, WEMF attains the best performance among evaluated methods, with a Dice of 70.45%, IoU of 66.89%, NSD of 72.33%, and HD95 of 5.12 mm. This model indicates stable and strong results on this challenging task. MasHeNe provides a benchmark for head-and-neck mass segmentation beyond malignancy-only datasets. The observed error patterns also suggest that this task remains challenging and requires further research. Our dataset and code are available at https://github.com/drthaodao3101/MasHeNe.git.

