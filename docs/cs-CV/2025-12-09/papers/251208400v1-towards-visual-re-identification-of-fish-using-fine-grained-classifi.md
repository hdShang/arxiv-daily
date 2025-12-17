---
layout: default
title: Towards Visual Re-Identification of Fish using Fine-Grained Classification for Electronic Monitoring in Fisheries
---

# Towards Visual Re-Identification of Fish using Fine-Grained Classification for Electronic Monitoring in Fisheries

**arXiv**: [2512.08400v1](https://arxiv.org/abs/2512.08400) | [PDF](https://arxiv.org/pdf/2512.08400.pdf)

**作者**: Samitha Nuwan Thilakarathna, Ercan Avsar, Martin Mathias Nielsen, Malte Pedersen

---

## 💡 一句话要点

**提出基于细粒度分类的深度学习流水线，用于渔业电子监控中的鱼类重识别。**

**关键词**: `鱼类重识别` `细粒度分类` `电子监控` `深度学习流水线` `视觉Transformer`

## 📋 核心要点

1. 核心问题：渔业电子监控视频数据量大，手动审核不可行，需自动化鱼类重识别。
2. 方法要点：使用硬三元组挖掘和自定义图像变换流水线，优化Swin-T架构以提升性能。
3. 实验或效果：Swin-T优于ResNet-50，最高mAP@k达41.65%，Rank-1准确率90.43%。

## 📄 摘要（原文）

> Accurate fisheries data are crucial for effective and sustainable marine resource management. With the recent adoption of Electronic Monitoring (EM) systems, more video data is now being collected than can be feasibly reviewed manually. This paper addresses this challenge by developing an optimized deep learning pipeline for automated fish re-identification (Re-ID) using the novel AutoFish dataset, which simulates EM systems with conveyor belts with six similarly looking fish species. We demonstrate that key Re-ID metrics (R1 and mAP@k) are substantially improved by using hard triplet mining in conjunction with a custom image transformation pipeline that includes dataset-specific normalization. By employing these strategies, we demonstrate that the Vision Transformer-based Swin-T architecture consistently outperforms the Convolutional Neural Network-based ResNet-50, achieving peak performance of 41.65% mAP@k and 90.43% Rank-1 accuracy. An in-depth analysis reveals that the primary challenge is distinguishing visually similar individuals of the same species (Intra-species errors), where viewpoint inconsistency proves significantly more detrimental than partial occlusion. The source code and documentation are available at: https://github.com/msamdk/Fish_Re_Identification.git

