---
layout: default
title: EmoDiffTalk:Emotion-aware Diffusion for Editable 3D Gaussian Talking Head
---

# EmoDiffTalk:Emotion-aware Diffusion for Editable 3D Gaussian Talking Head

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.05991" class="toolbar-btn" target="_blank">📄 arXiv: 2512.05991v2</a>
  <a href="https://arxiv.org/pdf/2512.05991.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.05991v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.05991v2', 'EmoDiffTalk:Emotion-aware Diffusion for Editable 3D Gaussian Talking Head')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Chang Liu, Tianjiao Jing, Chengcheng Ma, Xuanqi Zhou, Zhengxuan Lian, Qin Jin, Hongliang Yuan, Shi-Sheng Huang

**分类**: cs.CV

**发布日期**: 2025-11-30 (更新: 2025-12-10)

---

## 💡 一句话要点

**EmoDiffTalk：提出情感感知扩散模型，用于可编辑的3D高斯说话头生成。**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱三：空间感知 (Perception & SLAM)**

**关键词**: `3D说话头生成` `高斯溅射` `扩散模型` `情感感知` `动作单元` `多模态编辑` `文本到AU` `可编辑性`

## 📋 核心要点

1. 现有的基于3D高斯溅射的逼真说话头在情感表达操控方面存在不足，尤其是在使用多模态控制进行细粒度和广泛的动态情感编辑时。
2. EmoDiffTalk提出了一种情感感知高斯扩散方法，通过动作单元（AU）提示和文本到AU情感控制器，实现精细的情感控制和编辑。
3. 实验结果表明，EmoDiffTalk在情感表达的微妙性、口型同步的准确性和可控性方面均优于现有技术，为高质量3D说话头合成提供了新途径。

## 📝 摘要（中文）

本文提出了一种新的可编辑3D高斯说话头框架，名为EmoDiffTalk。核心思想是引入一种情感感知高斯扩散方法，包括用于精细面部动画控制的动作单元（AU）提示高斯扩散过程，以及一个精确的文本到AU情感控制器，从而实现使用文本输入进行准确和广泛的动态情感编辑。在公共EmoTalk3D和RenderMe-360数据集上的实验表明，EmoDiffTalk在情感微妙性、口型同步保真度和可控性方面优于现有方法，为高质量、扩散驱动、多模态可编辑3D说话头合成建立了一条有效途径。据我们所知，EmoDiffTalk是首批支持基于AU表情空间进行连续、多模态情感编辑的3D高斯溅射说话头生成框架之一。

## 🔬 方法详解

**问题定义**：现有3D说话头生成方法，特别是基于3D高斯溅射的方法，在情感表达的精细控制和多模态情感编辑方面存在局限性。难以实现细粒度的情感操控，并且缺乏通过文本等模态进行广泛情感编辑的能力。

**核心思路**：EmoDiffTalk的核心思路是利用扩散模型生成具有情感表达的3D高斯说话头。通过将动作单元（AU）作为扩散过程的提示，并结合文本到AU的情感控制器，实现对情感的精确控制和编辑。这种方法能够生成更自然、更富有表现力的说话头。

**技术框架**：EmoDiffTalk框架主要包含以下几个模块：1) 3D高斯溅射表示模块，用于表示3D说话头；2) 动作单元（AU）提示高斯扩散模块，用于生成具有特定AU表情的3D高斯参数；3) 文本到AU情感控制器，用于将文本情感信息转换为AU参数；4) 渲染模块，用于将3D高斯参数渲染成图像。整个流程是从文本输入开始，通过情感控制器生成AU参数，然后利用AU提示高斯扩散模块生成3D高斯参数，最后渲染得到说话头图像。

**关键创新**：EmoDiffTalk的关键创新在于情感感知高斯扩散方法，它将动作单元（AU）作为扩散过程的提示，并结合文本到AU的情感控制器，实现了对情感的精细控制和编辑。此外，该框架是首批支持基于AU表情空间进行连续、多模态情感编辑的3D高斯溅射说话头生成框架之一。

**关键设计**：在AU提示高斯扩散模块中，使用了噪声预测网络来预测噪声，并通过迭代去噪过程生成3D高斯参数。文本到AU情感控制器采用Transformer结构，将文本情感信息映射到AU参数。损失函数包括重建损失、AU损失和对抗损失，用于保证生成图像的质量、AU表情的准确性和生成结果的真实性。

## 📊 实验亮点

EmoDiffTalk在EmoTalk3D和RenderMe-360数据集上进行了评估，实验结果表明，EmoDiffTalk在情感微妙性、口型同步保真度和可控性方面优于现有方法。尤其是在情感编辑方面，EmoDiffTalk能够生成更自然、更富有表现力的说话头，并且能够通过文本输入进行精确的情感控制。

## 🎯 应用场景

EmoDiffTalk具有广泛的应用前景，包括虚拟现实、增强现实、游戏、电影制作、在线教育和虚拟助手等领域。它可以用于创建更逼真、更具表现力的虚拟角色，提升用户体验。此外，该技术还可以应用于情感分析和情感计算等研究领域，帮助理解和模拟人类情感。

## 📄 摘要（原文）

> Recent photo-realistic 3D talking head via 3D Gaussian Splatting still has significant shortcoming in emotional expression manipulation, especially for fine-grained and expansive dynamics emotional editing using multi-modal control. This paper introduces a new editable 3D Gaussian talking head, i.e. EmoDiffTalk. Our key idea is a novel Emotion-aware Gaussian Diffusion, which includes an action unit (AU) prompt Gaussian diffusion process for fine-grained facial animator, and moreover an accurate text-to-AU emotion controller to provide accurate and expansive dynamic emotional editing using text input. Experiments on public EmoTalk3D and RenderMe-360 datasets demonstrate superior emotional subtlety, lip-sync fidelity, and controllability of our EmoDiffTalk over previous works, establishing a principled pathway toward high-quality, diffusion-driven, multimodal editable 3D talking-head synthesis. To our best knowledge, our EmoDiffTalk is one of the first few 3D Gaussian Splatting talking-head generation framework, especially supporting continuous, multimodal emotional editing within the AU-based expression space.

