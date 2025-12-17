---
layout: default
title: From Orbit to Ground: Generative City Photogrammetry from Extreme Off-Nadir Satellite Images
---

# From Orbit to Ground: Generative City Photogrammetry from Extreme Off-Nadir Satellite Images

**arXiv**: [2512.07527v1](https://arxiv.org/abs/2512.07527) | [PDF](https://arxiv.org/pdf/2512.07527.pdf)

**作者**: Fei Yu, Yu Liu, Luyang Tang, Mingchao Sun, Zengye Ge, Rui Bu, Yuchao Jin, Haisen Zhao, He Sun, Yangyan Li, Mu Xu, Wenzheng Chen, Baoquan Chen

---

## 💡 一句话要点

**提出基于2.5D高度图和生成纹理恢复的方法，以解决从极端离天底卫星图像合成地面级城市视图的挑战。**

**关键词**: `城市3D重建` `卫星图像处理` `生成纹理恢复` `2.5D高度图` `可微分渲染`

## 📋 核心要点

1. 核心问题：从稀疏、视角极端的卫星图像进行城市尺度3D重建，需推断近90度视角差距，导致现有方法如NeRF和3DGS失效。
2. 方法要点：建模城市几何为2.5D高度图，使用Z单调符号距离场稳定优化；通过可微分渲染和生成网络恢复高频率纹理细节。
3. 实验或效果：在大规模城市重建实验中，从少量卫星图像重建4平方公里区域，合成逼真地面视图，性能达到先进水平。

## 📄 摘要（原文）

> City-scale 3D reconstruction from satellite imagery presents the challenge of extreme viewpoint extrapolation, where our goal is to synthesize ground-level novel views from sparse orbital images with minimal parallax. This requires inferring nearly $90^\circ$ viewpoint gaps from image sources with severely foreshortened facades and flawed textures, causing state-of-the-art reconstruction engines such as NeRF and 3DGS to fail.
>   To address this problem, we propose two design choices tailored for city structures and satellite inputs. First, we model city geometry as a 2.5D height map, implemented as a Z-monotonic signed distance field (SDF) that matches urban building layouts from top-down viewpoints. This stabilizes geometry optimization under sparse, off-nadir satellite views and yields a watertight mesh with crisp roofs and clean, vertically extruded facades. Second, we paint the mesh appearance from satellite images via differentiable rendering techniques. While the satellite inputs may contain long-range, blurry captures, we further train a generative texture restoration network to enhance the appearance, recovering high-frequency, plausible texture details from degraded inputs.
>   Our method's scalability and robustness are demonstrated through extensive experiments on large-scale urban reconstruction. For example, in our teaser figure, we reconstruct a $4\,\mathrm{km}^2$ real-world region from only a few satellite images, achieving state-of-the-art performance in synthesizing photorealistic ground views. The resulting models are not only visually compelling but also serve as high-fidelity, application-ready assets for downstream tasks like urban planning and simulation.

