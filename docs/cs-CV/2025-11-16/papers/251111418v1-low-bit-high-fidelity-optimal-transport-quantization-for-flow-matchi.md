---
layout: default
title: Low-Bit, High-Fidelity: Optimal Transport Quantization for Flow Matching
---

# Low-Bit, High-Fidelity: Optimal Transport Quantization for Flow Matching

**arXiv**: [2511.11418v1](https://arxiv.org/abs/2511.11418) | [PDF](https://arxiv.org/pdf/2511.11418.pdf)

**作者**: Dara Varam, Diaa A. Abuhani, Imran Zualkernan, Raghad AlDamani, Lujain Khalil

---

## 💡 一句话要点

**提出基于最优传输的后训练量化方法，以压缩流匹配生成模型用于边缘AI部署**

**关键词**: `流匹配生成模型` `后训练量化` `最优传输` `模型压缩` `边缘AI` `生成质量保持`

## 📋 核心要点

1. 流匹配生成模型因高精度参数需求难以实际部署，面临压缩挑战
2. 采用最优传输量化最小化权重量化前后2-Wasserstein距离，优于均匀、分段和对数量化
3. 理论分析量化生成退化上界，实验在多个数据集上保持生成质量至2-3比特

## 📄 摘要（原文）

> Flow Matching (FM) generative models offer efficient simulation-free training and deterministic sampling, but their practical deployment is challenged by high-precision parameter requirements. We adapt optimal transport (OT)-based post-training quantization to FM models, minimizing the 2-Wasserstein distance between quantized and original weights, and systematically compare its effectiveness against uniform, piecewise, and logarithmic quantization schemes. Our theoretical analysis provides upper bounds on generative degradation under quantization, and empirical results across five benchmark datasets of varying complexity show that OT-based quantization preserves both visual generation quality and latent space stability down to 2-3 bits per parameter, where alternative methods fail. This establishes OT-based quantization as a principled, effective approach to compress FM generative models for edge and embedded AI applications.

