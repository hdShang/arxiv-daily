---
layout: default
title: "QPoser: Quantized Explicit Pose Prior Modeling for Controllable Pose Generation"
---

# QPoser: Quantized Explicit Pose Prior Modeling for Controllable Pose Generation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2312.01104" class="toolbar-btn" target="_blank">📄 arXiv: 2312.01104v1</a>
  <a href="https://arxiv.org/pdf/2312.01104.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2312.01104v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2312.01104v1', 'QPoser: Quantized Explicit Pose Prior Modeling for Controllable Pose Generation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yumeng Li, Yaoxiang Ding, Zhong Ren, Kun Zhou

**分类**: cs.CV

**发布日期**: 2023-12-02

---

## 💡 一句话要点

**QPoser：量化的显式姿态先验模型，实现可控的姿态生成**

🎯 **匹配领域**: **支柱四：生成式动作 (Generative Motion)**

**关键词**: `姿态生成` `显式姿态先验` `向量量化` `自编码器` `可控生成`

## 📋 核心要点

1. 现有显式姿态先验模型难以兼顾姿态生成的正确性、表达性和可控性，尤其在可控性方面表现不足。
2. QPoser通过多头向量量化自编码器（MS-VQVAE）和全局-局部特征融合机制（GLIF-AE）来提升姿态表示的表达性和可控性。
3. 实验表明，QPoser在姿态表达和正确性上优于现有方法，并能方便地用于条件姿态生成，例如基于参考姿态和指令生成。

## 📝 摘要（中文）

本文提出了一种名为QPoser的高可控显式姿态先验模型，该模型保证了姿态生成的正确性和表达性。现有的显式姿态先验模型在正确性、表达性和可控性三个方面无法同时满足，尤其是在可控性方面。为了解决这个问题，QPoser采用多头向量量化自编码器（MS-VQVAE）来获得富有表现力的分布式姿态表示。此外，利用全局-局部特征融合机制（GLIF-AE）来解耦潜在表示，并将全身信息整合到局部关节特征中。实验结果表明，QPoser在表示富有表现力和正确的姿态方面明显优于现有方法，同时可以方便地用于从参考姿态和提示指令进行详细的条件生成。

## 🔬 方法详解

**问题定义**：论文旨在解决现有显式姿态先验模型在姿态生成任务中，难以同时保证正确性（生成物理上可行的姿态）、表达性（保留姿态细节）和可控性（易于从参考姿态和指令生成）的问题。现有方法通常在可控性方面表现较差，限制了其在下游任务中的应用。

**核心思路**：QPoser的核心思路是利用量化的潜在空间表示姿态，并通过解耦潜在表示和融合全局-局部特征来增强姿态的可控性。通过量化，可以更好地约束潜在空间，从而保证生成姿态的正确性。通过解耦和融合特征，可以更好地控制姿态的各个部分，从而实现更精细的条件生成。

**技术框架**：QPoser主要包含两个核心模块：多头向量量化自编码器（MS-VQVAE）和全局-局部特征融合自编码器（GLIF-AE）。MS-VQVAE用于学习姿态的量化潜在表示，将姿态编码为离散的码本索引。GLIF-AE则用于解耦潜在表示，并将全局的全身信息融入到局部的关节特征中，从而增强可控性。整体流程是先通过MS-VQVAE将姿态编码为量化码本索引，然后通过GLIF-AE进行特征解耦和融合，最后解码生成姿态。

**关键创新**：QPoser的关键创新在于将向量量化（VQ）引入到姿态先验建模中，并结合全局-局部特征融合机制。VQ能够有效地约束潜在空间，保证生成姿态的物理可行性。全局-局部特征融合则能够解耦潜在表示，使得可以独立控制姿态的各个部分，从而实现更精细的条件生成。与现有方法相比，QPoser在可控性方面具有显著优势。

**关键设计**：MS-VQVAE采用多头设计，每个头学习不同的码本，从而提高表示能力。GLIF-AE使用自注意力机制来融合全局和局部特征。损失函数包括重构损失、量化损失和对抗损失，用于保证生成姿态的质量和多样性。具体的网络结构和参数设置在论文中有详细描述，例如码本大小、隐藏层维度、注意力头数等。

## 📊 实验亮点

实验结果表明，QPoser在姿态表达和正确性方面优于现有方法。例如，在Human3.6M数据集上，QPoser在重构误差和姿态合理性指标上均取得了显著提升。此外，QPoser在条件姿态生成任务中表现出色，能够根据参考姿态和提示指令生成高质量的姿态，证明了其良好的可控性。

## 🎯 应用场景

QPoser可应用于各种姿态相关的下游任务，例如动画生成、动作捕捉、人机交互、虚拟现实和增强现实等。通过控制参考姿态和提示指令，可以生成各种各样的姿态，从而为这些应用提供更灵活和可控的姿态生成能力。该研究的实际价值在于提高了姿态生成的可控性和真实感，未来可能促进更自然和逼真的人机交互体验。

## 📄 摘要（原文）

> Explicit pose prior models compress human poses into latent representations for using in pose-related downstream tasks. A desirable explicit pose prior model should satisfy three desirable abilities: 1) correctness, i.e. ensuring to generate physically possible poses; 2) expressiveness, i.e. ensuring to preserve details in generation; 3) controllability, meaning that generation from reference poses and explicit instructions should be convenient. Existing explicit pose prior models fail to achieve all of three properties, in special controllability. To break this situation, we propose QPoser, a highly controllable explicit pose prior model which guarantees correctness and expressiveness. In QPoser, a multi-head vector quantized autoencoder (MS-VQVAE) is proposed for obtaining expressive and distributed pose representations. Furthermore, a global-local feature integration mechanism (GLIF-AE) is utilized to disentangle the latent representation and integrate full-body information into local-joint features. Experimental results show that QPoser significantly outperforms state-of-the-art approaches in representing expressive and correct poses, meanwhile is easily to be used for detailed conditional generation from reference poses and prompting instructions.

