---
layout: default
title: "HapticVLM: VLM-Driven Texture Recognition Aimed at Intelligent Haptic Interaction"
---

# HapticVLM: VLM-Driven Texture Recognition Aimed at Intelligent Haptic Interaction

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.02569" class="toolbar-btn" target="_blank">📄 arXiv: 2505.02569v1</a>
  <a href="https://arxiv.org/pdf/2505.02569.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.02569v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.02569v1', 'HapticVLM: VLM-Driven Texture Recognition Aimed at Intelligent Haptic Interaction')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Muhammad Haris Khan, Miguel Altamirano Cabrera, Dmitrii Iarchuk, Yara Mahmoud, Daria Trinitatova, Issatay Tokmurziyev, Dzmitry Tsetserukou

**分类**: cs.RO, cs.HC

**发布日期**: 2025-05-05

**备注**: Submitted to IEEE conf

---

## 💡 一句话要点

**提出HapticVLM以解决智能触觉交互中的材料识别问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多模态交互` `触觉反馈` `材料识别` `环境感知` `深度学习` `虚拟现实` `智能技术`

## 📋 核心要点

1. 现有的触觉交互系统在材料识别和环境感知方面存在局限，难以实现实时反馈。
2. HapticVLM通过结合视觉-语言模型与深度学习技术，提供准确的材料识别和环境温度推断，增强触觉体验。
3. 实验结果表明，HapticVLM在材料识别和温度估计方面分别达到了84.67%和86.7%的准确率，显示出良好的性能。

## 📝 摘要（中文）

本文介绍了HapticVLM，一个新颖的多模态系统，结合了视觉-语言推理与深度卷积网络，实现实时触觉反馈。HapticVLM利用基于ConvNeXt的材料识别模块生成稳健的视觉嵌入，以准确识别物体材料，同时采用先进的视觉-语言模型（Qwen2-VL-2B-Instruct）从环境线索中推断环境温度。该系统通过扬声器提供振动触觉反馈，并通过佩尔帖模块提供热线索，从而弥合视觉感知与触觉体验之间的差距。实验评估显示，在五种不同的听觉-触觉模式下，平均识别准确率为84.67%，在15种场景下的温度估计准确率为86.7%。尽管前景可期，但当前研究受限于使用的小样本模式和参与者数量。未来的工作将集中在扩展触觉模式范围和增加用户研究，以进一步优化和验证系统性能。总体而言，HapticVLM在上下文感知的多模态触觉交互方面迈出了重要一步，具有在虚拟现实和辅助技术中的潜在应用。

## 🔬 方法详解

**问题定义**：本研究旨在解决智能触觉交互中材料识别和环境温度感知的不足，现有方法在实时反馈和准确性上存在挑战。

**核心思路**：HapticVLM通过结合视觉-语言推理与深度卷积网络，利用视觉嵌入和环境线索来实现更精准的触觉反馈。

**技术框架**：系统主要包括材料识别模块、环境温度推断模块和触觉反馈模块。材料识别模块基于ConvNeXt架构，温度推断模块使用Qwen2-VL-2B-Instruct模型，触觉反馈通过扬声器和佩尔帖模块实现。

**关键创新**：HapticVLM的创新在于将视觉-语言模型与深度学习相结合，提供了一种新的触觉交互方式，显著提升了材料识别和环境感知的准确性。

**关键设计**：在材料识别中，采用ConvNeXt网络结构以提高视觉嵌入的稳健性；温度推断采用基于容忍度的评估方法，设置了8°C的误差范围以确保准确性。实验中使用了五种听觉-触觉模式进行评估。

## 📊 实验亮点

实验结果显示，HapticVLM在五种不同的听觉-触觉模式下实现了84.67%的平均识别准确率，温度估计准确率为86.7%，相较于现有技术有显著提升，展示了系统在多模态交互中的有效性。

## 🎯 应用场景

HapticVLM的研究成果在虚拟现实和辅助技术领域具有广泛的应用潜力。通过提供更真实的触觉反馈，该系统可以提升用户体验，特别是在远程操作、教育培训和医疗康复等场景中，能够有效增强用户的交互感知和操作能力。

## 📄 摘要（原文）

> This paper introduces HapticVLM, a novel multimodal system that integrates vision-language reasoning with deep convolutional networks to enable real-time haptic feedback. HapticVLM leverages a ConvNeXt-based material recognition module to generate robust visual embeddings for accurate identification of object materials, while a state-of-the-art Vision-Language Model (Qwen2-VL-2B-Instruct) infers ambient temperature from environmental cues. The system synthesizes tactile sensations by delivering vibrotactile feedback through speakers and thermal cues via a Peltier module, thereby bridging the gap between visual perception and tactile experience. Experimental evaluations demonstrate an average recognition accuracy of 84.67% across five distinct auditory-tactile patterns and a temperature estimation accuracy of 86.7% based on a tolerance-based evaluation method with an 8°C margin of error across 15 scenarios. Although promising, the current study is limited by the use of a small set of prominent patterns and a modest participant pool. Future work will focus on expanding the range of tactile patterns and increasing user studies to further refine and validate the system's performance. Overall, HapticVLM presents a significant step toward context-aware, multimodal haptic interaction with potential applications in virtual reality, and assistive technologies.

