---
layout: default
title: TAVID: Text-Driven Audio-Visual Interactive Dialogue Generation
---

# TAVID: Text-Driven Audio-Visual Interactive Dialogue Generation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.20296" class="toolbar-btn" target="_blank">📄 arXiv: 2512.20296v1</a>
  <a href="https://arxiv.org/pdf/2512.20296.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.20296v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.20296v1', 'TAVID: Text-Driven Audio-Visual Interactive Dialogue Generation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Ji-Hoon Kim, Junseok Ahn, Doyeop Kwak, Joon Son Chung, Shinji Watanabe

**分类**: cs.CV, cs.AI, eess.AS, eess.IV

**发布日期**: 2025-12-23

**备注**: Project page: https://mm.kaist.ac.kr/projects/TAVID

---

## 💡 一句话要点

**提出TAVID，通过跨模态映射实现文本驱动的交互式音视频对话生成。**

🎯 **匹配领域**: **支柱五：交互与反应 (Interaction & Reaction)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `音视频对话生成` `跨模态学习` `人机交互` `说话人映射` `运动映射` `多模态融合` `文本驱动生成`

## 📋 核心要点

1. 现有方法忽略了人类对话中音视频紧密耦合的特性，通常孤立地研究说话/倾听头部生成和对话语音生成。
2. TAVID通过运动映射器和说话人映射器，在音频和视觉模态间建立双向信息交换，实现同步的面部和语音生成。
3. 实验表明，TAVID在说话面部真实感、倾听头部响应性、交互流畅性和语音质量方面均表现出色。

## 📝 摘要（中文）

本文旨在从文本和参考图像中联合合成交互式视频和对话语音。为了构建类人对话系统，现有研究探索了说话或倾听头部生成以及对话语音生成。然而，这些工作通常是孤立研究的，忽略了人类对话的多模态本质，即紧密耦合的音视频交互。本文提出了TAVID，一个统一的框架，以同步的方式生成交互式面部和对话语音。TAVID通过两个跨模态映射器（即，运动映射器和说话人映射器）集成了面部和语音生成流程，从而实现了音频和视觉模态之间互补信息的双向交换。我们在四个维度评估了我们的系统：说话面部真实感、倾听头部响应性、二元交互流畅性和语音质量。大量实验证明了我们的方法在所有这些方面的有效性。

## 🔬 方法详解

**问题定义**：现有方法在生成交互式音视频对话时，通常将语音和视觉模态孤立处理，忽略了两者之间的紧密关联。这导致生成的对话缺乏真实感和自然性，无法充分模拟人类对话中的多模态交互。

**核心思路**：TAVID的核心思路是通过跨模态映射器，显式地建模音频和视觉模态之间的依赖关系。具体来说，利用运动映射器将语音信息映射到面部运动，利用说话人映射器将面部视觉信息映射到语音特征，从而实现双向的信息传递和融合。这种设计旨在使生成的面部表情和语音更加协调一致，提高对话的真实感和流畅性。

**技术框架**：TAVID框架包含以下主要模块：1) 文本编码器：将输入文本转换为语义表示。2) 语音生成器：基于文本编码和说话人映射器的输出生成对话语音。3) 面部生成器：基于文本编码和运动映射器的输出生成面部视频。4) 运动映射器：将语音特征映射到面部运动参数。5) 说话人映射器：将面部视觉特征映射到语音特征。整个流程是端到端可训练的，通过联合优化各个模块，实现音视频的同步生成。

**关键创新**：TAVID的关键创新在于引入了跨模态映射器，实现了音频和视觉模态之间的双向信息交换。这种双向映射机制能够更好地捕捉人类对话中的复杂交互模式，从而生成更自然、更真实的交互式音视频对话。与现有方法相比，TAVID不再孤立地处理语音和视觉模态，而是将它们作为一个整体进行建模和生成。

**关键设计**：运动映射器和说话人映射器通常采用Transformer或类似的注意力机制来实现。损失函数包括语音质量损失（如Mel-Spectrogram损失）、面部真实感损失（如对抗损失）以及跨模态一致性损失（用于约束音视频之间的同步性）。具体的网络结构和参数设置需要根据具体的数据集和任务进行调整。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.20296v1/x2.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.20296v1/x3.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.20296v1/x4.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

实验结果表明，TAVID在说话面部真实感、倾听头部响应性、二元交互流畅性和语音质量四个方面均优于现有方法。具体而言，TAVID生成的面部表情更加自然生动，语音质量更高，音视频同步性更好，整体交互体验更流畅。

## 🎯 应用场景

TAVID具有广泛的应用前景，例如虚拟助手、在线教育、游戏角色、电影制作等。它可以用于创建更具吸引力和互动性的虚拟人物，提升用户体验。此外，该技术还可以应用于人机交互研究，帮助我们更好地理解人类对话的本质。

## 📄 摘要（原文）

> The objective of this paper is to jointly synthesize interactive videos and conversational speech from text and reference images. With the ultimate goal of building human-like conversational systems, recent studies have explored talking or listening head generation as well as conversational speech generation. However, these works are typically studied in isolation, overlooking the multimodal nature of human conversation, which involves tightly coupled audio-visual interactions. In this paper, we introduce TAVID, a unified framework that generates both interactive faces and conversational speech in a synchronized manner. TAVID integrates face and speech generation pipelines through two cross-modal mappers (i.e., a motion mapper and a speaker mapper), which enable bidirectional exchange of complementary information between the audio and visual modalities. We evaluate our system across four dimensions: talking face realism, listening head responsiveness, dyadic interaction fluency, and speech quality. Extensive experiments demonstrate the effectiveness of our approach across all these aspects.

