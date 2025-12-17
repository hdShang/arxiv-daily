---
layout: default
title: PGP-DiffSR: Phase-Guided Progressive Pruning for Efficient Diffusion-based Image Super-Resolution
---

# PGP-DiffSR: Phase-Guided Progressive Pruning for Efficient Diffusion-based Image Super-Resolution

**arXiv**: [2512.02681v1](https://arxiv.org/abs/2512.02681) | [PDF](https://arxiv.org/pdf/2512.02681.pdf)

**作者**: Zhongbao Yang, Jiangxin Dong, Yazhou Yao, Jinhui Tang, Jinshan Pan

---

## 💡 一句话要点

**提出PGP-DiffSR，通过相位引导的渐进剪枝实现高效扩散图像超分辨率。**

**关键词**: `图像超分辨率` `扩散模型` `模型剪枝` `相位信息` `轻量化方法`

## 📋 核心要点

1. 扩散模型在图像超分辨率中计算和内存成本高，需轻量化。
2. 采用渐进剪枝去除冗余块，并引入相位交换适配器提升恢复性能。
3. 实验表明方法在降低计算负载的同时保持竞争性恢复质量。

## 📄 摘要（原文）

> Although diffusion-based models have achieved impressive results in image super-resolution, they often rely on large-scale backbones such as Stable Diffusion XL (SDXL) and Diffusion Transformers (DiT), which lead to excessive computational and memory costs during training and inference. To address this issue, we develop a lightweight diffusion method, PGP-DiffSR, by removing redundant information from diffusion models under the guidance of the phase information of inputs for efficient image super-resolution. We first identify the intra-block redundancy within the diffusion backbone and propose a progressive pruning approach that removes redundant blocks while reserving restoration capability. We note that the phase information of the restored images produced by the pruned diffusion model is not well estimated. To solve this problem, we propose a phase-exchange adapter module that explores the phase information of the inputs to guide the pruned diffusion model for better restoration performance. We formulate the progressive pruning approach and the phase-exchange adapter module into a unified model. Extensive experiments demonstrate that our method achieves competitive restoration quality while significantly reducing computational load and memory consumption. The code is available at https://github.com/yzb1997/PGP-DiffSR.

