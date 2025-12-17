---
layout: default
title: Venus: An Efficient Edge Memory-and-Retrieval System for VLM-based Online Video Understanding
---

# Venus: An Efficient Edge Memory-and-Retrieval System for VLM-based Online Video Understanding

**arXiv**: [2512.07344v1](https://arxiv.org/abs/2512.07344) | [PDF](https://arxiv.org/pdf/2512.07344.pdf)

**作者**: Shengyuan Ye, Bei Ouyang, Tianyi Qian, Liekang Zeng, Mu Yuan, Xiaowen Chu, Weijie Hong, Xu Chen

---

## 💡 一句话要点

**提出Venus边缘内存检索系统，以解决VLM在线视频理解中的部署开销问题。**

**关键词**: `在线视频理解` `边缘计算` `内存检索系统` `视觉语言模型` `渐进采样`

## 📋 核心要点

1. 核心问题：VLM在线视频理解部署时系统开销大，忽略实际约束。
2. 方法要点：采用边缘-云分离架构，通过场景分割、聚类和渐进采样实现高效内存构建与检索。
3. 实验或效果：相比现有方法，总响应延迟加速15-131倍，保持或提升推理精度。

## 📄 摘要（原文）

> Vision-language models (VLMs) have demonstrated impressive multimodal comprehension capabilities and are being deployed in an increasing number of online video understanding applications. While recent efforts extensively explore advancing VLMs' reasoning power in these cases, deployment constraints are overlooked, leading to overwhelming system overhead in real-world deployments. To address that, we propose Venus, an on-device memory-and-retrieval system for efficient online video understanding. Venus proposes an edge-cloud disaggregated architecture that sinks memory construction and keyframe retrieval from cloud to edge, operating in two stages. In the ingestion stage, Venus continuously processes streaming edge videos via scene segmentation and clustering, where the selected keyframes are embedded with a multimodal embedding model to build a hierarchical memory for efficient storage and retrieval. In the querying stage, Venus indexes incoming queries from memory, and employs a threshold-based progressive sampling algorithm for keyframe selection that enhances diversity and adaptively balances system cost and reasoning accuracy. Our extensive evaluation shows that Venus achieves a 15x-131x speedup in total response latency compared to state-of-the-art methods, enabling real-time responses within seconds while maintaining comparable or even superior reasoning accuracy.

