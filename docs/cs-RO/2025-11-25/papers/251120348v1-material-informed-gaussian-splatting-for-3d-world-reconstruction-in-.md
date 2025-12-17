---
layout: default
title: Material-informed Gaussian Splatting for 3D World Reconstruction in a Digital Twin
---

# Material-informed Gaussian Splatting for 3D World Reconstruction in a Digital Twin

**arXiv**: [2511.20348v1](https://arxiv.org/abs/2511.20348) | [PDF](https://arxiv.org/pdf/2511.20348.pdf)

**作者**: João Malheiro Silva, Andy Huynh, Tong Duy Son, Holger Caesar

---

## 💡 一句话要点

**提出基于相机和材料感知的高斯溅射方法，用于数字孪生中的3D重建与传感器模拟**

**关键词**: `3D重建` `高斯溅射` `数字孪生` `材料感知` `传感器模拟` `多视图图像`

## 📋 核心要点

1. 核心问题：LiDAR方法几何准确但缺乏语义和纹理，融合方法复杂且对玻璃等材料处理不佳
2. 方法要点：使用多视图图像进行3D高斯溅射重建，提取语义材料掩码并转换为带标签的网格
3. 实验或效果：在内部数据集验证，利用LiDAR作为反射率真值，传感器模拟保真度与融合方法相当

## 📄 摘要（原文）

> 3D reconstruction for Digital Twins often relies on LiDAR-based methods, which provide accurate geometry but lack the semantics and textures naturally captured by cameras. Traditional LiDAR-camera fusion approaches require complex calibration and still struggle with certain materials like glass, which are visible in images but poorly represented in point clouds. We propose a camera-only pipeline that reconstructs scenes using 3D Gaussian Splatting from multi-view images, extracts semantic material masks via vision models, converts Gaussian representations to mesh surfaces with projected material labels, and assigns physics-based material properties for accurate sensor simulation in modern graphics engines and simulators. This approach combines photorealistic reconstruction with physics-based material assignment, providing sensor simulation fidelity comparable to LiDAR-camera fusion while eliminating hardware complexity and calibration requirements. We validate our camera-only method using an internal dataset from an instrumented test vehicle, leveraging LiDAR as ground truth for reflectivity validation alongside image similarity metrics.

