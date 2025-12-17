---
layout: default
title: LiSTAR: Ray-Centric World Models for 4D LiDAR Sequences in Autonomous Driving
---

# LiSTAR: Ray-Centric World Models for 4D LiDAR Sequences in Autonomous Driving

**arXiv**: [2511.16049v1](https://arxiv.org/abs/2511.16049) | [PDF](https://arxiv.org/pdf/2511.16049.pdf)

**作者**: Pei Liu, Songtao Wang, Lang Zhang, Xingyue Peng, Yuandong Lyu, Jiaxin Deng, Songxin Lu, Weiliang Ma, Xueyang Zhang, Yifei Zhan, XianPeng Lang, Jun Ma

---

## 💡 一句话要点

**提出LiSTAR模型以解决自动驾驶中4D LiDAR数据合成挑战**

**关键词**: `4D LiDAR合成` `生成世界模型` `射线中心变换器` `自动驾驶模拟` `可控生成` `时空注意力`

## 📋 核心要点

1. 核心问题：4D LiDAR数据合成因球形几何、时间稀疏性和动态场景复杂性而困难。
2. 方法要点：采用混合柱面-球面表示和射线中心变换器，提升数据保真度和时间一致性。
3. 实验或效果：在重建、预测和生成任务中表现优异，MMD降低76%，IoU提高32%。

## 📄 摘要（原文）

> Synthesizing high-fidelity and controllable 4D LiDAR data is crucial for creating scalable simulation environments for autonomous driving. This task is inherently challenging due to the sensor's unique spherical geometry, the temporal sparsity of point clouds, and the complexity of dynamic scenes. To address these challenges, we present LiSTAR, a novel generative world model that operates directly on the sensor's native geometry. LiSTAR introduces a Hybrid-Cylindrical-Spherical (HCS) representation to preserve data fidelity by mitigating quantization artifacts common in Cartesian grids. To capture complex dynamics from sparse temporal data, it utilizes a Spatio-Temporal Attention with Ray-Centric Transformer (START) that explicitly models feature evolution along individual sensor rays for robust temporal coherence. Furthermore, for controllable synthesis, we propose a novel 4D point cloud-aligned voxel layout for conditioning and a corresponding discrete Masked Generative START (MaskSTART) framework, which learns a compact, tokenized representation of the scene, enabling efficient, high-resolution, and layout-guided compositional generation. Comprehensive experiments validate LiSTAR's state-of-the-art performance across 4D LiDAR reconstruction, prediction, and conditional generation, with substantial quantitative gains: reducing generation MMD by a massive 76%, improving reconstruction IoU by 32%, and lowering prediction L1 Med by 50%. This level of performance provides a powerful new foundation for creating realistic and controllable autonomous systems simulations. Project link: https://ocean-luna.github.io/LiSTAR.gitub.io.

