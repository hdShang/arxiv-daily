---
layout: default
title: Towards Test-time Efficient Visual Place Recognition via Asymmetric Query Processing
---

# Towards Test-time Efficient Visual Place Recognition via Asymmetric Query Processing

**arXiv**: [2512.13055v1](https://arxiv.org/abs/2512.13055) | [PDF](https://arxiv.org/pdf/2512.13055.pdf)

**作者**: Jaeyoon Kim, Yoonki Cho, Sung-Eui Yoon

---

## 💡 一句话要点

**提出非对称查询处理框架以解决资源受限设备上的视觉地点识别效率问题**

**关键词**: `视觉地点识别` `非对称查询处理` `地理记忆库` `隐式嵌入增强` `资源受限设备` `高效检索`

## 📋 核心要点

1. 核心问题：高容量基础模型在视觉地点识别中计算成本高，难以部署于资源受限设备
2. 方法要点：采用非对称框架，结合离线高容量图库模型和在线轻量查询网络，引入地理记忆库和隐式嵌入增强技术
3. 实验或效果：显著降低计算成本，超越现有非对称检索方法，适用于资源有限环境

## 📄 摘要（原文）

> Visual Place Recognition (VPR) has advanced significantly with high-capacity foundation models like DINOv2, achieving remarkable performance. Nonetheless, their substantial computational cost makes deployment on resource-constrained devices impractical. In this paper, we introduce an efficient asymmetric VPR framework that incorporates a high-capacity gallery model for offline feature extraction with a lightweight query network for online processing. A key challenge in this setting is ensuring compatibility between these heterogeneous networks, which conventional approaches address through computationally expensive k-NN-based compatible training. To overcome this, we propose a geographical memory bank that structures gallery features using geolocation metadata inherent in VPR databases, eliminating the need for exhaustive k-NN computations. Additionally, we introduce an implicit embedding augmentation technique that enhances the query network to model feature variations despite its limited capacity. Extensive experiments demonstrate that our method not only significantly reduces computational costs but also outperforms existing asymmetric retrieval techniques, establishing a new aspect for VPR in resource-limited environments. The code is available at https://github.com/jaeyoon1603/AsymVPR

