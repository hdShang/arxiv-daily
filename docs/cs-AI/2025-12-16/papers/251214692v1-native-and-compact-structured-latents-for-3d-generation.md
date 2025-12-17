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

**提出O-Voxel稀疏体素表示与稀疏压缩VAE，以解决3D生成中复杂拓扑与细节外观建模的挑战。**

🎯 **匹配领域**: **视觉里程计**

**关键词**: `3D生成建模` `稀疏体素表示` `结构化潜在空间` `变分自编码器` `流匹配模型` `复杂拓扑建模` `物理渲染参数` `大规模参数训练`

## 📋 核心要点

1. 现有3D表示方法难以有效建模复杂拓扑（如开放、非流形表面）和详细外观（如物理渲染参数），限制了生成资产的真实感。
2. 提出O-Voxel稀疏体素表示，统一编码几何与外观，并基于此设计稀疏压缩VAE，实现高压缩率和紧凑潜在空间，支持大规模流匹配训练。
3. 实验表明，生成资产的几何和材质质量显著超越现有模型，且40亿参数模型推理高效，在公共数据集上验证了方法的优越性。

## 📝 摘要（中文）

近年来，3D生成建模在生成真实感方面取得了显著进展，但该领域仍受限于现有表示方法，这些方法难以捕捉具有复杂拓扑和详细外观的资产。本文提出了一种从原生3D数据中学习结构化潜在表示的方法来解决这一挑战。其核心是一种称为O-Voxel的新稀疏体素结构，这是一种全向体素表示，能够同时编码几何和外观。O-Voxel能够稳健地建模任意拓扑，包括开放、非流形和完全封闭的表面，同时捕捉超越纹理颜色的全面表面属性，例如基于物理的渲染参数。基于O-Voxel，我们设计了一种稀疏压缩变分自编码器，提供了高空间压缩率和紧凑的潜在空间。我们使用多样化的公共3D资产数据集训练了包含40亿参数的大规模流匹配模型用于3D生成。尽管模型规模庞大，推理仍然非常高效。同时，我们生成资产的几何和材质质量远超现有模型。我们相信，我们的方法为3D生成建模提供了重要进展。

## 🔬 方法详解

论文提出一种基于结构化潜在表示的3D生成框架。整体框架包括：首先，引入O-Voxel稀疏体素表示，这是一种全向体素结构，能够同时编码几何（如任意拓扑表面）和外观（如纹理、物理渲染参数），解决了传统表示在复杂资产建模上的不足。其次，基于O-Voxel设计稀疏压缩变分自编码器，通过高效压缩实现高空间压缩率和紧凑潜在空间，便于后续生成建模。关键技术创新点在于O-Voxel的稀疏性和多属性编码能力，以及VAE的压缩优化。与现有方法的主要区别在于：O-Voxel比传统体素或网格更灵活地处理拓扑，且整合了更丰富的表面属性；稀疏压缩VAE相比标准VAE提供了更高效的潜在表示，支持大规模参数模型训练。

## 📊 实验亮点

最重要的实验结果包括：生成资产的几何和材质质量远超现有模型，在公共数据集上表现出色；训练了40亿参数的大规模流匹配模型，尽管规模庞大，推理仍保持高效，验证了方法的可扩展性和实用性。

## 🎯 应用场景

该研究在3D内容生成领域具有广泛潜在应用，如游戏开发、虚拟现实、影视特效和工业设计，可用于快速生成高质量、复杂拓扑的3D资产，提升创作效率和真实感，推动数字孪生和元宇宙等技术的发展。

## 📄 摘要（原文）

> Recent advancements in 3D generative modeling have significantly improved the generation realism, yet the field is still hampered by existing representations, which struggle to capture assets with complex topologies and detailed appearance. This paper present an approach for learning a structured latent representation from native 3D data to address this challenge. At its core is a new sparse voxel structure called O-Voxel, an omni-voxel representation that encodes both geometry and appearance. O-Voxel can robustly model arbitrary topology, including open, non-manifold, and fully-enclosed surfaces, while capturing comprehensive surface attributes beyond texture color, such as physically-based rendering parameters. Based on O-Voxel, we design a Sparse Compression VAE which provides a high spatial compression rate and a compact latent space. We train large-scale flow-matching models comprising 4B parameters for 3D generation using diverse public 3D asset datasets. Despite their scale, inference remains highly efficient. Meanwhile, the geometry and material quality of our generated assets far exceed those of existing models. We believe our approach offers a significant advancement in 3D generative modeling.

