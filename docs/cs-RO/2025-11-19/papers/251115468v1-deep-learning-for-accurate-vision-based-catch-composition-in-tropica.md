---
layout: default
title: Deep Learning for Accurate Vision-based Catch Composition in Tropical Tuna Purse Seiners
---

# Deep Learning for Accurate Vision-based Catch Composition in Tropical Tuna Purse Seiners

**arXiv**: [2511.15468v1](https://arxiv.org/abs/2511.15468) | [PDF](https://arxiv.org/pdf/2511.15468.pdf)

**作者**: Xabier Lekunberri, Ahmad Kamal, Izaro Goienetxea, Jon Ruiz, Iñaki Quincoces, Jaime Valls Miro, Ignacio Arganda-Carreras, Jose A. Fernandes-Salvador

---

## 💡 一句话要点

**提出基于YOLOv9-SAM2与分层分类的视觉管道，以准确估计热带金枪鱼围网渔获物组成。**

**关键词**: `物种识别` `实例分割` `目标跟踪` `分层分类` `电子监控` `渔业管理`

## 📋 核心要点

1. 核心问题：专家区分大眼金枪鱼与黄鳍金枪鱼的一致率低，AI物种识别需平衡性能。
2. 方法要点：比较多种分割方法，YOLOv9-SAM2表现最佳，结合ByteTrack跟踪与分层分类。
3. 实验效果：最佳模型实现84.8%个体分割分类，平均误差4.5%，验证mAP为0.66。

## 📄 摘要（原文）

> Purse seiners play a crucial role in tuna fishing, as approximately 69% of the world's tropical tuna is caught using this gear. All tuna Regional Fisheries Management Organizations have established minimum standards to use electronic monitoring (EM) in fisheries in addition to traditional observers. The EM systems produce a massive amount of video data that human analysts must process. Integrating artificial intelligence (AI) into their workflow can decrease that workload and improve the accuracy of the reports. However, species identification still poses significant challenges for AI, as achieving balanced performance across all species requires appropriate training data. Here, we quantify the difficulty experts face to distinguish bigeye tuna (BET, Thunnus Obesus) from yellowfin tuna (YFT, Thunnus Albacares) using images captured by EM systems. We found inter-expert agreements of 42.9% $\pm$ 35.6% for BET and 57.1% $\pm$ 35.6% for YFT. We then present a multi-stage pipeline to estimate the species composition of the catches using a reliable ground-truth dataset based on identifications made by observers on board. Three segmentation approaches are compared: Mask R-CNN, a combination of DINOv2 with SAM2, and a integration of YOLOv9 with SAM2. We found that the latest performs the best, with a validation mean average precision of 0.66 $\pm$ 0.03 and a recall of 0.88 $\pm$ 0.03. Segmented individuals are tracked using ByteTrack. For classification, we evaluate a standard multiclass classification model and a hierarchical approach, finding a superior generalization by the hierarchical. All our models were cross-validated during training and tested on fishing operations with fully known catch composition. Combining YOLOv9-SAM2 with the hierarchical classification produced the best estimations, with 84.8% of the individuals being segmented and classified with a mean average error of 4.5%.

