---
layout: default
title: You Only Train Once (YOTO): A Retraining-Free Object Detection Framework
---

# You Only Train Once (YOTO): A Retraining-Free Object Detection Framework

**arXiv**: [2512.04888v1](https://arxiv.org/abs/2512.04888) | [PDF](https://arxiv.org/pdf/2512.04888.pdf)

**作者**: Priyanto Hidayatullah, Nurjannah Syakrani, Yudi Widhiyasana, Muhammad Rizqi Sholahuddin, Refdinal Tubagus, Zahri Al Adzani Hidayat, Hanri Fajar Ramadhan, Dafa Alfarizki Pratama, Farhan Muhammad Yasin

---

## 💡 一句话要点

**提出YOTO框架以解决零售场景中目标检测的灾难性遗忘问题，无需重训练即可添加新产品。**

**关键词**: `目标检测` `灾难性遗忘` `零售应用` `边缘计算` `向量数据库` `度量学习`

## 📋 核心要点

1. 核心问题：目标检测面临灾难性遗忘，添加新产品需重训练全部数据，增加成本和时间。
2. 方法要点：结合YOLO11n定位、DeIT特征提取和代理锚点损失，通过余弦相似度在向量数据库中分类。
3. 实验或效果：在140产品零售案例中，准确率良好，训练效率提升近3倍，推理时间580ms/图像于边缘设备。

## 📄 摘要（原文）

> Object detection constitutes the primary task within the domain of computer vision. It is utilized in numerous domains. Nonetheless, object detection continues to encounter the issue of catastrophic forgetting. The model must be retrained whenever new products are introduced, utilizing not only the new products dataset but also the entirety of the previous dataset. The outcome is obvious: increasing model training expenses and significant time consumption. In numerous sectors, particularly retail checkout, the frequent introduction of new products presents a great challenge. This study introduces You Only Train Once (YOTO), a methodology designed to address the issue of catastrophic forgetting by integrating YOLO11n for object localization with DeIT and Proxy Anchor Loss for feature extraction and metric learning. For classification, we utilize cosine similarity between the embedding features of the target product and those in the Qdrant vector database. In a case study conducted in a retail store with 140 products, the experimental results demonstrate that our proposed framework achieves encouraging accuracy, whether for detecting new or existing products. Furthermore, without retraining, the training duration difference is significant. We achieve almost 3 times the training time efficiency compared to classical object detection approaches. This efficiency escalates as additional new products are added to the product database. The average inference time is 580 ms per image containing multiple products, on an edge device, validating the proposed framework's feasibility for practical use.

