---
layout: default
title: Improving Cross-view Object Geo-localization: A Dual Attention Approach with Cross-view Interaction and Multi-Scale Spatial Features
---

# Improving Cross-view Object Geo-localization: A Dual Attention Approach with Cross-view Interaction and Multi-Scale Spatial Features

**arXiv**: [2510.27139v1](https://arxiv.org/abs/2510.27139) | [PDF](https://arxiv.org/pdf/2510.27139.pdf)

**作者**: Xingtao Ling Yingying Zhu

---

## 💡 一句话要点

**提出双注意力方法以改进跨视角物体地理定位，提升定位精度。**

**关键词**: `跨视角物体地理定位` `注意力机制` `多尺度空间特征` `数据集构建` `无人机定位`

## 📋 核心要点

1. 现有方法在跨视角信息传递和空间特征优化方面不足，导致模型关注无关噪声。
2. 引入跨视角交叉注意力模块和多头空间注意力模块，增强特征表示和抑制噪声。
3. 在CVOGL和G2D数据集上实验，定位精度超越当前最优方法。

## 📄 摘要（原文）

> Cross-view object geo-localization has recently gained attention due to
> potential applications. Existing methods aim to capture spatial dependencies of
> query objects between different views through attention mechanisms to obtain
> spatial relationship feature maps, which are then used to predict object
> locations. Although promising, these approaches fail to effectively transfer
> information between views and do not further refine the spatial relationship
> feature maps. This results in the model erroneously focusing on irrelevant edge
> noise, thereby affecting localization performance. To address these
> limitations, we introduce a Cross-view and Cross-attention Module (CVCAM),
> which performs multiple iterations of interaction between the two views,
> enabling continuous exchange and learning of contextual information about the
> query object from both perspectives. This facilitates a deeper understanding of
> cross-view relationships while suppressing the edge noise unrelated to the
> query object. Furthermore, we integrate a Multi-head Spatial Attention Module
> (MHSAM), which employs convolutional kernels of various sizes to extract
> multi-scale spatial features from the feature maps containing implicit
> correspondences, further enhancing the feature representation of the query
> object. Additionally, given the scarcity of datasets for cross-view object
> geo-localization, we created a new dataset called G2D for the "Ground-to-Drone"
> localization task, enriching existing datasets and filling the gap in
> "Ground-to-Drone" localization task. Extensive experiments on the CVOGL and G2D
> datasets demonstrate that our proposed method achieves high localization
> accuracy, surpassing the current state-of-the-art.

