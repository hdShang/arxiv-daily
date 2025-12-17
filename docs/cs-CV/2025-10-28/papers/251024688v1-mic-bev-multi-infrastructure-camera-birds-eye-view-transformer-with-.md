---
layout: default
title: MIC-BEV: Multi-Infrastructure Camera Bird's-Eye-View Transformer with Relation-Aware Fusion for 3D Object Detection
---

# MIC-BEV: Multi-Infrastructure Camera Bird's-Eye-View Transformer with Relation-Aware Fusion for 3D Object Detection

**arXiv**: [2510.24688v1](https://arxiv.org/abs/2510.24688) | [PDF](https://arxiv.org/pdf/2510.24688.pdf)

**作者**: Yun Zhang, Zhaoliang Zheng, Johnson Liu, Zhiyu Huang, Zewei Zhou, Zonglin Meng, Tianhui Cai, Jiaqi Ma

---

## 💡 一句话要点

**提出MIC-BEV以解决基础设施多相机3D目标检测中的多视图融合挑战**

**关键词**: `鸟瞰图感知` `多相机融合` `3D目标检测` `基础设施感知` `Transformer模型`

## 📋 核心要点

1. 核心问题：基础设施多相机设置下，现有模型因视图多样、配置异构和视觉退化而性能不足
2. 方法要点：使用Transformer和关系感知融合模块，将多视图特征整合到BEV空间
3. 实验或效果：在合成和真实数据集上实现SOTA性能，并在恶劣条件下保持鲁棒性

## 📄 摘要（原文）

> Infrastructure-based perception plays a crucial role in intelligent
> transportation systems, offering global situational awareness and enabling
> cooperative autonomy. However, existing camera-based detection models often
> underperform in such scenarios due to challenges such as multi-view
> infrastructure setup, diverse camera configurations, degraded visual inputs,
> and various road layouts. We introduce MIC-BEV, a Transformer-based
> bird's-eye-view (BEV) perception framework for infrastructure-based
> multi-camera 3D object detection. MIC-BEV flexibly supports a variable number
> of cameras with heterogeneous intrinsic and extrinsic parameters and
> demonstrates strong robustness under sensor degradation. The proposed
> graph-enhanced fusion module in MIC-BEV integrates multi-view image features
> into the BEV space by exploiting geometric relationships between cameras and
> BEV cells alongside latent visual cues. To support training and evaluation, we
> introduce M2I, a synthetic dataset for infrastructure-based object detection,
> featuring diverse camera configurations, road layouts, and environmental
> conditions. Extensive experiments on both M2I and the real-world dataset
> RoScenes demonstrate that MIC-BEV achieves state-of-the-art performance in 3D
> object detection. It also remains robust under challenging conditions,
> including extreme weather and sensor degradation. These results highlight the
> potential of MIC-BEV for real-world deployment. The dataset and source code are
> available at: https://github.com/HandsomeYun/MIC-BEV.

