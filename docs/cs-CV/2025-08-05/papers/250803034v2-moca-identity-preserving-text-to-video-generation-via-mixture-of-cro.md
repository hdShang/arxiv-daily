---
layout: default
title: "MoCA: Identity-Preserving Text-to-Video Generation via Mixture of Cross Attention"
---

# MoCA: Identity-Preserving Text-to-Video Generation via Mixture of Cross Attention

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.03034" class="toolbar-btn" target="_blank">📄 arXiv: 2508.03034v2</a>
  <a href="https://arxiv.org/pdf/2508.03034.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.03034v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.03034v2', 'MoCA: Identity-Preserving Text-to-Video Generation via Mixture of Cross Attention')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Qi Xie, Yongjia Ma, Donglin Di, Xuehao Gao, Xun Yang

**分类**: cs.CV

**发布日期**: 2025-08-05 (更新: 2025-08-13)

---

## 💡 一句话要点

**提出MoCA以解决文本到视频生成中的身份保持问题**

🎯 **匹配领域**: **支柱八：物理动画 (Physics-based Animation)**

**关键词**: `文本到视频生成` `身份保持` `扩散模型` `交叉注意力` `时空建模` `面部动态` `视频生成` `深度学习`

## 📋 核心要点

1. 现有文本到视频生成方法在身份保持和细致面部动态捕捉方面存在明显不足，导致生成视频的质量不高。
2. 本文提出MoCA，通过在扩散变换器中引入混合交叉注意力机制，增强了视频生成中的身份一致性和细节表现。
3. 在CelebIPVid数据集上进行的实验表明，MoCA在面部相似性指标上比现有方法提高了超过5%的性能。

## 📝 摘要（中文）

尽管最近在扩散模型方面取得了进展，实现身份保持的文本到视频生成仍然具有挑战性。现有方法往往无法捕捉细致的面部动态或保持时间上的身份一致性。为了解决这些局限性，本文提出了MoCA，一个基于扩散变换器（DiT）骨干网的新型视频扩散模型，结合了受专家混合范式启发的混合交叉注意力机制。我们的框架通过在每个DiT块中嵌入MoCA层来改善帧间身份一致性，其中分层时间池捕捉不同时间尺度上的身份特征，时间感知交叉注意力专家动态建模时空关系。我们还引入了潜在视频感知损失，以增强视频帧之间的身份一致性和细节。通过在CelebIPVid数据集上的广泛实验，MoCA在面部相似性方面超过现有T2V方法5%以上。

## 🔬 方法详解

**问题定义**：本文旨在解决文本到视频生成中的身份保持问题，现有方法在捕捉细致面部动态和保持时间一致性方面存在不足。

**核心思路**：MoCA通过引入混合交叉注意力机制，结合分层时间池和时间感知交叉注意力专家，动态建模时空关系，从而改善身份一致性。

**技术框架**：MoCA的整体架构基于扩散变换器（DiT），在每个DiT块中嵌入MoCA层，分层时间池用于捕捉身份特征，交叉注意力专家用于建模时空关系。

**关键创新**：MoCA的主要创新在于混合交叉注意力机制的引入，使得模型能够更好地处理身份一致性问题，这与传统方法的静态注意力机制形成鲜明对比。

**关键设计**：模型中采用了潜在视频感知损失函数，以增强视频帧之间的身份一致性和细节表现，同时在数据集CelebIPVid上进行训练，确保模型的跨种族泛化能力。

## 📊 实验亮点

在CelebIPVid数据集上的实验结果显示，MoCA在面部相似性方面比现有的文本到视频生成方法提高了超过5%的性能，证明了其在身份保持和细节捕捉方面的显著优势。

## 🎯 应用场景

该研究在影视制作、游戏开发和虚拟现实等领域具有广泛的应用潜力。通过提高文本到视频生成的身份保持能力，MoCA可以帮助创作者生成更高质量的内容，增强用户体验。此外，随着技术的进步，未来可能在个性化视频生成和自动化内容创作中发挥重要作用。

## 📄 摘要（原文）

> Achieving ID-preserving text-to-video (T2V) generation remains challenging despite recent advances in diffusion-based models. Existing approaches often fail to capture fine-grained facial dynamics or maintain temporal identity coherence. To address these limitations, we propose MoCA, a novel Video Diffusion Model built on a Diffusion Transformer (DiT) backbone, incorporating a Mixture of Cross-Attention mechanism inspired by the Mixture-of-Experts paradigm. Our framework improves inter-frame identity consistency by embedding MoCA layers into each DiT block, where Hierarchical Temporal Pooling captures identity features over varying timescales, and Temporal-Aware Cross-Attention Experts dynamically model spatiotemporal relationships. We further incorporate a Latent Video Perceptual Loss to enhance identity coherence and fine-grained details across video frames. To train this model, we collect CelebIPVid, a dataset of 10,000 high-resolution videos from 1,000 diverse individuals, promoting cross-ethnicity generalization. Extensive experiments on CelebIPVid show that MoCA outperforms existing T2V methods by over 5% across Face similarity.

