---
layout: default
title: VGGTFace: Topologically Consistent Facial Geometry Reconstruction in the Wild
---

# VGGTFace: Topologically Consistent Facial Geometry Reconstruction in the Wild

**arXiv**: [2511.20366v1](https://arxiv.org/abs/2511.20366) | [PDF](https://arxiv.org/pdf/2511.20366.pdf)

**作者**: Xin Ming, Yuxuan Han, Tianyu Huang, Feng Xu

---

## 💡 一句话要点

**提出VGGTFace以从日常多视角图像自动重建拓扑一致的面部几何**

**关键词**: `面部几何重建` `拓扑一致性` `3D基础模型` `多视角图像` `束调整`

## 📋 核心要点

1. 现有方法需手动操作、泛化性差或受限于3D形变模型表达能力
2. 结合VGGT和Pixel3DMM注入拓扑信息，并通过拓扑感知束调整融合点云
3. 在16视图下10秒内高质量重建，基准测试和野外数据泛化表现优异

## 📄 摘要（原文）

> Reconstructing topologically consistent facial geometry is crucial for the digital avatar creation pipelines. Existing methods either require tedious manual efforts, lack generalization to in-the-wild data, or are constrained by the limited expressiveness of 3D Morphable Models. To address these limitations, we propose VGGTFace, an automatic approach that innovatively applies the 3D foundation model, \emph{i.e.} VGGT, for topologically consistent facial geometry reconstruction from in-the-wild multi-view images captured by everyday users. Our key insight is that, by leveraging VGGT, our method naturally inherits strong generalization ability and expressive power from its large-scale training and point map representation. However, it is unclear how to reconstruct a topologically consistent mesh from VGGT, as the topology information is missing in its prediction. To this end, we augment VGGT with Pixel3DMM for injecting topology information via pixel-aligned UV values. In this manner, we convert the pixel-aligned point map of VGGT to a point cloud with topology. Tailored to this point cloud with known topology, we propose a novel Topology-Aware Bundle Adjustment strategy to fuse them, where we construct a Laplacian energy for the Bundle Adjustment objective. Our method achieves high-quality reconstruction in 10 seconds for 16 views on a single NVIDIA RTX 4090. Experiments demonstrate state-of-the-art results on benchmarks and impressive generalization to in-the-wild data. Code is available at https://github.com/grignarder/vggtface.

