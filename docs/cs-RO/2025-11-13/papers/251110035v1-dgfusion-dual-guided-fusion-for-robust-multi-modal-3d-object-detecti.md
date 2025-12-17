---
layout: default
title: DGFusion: Dual-guided Fusion for Robust Multi-Modal 3D Object Detection
---

# DGFusion: Dual-guided Fusion for Robust Multi-Modal 3D Object Detection

**arXiv**: [2511.10035v1](https://arxiv.org/abs/2511.10035) | [PDF](https://arxiv.org/pdf/2511.10035.pdf)

**作者**: Feiyang Jia, Caiyan Jia, Ailin Liu, Shaoqing Xu, Qiming Xia, Lin Liu, Lei Yang, Yan Gong, Ziying Song

---

## 💡 一句话要点

**提出DGFusion双引导融合方法以解决自动驾驶中多模态3D目标检测对困难实例的挑战**

**关键词**: `多模态3D目标检测` `双引导融合` `难度感知匹配` `自动驾驶感知` `困难实例检测` `特征融合`

## 📋 核心要点

1. 核心问题：现有多模态3D检测方法采用单引导范式，难以处理远距离、小尺寸或遮挡对象。
2. 方法要点：引入双引导范式，结合点云引导图像和图像引导点云，通过难度感知实例匹配实现特征融合。
3. 实验效果：在nuScenes数据集上，mAP、NDS和平均召回率分别提升1.0%、0.8%和1.3%。

## 📄 摘要（原文）

> As a critical task in autonomous driving perception systems, 3D object detection is used to identify and track key objects, such as vehicles and pedestrians. However, detecting distant, small, or occluded objects (hard instances) remains a challenge, which directly compromises the safety of autonomous driving systems. We observe that existing multi-modal 3D object detection methods often follow a single-guided paradigm, failing to account for the differences in information density of hard instances between modalities. In this work, we propose DGFusion, based on the Dual-guided paradigm, which fully inherits the advantages of the Point-guide-Image paradigm and integrates the Image-guide-Point paradigm to address the limitations of the single paradigms. The core of DGFusion, the Difficulty-aware Instance Pair Matcher (DIPM), performs instance-level feature matching based on difficulty to generate easy and hard instance pairs, while the Dual-guided Modules exploit the advantages of both pair types to enable effective multi-modal feature fusion. Experimental results demonstrate that our DGFusion outperforms the baseline methods, with respective improvements of +1.0\% mAP, +0.8\% NDS, and +1.3\% average recall on nuScenes. Extensive experiments demonstrate consistent robustness gains for hard instance detection across ego-distance, size, visibility, and small-scale training scenarios.

