---
layout: default
title: MRASfM: Multi-Camera Reconstruction and Aggregation through Structure-from-Motion in Driving Scenes
---

# MRASfM: Multi-Camera Reconstruction and Aggregation through Structure-from-Motion in Driving Scenes

**arXiv**: [2510.15467v1](https://arxiv.org/abs/2510.15467) | [PDF](https://arxiv.org/pdf/2510.15467.pdf)

**作者**: Lingfeng Xuan, Chang Nie, Yiqing Xu, Zhe Liu, Yanzi Miao, Hesheng Wang

---

## 💡 一句话要点

**提出MRASfM框架以解决驾驶场景中多相机SfM的可靠性、精度和效率问题**

**关键词**: `多相机重建` `结构从运动` `驾驶场景` `捆绑调整` `路面重建` `姿态估计`

## 📋 核心要点

1. 核心问题：多相机系统在驾驶场景中SfM应用存在姿态估计不可靠、路面重建异常点多和效率低
2. 方法要点：利用固定相机关系增强姿态估计，平面模型去除路面错误点，捆绑调整优化效率
3. 实验或效果：在nuScenes数据集上实现0.124绝对姿态误差，验证泛化性和鲁棒性

## 📄 摘要（原文）

> Structure from Motion (SfM) estimates camera poses and reconstructs point
> clouds, forming a foundation for various tasks. However, applying SfM to
> driving scenes captured by multi-camera systems presents significant
> difficulties, including unreliable pose estimation, excessive outliers in road
> surface reconstruction, and low reconstruction efficiency. To address these
> limitations, we propose a Multi-camera Reconstruction and Aggregation
> Structure-from-Motion (MRASfM) framework specifically designed for driving
> scenes. MRASfM enhances the reliability of camera pose estimation by leveraging
> the fixed spatial relationships within the multi-camera system during the
> registration process. To improve the quality of road surface reconstruction,
> our framework employs a plane model to effectively remove erroneous points from
> the triangulated road surface. Moreover, treating the multi-camera set as a
> single unit in Bundle Adjustment (BA) helps reduce optimization variables to
> boost efficiency. In addition, MRASfM achieves multi-scene aggregation through
> scene association and assembly modules in a coarse-to-fine fashion. We deployed
> multi-camera systems on actual vehicles to validate the generalizability of
> MRASfM across various scenes and its robustness in challenging conditions
> through real-world applications. Furthermore, large-scale validation results on
> public datasets show the state-of-the-art performance of MRASfM, achieving
> 0.124 absolute pose error on the nuScenes dataset.

