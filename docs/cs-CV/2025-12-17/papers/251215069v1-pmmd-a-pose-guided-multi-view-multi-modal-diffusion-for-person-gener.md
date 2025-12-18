---
layout: default
title: PMMD: A pose-guided multi-view multi-modal diffusion for person generation
---

# PMMD: A pose-guided multi-view multi-modal diffusion for person generation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.15069" class="toolbar-btn" target="_blank">📄 arXiv: 2512.15069v1</a>
  <a href="https://arxiv.org/pdf/2512.15069.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.15069v1" onclick="toggleFavorite(this, '2512.15069v1', 'PMMD: A pose-guided multi-view multi-modal diffusion for person generation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Ziyu Shang, Haoran Liu, Rongchao Zhang, Zhiqian Wei, Tongtong Feng

**分类**: cs.CV, cs.AI

**发布日期**: 2025-12-17

**🔗 代码/项目**: [GITHUB](https://github.com/ZANMANGLOOPYE/PMMD)

---

## 💡 一句话要点

**提出PMMD框架，通过多视角多模态扩散模型实现姿态引导下的高质量人物生成。**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `人物生成` `扩散模型` `多视角学习` `多模态融合` `姿态引导`

## 📋 核心要点

1. 现有方法在可控人物图像生成中，面临遮挡、服装风格漂移和姿态不对齐等挑战。
2. PMMD框架通过多视角参考、姿态图和文本提示，利用扩散模型合成逼真人物图像。
3. 实验表明，PMMD在一致性、细节保留和可控性方面优于现有方法，提升了生成质量。

## 📝 摘要（中文）

本文提出了一种姿态引导的多视角多模态扩散框架（PMMD），用于合成逼真的人物图像，该图像可以根据多视角参考、姿态图和文本提示进行控制。现有方法常受遮挡、服装风格漂移和姿态不对齐等问题的影响。PMMD通过多模态编码器联合建模视觉视角、姿态特征和语义描述，从而减少跨模态差异并提高身份保真度。此外，还设计了一个ResCVA模块来增强局部细节，同时保留全局结构，以及一个跨模态融合模块，该模块在整个去噪过程中将图像语义与文本集成。在DeepFashion MultiModal数据集上的实验表明，PMMD在一致性、细节保留和可控性方面优于代表性的基线方法。项目主页和代码可在https://github.com/ZANMANGLOOPYE/PMMD 找到。

## 🔬 方法详解

**问题定义**：论文旨在解决在给定姿态、多视角图像参考和文本描述的情况下，生成高质量、一致性好的人物图像的问题。现有方法在处理遮挡、服装风格迁移以及姿态精确对齐方面存在不足，导致生成的人物图像质量不高，身份信息保持不佳。

**核心思路**：论文的核心思路是利用扩散模型强大的生成能力，并结合多视角信息、姿态信息和文本信息，通过多模态融合的方式，指导扩散模型的去噪过程，从而生成高质量的人物图像。通过联合建模不同模态的信息，可以减少跨模态差异，提高生成图像的身份保真度。

**技术框架**：PMMD框架主要包含以下几个模块：1) 多模态编码器：用于联合编码多视角图像、姿态特征和文本描述，生成统一的特征表示。2) ResCVA模块：用于增强生成图像的局部细节，同时保持全局结构的一致性。3) 跨模态融合模块：用于在扩散模型的去噪过程中，将图像语义信息与文本信息进行融合，从而更好地指导图像生成。整个流程是先通过编码器提取特征，然后将特征输入到扩散模型中进行迭代去噪，最终生成人物图像。

**关键创新**：论文的关键创新在于提出了一个多模态扩散框架，该框架能够有效地融合多视角图像、姿态信息和文本信息，从而生成高质量的人物图像。ResCVA模块和跨模态融合模块的设计，进一步提升了生成图像的细节和一致性。与现有方法相比，PMMD能够更好地处理遮挡、服装风格迁移和姿态对齐等问题。

**关键设计**：多模态编码器采用Transformer结构，用于学习不同模态之间的关联。ResCVA模块采用残差连接和通道注意力机制，用于增强局部细节。跨模态融合模块采用交叉注意力机制，用于将图像语义信息与文本信息进行融合。损失函数包括L1损失、L2损失和感知损失，用于优化生成图像的质量和一致性。具体的参数设置和网络结构细节可以在论文的补充材料中找到。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.15069v1/x1.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.15069v1/x2.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.15069v1/x3.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

实验结果表明，PMMD在DeepFashion MultiModal数据集上取得了显著的性能提升，在一致性、细节保留和可控性方面均优于现有方法。具体而言，PMMD能够生成更逼真的人物图像，更好地保持身份信息，并且能够根据给定的姿态和文本描述生成符合要求的图像。项目主页提供了详细的实验结果和可视化效果。

## 🎯 应用场景

该研究成果可广泛应用于虚拟试衣、图像编辑、数字人创建等领域。例如，用户可以通过输入自己的照片和想要的姿势，生成穿着不同服装的图像，从而实现虚拟试衣。此外，该技术还可以用于创建逼真的数字人，应用于游戏、电影等领域，具有重要的商业价值和应用前景。

## 📄 摘要（原文）

> Generating consistent human images with controllable pose and appearance is essential for applications in virtual try on, image editing, and digital human creation. Current methods often suffer from occlusions, garment style drift, and pose misalignment. We propose Pose-guided Multi-view Multimodal Diffusion (PMMD), a diffusion framework that synthesizes photorealistic person images conditioned on multi-view references, pose maps, and text prompts. A multimodal encoder jointly models visual views, pose features, and semantic descriptions, which reduces cross modal discrepancy and improves identity fidelity. We further design a ResCVA module to enhance local detail while preserving global structure, and a cross modal fusion module that integrates image semantics with text throughout the denoising pipeline. Experiments on the DeepFashion MultiModal dataset show that PMMD outperforms representative baselines in consistency, detail preservation, and controllability. Project page and code are available at https://github.com/ZANMANGLOOPYE/PMMD.

