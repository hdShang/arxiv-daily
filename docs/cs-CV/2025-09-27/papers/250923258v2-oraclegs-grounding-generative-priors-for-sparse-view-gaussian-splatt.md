---
layout: default
title: "OracleGS: Grounding Generative Priors for Sparse-View Gaussian Splatting"
---

# OracleGS: Grounding Generative Priors for Sparse-View Gaussian Splatting

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.23258" class="toolbar-btn" target="_blank">📄 arXiv: 2509.23258v2</a>
  <a href="https://arxiv.org/pdf/2509.23258.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.23258v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.23258v2', 'OracleGS: Grounding Generative Priors for Sparse-View Gaussian Splatting')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Atakan Topaloglu, Kunyi Li, Michael Niemeyer, Nassir Navab, A. Murat Tekalp, Federico Tombari

**分类**: cs.CV

**发布日期**: 2025-09-27 (更新: 2025-10-04)

**备注**: Project page available at: https://atakan-topaloglu.github.io/oraclegs/

---

## 💡 一句话要点

**OracleGS：通过生成先验引导的稀疏视角高斯溅射**

🎯 **匹配领域**: **支柱三：空间感知与语义 (Perception & Semantics)**

**关键词**: `新视角合成` `高斯溅射` `生成模型` `多视角立体` `扩散模型` `三维重建` `稀疏视角`

## 📋 核心要点

1. 现有稀疏视角新视角合成方法在几何保真度和场景完整性之间存在trade-off，回归模型保真但缺失，生成模型完整但结构不一致。
2. OracleGS提出一种“提议-验证”框架，利用3D感知扩散模型生成完整场景，并使用MVS模型作为Oracle验证生成视角的不确定性。
3. 通过不确定性加权损失优化3D高斯溅射模型，在Mip-NeRF 360和NeRF Synthetic等数据集上超越了现有技术水平。

## 📝 摘要（中文）

稀疏视角下的新视角合成由于严重的几何歧义而存在根本性的不适定性。现有方法陷入了一种权衡：回归模型在几何上是忠实的，但并不完整；而生成模型可以补全场景，但经常引入结构上的不一致性。我们提出了OracleGS，这是一个新颖的框架，它将生成模型的完整性与回归模型的保真度相结合，用于稀疏视角高斯溅射。我们的“提议-验证”框架不是使用生成模型来修补不完整的重建，而是首先利用预训练的3D感知扩散模型来合成新视角，从而提出一个完整的场景。然后，我们将多视角立体（MVS）模型重新用作3D感知Oracle，以验证生成视角的3D不确定性，使用其注意力图来揭示生成视角得到多视角证据良好支持的区域，以及由于遮挡、缺乏纹理或直接不一致而导致的高不确定性区域。这种不确定性信号通过不确定性加权损失直接指导3D高斯溅射模型的优化。我们的方法将强大的生成先验建立在多视角几何证据的基础上，过滤掉幻觉伪影，同时保留欠约束区域中合理的补全，在包括Mip-NeRF 360和NeRF Synthetic在内的数据集上优于最先进的方法。

## 🔬 方法详解

**问题定义**：论文旨在解决稀疏视角下新视角合成中几何歧义导致的场景不完整或结构不一致的问题。现有方法要么依赖回归模型，几何保真但无法补全缺失区域；要么依赖生成模型，可以补全场景但容易引入幻觉伪影和结构错误。

**核心思路**：论文的核心思路是结合生成模型和回归模型的优点，利用生成模型提供场景的完整先验，然后利用回归模型（MVS）验证生成内容的几何一致性，从而在保证场景完整性的同时避免引入不合理的结构。

**技术框架**：OracleGS框架包含两个主要阶段：1) **场景提议阶段**：使用预训练的3D感知扩散模型生成新视角，从而提出一个完整的场景。2) **场景验证阶段**：使用多视角立体（MVS）模型作为3D感知Oracle，评估生成视角的3D不确定性。MVS模型的注意力图用于指示哪些区域具有良好的多视角一致性，哪些区域存在高不确定性。最后，使用不确定性加权损失来优化3D高斯溅射模型。

**关键创新**：该方法最重要的创新点在于将生成模型的先验知识与多视角几何约束相结合。通过MVS模型提供的几何一致性信息来引导生成模型的优化，从而避免了生成模型产生的幻觉伪影，并保留了在欠约束区域中合理的补全。

**关键设计**：关键设计包括：1) 使用预训练的3D感知扩散模型，例如，可以生成具有几何一致性的新视角。2) 将MVS模型的注意力图作为不确定性度量，用于指导高斯溅射模型的优化。3) 使用不确定性加权损失，对不确定性高的区域降低损失权重，从而允许生成模型在这些区域进行合理的补全，同时对确定性高的区域增加损失权重，以保证几何一致性。

## 📊 实验亮点

OracleGS在Mip-NeRF 360和NeRF Synthetic数据集上取得了显著的性能提升，超越了现有的state-of-the-art方法。通过结合生成先验和几何约束，该方法能够生成更完整、更真实的场景表示，尤其是在稀疏视角的情况下。

## 🎯 应用场景

OracleGS在机器人导航、自动驾驶、虚拟现实/增强现实、三维重建等领域具有广泛的应用前景。它可以用于在稀疏的传感器数据下生成高质量的场景表示，从而提高机器人对环境的理解能力，增强虚拟现实/增强现实的沉浸感，并加速三维重建过程。

## 📄 摘要（原文）

> Sparse-view novel view synthesis is fundamentally ill-posed due to severe geometric ambiguity. Current methods are caught in a trade-off: regressive models are geometrically faithful but incomplete, whereas generative models can complete scenes but often introduce structural inconsistencies. We propose OracleGS, a novel framework that reconciles generative completeness with regressive fidelity for sparse view Gaussian Splatting. Instead of using generative models to patch incomplete reconstructions, our "propose-and-validate" framework first leverages a pre-trained 3D-aware diffusion model to synthesize novel views to propose a complete scene. We then repurpose a multi-view stereo (MVS) model as a 3D-aware oracle to validate the 3D uncertainties of generated views, using its attention maps to reveal regions where the generated views are well-supported by multi-view evidence versus where they fall into regions of high uncertainty due to occlusion, lack of texture, or direct inconsistency. This uncertainty signal directly guides the optimization of a 3D Gaussian Splatting model via an uncertainty-weighted loss. Our approach conditions the powerful generative prior on multi-view geometric evidence, filtering hallucinatory artifacts while preserving plausible completions in under-constrained regions, outperforming state-of-the-art methods on datasets including Mip-NeRF 360 and NeRF Synthetic.

