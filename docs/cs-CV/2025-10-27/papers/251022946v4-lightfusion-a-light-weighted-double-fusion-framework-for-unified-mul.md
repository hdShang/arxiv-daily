---
layout: default
title: LightFusion: A Light-weighted, Double Fusion Framework for Unified Multimodal Understanding and Generation
---

# LightFusion: A Light-weighted, Double Fusion Framework for Unified Multimodal Understanding and Generation

<div class="paper-toolbar">
  <div class="toolbar-left">
    <a href="https://arxiv.org/abs/2510.22946" target="_blank" class="toolbar-btn">arXiv: 2510.22946v4</a>
    <a href="https://arxiv.org/pdf/2510.22946.pdf" target="_blank" class="toolbar-btn">PDF</a>
  </div>
  <div class="toolbar-right">
    <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.22946v4" 
            onclick="toggleFavorite(this, '2510.22946v4', 'LightFusion: A Light-weighted, Double Fusion Framework for Unified Multimodal Understanding and Generation')" title="收藏">
      ☆ 收藏
    </button>
    <button class="toolbar-btn share-btn" onclick="copyLink()" title="复制链接">
      🔗 分享
    </button>
  </div>
</div>


**作者**: Zeyu Wang, Zilong Chen, Chenhui Gou, Feng Li, Chaorui Deng, Deyao Zhu, Kunchang Li, Weihao Yu, Haoqin Tu, Haoqi Fan, Cihang Xie

**分类**: cs.CV

**发布日期**: 2025-10-27 (更新: 2025-11-20)

**备注**: Preprint. Work in progress

---

## 💡 一句话要点

**LightFusion：轻量级双重融合框架，用于统一多模态理解与生成**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多模态融合` `文本到图像生成` `图像编辑` `轻量级模型` `预训练模型`

## 📋 核心要点

1. 现有统一多模态模型训练成本高昂，需要大量计算资源，限制了其应用和发展。
2. LightFusion通过双重融合机制，有效融合预训练的生成和理解模型，降低训练成本，同时保持性能。
3. 实验表明，LightFusion在多个文本到图像生成和图像编辑基准测试中取得了优异的性能，证明了其有效性。

## 📝 摘要（中文）

统一多模态模型最近在能力和通用性方面表现出显著的提升，但大多数领先系统仍然是从头开始训练，并且需要大量的计算资源。本文表明，通过策略性地融合公开可用的、专门用于生成或理解的模型，可以更有效地获得具有竞争力的性能。我们的关键设计是保留原始模块，同时在网络中穿插多模态自注意力模块。这种双重融合机制（1）有效地实现了丰富的多模态融合，同时在很大程度上保留了基础模型的原始优势，并且（2）促进了来自理解编码器的高级语义表示与来自生成编码器的低级空间信号的协同融合。通过仅使用约350亿个token进行训练，该方法在多个基准测试中取得了强大的结果：在GenEval上，组合文本到图像生成达到0.91；在DPG-Bench上，复杂文本到图像生成达到82.16；在GEditBench上，图像编辑达到6.06；在ImgEdit-Bench上，图像编辑达到3.77。我们完全发布了整套代码、模型权重和数据集，希望支持未来对统一多模态建模的研究。

## 🔬 方法详解

**问题定义**：现有统一多模态模型通常需要从头开始训练，这导致了巨大的计算资源消耗和时间成本。此外，如何有效地融合不同模态的信息，特别是如何将理解模型中的高级语义信息与生成模型中的低级空间信息相结合，仍然是一个挑战。

**核心思路**：LightFusion的核心思路是利用预训练的、分别擅长生成和理解的模型，通过一种轻量级的融合机制，将它们的能力结合起来。这种方法避免了从头开始训练的需要，大大降低了计算成本。同时，通过精心设计的融合模块，实现了不同模态信息的有效交互。

**技术框架**：LightFusion框架主要包含两个预训练的编码器：一个用于理解（例如，文本编码器），另一个用于生成（例如，图像编码器）。这两个编码器的原始模块被保留，并在其中穿插多模态自注意力模块。这些自注意力模块负责融合来自不同模态的信息。整个框架通过一个统一的损失函数进行训练，以优化多模态理解和生成的能力。

**关键创新**：LightFusion的关键创新在于其双重融合机制。一方面，它保留了预训练模型的原始模块，从而继承了它们的固有优势。另一方面，它通过穿插多模态自注意力模块，实现了不同模态信息的有效融合。这种双重融合机制使得模型既能保持高性能，又能降低训练成本。

**关键设计**：LightFusion的关键设计包括：(1) 选择合适的预训练模型作为基础编码器；(2) 设计高效的多模态自注意力模块，以实现不同模态信息的有效交互；(3) 使用合适的损失函数，以优化多模态理解和生成的能力。具体的参数设置和网络结构细节需要在实际应用中进行调整和优化。

## 📊 实验亮点

LightFusion在GenEval（组合文本到图像生成）上取得了0.91的成绩，在DPG-Bench（复杂文本到图像生成）上取得了82.16的成绩，在GEditBench和ImgEdit-Bench（图像编辑）上分别取得了6.06和3.77的成绩。这些结果表明，LightFusion在多个多模态任务上都取得了具有竞争力的性能，证明了其有效性。

## 🎯 应用场景

LightFusion具有广泛的应用前景，包括文本到图像生成、图像编辑、视觉问答、多模态对话等。该研究降低了统一多模态模型的训练成本，使得更多研究者和开发者能够参与到多模态人工智能的研究和应用中来。未来，LightFusion可以应用于智能设计、内容创作、人机交互等领域。

## 📄 摘要（原文）

> Unified multimodal models have recently shown remarkable gains in both capability and versatility, yet most leading systems are still trained from scratch and require substantial computational resources. In this paper, we show that competitive performance can be obtained far more efficiently by strategically fusing publicly available models specialized for either generation or understanding. Our key design is to retain the original blocks while additionally interleaving multimodal self-attention blocks throughout the networks. This double fusion mechanism (1) effectively enables rich multi-modal fusion while largely preserving the original strengths of the base models, and (2) catalyzes synergistic fusion of high-level semantic representations from the understanding encoder with low-level spatial signals from the generation encoder. By training with only ~ 35B tokens, this approach achieves strong results across multiple benchmarks: 0.91 on GenEval for compositional text-to-image generation, 82.16 on DPG-Bench for complex text-to-image generation, 6.06 on GEditBench, and 3.77 on ImgEdit-Bench for image editing. By fully releasing the entire suite of code, model weights, and datasets, we hope to support future research on unified multimodal modeling.

