---
layout: default
title: SWiT-4D: Sliding-Window Transformer for Lossless and Parameter-Free Temporal 4D Generation
---

# SWiT-4D: Sliding-Window Transformer for Lossless and Parameter-Free Temporal 4D Generation

**arXiv**: [2512.10860v1](https://arxiv.org/abs/2512.10860) | [PDF](https://arxiv.org/pdf/2512.10860.pdf)

**作者**: Kehong Gong, Zhengyu Wen, Mingxi Xu, Weixia He, Qi Wang, Ning Zhang, Zhengyu Li, Chenbin Li, Dongze Lian, Wei Zhao, Xiaoyu He, Mingyuan Zhang

---

## 💡 一句话要点

**提出SWiT-4D滑动窗口Transformer，实现无损失、无参数的单目视频到4D网格生成**

**关键词**: `4D内容生成` `单目视频重建` `扩散Transformer` `时空建模` `无参数微调` `轨迹优化`

## 📋 核心要点

1. 核心问题：单目视频转高质量4D网格困难，缺乏大规模4D数据集限制数据驱动训练
2. 方法要点：基于扩散Transformer图像到3D生成器，添加时空建模，支持任意长度视频，引入轨迹模块恢复全局平移
3. 实验或效果：仅需单个短视频微调，在几何保真度和时间一致性上优于基线，验证数据效率

## 📄 摘要（原文）

> Despite significant progress in 4D content generation, the conversion of monocular videos into high-quality animated 3D assets with explicit 4D meshes remains considerably challenging. The scarcity of large-scale, naturally captured 4D mesh datasets further limits the ability to train generalizable video-to-4D models from scratch in a purely data-driven manner. Meanwhile, advances in image-to-3D generation, supported by extensive datasets, offer powerful prior models that can be leveraged. To better utilize these priors while minimizing reliance on 4D supervision, we introduce SWiT-4D, a Sliding-Window Transformer for lossless, parameter-free temporal 4D mesh generation. SWiT-4D integrates seamlessly with any Diffusion Transformer (DiT)-based image-to-3D generator, adding spatial-temporal modeling across video frames while preserving the original single-image forward process, enabling 4D mesh reconstruction from videos of arbitrary length. To recover global translation, we further introduce an optimization-based trajectory module tailored for static-camera monocular videos. SWiT-4D demonstrates strong data efficiency: with only a single short (<10s) video for fine-tuning, it achieves high-fidelity geometry and stable temporal consistency, indicating practical deployability under extremely limited 4D supervision. Comprehensive experiments on both in-domain zoo-test sets and challenging out-of-domain benchmarks (C4D, Objaverse, and in-the-wild videos) show that SWiT-4D consistently outperforms existing baselines in temporal smoothness. Project page: https://animotionlab.github.io/SWIT4D/

