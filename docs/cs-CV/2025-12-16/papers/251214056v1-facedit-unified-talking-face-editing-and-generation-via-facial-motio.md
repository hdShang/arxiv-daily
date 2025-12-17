---
layout: default
title: FacEDiT: Unified Talking Face Editing and Generation via Facial Motion Infilling
---

# FacEDiT: Unified Talking Face Editing and Generation via Facial Motion Infilling

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.14056" class="toolbar-btn" target="_blank">📄 arXiv: 2512.14056v1</a>
  <a href="https://arxiv.org/pdf/2512.14056.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.14056v1" onclick="toggleFavorite(this, '2512.14056v1', 'FacEDiT: Unified Talking Face Editing and Generation via Facial Motion Infilling')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Kim Sung-Bin, Joohyun Chang, David Harwath, Tae-Hyun Oh

**分类**: cs.CV, cs.AI

**发布日期**: 2025-12-16

**备注**: Project page: https://facedit.github.io/

---

## 💡 一句话要点

**FacEDiT：通过面部运动填充实现统一的说话人脸编辑与生成**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `说话人脸编辑` `人脸生成` `面部运动填充` `扩散模型` `Transformer`

## 📋 核心要点

1. 现有说话人脸编辑和生成方法通常被视为独立任务，忽略了它们之间的内在联系。
2. FacEDiT将二者统一为语音条件下的面部运动填充问题，利用扩散Transformer学习合成和编辑面部运动。
3. FacEDiT在FacEDiTBench数据集上验证了其有效性，实现了准确的语音对齐、身份保持和平滑过渡。

## 📝 摘要（中文）

本文提出了一种统一的视角，将说话人脸编辑和人脸生成视为语音条件下的面部运动填充的子任务。我们探索了面部运动填充作为一种自监督的预训练任务，它也作为动态说话人脸合成的统一公式。为了实现这个想法，我们提出了FacEDiT，一个使用流匹配训练的语音条件扩散Transformer。受到掩码自编码器的启发，FacEDiT学习合成被掩盖的面部运动，条件是周围的运动和语音。这种公式能够进行局部生成和编辑，例如替换、插入和删除，同时确保与未编辑区域的无缝过渡。此外，有偏注意力机制和时间平滑约束增强了边界连续性和唇部同步。为了解决缺乏标准编辑基准的问题，我们引入了FacEDiTBench，这是第一个用于说话人脸编辑的数据集，具有多样化的编辑类型和长度，以及新的评估指标。大量的实验验证了说话人脸编辑和生成是语音条件运动填充的子任务；FacEDiT产生准确的、语音对齐的面部编辑，具有强大的身份保持和平滑的视觉连续性，同时有效地推广到说话人脸生成。

## 🔬 方法详解

**问题定义**：现有方法通常将说话人脸编辑和生成视为两个独立的问题，缺乏统一的建模框架。这导致了模型在编辑和生成任务之间难以迁移，并且难以保证编辑区域与未编辑区域之间的平滑过渡。此外，缺乏专门用于说话人脸编辑的基准数据集，阻碍了该领域的研究进展。

**核心思路**：本文的核心思路是将说话人脸编辑和生成统一建模为语音条件下的面部运动填充问题。通过学习在给定语音和周围运动的情况下填充缺失的面部运动，模型可以同时实现编辑和生成。这种方法借鉴了掩码自编码器的思想，允许模型学习面部运动的上下文信息，从而实现平滑的过渡。

**技术框架**：FacEDiT的整体框架是一个语音条件扩散Transformer，它由以下几个主要模块组成：1) 语音编码器：将输入的语音信号编码成语音特征向量。2) 面部运动编码器：将输入的面部运动序列编码成运动特征向量。3) 扩散Transformer：一个基于Transformer的扩散模型，用于学习面部运动的分布，并根据语音和周围运动生成或编辑面部运动。4) 流匹配模块：用于训练扩散Transformer，通过最小化预测运动和真实运动之间的差异来优化模型。

**关键创新**：FacEDiT的关键创新在于将说话人脸编辑和生成统一建模为语音条件下的面部运动填充问题。这种统一的视角使得模型可以同时学习编辑和生成，并且能够保证编辑区域与未编辑区域之间的平滑过渡。此外，FacEDiT还引入了有偏注意力机制和时间平滑约束，以增强边界连续性和唇部同步。

**关键设计**：FacEDiT使用扩散Transformer作为其核心模型，并采用流匹配方法进行训练。扩散Transformer由多个Transformer块组成，每个块包含自注意力层和前馈神经网络。有偏注意力机制通过调整注意力权重，使得模型更加关注边界区域，从而增强边界连续性。时间平滑约束通过惩罚相邻帧之间的运动差异，从而保证运动的平滑性。损失函数包括流匹配损失、边界连续性损失和时间平滑损失。

## 📊 实验亮点

FacEDiT在FacEDiTBench数据集上取得了显著的成果，在多个编辑任务上优于现有方法。实验结果表明，FacEDiT能够生成准确的、语音对齐的面部编辑，同时保持强大的身份保持和平滑的视觉连续性。此外，FacEDiT还能够有效地推广到说话人脸生成任务。

## 🎯 应用场景

FacEDiT在虚拟形象定制、视频内容创作、在线会议等领域具有广泛的应用前景。它可以用于生成逼真的说话人脸视频，编辑现有的视频内容，以及改善在线交流的用户体验。未来，该技术有望应用于更复杂的场景，例如个性化教育、远程医疗等。

## 📄 摘要（原文）

> Talking face editing and face generation have often been studied as distinct problems. In this work, we propose viewing both not as separate tasks but as subtasks of a unifying formulation, speech-conditional facial motion infilling. We explore facial motion infilling as a self-supervised pretext task that also serves as a unifying formulation of dynamic talking face synthesis. To instantiate this idea, we propose FacEDiT, a speech-conditional Diffusion Transformer trained with flow matching. Inspired by masked autoencoders, FacEDiT learns to synthesize masked facial motions conditioned on surrounding motions and speech. This formulation enables both localized generation and edits, such as substitution, insertion, and deletion, while ensuring seamless transitions with unedited regions. In addition, biased attention and temporal smoothness constraints enhance boundary continuity and lip synchronization. To address the lack of a standard editing benchmark, we introduce FacEDiTBench, the first dataset for talking face editing, featuring diverse edit types and lengths, along with new evaluation metrics. Extensive experiments validate that talking face editing and generation emerge as subtasks of speech-conditional motion infilling; FacEDiT produces accurate, speech-aligned facial edits with strong identity preservation and smooth visual continuity while generalizing effectively to talking face generation.

