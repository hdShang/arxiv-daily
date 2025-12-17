---
layout: default
title: TUNA: Taming Unified Visual Representations for Native Unified Multimodal Models
---

# TUNA: Taming Unified Visual Representations for Native Unified Multimodal Models

**arXiv**: [2512.02014v1](https://arxiv.org/abs/2512.02014) | [PDF](https://arxiv.org/pdf/2512.02014.pdf)

**作者**: Zhiheng Liu, Weiming Ren, Haozhe Liu, Zijian Zhou, Shoufa Chen, Haonan Qiu, Xiaoke Huang, Zhaochong An, Fanny Yang, Aditya Patel, Viktar Atliha, Tony Ng, Xiao Han, Chuyan Zhu, Chenyang Zhang, Ding Liu, Juan-Manuel Perez-Rua, Sen He, Jürgen Schmidhuber, Wenhu Chen, Ping Luo, Wei Liu, Tao Xiang, Jonas Schult, Yuren Cong

---

## 💡 一句话要点

**提出TUNA以构建统一视觉表示，实现原生统一多模态模型的理解与生成任务。**

**关键词**: `统一多模态模型` `视觉表示学习` `图像生成` `视频理解` `端到端训练`

## 📋 核心要点

1. 核心问题：统一多模态模型存在表示格式不匹配，影响理解与生成性能。
2. 方法要点：通过级联VAE编码器与表示编码器，构建统一连续视觉表示空间。
3. 实验或效果：在图像和视频理解、生成及编辑任务中取得先进结果，验证统一表示的有效性。

## 📄 摘要（原文）

> Unified multimodal models (UMMs) aim to jointly perform multimodal understanding and generation within a single framework. We present TUNA, a native UMM that builds a unified continuous visual representation by cascading a VAE encoder with a representation encoder. This unified representation space allows end-to-end processing of images and videos for both understanding and generation tasks. Compared to prior UMMs with decoupled representations, TUNA's unified visual space avoids representation format mismatches introduced by separate encoders, outperforming decoupled alternatives in both understanding and generation. Moreover, we observe that stronger pretrained representation encoders consistently yield better performance across all multimodal tasks, highlighting the importance of the representation encoder. Finally, in this unified setting, jointly training on both understanding and generation data allows the two tasks to benefit from each other rather than interfere. Our extensive experiments on multimodal understanding and generation benchmarks show that TUNA achieves state-of-the-art results in image and video understanding, image and video generation, and image editing, demonstrating the effectiveness and scalability of its unified representation design.

