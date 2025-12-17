---
layout: default
title: Native and Compact Structured Latents for 3D Generation
---

# Native and Compact Structured Latents for 3D Generation

**arXiv**: [2512.14692v1](https://arxiv.org/abs/2512.14692) | [PDF](https://arxiv.org/pdf/2512.14692.pdf)

**作者**: Jianfeng Xiang, Xiaoxue Chen, Sicheng Xu, Ruicheng Wang, Zelong Lv, Yu Deng, Hongyuan Zhu, Yue Dong, Hao Zhao, Nicholas Jing Yuan, Jiaolong Yang

**分类**: cs.CV, cs.AI

**发布日期**: 2025-12-16

**备注**: Project Page: https://microsoft.github.io/TRELLIS.2/

---

## 💡 一句话要点

**提出O-Voxel稀疏体素表示与稀疏压缩VAE，以解决3D生成中复杂拓扑与细节外观建模的挑战**

**关键词**: `3D生成建模` `稀疏体素表示` `结构化潜在空间` `流匹配模型` `几何与外观编码` `大规模参数训练` `物理渲染参数` `复杂拓扑建模`

## 📋 核心要点

1. 现有3D表示方法难以有效捕捉复杂拓扑（如开放、非流形表面）和超越颜色的详细外观属性（如物理渲染参数）。
2. 提出O-Voxel稀疏体素表示，统一编码几何与外观；并基于此设计稀疏压缩VAE，实现高压缩率与紧凑潜在空间。
3. 训练40亿参数流匹配模型，生成资产在几何与材质质量上远超现有方法，且推理高效，验证了方法的有效性。

## 📝 摘要（中文）

近年来，3D生成建模在生成真实感方面取得了显著进展，但该领域仍受限于现有表示方法，这些方法难以捕捉具有复杂拓扑结构和详细外观的资产。本文提出了一种从原生3D数据中学习结构化潜在表示的方法来应对这一挑战。其核心是一种名为O-Voxel的新型稀疏体素结构，这是一种全向体素表示，能够同时编码几何和外观信息。O-Voxel能够稳健地建模任意拓扑结构，包括开放、非流形和完全封闭的表面，同时捕捉超越纹理颜色的全面表面属性，例如基于物理的渲染参数。基于O-Voxel，我们设计了一种稀疏压缩变分自编码器，它提供了高空间压缩率和紧凑的潜在空间。我们使用多样化的公共3D资产数据集，训练了包含40亿参数的大规模流匹配模型用于3D生成。尽管模型规模庞大，推理过程仍然保持高效。同时，我们生成资产的几何和材质质量远超现有模型。我们相信，我们的方法为3D生成建模提供了重要进展。

## 🔬 方法详解

论文提出一个基于结构化潜在表示的3D生成框架。核心是O-Voxel稀疏体素表示，它作为原生3D数据的统一编码器，能处理任意拓扑并包含几何与外观（如物理渲染参数）信息。基于O-Voxel，设计了稀疏压缩变分自编码器，通过稀疏性实现高空间压缩，形成紧凑的潜在空间。在此基础上，训练大规模流匹配模型进行生成。与现有方法相比，主要区别在于使用O-Voxel作为底层表示，克服了传统网格或体素在拓扑和细节上的限制，并通过稀疏压缩优化了潜在空间效率。

## 📊 实验亮点

实验表明，生成的3D资产在几何细节和材质质量上显著超越现有模型，同时基于40亿参数的大规模流匹配模型实现了高效推理，验证了O-Voxel表示和稀疏压缩VAE的有效性与优越性。

## 🎯 应用场景

该研究在3D内容创作、虚拟现实、游戏开发、工业设计等领域具有广泛应用潜力，能高效生成高质量、复杂拓扑的3D资产，提升自动化生成的真实感和多样性，降低人工建模成本。

## 📄 摘要（原文）

> Recent advancements in 3D generative modeling have significantly improved the generation realism, yet the field is still hampered by existing representations, which struggle to capture assets with complex topologies and detailed appearance. This paper present an approach for learning a structured latent representation from native 3D data to address this challenge. At its core is a new sparse voxel structure called O-Voxel, an omni-voxel representation that encodes both geometry and appearance. O-Voxel can robustly model arbitrary topology, including open, non-manifold, and fully-enclosed surfaces, while capturing comprehensive surface attributes beyond texture color, such as physically-based rendering parameters. Based on O-Voxel, we design a Sparse Compression VAE which provides a high spatial compression rate and a compact latent space. We train large-scale flow-matching models comprising 4B parameters for 3D generation using diverse public 3D asset datasets. Despite their scale, inference remains highly efficient. Meanwhile, the geometry and material quality of our generated assets far exceed those of existing models. We believe our approach offers a significant advancement in 3D generative modeling.

