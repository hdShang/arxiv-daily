---
layout: default
title: Visibility-Aware Densification for 3D Gaussian Splatting in Dynamic Urban Scenes
---

# Visibility-Aware Densification for 3D Gaussian Splatting in Dynamic Urban Scenes

**arXiv**: [2510.09364v1](https://arxiv.org/abs/2510.09364) | [PDF](https://arxiv.org/pdf/2510.09364.pdf)

**作者**: Yikang Zhang, Rui Fan

---

## 💡 一句话要点

**提出VAD-GS框架以解决动态城市场景中3D高斯溅射的几何恢复问题**

**关键词**: `3D高斯溅射` `几何恢复` `动态城市场景` `多视图立体重建` `可见性推理`

## 📋 核心要点

1. 核心问题：动态城市场景中初始点云覆盖不均导致3D高斯溅射产生失真和伪影
2. 方法要点：通过体素可见性推理、多样性视图选择和补丁匹配多视图立体重建恢复缺失结构
3. 实验或效果：在Waymo和nuScenes数据集上优于现有方法，提升静态和动态对象重建质量

## 📄 摘要（原文）

> 3D Gaussian splatting (3DGS) has demonstrated impressive performance in
> synthesizing high-fidelity novel views. Nonetheless, its effectiveness
> critically depends on the quality of the initialized point cloud. Specifically,
> achieving uniform and complete point coverage over the underlying scene
> structure requires overlapping observation frustums, an assumption that is
> often violated in unbounded, dynamic urban environments. Training Gaussian
> models with partially initialized point clouds often leads to distortions and
> artifacts, as camera rays may fail to intersect valid surfaces, resulting in
> incorrect gradient propagation to Gaussian primitives associated with occluded
> or invisible geometry. Additionally, existing densification strategies simply
> clone and split Gaussian primitives from existing ones, incapable of
> reconstructing missing structures. To address these limitations, we propose
> VAD-GS, a 3DGS framework tailored for geometry recovery in challenging urban
> scenes. Our method identifies unreliable geometry structures via voxel-based
> visibility reasoning, selects informative supporting views through
> diversity-aware view selection, and recovers missing structures via patch
> matching-based multi-view stereo reconstruction. This design enables the
> generation of new Gaussian primitives guided by reliable geometric priors, even
> in regions lacking initial points. Extensive experiments on the Waymo and
> nuScenes datasets demonstrate that VAD-GS outperforms state-of-the-art 3DGS
> approaches and significantly improves the quality of reconstructed geometry for
> both static and dynamic objects. Source code will be released upon publication.

