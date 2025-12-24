---
layout: default
title: "NaTex: Seamless Texture Generation as Latent Color Diffusion"
---

# NaTex: Seamless Texture Generation as Latent Color Diffusion

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2511.16317" class="toolbar-btn" target="_blank">📄 arXiv: 2511.16317v1</a>
  <a href="https://arxiv.org/pdf/2511.16317.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2511.16317v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2511.16317v1', 'NaTex: Seamless Texture Generation as Latent Color Diffusion')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Zeqiang Lai, Yunfei Zhao, Zibo Zhao, Xin Yang, Xin Huang, Jingwei Huang, Xiangyu Yue, Chunchao Guo

**分类**: cs.CV

**发布日期**: 2025-11-20

**备注**: Technical Report

---

## 💡 一句话要点

**NaTex：提出一种基于潜在颜色扩散的无缝纹理生成框架，直接在3D空间预测纹理颜色。**

🎯 **匹配领域**: **支柱三：空间感知 (Perception & SLAM)**

**关键词**: `纹理生成` `3D纹理` `扩散模型` `VAE` `几何感知` `点云` `潜在空间`

## 📋 核心要点

1. 现有方法依赖多视角扩散模型烘焙2D图像，难以处理遮挡、精确对齐和跨视角一致性问题。
2. NaTex将纹理视为3D空间中的颜色点云，提出潜在颜色扩散，直接在3D空间中生成纹理。
3. 实验表明，NaTex在纹理连贯性和对齐方面显著优于现有方法，并具有良好的泛化能力。

## 📝 摘要（中文）

NaTex是一个原生纹理生成框架，它直接在3D空间中预测纹理颜色。与之前依赖于几何条件多视角扩散模型(MVDs)合成的2D多视角图像烘焙的方法不同，NaTex避免了MVD流程的一些固有局限性，包括处理需要修复的遮挡区域的困难，实现精确的网格-纹理边界对齐，以及保持内容和颜色强度上的跨视角一致性和连贯性。NaTex提出了一种新范式，将纹理视为密集的颜色点云，从而解决上述问题。基于此，我们提出了潜在颜色扩散，它包含一个几何感知颜色点云VAE和一个多控制扩散Transformer (DiT)，完全从头开始使用3D数据进行训练，用于纹理重建和生成。为了实现精确对齐，我们引入了原生几何控制，通过位置嵌入和几何潜在变量将DiT置于直接3D空间信息的条件下。我们共同设计了VAE-DiT架构，其中几何潜在变量通过一个与颜色VAE紧密耦合的专用几何分支提取，提供细粒度的表面指导，保持与纹理的强对应关系。通过这些设计，NaTex表现出强大的性能，在纹理连贯性和对齐方面显著优于以前的方法。此外，NaTex还表现出强大的泛化能力，无论是免训练还是通过简单的微调，都适用于各种下游应用，例如材质生成、纹理细化以及零件分割和纹理化。

## 🔬 方法详解

**问题定义**：现有纹理生成方法依赖于从多视角图像烘焙纹理，这导致了几个问题：一是难以处理遮挡区域，需要额外的图像修复步骤；二是难以保证网格-纹理边界的精确对齐，尤其是在复杂几何体上；三是难以维持跨视角的内容和颜色一致性。这些问题限制了生成纹理的质量和适用性。

**核心思路**：NaTex的核心思路是将纹理视为3D空间中的密集颜色点云，并直接在3D空间中进行纹理生成。通过这种方式，可以避免多视角图像烘焙带来的问题，并实现更精确的几何对齐和更好的跨视角一致性。这种方法的核心在于学习一个能够理解3D几何信息并生成相应纹理颜色的模型。

**技术框架**：NaTex的整体架构包括两个主要模块：几何感知颜色点云VAE和一个多控制扩散Transformer (DiT)。首先，几何感知颜色点云VAE用于学习颜色点云的潜在表示，并提取几何潜在变量。然后，多控制扩散Transformer (DiT)基于这些潜在表示和几何信息，通过扩散过程生成纹理颜色。整个流程从3D数据开始，经过VAE编码，DiT扩散生成，最终得到3D纹理。

**关键创新**：NaTex的关键创新在于以下几点：一是提出了潜在颜色扩散的概念，直接在3D空间中进行纹理生成；二是引入了原生几何控制，通过位置嵌入和几何潜在变量将DiT置于直接3D空间信息的条件下；三是共同设计了VAE-DiT架构，使得几何信息能够有效地指导纹理生成。与现有方法相比，NaTex避免了多视角图像烘焙，从而解决了遮挡、对齐和一致性问题。

**关键设计**：在VAE-DiT架构中，几何分支与颜色VAE紧密耦合，用于提取细粒度的表面几何信息。DiT使用位置嵌入来编码3D空间位置信息，并使用几何潜在变量来指导纹理生成。损失函数的设计旨在鼓励生成的纹理与几何形状保持一致，并具有良好的视觉质量。具体的参数设置和网络结构细节未在摘要中详细说明，属于未知信息。

## 📊 实验亮点

NaTex在纹理连贯性和对齐方面显著优于现有方法。摘要中未提供具体的性能数据和对比基线，但强调了NaTex在多个下游任务上的强大泛化能力，例如材质生成、纹理细化以及零件分割和纹理化，无需大量训练或只需简单微调即可实现。

## 🎯 应用场景

NaTex具有广泛的应用前景，包括材质生成、纹理细化、零件分割和纹理化等。它可以用于游戏开发、电影制作、工业设计等领域，提高纹理生成的效率和质量。此外，NaTex的泛化能力使其能够适应不同的3D模型和纹理风格，具有很高的实用价值。

## 📄 摘要（原文）

> We present NaTex, a native texture generation framework that predicts texture color directly in 3D space. In contrast to previous approaches that rely on baking 2D multi-view images synthesized by geometry-conditioned Multi-View Diffusion models (MVDs), NaTex avoids several inherent limitations of the MVD pipeline. These include difficulties in handling occluded regions that require inpainting, achieving precise mesh-texture alignment along boundaries, and maintaining cross-view consistency and coherence in both content and color intensity. NaTex features a novel paradigm that addresses the aforementioned issues by viewing texture as a dense color point cloud. Driven by this idea, we propose latent color diffusion, which comprises a geometry-awared color point cloud VAE and a multi-control diffusion transformer (DiT), entirely trained from scratch using 3D data, for texture reconstruction and generation. To enable precise alignment, we introduce native geometry control that conditions the DiT on direct 3D spatial information via positional embeddings and geometry latents. We co-design the VAE-DiT architecture, where the geometry latents are extracted via a dedicated geometry branch tightly coupled with the color VAE, providing fine-grained surface guidance that maintains strong correspondence with the texture. With these designs, NaTex demonstrates strong performance, significantly outperforming previous methods in texture coherence and alignment. Moreover, NaTex also exhibits strong generalization capabilities, either training-free or with simple tuning, for various downstream applications, e.g., material generation, texture refinement, and part segmentation and texturing.

