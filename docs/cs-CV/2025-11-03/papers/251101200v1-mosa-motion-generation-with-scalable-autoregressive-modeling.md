---
layout: default
title: MoSa: Motion Generation with Scalable Autoregressive Modeling
---

# MoSa: Motion Generation with Scalable Autoregressive Modeling

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2511.01200" class="toolbar-btn" target="_blank">📄 arXiv: 2511.01200v1</a>
  <a href="https://arxiv.org/pdf/2511.01200.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2511.01200v1" onclick="toggleFavorite(this, '2511.01200v1', 'MoSa: Motion Generation with Scalable Autoregressive Modeling')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Mengyuan Liu, Sheng Yan, Yong Wang, Yingjie Li, Gui-Bin Bian, Hong Liu

**分类**: cs.CV

**发布日期**: 2025-11-03

**🔗 代码/项目**: [PROJECT_PAGE](https://mosa-web.github.io/MoSa-web)

---

## 💡 一句话要点

**MoSa：基于可扩展自回归建模的运动生成框架，提升文本驱动3D人体运动生成质量与效率。**

🎯 **匹配领域**: **支柱四：生成式动作 (Generative Motion)**

**关键词**: `文本驱动运动生成` `3D人体运动` `向量量化` `自回归建模` `分层生成` `Transformer` `运动编辑`

## 📋 核心要点

1. 现有文本驱动3D人体运动生成方法在生成质量和推理效率上存在挑战，难以兼顾。
2. MoSa通过分层残差向量量化和可扩展自回归建模，实现了粗到精的运动生成，提高了生成质量和效率。
3. 实验表明，MoSa在Motion-X数据集上取得了SOTA结果，FID显著降低，推理速度提升，并能泛化到运动编辑任务。

## 📝 摘要（中文）

本文提出了一种名为MoSa的新型分层运动生成框架，用于文本驱动的3D人体运动生成。MoSa通过粗到精的可扩展生成过程，增强了向量量化引导的生成Transformer（VQ-GT）范式。MoSa集成了多尺度Token保留策略（MTPS）到分层残差向量量化变分自编码器（RQ-VAE）中。MTPS在每个分层量化层采用插值，有效地保留了粗到精的多尺度token。由此，生成Transformer支持可扩展自回归（SAR）建模，预测尺度token，而非传统方法中每步仅预测一个token。因此，MoSa仅需10步推理，与RQ-VAE量化层数匹配。为解决频繁插值可能导致的重建退化问题，本文提出CAQ-VAE，一种轻量级但富有表现力的卷积-注意力混合VQ-VAE。CAQ-VAE增强了残差块设计，并融入注意力机制以更好地捕捉全局依赖关系。大量实验表明，MoSa实现了最先进的生成质量和效率，在保真度和速度方面均优于现有方法。在Motion-X数据集上，MoSa实现了0.06的FID（相比MoMask的0.20），同时减少了27%的推理时间。此外，MoSa可以很好地泛化到运动编辑等下游任务，无需额外微调。

## 🔬 方法详解

**问题定义**：本文旨在解决文本驱动的3D人体运动生成问题。现有方法，如基于VQ-GT的方法，通常需要较多的推理步骤，效率较低，并且难以在生成质量和推理速度之间取得平衡。频繁的插值操作也可能导致重建质量下降。

**核心思路**：MoSa的核心思路是通过分层量化和可扩展自回归建模，实现粗到精的运动生成。通过多尺度Token保留策略（MTPS）保留不同尺度的运动信息，并利用可扩展自回归（SAR）建模一次性预测多个尺度的token，从而减少推理步骤，提高效率。同时，采用卷积-注意力混合VQ-VAE（CAQ-VAE）来提升重建质量。

**技术框架**：MoSa的整体框架包括：1) 分层残差向量量化变分自编码器（RQ-VAE），用于将运动数据编码为离散的token序列；2) 多尺度Token保留策略（MTPS），用于在分层量化过程中保留不同尺度的token；3) 可扩展自回归（SAR）建模的生成Transformer，用于根据文本描述生成运动token序列；4) 卷积-注意力混合VQ-VAE（CAQ-VAE），用于提升重建质量。

**关键创新**：MoSa的关键创新在于：1) 提出了多尺度Token保留策略（MTPS），通过插值保留不同尺度的运动信息；2) 提出了可扩展自回归（SAR）建模，一次性预测多个尺度的token，减少推理步骤；3) 提出了卷积-注意力混合VQ-VAE（CAQ-VAE），通过卷积和注意力机制的结合，提升重建质量。与现有方法相比，MoSa能够更有效地利用多尺度信息，并减少推理步骤，从而提高生成质量和效率。

**关键设计**：MTPS在每个量化层使用插值来保留token，插值权重是可学习的参数。SAR建模的Transformer使用多头注意力机制，并根据文本描述预测多个尺度的token。CAQ-VAE在残差块中引入了卷积和注意力机制，以更好地捕捉局部和全局依赖关系。损失函数包括重建损失、量化损失和KL散度损失。

## 📊 实验亮点

MoSa在Motion-X数据集上取得了显著的性能提升，FID指标从MoMask的0.20降低到0.06，推理时间减少了27%。实验结果表明，MoSa在生成质量和效率方面均优于现有方法，并且具有良好的泛化能力，可以应用于运动编辑等下游任务。

## 🎯 应用场景

MoSa在虚拟现实、游戏开发、动画制作、人机交互等领域具有广泛的应用前景。它可以根据文本描述自动生成逼真的人体运动，从而降低运动生成成本，提高创作效率。此外，MoSa还可以用于运动编辑、动作捕捉数据修复等任务，具有重要的实际价值。

## 📄 摘要（原文）

> We introduce MoSa, a novel hierarchical motion generation framework for text-driven 3D human motion generation that enhances the Vector Quantization-guided Generative Transformers (VQ-GT) paradigm through a coarse-to-fine scalable generation process. In MoSa, we propose a Multi-scale Token Preservation Strategy (MTPS) integrated into a hierarchical residual vector quantization variational autoencoder (RQ-VAE). MTPS employs interpolation at each hierarchical quantization to effectively retain coarse-to-fine multi-scale tokens. With this, the generative transformer supports Scalable Autoregressive (SAR) modeling, which predicts scale tokens, unlike traditional methods that predict only one token at each step. Consequently, MoSa requires only 10 inference steps, matching the number of RQ-VAE quantization layers. To address potential reconstruction degradation from frequent interpolation, we propose CAQ-VAE, a lightweight yet expressive convolution-attention hybrid VQ-VAE. CAQ-VAE enhances residual block design and incorporates attention mechanisms to better capture global dependencies. Extensive experiments show that MoSa achieves state-of-the-art generation quality and efficiency, outperforming prior methods in both fidelity and speed. On the Motion-X dataset, MoSa achieves an FID of 0.06 (versus MoMask's 0.20) while reducing inference time by 27 percent. Moreover, MoSa generalizes well to downstream tasks such as motion editing, requiring no additional fine-tuning. The code is available at https://mosa-web.github.io/MoSa-web

