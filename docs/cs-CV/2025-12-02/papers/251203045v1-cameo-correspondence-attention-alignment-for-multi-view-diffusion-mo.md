---
layout: default
title: CAMEO: Correspondence-Attention Alignment for Multi-View Diffusion Models
---

# CAMEO: Correspondence-Attention Alignment for Multi-View Diffusion Models

**arXiv**: [2512.03045v1](https://arxiv.org/abs/2512.03045) | [PDF](https://arxiv.org/pdf/2512.03045.pdf)

**作者**: Minkyung Kwon, Jinhyeok Choi, Jiho Park, Seonghu Jeon, Jinhyuk Jang, Junyoung Seo, Minseop Kwak, Jin-Hwa Kim, Seungryong Kim

---

## 💡 一句话要点

**提出CAMEO训练技术，通过几何对应监督注意力图以提升多视图扩散模型的效率和生成质量。**

**关键词**: `多视图扩散模型` `注意力机制` `几何对应` `新视图合成` `训练效率` `模型无关性`

## 📋 核心要点

1. 核心问题：多视图扩散模型的视图一致性机制不明确，注意力图对应信号不完整，影响大视角变化下的生成准确性。
2. 方法要点：直接使用几何对应监督注意力图，仅需监督单个注意力层，以学习精确对应并保持参考图像几何结构。
3. 实验或效果：训练迭代次数减半，收敛加速，新视图合成性能提升，方法模型无关，可应用于任何多视图扩散模型。

## 📄 摘要（原文）

> Multi-view diffusion models have recently emerged as a powerful paradigm for novel view synthesis, yet the underlying mechanism that enables their view-consistency remains unclear. In this work, we first verify that the attention maps of these models acquire geometric correspondence throughout training, attending to the geometrically corresponding regions across reference and target views for view-consistent generation. However, this correspondence signal remains incomplete, with its accuracy degrading under large viewpoint changes. Building on these findings, we introduce CAMEO, a simple yet effective training technique that directly supervises attention maps using geometric correspondence to enhance both the training efficiency and generation quality of multi-view diffusion models. Notably, supervising a single attention layer is sufficient to guide the model toward learning precise correspondences, thereby preserving the geometry and structure of reference images, accelerating convergence, and improving novel view synthesis performance. CAMEO reduces the number of training iterations required for convergence by half while achieving superior performance at the same iteration counts. We further demonstrate that CAMEO is model-agnostic and can be applied to any multi-view diffusion model.

