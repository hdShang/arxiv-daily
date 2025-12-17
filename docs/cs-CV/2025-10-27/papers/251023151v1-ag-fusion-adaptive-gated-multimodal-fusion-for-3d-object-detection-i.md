---
layout: default
title: AG-Fusion: adaptive gated multimodal fusion for 3d object detection in complex scenes
---

# AG-Fusion: adaptive gated multimodal fusion for 3d object detection in complex scenes

**arXiv**: [2510.23151v1](https://arxiv.org/abs/2510.23151) | [PDF](https://arxiv.org/pdf/2510.23151.pdf)

**作者**: Sixian Liu, Chen Xu, Qiang Wang, Donghai Shi, Yiwen Li

---

## 💡 一句话要点

**提出自适应门控融合方法以提升复杂场景中3D目标检测的鲁棒性**

**关键词**: `3D目标检测` `多模态融合` `自适应门控` `BEV表示` `鲁棒性` `复杂场景`

## 📋 核心要点

1. 核心问题：现有多模态融合方法在传感器退化或环境干扰场景中性能显著下降
2. 方法要点：在BEV空间使用窗口注意力和跨模态注意力门控融合特征
3. 实验或效果：在KITTI数据集达93.92%精度，E3D数据集比基线提升24.88%

## 📄 摘要（原文）

> Multimodal camera-LiDAR fusion technology has found extensive application in
> 3D object detection, demonstrating encouraging performance. However, existing
> methods exhibit significant performance degradation in challenging scenarios
> characterized by sensor degradation or environmental disturbances. We propose a
> novel Adaptive Gated Fusion (AG-Fusion) approach that selectively integrates
> cross-modal knowledge by identifying reliable patterns for robust detection in
> complex scenes. Specifically, we first project features from each modality into
> a unified BEV space and enhance them using a window-based attention mechanism.
> Subsequently, an adaptive gated fusion module based on cross-modal attention is
> designed to integrate these features into reliable BEV representations robust
> to challenging environments. Furthermore, we construct a new dataset named
> Excavator3D (E3D) focusing on challenging excavator operation scenarios to
> benchmark performance in complex conditions. Our method not only achieves
> competitive performance on the standard KITTI dataset with 93.92% accuracy, but
> also significantly outperforms the baseline by 24.88% on the challenging E3D
> dataset, demonstrating superior robustness to unreliable modal information in
> complex industrial scenes.

