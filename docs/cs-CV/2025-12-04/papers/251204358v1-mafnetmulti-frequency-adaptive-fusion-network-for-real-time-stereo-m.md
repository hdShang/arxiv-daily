---
layout: default
title: MAFNet:Multi-frequency Adaptive Fusion Network for Real-time Stereo Matching
---

# MAFNet:Multi-frequency Adaptive Fusion Network for Real-time Stereo Matching

**arXiv**: [2512.04358v1](https://arxiv.org/abs/2512.04358) | [PDF](https://arxiv.org/pdf/2512.04358.pdf)

**作者**: Ao Xu, Rujin Zhao, Xiong Xu, Boceng Huang, Yujia Jia, Hongfeng Long, Fuxuan Chen, Zilong Cao, Fangyuan Chen

---

## 💡 一句话要点

**提出MAFNet多频自适应融合网络，以高效2D卷积实现实时立体匹配，平衡精度与速度。**

**关键词**: `立体匹配` `实时计算` `频域滤波` `注意力机制` `2D卷积` `移动设备部署`

## 📋 核心要点

1. 现有立体匹配网络在移动设备上实时性差，因3D卷积计算开销大或迭代优化缺乏非局部上下文建模。
2. MAFNet设计自适应频域滤波注意力模块，分解成本体积为高低频部分，并基于Linformer低秩注意力融合信息。
3. 在Scene Flow和KITTI 2015数据集上，MAFNet优于现有实时方法，展现精度与实时性能的良好平衡。

## 📄 摘要（原文）

> Existing stereo matching networks typically rely on either cost-volume construction based on 3D convolutions or deformation methods based on iterative optimization. The former incurs significant computational overhead during cost aggregation, whereas the latter often lacks the ability to model non-local contextual information. These methods exhibit poor compatibility on resource-constrained mobile devices, limiting their deployment in real-time applications. To address this, we propose a Multi-frequency Adaptive Fusion Network (MAFNet), which can produce high-quality disparity maps using only efficient 2D convolutions. Specifically, we design an adaptive frequency-domain filtering attention module that decomposes the full cost volume into high-frequency and low-frequency volumes, performing frequency-aware feature aggregation separately. Subsequently, we introduce a Linformer-based low-rank attention mechanism to adaptively fuse high- and low-frequency information, yielding more robust disparity estimation. Extensive experiments demonstrate that the proposed MAFNet significantly outperforms existing real-time methods on public datasets such as Scene Flow and KITTI 2015, showing a favorable balance between accuracy and real-time performance.

