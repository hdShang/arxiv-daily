---
layout: default
title: "Lynx: Towards High-Fidelity Personalized Video Generation"
---

# Lynx: Towards High-Fidelity Personalized Video Generation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.15496" class="toolbar-btn" target="_blank">📄 arXiv: 2509.15496v1</a>
  <a href="https://arxiv.org/pdf/2509.15496.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.15496v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.15496v1', 'Lynx: Towards High-Fidelity Personalized Video Generation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Shen Sang, Tiancheng Zhi, Tianpei Gu, Jing Liu, Linjie Luo

**分类**: cs.CV

**发布日期**: 2025-09-19

**备注**: Lynx Technical Report

---

## 💡 一句话要点

**Lynx：面向高保真个性化视频生成的扩散Transformer模型**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `个性化视频生成` `扩散Transformer` `身份保持` `视频合成` `DiT` `Perceiver Resampler` `VAE` `交叉注意力`

## 📋 核心要点

1. 现有方法在个性化视频生成中难以兼顾身份保持、时间一致性和视觉质量，面临诸多挑战。
2. Lynx通过ID-adapter和Ref-adapter两个轻量级模块，分别从身份嵌入和参考图像中提取信息，增强身份保真度。
3. 实验表明，Lynx在面部相似性、提示遵循和视频质量方面均表现出色，显著提升了个性化视频生成的水平。

## 📝 摘要（中文）

本文提出Lynx，一个基于单张输入图像的高保真个性化视频合成模型。Lynx构建于开源的扩散Transformer (DiT) 基础模型之上，引入了两个轻量级的适配器以确保身份保真度。ID-adapter采用Perceiver Resampler将ArcFace导出的面部嵌入转换为紧凑的身份tokens用于条件控制；Ref-adapter集成了来自冻结参考路径的密集VAE特征，通过交叉注意力在所有Transformer层中注入细粒度的细节。这些模块共同实现了强大的身份保持，同时保持了时间一致性和视觉真实感。在包含40个对象和20个无偏提示的基准测试中（共800个测试用例），Lynx展示了卓越的面部相似性、有竞争力的提示遵循能力和强大的视频质量，从而推进了个性化视频生成的技术水平。

## 🔬 方法详解

**问题定义**：论文旨在解决从单张图像生成个性化视频的问题。现有方法在保持生成视频中人物身份的保真度、维持视频的时间一致性以及保证视频的视觉质量方面存在不足，难以同时满足这些要求。

**核心思路**：论文的核心思路是利用扩散Transformer (DiT) 作为基础模型，并引入两个轻量级的适配器（ID-adapter和Ref-adapter）来分别处理身份信息和参考图像的细节信息。通过这种方式，模型能够更好地学习和保持人物的身份特征，并生成高质量的视频。

**技术框架**：Lynx的整体框架包括以下几个主要模块：1) 基于DiT的视频生成主干网络；2) ID-adapter，用于提取和编码身份信息；3) Ref-adapter，用于提取和编码参考图像的细节信息。ID-adapter使用Perceiver Resampler将ArcFace提取的面部嵌入转换为身份tokens，Ref-adapter则利用VAE提取参考图像的密集特征。这两个适配器的输出通过交叉注意力机制注入到DiT的各个Transformer层中。

**关键创新**：论文的关键创新在于提出了ID-adapter和Ref-adapter这两个轻量级且有效的适配器。ID-adapter能够将高维的面部嵌入压缩成紧凑的身份tokens，从而降低计算复杂度并提高效率。Ref-adapter则能够将参考图像的细粒度细节注入到视频生成过程中，从而提高视频的视觉质量。

**关键设计**：ID-adapter使用Perceiver Resampler来处理面部嵌入，该模块能够将不同长度的输入序列转换为固定长度的输出序列。Ref-adapter使用预训练的VAE来提取参考图像的特征，并使用交叉注意力机制将这些特征注入到DiT的各个Transformer层中。损失函数方面，论文可能采用了标准的扩散模型训练损失，并可能针对身份保持和视频质量添加了额外的正则化项（具体细节未知）。

## 📊 实验亮点

Lynx在包含40个对象和20个无偏提示的基准测试中表现出色，共计800个测试用例。实验结果表明，Lynx在面部相似性方面取得了显著的提升，同时在提示遵循和视频质量方面也具有竞争力。相较于其他个性化视频生成方法，Lynx能够生成更逼真、更符合用户期望的视频内容。

## 🎯 应用场景

Lynx具有广泛的应用前景，包括虚拟化身生成、个性化内容创作、电影特效制作、游戏角色定制等。该技术可以帮助用户轻松创建逼真且个性化的视频内容，极大地丰富了数字娱乐和社交体验。未来，该技术有望应用于更广泛的领域，例如教育、医疗和工业等。

## 📄 摘要（原文）

> We present Lynx, a high-fidelity model for personalized video synthesis from a single input image. Built on an open-source Diffusion Transformer (DiT) foundation model, Lynx introduces two lightweight adapters to ensure identity fidelity. The ID-adapter employs a Perceiver Resampler to convert ArcFace-derived facial embeddings into compact identity tokens for conditioning, while the Ref-adapter integrates dense VAE features from a frozen reference pathway, injecting fine-grained details across all transformer layers through cross-attention. These modules collectively enable robust identity preservation while maintaining temporal coherence and visual realism. Through evaluation on a curated benchmark of 40 subjects and 20 unbiased prompts, which yielded 800 test cases, Lynx has demonstrated superior face resemblance, competitive prompt following, and strong video quality, thereby advancing the state of personalized video generation.

