---
layout: default
title: A Critical Study towards the Detection of Parkinsons Disease using ML Technologies
---

# A Critical Study towards the Detection of Parkinsons Disease using ML Technologies

**arXiv**: [2510.24456v1](https://arxiv.org/abs/2510.24456) | [PDF](https://arxiv.org/pdf/2510.24456.pdf)

**作者**: Vivek Chetia, Abdul Taher Khan, Rahish Gogoi, David Kapsian Khual, Purnendu Bikash, Sajal Saha

---

## 💡 一句话要点

**提出基于深度学习的茶叶病害检测方法，用于分类和分割叶片受损区域。**

**关键词**: `茶叶病害检测` `深度学习` `目标检测` `实例分割` `Faster R-CNN` `Mask R-CNN`

## 📋 核心要点

1. 核心问题：检测茶叶病害，包括红锈病、Helopeltis和红蜘蛛螨，并评估受损面积。
2. 方法要点：使用SSD MobileNet V2和Faster R-CNN ResNet50 V1进行目标检测，Mask R-CNN进行实例分割。
3. 实验或效果：Faster R-CNN mAP达25%，优于SSD的20.9%；Mask R-CNN用于计算病害区域。

## 📄 摘要（原文）

> The proposed solution is Deep Learning Technique that will be able classify
> three types of tea leaves diseases from which two diseases are caused by the
> pests and one due to pathogens (infectious organisms) and environmental
> conditions and also show the area damaged by a disease in leaves. Namely Red
> Rust, Helopeltis and Red spider mite respectively. In this paper we have
> evaluated two models namely SSD MobileNet V2 and Faster R-CNN ResNet50 V1 for
> the object detection. The SSD MobileNet V2 gave precision of 0.209 for IOU
> range of 0.50:0.95 with recall of 0.02 on IOU 0.50:0.95 and final mAP of 20.9%.
> While Faster R-CNN ResNet50 V1 has precision of 0.252 on IOU range of 0.50:0.95
> and recall of 0.044 on IOU of 0.50:0.95 with a mAP of 25%, which is better than
> SSD. Also used Mask R-CNN for Object Instance Segmentation where we have
> implemented our custom method to calculate the damaged diseased portion of
> leaves. Keywords: Tea Leaf Disease, Deep Learning, Red Rust, Helopeltis and Red
> Spider Mite, SSD MobileNet V2, Faster R-CNN ResNet50 V1 and Mask RCNN.

