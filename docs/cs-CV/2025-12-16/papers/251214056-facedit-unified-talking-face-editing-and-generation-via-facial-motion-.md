---
layout: default
title: FacEDiT: Unified Talking Face Editing and Generation via Facial Motion Infilling
---

# FacEDiT: Unified Talking Face Editing and Generation via Facial Motion Infilling

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.14056" class="toolbar-btn" target="_blank">📄 arXiv: 2512.14056</a>
  <a href="https://arxiv.org/pdf/2512.14056.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.14056" onclick="toggleFavorite(this, '2512.14056', 'FacEDiT: Unified Talking Face Editing and Generation via Facial Motion Infilling')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Kim Sung-Bin, Joohyun Chang, David Harwath, Tae-Hyun Oh

**分类**: cs.CV, cs.AI

**发布日期**: 2025-12-18

---

## 💡 一句话要点

**FacEDiT：通过面部运动填充统一实现说话人脸编辑与生成**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `说话人脸编辑` `人脸生成` `面部运动填充` `扩散Transformer` `语音条件生成`

## 📋 核心要点

1. 现有的说话人脸编辑和生成通常被视为独立的问题，缺乏统一的建模框架，限制了它们之间的相互借鉴和性能提升。
2. FacEDiT将说话人脸编辑和生成统一建模为语音条件下的面部运动填充任务，利用扩散Transformer学习合成被掩盖的面部运动。
3. 实验表明，FacEDiT在说话人脸编辑和生成任务上均表现出色，实现了准确的语音对齐、身份保持和平滑的视觉效果。

## 📝 摘要（中文）

本文提出了一种统一的视角，将说话人脸编辑和人脸生成视为语音条件下的面部运动填充的子任务。我们探索了面部运动填充作为一种自监督的预训练任务，它也作为动态说话人脸合成的统一公式。为了实现这个想法，我们提出了FacEDiT，一个使用流匹配训练的语音条件扩散Transformer。受到掩码自编码器的启发，FacEDiT学习合成被掩盖的面部运动，条件是周围的运动和语音。这种公式能够实现局部生成和编辑，例如替换、插入和删除，同时确保与未编辑区域的无缝过渡。此外，有偏注意力机制和时间平滑约束增强了边界连续性和唇部同步。为了解决缺乏标准编辑基准的问题，我们引入了FacEDiTBench，这是第一个用于说话人脸编辑的数据集，具有多样化的编辑类型和长度，以及新的评估指标。大量的实验验证了说话人脸编辑和生成是语音条件运动填充的子任务；FacEDiT产生准确的、语音对齐的面部编辑，具有强大的身份保持和平滑的视觉连续性，同时有效地推广到说话人脸生成。

## 🔬 方法详解

**问题定义**：论文旨在解决说话人脸编辑和生成任务，现有方法通常将二者视为独立问题，缺乏统一的建模框架，导致无法充分利用彼此的信息，限制了性能提升。此外，缺乏标准的说话人脸编辑数据集和评估指标，阻碍了相关研究的进展。

**核心思路**：论文的核心思路是将说话人脸编辑和生成统一建模为语音条件下的面部运动填充任务。通过学习在给定语音和周围运动的情况下填充缺失的面部运动，模型可以同时实现编辑和生成功能。这种统一的视角使得模型能够更好地利用语音信息和上下文信息，从而生成更自然、更逼真的说话人脸。

**技术框架**：FacEDiT采用基于扩散Transformer的架构。整体流程如下：首先，输入语音和部分面部运动序列（部分被mask）。然后，扩散Transformer根据语音和未被mask的运动序列，预测被mask部分的运动。最后，通过流匹配训练，优化模型，使其能够生成高质量的面部运动序列。

**关键创新**：论文的关键创新在于将说话人脸编辑和生成统一建模为语音条件下的面部运动填充任务。此外，论文还提出了FacEDiTBench数据集，这是一个专门用于说话人脸编辑的数据集，包含多种编辑类型和长度，并提供了新的评估指标。

**关键设计**：FacEDiT的关键设计包括：1) 使用扩散Transformer作为生成模型，能够生成高质量的面部运动序列；2) 采用流匹配训练方法，提高训练效率和稳定性；3) 引入有偏注意力机制，增强边界连续性；4) 采用时间平滑约束，保证唇部同步；5) FacEDiTBench数据集，包含多样化的编辑类型和长度，以及新的评估指标。

## 📊 实验亮点

实验结果表明，FacEDiT在说话人脸编辑和生成任务上均取得了显著的性能提升。与现有方法相比，FacEDiT能够生成更准确、语音对齐的面部编辑，同时保持强大的身份信息和平滑的视觉连续性。此外，FacEDiT在FacEDiTBench数据集上表现出色，验证了其在说话人脸编辑任务上的有效性。

## 🎯 应用场景

FacEDiT在视频会议、虚拟助手、电影制作、游戏开发等领域具有广泛的应用前景。例如，可以用于实时编辑视频会议中的人脸表情，创建更逼真的虚拟助手，或者在电影制作中生成高质量的说话人脸动画。该研究的未来影响在于推动人机交互和数字内容创作的发展。

## 📄 摘要（原文）

> Talking face editing and face generation have often been studied as distinct problems. In this work, we propose viewing both not as separate tasks but as subtasks of a unifying formulation, speech-conditional facial motion infilling. We explore facial motion infilling as a self-supervised pretext task that also serves as a unifying formulation of dynamic talking face synthesis. To instantiate this idea, we propose FacEDiT, a speech-conditional Diffusion Transformer trained with flow matching. Inspired by masked autoencoders, FacEDiT learns to synthesize masked facial motions conditioned on surrounding motions and speech. This formulation enables both localized generation and edits, such as substitution, insertion, and deletion, while ensuring seamless transitions with unedited regions. In addition, biased attention and temporal smoothness constraints enhance boundary continuity and lip synchronization. To address the lack of a standard editing benchmark, we introduce FacEDiTBench, the first dataset for talking face editing, featuring diverse edit types and lengths, along with new evaluation metrics. Extensive experiments validate that talking face editing and generation emerge as subtasks of speech-conditional motion infilling; FacEDiT produces accurate, speech-aligned facial edits with strong identity preservation and smooth visual continuity while generalizing effectively to talking face generation.

