---
layout: default
title: LongVie 2: Multimodal Controllable Ultra-Long Video World Model
---

# LongVie 2: Multimodal Controllable Ultra-Long Video World Model

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.13604" class="toolbar-btn" target="_blank">📄 arXiv: 2512.13604v1</a>
  <a href="https://arxiv.org/pdf/2512.13604.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.13604v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.13604v1', 'LongVie 2: Multimodal Controllable Ultra-Long Video World Model')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Jianxiong Gao, Zhaoxi Chen, Xian Liu, Junhao Zhuang, Chengming Xu, Jianfeng Feng, Yu Qiao, Yanwei Fu, Chenyang Si, Ziwei Liu

**分类**: cs.CV

**发布日期**: 2025-12-15

**备注**: Project Page: https://vchitect.github.io/LongVie2-project/

---

## 💡 一句话要点

**LongVie 2：多模态可控超长视频世界模型，实现高质量长时序视频生成。**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `视频世界模型` `长视频生成` `多模态控制` `自回归模型` `时间一致性` `视觉质量` `可控视频生成` `视频生成基准`

## 📋 核心要点

1. 现有视频世界模型在可控性、长期视觉质量和时间一致性方面存在挑战，难以生成高质量长时序视频。
2. LongVie 2通过多模态指导增强可控性，退化感知训练保持视觉质量，历史上下文指导确保时间一致性。
3. LongVie 2在LongVGenBench基准测试中表现出色，实现了最先进的性能，并支持长达五分钟的连续视频生成。

## 📝 摘要（中文）

构建于预训练视频生成系统之上的视频世界模型是通往通用时空智能的重要一步，但也极具挑战。一个世界模型应具备三个基本属性：可控性、长期视觉质量和时间一致性。为此，我们采取了一种渐进式的方法——首先增强可控性，然后扩展到长期、高质量的生成。我们提出了LongVie 2，一个端到端的自回归框架，通过三个阶段进行训练：（1）多模态指导，整合密集和稀疏控制信号，提供隐式的世界级监督，并提高可控性；（2）输入帧上的退化感知训练，弥合训练和长期推理之间的差距，以保持高视觉质量；（3）历史上下文指导，对齐相邻片段之间的上下文信息，以确保时间一致性。我们进一步推出了LongVGenBench，一个包含100个高分辨率一分钟视频的综合基准，涵盖了各种真实和合成环境。大量实验表明，LongVie 2在长程可控性、时间连贯性和视觉保真度方面达到了最先进的性能，并支持长达五分钟的连续视频生成，标志着朝着统一视频世界建模迈出了重要一步。

## 🔬 方法详解

**问题定义**：论文旨在解决视频世界模型在生成长时序视频时面临的可控性差、视觉质量下降以及时间一致性难以保持的问题。现有方法通常难以同时兼顾这三个方面，尤其是在生成超长视频时，问题会更加突出。

**核心思路**：LongVie 2的核心思路是采用一种渐进式的训练策略，分阶段地解决可控性、视觉质量和时间一致性问题。首先通过多模态指导增强模型的可控性，然后通过退化感知训练来提升长期视觉质量，最后通过历史上下文指导来保证时间一致性。

**技术框架**：LongVie 2是一个端到端的自回归框架，包含三个主要的训练阶段：
1. **多模态指导**：整合密集和稀疏控制信号，例如语义分割图、动作指令等，为视频生成提供更丰富的控制信息。
2. **退化感知训练**：通过在训练过程中模拟视频帧的退化现象，例如模糊、噪声等，来提高模型在长期推理过程中的鲁棒性，从而保持视觉质量。
3. **历史上下文指导**：利用相邻视频片段的上下文信息，例如前一帧的隐藏状态，来指导当前帧的生成，从而保证时间一致性。

**关键创新**：LongVie 2的关键创新在于其综合利用了多模态信息、退化感知训练和历史上下文信息，从而在可控性、视觉质量和时间一致性方面都取得了显著的提升。与现有方法相比，LongVie 2能够生成更长、更逼真、更可控的视频。

**关键设计**：
* **多模态融合**：采用注意力机制将不同模态的控制信号融合到视频生成过程中。
* **退化模型**：设计多种退化模型来模拟真实视频中可能出现的各种退化现象。
* **损失函数**：采用对抗损失、感知损失和时间一致性损失等多种损失函数来优化模型。

## 📊 实验亮点

LongVie 2在LongVGenBench基准测试中，相比现有方法，在长程可控性、时间连贯性和视觉保真度方面均取得了显著提升。实验结果表明，LongVie 2能够生成长达五分钟的连续视频，并且在视觉质量和时间一致性方面表现出色。

## 🎯 应用场景

LongVie 2在游戏开发、电影制作、虚拟现实、机器人控制等领域具有广泛的应用前景。它可以用于生成逼真的游戏场景、创建高质量的电影特效、构建沉浸式的虚拟现实体验，以及训练机器人在复杂环境中的行为。

## 📄 摘要（原文）

> Building video world models upon pretrained video generation systems represents an important yet challenging step toward general spatiotemporal intelligence. A world model should possess three essential properties: controllability, long-term visual quality, and temporal consistency. To this end, we take a progressive approach-first enhancing controllability and then extending toward long-term, high-quality generation. We present LongVie 2, an end-to-end autoregressive framework trained in three stages: (1) Multi-modal guidance, which integrates dense and sparse control signals to provide implicit world-level supervision and improve controllability; (2) Degradation-aware training on the input frame, bridging the gap between training and long-term inference to maintain high visual quality; and (3) History-context guidance, which aligns contextual information across adjacent clips to ensure temporal consistency. We further introduce LongVGenBench, a comprehensive benchmark comprising 100 high-resolution one-minute videos covering diverse real-world and synthetic environments. Extensive experiments demonstrate that LongVie 2 achieves state-of-the-art performance in long-range controllability, temporal coherence, and visual fidelity, and supports continuous video generation lasting up to five minutes, marking a significant step toward unified video world modeling.

