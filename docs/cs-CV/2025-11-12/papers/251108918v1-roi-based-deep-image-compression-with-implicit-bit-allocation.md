---
layout: default
title: ROI-based Deep Image Compression with Implicit Bit Allocation
---

# ROI-based Deep Image Compression with Implicit Bit Allocation

**arXiv**: [2511.08918v1](https://arxiv.org/abs/2511.08918) | [PDF](https://arxiv.org/pdf/2511.08918.pdf)

**作者**: Kai Hu, Han Wang, Renhe Liu, Zhilin Li, Shenghui Song, Yu Liu

---

## 💡 一句话要点

**提出基于隐式比特分配的ROI图像压缩方法，以提升编码性能。**

**关键词**: `ROI图像压缩` `隐式比特分配` `Mask-Guided Feature Enhancement` `率失真性能` `双解码器` `特征增强`

## 📋 核心要点

1. 现有ROI压缩方法使用显式比特分配，影响熵模型统计分布，限制性能。
2. 引入Mask-Guided Feature Enhancement模块，实现隐式比特分配和特征增强。
3. 在COCO2017数据集上，方法在率失真性能上优于显式分配，背景质量保持良好。

## 📄 摘要（原文）

> Region of Interest (ROI)-based image compression has rapidly developed due to its ability to maintain high fidelity in important regions while reducing data redundancy. However, existing compression methods primarily apply masks to suppress background information before quantization. This explicit bit allocation strategy, which uses hard gating, significantly impacts the statistical distribution of the entropy model, thereby limiting the coding performance of the compression model. In response, this work proposes an efficient ROI-based deep image compression model with implicit bit allocation. To better utilize ROI masks for implicit bit allocation, this paper proposes a novel Mask-Guided Feature Enhancement (MGFE) module, comprising a Region-Adaptive Attention (RAA) block and a Frequency-Spatial Collaborative Attention (FSCA) block. This module allows for flexible bit allocation across different regions while enhancing global and local features through frequencyspatial domain collaboration. Additionally, we use dual decoders to separately reconstruct foreground and background images, enabling the coding network to optimally balance foreground enhancement and background quality preservation in a datadriven manner. To the best of our knowledge, this is the first work to utilize implicit bit allocation for high-quality regionadaptive coding. Experiments on the COCO2017 dataset show that our implicit-based image compression method significantly outperforms explicit bit allocation approaches in rate-distortion performance, achieving optimal results while maintaining satisfactory visual quality in the reconstructed background regions.

