---
layout: default
title: Universal Acoustic Adversarial Attacks for Flexible Control of Speech-LLMs
---

# Universal Acoustic Adversarial Attacks for Flexible Control of Speech-LLMs

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.14286" class="toolbar-btn" target="_blank">📄 arXiv: 2505.14286v1</a>
  <a href="https://arxiv.org/pdf/2505.14286.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.14286v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.14286v1', 'Universal Acoustic Adversarial Attacks for Flexible Control of Speech-LLMs')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Rao Ma, Mengjie Qian, Vyas Raina, Mark Gales, Kate Knill

**分类**: cs.CL, cs.SD, eess.AS

**发布日期**: 2025-05-20

---

## 💡 一句话要点

**提出通用声学对抗攻击以灵活控制语音大语言模型**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `对抗攻击` `语音大语言模型` `声学特征` `输入属性选择` `模型安全性`

## 📋 核心要点

1. 现有的语音大语言模型在灵活性上表现优异，但也因此暴露出对抗攻击的脆弱性。
2. 本文提出了一种通用声学对抗攻击方法，通过在输入音频前附加固定的对抗音频段来控制模型输出。
3. 实验结果显示，针对特定输入属性的选择性攻击能够有效影响模型输出，揭示了现有模型的安全隐患。

## 📝 摘要（中文）

随着预训练语音编码器与大型语言模型的结合，语音大语言模型（Speech LLMs）能够处理多种口语语言处理任务。然而，这种灵活性也使得模型更容易受到对抗攻击。本文研究了对语音大语言模型的通用声学对抗攻击，提出将固定的对抗音频段附加到原始输入音频上。研究发现，这种攻击可以导致模型不输出结果或执行修改后的任务，同时还可以选择性激活，针对特定输入属性如说话者性别或语言。研究结果揭示了Qwen2-Audio和Granite-Speech的关键脆弱性，强调了需要更强的训练策略以提高对抗攻击的抵抗力。

## 🔬 方法详解

**问题定义**：本文旨在解决语音大语言模型在灵活性带来的对抗攻击脆弱性问题。现有方法未能有效抵御针对特定输入属性的攻击，导致模型输出不稳定。

**核心思路**：论文提出的核心思路是使用固定的对抗音频段，附加到原始输入音频上，以实现对模型输出的灵活控制。这种设计允许攻击在特定条件下激活，从而不影响其他输入。

**技术框架**：整体架构包括对抗音频生成、输入音频处理和模型输出控制三个主要模块。首先生成通用对抗音频段，然后将其与原始输入音频结合，最后通过模型进行处理以观察输出变化。

**关键创新**：最重要的技术创新在于提出了选择性激活的对抗攻击策略，使得攻击能够针对特定属性而非普遍影响，从而实现更精细的控制。这与现有方法的广泛影响形成鲜明对比。

**关键设计**：在参数设置上，选择了适合的对抗音频长度和频率特征，同时采用了特定的损失函数以优化对抗效果。网络结构上，结合了预训练的语音编码器与语言模型，以增强对抗攻击的效果。

## 📊 实验亮点

实验结果表明，针对Qwen2-Audio和Granite-Speech的对抗攻击成功率显著，能够使模型在特定输入条件下产生错误输出。研究显示，选择性激活的攻击策略在特定属性下的影响力更强，揭示了模型的安全隐患。

## 🎯 应用场景

该研究的潜在应用领域包括语音识别、语音合成和人机交互等。通过提高模型对对抗攻击的抵抗力，可以增强语音大语言模型在实际应用中的安全性和可靠性，进而推动智能语音技术的发展。

## 📄 摘要（原文）

> The combination of pre-trained speech encoders with large language models has enabled the development of speech LLMs that can handle a wide range of spoken language processing tasks. While these models are powerful and flexible, this very flexibility may make them more vulnerable to adversarial attacks. To examine the extent of this problem, in this work we investigate universal acoustic adversarial attacks on speech LLMs. Here a fixed, universal, adversarial audio segment is prepended to the original input audio. We initially investigate attacks that cause the model to either produce no output or to perform a modified task overriding the original prompt. We then extend the nature of the attack to be selective so that it activates only when specific input attributes, such as a speaker gender or spoken language, are present. Inputs without the targeted attribute should be unaffected, allowing fine-grained control over the model outputs. Our findings reveal critical vulnerabilities in Qwen2-Audio and Granite-Speech and suggest that similar speech LLMs may be susceptible to universal adversarial attacks. This highlights the need for more robust training strategies and improved resistance to adversarial attacks.

