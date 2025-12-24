---
layout: default
title: "Hunyuan3D 2.5: Towards High-Fidelity 3D Assets Generation with Ultimate Details"
---

# Hunyuan3D 2.5: Towards High-Fidelity 3D Assets Generation with Ultimate Details

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.16504" class="toolbar-btn" target="_blank">📄 arXiv: 2506.16504v1</a>
  <a href="https://arxiv.org/pdf/2506.16504.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.16504v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.16504v1', 'Hunyuan3D 2.5: Towards High-Fidelity 3D Assets Generation with Ultimate Details')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Zeqiang Lai, Yunfei Zhao, Haolin Liu, Zibo Zhao, Qingxiang Lin, Huiwen Shi, Xianghui Yang, Mingxin Yang, Shuhui Yang, Yifei Feng, Sheng Zhang, Xin Huang, Di Luo, Fan Yang, Fang Yang, Lifu Wang, Sicong Liu, Yixuan Tang, Yulin Cai, Zebin He, Tian Liu, Yuhong Liu, Jie Jiang, Linus, Jingwei Huang, Chunchao Guo

**分类**: cs.CV, cs.AI

**发布日期**: 2025-06-19

**备注**: Technical report

---

## 💡 一句话要点

**提出Hunyuan3D 2.5以生成高保真3D资产**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `3D资产生成` `扩散模型` `物理基础渲染` `高保真` `细节生成`

## 📋 核心要点

1. 现有的3D资产生成方法在细节和真实感方面存在不足，难以与手工制作的3D形状相媲美。
2. Hunyuan3D 2.5通过引入新的形状基础模型LATTICE和物理基础渲染技术，显著提升了3D形状和纹理的生成质量。
3. 实验结果显示，Hunyuan3D 2.5在形状和纹理生成方面的性能显著优于以往的方法，尤其是在细节和真实感上有显著提升。

## 📝 摘要（中文）

在本报告中，我们介绍了Hunyuan3D 2.5，这是一个强大的3D扩散模型套件，旨在生成高保真和细致纹理的3D资产。Hunyuan3D 2.5遵循其前身Hunyuan3D 2.0的两阶段流程，同时在形状和纹理生成方面展示了显著的进步。在形状生成方面，我们引入了一种新的形状基础模型——LATTICE，该模型使用高质量数据集进行训练。我们的最大模型达到100亿参数，能够生成清晰且细致的3D形状，并保持网格表面光滑，显著缩小了生成形状与手工制作形状之间的差距。在纹理生成方面，通过从Hunyuan3D 2.0 Paint模型扩展的多视角架构进行了物理基础渲染（PBR）升级。我们的广泛评估表明，Hunyuan3D 2.5在形状和端到端纹理生成方面显著优于之前的方法。

## 🔬 方法详解

**问题定义**：本论文旨在解决现有3D资产生成方法在细节和真实感方面的不足，尤其是生成的3D形状与手工制作形状之间的差距。

**核心思路**：论文提出了一种新的形状基础模型LATTICE，并结合物理基础渲染技术，旨在提升生成3D资产的质量和细节表现。

**技术框架**：Hunyuan3D 2.5采用两阶段的生成流程，首先生成3D形状，然后进行纹理生成。形状生成使用LATTICE模型，纹理生成则通过多视角架构实现。

**关键创新**：最重要的创新在于引入了LATTICE模型和物理基础渲染技术，使得生成的3D形状更加清晰、细致，并且网格表面保持光滑，显著提高了生成质量。

**关键设计**：模型参数设置达到100亿，使用高质量数据集进行训练，损失函数设计上注重形状与纹理的协调性，确保生成结果的真实感和细节表现。

## 📊 实验亮点

实验结果表明，Hunyuan3D 2.5在形状生成和纹理生成方面的性能显著优于以往的方法，尤其是在细节表现上，生成的3D形状与手工制作形状的差距大幅缩小，具体性能提升幅度未知。

## 🎯 应用场景

该研究的潜在应用领域包括游戏开发、虚拟现实、动画制作等，能够为3D资产的快速生成提供高质量的解决方案，提升创作效率和效果。未来，该技术可能在更多领域中得到应用，如建筑可视化和数字艺术创作等。

## 📄 摘要（原文）

> In this report, we present Hunyuan3D 2.5, a robust suite of 3D diffusion models aimed at generating high-fidelity and detailed textured 3D assets. Hunyuan3D 2.5 follows two-stages pipeline of its previous version Hunyuan3D 2.0, while demonstrating substantial advancements in both shape and texture generation. In terms of shape generation, we introduce a new shape foundation model -- LATTICE, which is trained with scaled high-quality datasets, model-size, and compute. Our largest model reaches 10B parameters and generates sharp and detailed 3D shape with precise image-3D following while keeping mesh surface clean and smooth, significantly closing the gap between generated and handcrafted 3D shapes. In terms of texture generation, it is upgraded with phyiscal-based rendering (PBR) via a novel multi-view architecture extended from Hunyuan3D 2.0 Paint model. Our extensive evaluation shows that Hunyuan3D 2.5 significantly outperforms previous methods in both shape and end-to-end texture generation.

