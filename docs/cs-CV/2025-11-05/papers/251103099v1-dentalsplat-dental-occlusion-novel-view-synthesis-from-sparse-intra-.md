---
layout: default
title: DentalSplat: Dental Occlusion Novel View Synthesis from Sparse Intra-Oral Photographs
---

# DentalSplat: Dental Occlusion Novel View Synthesis from Sparse Intra-Oral Photographs

**arXiv**: [2511.03099v1](https://arxiv.org/abs/2511.03099) | [PDF](https://arxiv.org/pdf/2511.03099.pdf)

**作者**: Yiyi Miao, Taoyu Wu, Tong Chen, Sihao Li, Ji Jiang, Youpeng Yang, Angelos Stefanidis, Limin Yu, Jionglong Su

---

## 💡 一句话要点

**提出DentalSplat框架，从稀疏口腔照片合成牙齿咬合新视图，以支持远程正畸诊断。**

**关键词**: `3D高斯溅射` `稀疏视图重建` `牙齿咬合可视化` `远程正畸` `光流约束` `点云初始化`

## 📋 核心要点

1. 核心问题：稀疏输入视图和未知相机姿态导致3D重建质量下降，限制正畸远程医疗应用。
2. 方法要点：结合先验引导点云初始化、尺度自适应剪枝和光流几何约束，提升3D高斯溅射效率与渲染保真度。
3. 实验或效果：在950临床案例和195视频测试集上验证，优于现有技术，实现高质量新视图合成。

## 📄 摘要（原文）

> In orthodontic treatment, particularly within telemedicine contexts,
> observing patients' dental occlusion from multiple viewpoints facilitates
> timely clinical decision-making. Recent advances in 3D Gaussian Splatting
> (3DGS) have shown strong potential in 3D reconstruction and novel view
> synthesis. However, conventional 3DGS pipelines typically rely on densely
> captured multi-view inputs and precisely initialized camera poses, limiting
> their practicality. Orthodontic cases, in contrast, often comprise only three
> sparse images, specifically, the anterior view and bilateral buccal views,
> rendering the reconstruction task especially challenging. The extreme sparsity
> of input views severely degrades reconstruction quality, while the absence of
> camera pose information further complicates the process. To overcome these
> limitations, we propose DentalSplat, an effective framework for 3D
> reconstruction from sparse orthodontic imagery. Our method leverages a
> prior-guided dense stereo reconstruction model to initialize the point cloud,
> followed by a scale-adaptive pruning strategy to improve the training
> efficiency and reconstruction quality of 3DGS. In scenarios with extremely
> sparse viewpoints, we further incorporate optical flow as a geometric
> constraint, coupled with gradient regularization, to enhance rendering
> fidelity. We validate our approach on a large-scale dataset comprising 950
> clinical cases and an additional video-based test set of 195 cases designed to
> simulate real-world remote orthodontic imaging conditions. Experimental results
> demonstrate that our method effectively handles sparse input scenarios and
> achieves superior novel view synthesis quality for dental occlusion
> visualization, outperforming state-of-the-art techniques.

