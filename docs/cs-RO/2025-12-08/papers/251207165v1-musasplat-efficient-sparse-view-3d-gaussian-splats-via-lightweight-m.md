---
layout: default
title: MuSASplat: Efficient Sparse-View 3D Gaussian Splats via Lightweight Multi-Scale Adaptation
---

# MuSASplat: Efficient Sparse-View 3D Gaussian Splats via Lightweight Multi-Scale Adaptation

**arXiv**: [2512.07165v1](https://arxiv.org/abs/2512.07165) | [PDF](https://arxiv.org/pdf/2512.07165.pdf)

**作者**: Muyu Xu, Fangneng Zhan, Xiaoqin Zhang, Ling Shao, Shijian Lu

---

## 💡 一句话要点

**提出MuSASplat框架，通过轻量级多尺度适配器高效训练稀疏视图3D高斯溅射模型。**

**关键词**: `稀疏视图3D重建` `3D高斯溅射` `轻量级微调` `多尺度适配器` `特征融合聚合器`

## 📋 核心要点

1. 稀疏视图3D高斯溅射训练计算成本高，现有方法依赖大模型全微调。
2. 引入轻量级多尺度适配器，仅微调少量参数，降低GPU开销。
3. 实验表明，在保持渲染质量的同时，显著减少参数和训练资源需求。

## 📄 摘要（原文）

> Sparse-view 3D Gaussian splatting seeks to render high-quality novel views of 3D scenes from a limited set of input images. While recent pose-free feed-forward methods leveraging pre-trained 3D priors have achieved impressive results, most of them rely on full fine-tuning of large Vision Transformer (ViT) backbones and incur substantial GPU costs. In this work, we introduce MuSASplat, a novel framework that dramatically reduces the computational burden of training pose-free feed-forward 3D Gaussian splats models with little compromise of rendering quality. Central to our approach is a lightweight Multi-Scale Adapter that enables efficient fine-tuning of ViT-based architectures with only a small fraction of training parameters. This design avoids the prohibitive GPU overhead associated with previous full-model adaptation techniques while maintaining high fidelity in novel view synthesis, even with very sparse input views. In addition, we introduce a Feature Fusion Aggregator that integrates features across input views effectively and efficiently. Unlike widely adopted memory banks, the Feature Fusion Aggregator ensures consistent geometric integration across input views and meanwhile mitigates the memory usage, training complexity, and computational costs significantly. Extensive experiments across diverse datasets show that MuSASplat achieves state-of-the-art rendering quality but has significantly reduced parameters and training resource requirements as compared with existing methods.

