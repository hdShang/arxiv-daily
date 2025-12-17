---
layout: default
title: Neural B-frame Video Compression with Bi-directional Reference Harmonization
---

# Neural B-frame Video Compression with Bi-directional Reference Harmonization

**arXiv**: [2511.08938v1](https://arxiv.org/abs/2511.08938) | [PDF](https://arxiv.org/pdf/2511.08938.pdf)

**作者**: Yuxi Liu, Dengchao Jin, Shuai Huo, Jiawen Gu, Chao Zhou, Huihui Bai, Ming Lu, Zhan Ma

---

## 💡 一句话要点

**提出BRHVC方法以解决B帧压缩中双向参考不平衡问题**

**关键词**: `神经视频压缩` `B帧压缩` `双向参考` `运动补偿` `上下文融合` `HEVC数据集`

## 📋 核心要点

1. B帧压缩中双向参考帧贡献不平衡，影响压缩性能
2. 引入BMC和BCF模块，优化运动压缩和上下文融合
3. 实验显示BRHVC优于现有方法，在HEVC数据集上超越VTM-RA

## 📄 摘要（原文）

> Neural video compression (NVC) has made significant progress in recent years, while neural B-frame video compression (NBVC) remains underexplored compared to P-frame compression. NBVC can adopt bi-directional reference frames for better compression performance. However, NBVC's hierarchical coding may complicate continuous temporal prediction, especially at some hierarchical levels with a large frame span, which could cause the contribution of the two reference frames to be unbalanced. To optimize reference information utilization, we propose a novel NBVC method, termed Bi-directional Reference Harmonization Video Compression (BRHVC), with the proposed Bi-directional Motion Converge (BMC) and Bi-directional Contextual Fusion (BCF). BMC converges multiple optical flows in motion compression, leading to more accurate motion compensation on a larger scale. Then BCF explicitly models the weights of reference contexts under the guidance of motion compensation accuracy. With more efficient motions and contexts, BRHVC can effectively harmonize bi-directional references. Experimental results indicate that our BRHVC outperforms previous state-of-the-art NVC methods, even surpassing the traditional coding, VTM-RA (under random access configuration), on the HEVC datasets. The source code is released at https://github.com/kwai/NVC.

