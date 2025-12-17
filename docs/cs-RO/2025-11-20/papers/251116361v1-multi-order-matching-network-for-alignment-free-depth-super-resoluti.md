---
layout: default
title: Multi-Order Matching Network for Alignment-Free Depth Super-Resolution
---

# Multi-Order Matching Network for Alignment-Free Depth Super-Resolution

**arXiv**: [2511.16361v1](https://arxiv.org/abs/2511.16361) | [PDF](https://arxiv.org/pdf/2511.16361.pdf)

**作者**: Zhengxue Wang, Zhiqiang Yan, Yuan Wu, Guangwei Gao, Xiang Li, Jian Yang

---

## 💡 一句话要点

**提出多阶匹配网络以解决未对齐RGB-D场景的深度超分辨率问题**

**关键词**: `深度超分辨率` `多阶匹配` `对齐自由` `RGB-D融合` `特征检索` `鲁棒性`

## 📋 核心要点

1. 核心问题：真实场景中RGB与深度图未严格对齐，导致现有方法性能下降
2. 方法要点：通过多阶匹配机制自适应检索和选择RGB信息，结合多阶聚合进行特征融合
3. 实验或效果：在广泛实验中实现先进性能，并表现出优异的鲁棒性

## 📄 摘要（原文）

> Recent guided depth super-resolution methods are premised on the assumption of strictly spatial alignment between depth and RGB, achieving high-quality depth reconstruction. However, in real-world scenarios, the acquisition of strictly aligned RGB-D is hindered by inherent hardware limitations (e.g., physically separate RGB-D sensors) and unavoidable calibration drift induced by mechanical vibrations or temperature variations. Consequently, existing approaches often suffer inevitable performance degradation when applied to misaligned real-world scenes. In this paper, we propose the Multi-Order Matching Network (MOMNet), a novel alignment-free framework that adaptively retrieves and selects the most relevant information from misaligned RGB. Specifically, our method begins with a multi-order matching mechanism, which jointly performs zero-order, first-order, and second-order matching to comprehensively identify RGB information consistent with depth across multi-order feature spaces. To effectively integrate the retrieved RGB and depth, we further introduce a multi-order aggregation composed of multiple structure detectors. This strategy uses multi-order priors as prompts to facilitate the selective feature transfer from RGB to depth. Extensive experiments demonstrate that MOMNet achieves state-of-the-art performance and exhibits outstanding robustness.

