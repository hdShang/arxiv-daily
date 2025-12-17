---
layout: default
title: Parameter-Free Neural Lens Blur Rendering for High-Fidelity Composites
---

# Parameter-Free Neural Lens Blur Rendering for High-Fidelity Composites

**arXiv**: [2511.17014v1](https://arxiv.org/abs/2511.17014) | [PDF](https://arxiv.org/pdf/2511.17014.pdf)

**作者**: Lingyan Ruan, Bin Chen, Taehyun Rhee

---

## 💡 一句话要点

**提出参数自由神经镜头模糊渲染方法，用于高保真混合现实合成**

**关键词**: `镜头模糊渲染` `混合现实合成` `弥散圆估计` `神经重模糊网络` `参数自由方法`

## 📋 核心要点

1. 核心问题：混合现实中虚拟对象与真实场景融合时，镜头模糊不一致影响视觉保真度，且传统方法依赖相机参数和场景深度，普通用户难以获取。
2. 方法要点：直接从RGB图像估计弥散圆图，通过线性关系推断虚拟对象模糊，使用神经重模糊网络渲染真实镜头模糊。
3. 实验或效果：实验显示方法在定性和定量评估中优于现有技术，实现高保真合成与真实散焦效果。

## 📄 摘要（原文）

> Consistent and natural camera lens blur is important for seamlessly blending 3D virtual objects into photographed real-scenes. Since lens blur typically varies with scene depth, the placement of virtual objects and their corresponding blur levels significantly affect the visual fidelity of mixed reality compositions. Existing pipelines often rely on camera parameters (e.g., focal length, focus distance, aperture size) and scene depth to compute the circle of confusion (CoC) for realistic lens blur rendering. However, such information is often unavailable to ordinary users, limiting the accessibility and generalizability of these methods. In this work, we propose a novel compositing approach that directly estimates the CoC map from RGB images, bypassing the need for scene depth or camera metadata. The CoC values for virtual objects are inferred through a linear relationship between its signed CoC map and depth, and realistic lens blur is rendered using a neural reblurring network. Our method provides flexible and practical solution for real-world applications. Experimental results demonstrate that our method achieves high-fidelity compositing with realistic defocus effects, outperforming state-of-the-art techniques in both qualitative and quantitative evaluations.

