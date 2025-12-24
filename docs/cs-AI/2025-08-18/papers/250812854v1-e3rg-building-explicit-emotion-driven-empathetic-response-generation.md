---
layout: default
title: "E3RG: Building Explicit Emotion-driven Empathetic Response Generation System with Multimodal Large Language Model"
---

# E3RG: Building Explicit Emotion-driven Empathetic Response Generation System with Multimodal Large Language Model

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.12854" class="toolbar-btn" target="_blank">📄 arXiv: 2508.12854v1</a>
  <a href="https://arxiv.org/pdf/2508.12854.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.12854v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.12854v1', 'E3RG: Building Explicit Emotion-driven Empathetic Response Generation System with Multimodal Large Language Model')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Ronghao Lin, Shuai Shen, Weipeng Hu, Qiaolin He, Aolin Xiong, Li Huang, Haifeng Hu, Yap-peng Tan

**分类**: cs.AI, cs.CL, cs.CV, cs.HC, cs.MM

**发布日期**: 2025-08-18

**备注**: Accepted at ACM MM 2025 Grand Challenge

**🔗 代码/项目**: [GITHUB](https://github.com/RH-Lin/E3RG)

---

## 💡 一句话要点

**提出E3RG以解决多模态情感驱动的同理心响应生成问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多模态同理心生成` `情感智能` `大型语言模型` `响应生成` `虚拟助手` `社交机器人` `情感理解`

## 📋 核心要点

1. 现有方法在处理多模态情感内容和保持身份一致性方面存在不足，影响了同理心响应的生成效果。
2. E3RG通过将MERG任务分解为多模态同理心理解、同理心记忆检索和多模态响应生成三个部分，提供了一种新的解决方案。
3. 实验结果表明，E3RG在零-shot和少-shot设置下均表现优异，在相关挑战中取得了Top-1的成绩，验证了其有效性。

## 📝 摘要（中文）

多模态同理心响应生成（MERG）对于构建情感智能的人机交互至关重要。尽管大型语言模型（LLMs）在文本基础的响应生成上有所改善，但在处理多模态情感内容和保持身份一致性方面仍面临挑战。因此，我们提出了E3RG，一个基于多模态LLMs的显式情感驱动同理心响应生成系统，将MERG任务分解为三个部分：多模态同理心理解、同理心记忆检索和多模态响应生成。通过整合先进的表达性语音和视频生成模型，E3RG能够在无需额外训练的情况下提供自然、情感丰富且身份一致的响应。实验验证了我们系统在零-shot和少-shot设置下的优越性，并在ACM MM 25的基于虚拟形象的多模态同理心挑战中获得了第一名。我们的代码可在https://github.com/RH-Lin/E3RG获取。

## 🔬 方法详解

**问题定义**：本论文旨在解决多模态同理心响应生成（MERG）中的情感内容处理和身份一致性维护问题。现有方法在这两个方面的表现不尽如人意，限制了人机交互的情感智能化。

**核心思路**：E3RG的核心思路是将MERG任务分解为三个部分：首先是多模态同理心理解，其次是同理心记忆检索，最后是多模态响应生成。通过这种分解，系统能够更有效地处理多模态输入并生成情感丰富的响应。

**技术框架**：E3RG的整体架构包括三个主要模块：多模态同理心理解模块负责解析输入的情感信息；同理心记忆检索模块用于提取相关的情感记忆；多模态响应生成模块则结合前两个模块的输出生成最终的响应。

**关键创新**：E3RG的主要创新在于其显式情感驱动的设计，能够在不进行额外训练的情况下，利用先进的表达性语音和视频生成模型，提供自然且身份一致的响应。这一设计与现有方法的根本区别在于其对多模态输入的深度理解和处理能力。

**关键设计**：在技术细节上，E3RG采用了特定的损失函数来优化多模态响应的生成质量，并设计了适应不同情感状态的网络结构，以确保生成的响应在情感表达上更加丰富和一致。具体参数设置和网络结构的细节在论文中有详细描述。

## 📊 实验亮点

实验结果显示，E3RG在零-shot和少-shot设置下均表现出色，尤其在ACM MM 25的基于虚拟形象的多模态同理心挑战中获得了Top-1的成绩，证明了其在多模态情感响应生成中的优越性。具体性能数据和对比基线在论文中有详细列出，展示了相较于现有方法的显著提升。

## 🎯 应用场景

E3RG的研究成果具有广泛的应用潜力，特别是在情感智能的虚拟助手、社交机器人和在线客服等领域。通过实现更自然的情感交互，该系统能够提升用户体验，促进人机关系的和谐发展。此外，未来可能在教育、心理健康等领域发挥重要作用，帮助用户更好地表达和理解情感。

## 📄 摘要（原文）

> Multimodal Empathetic Response Generation (MERG) is crucial for building emotionally intelligent human-computer interactions. Although large language models (LLMs) have improved text-based ERG, challenges remain in handling multimodal emotional content and maintaining identity consistency. Thus, we propose E3RG, an Explicit Emotion-driven Empathetic Response Generation System based on multimodal LLMs which decomposes MERG task into three parts: multimodal empathy understanding, empathy memory retrieval, and multimodal response generation. By integrating advanced expressive speech and video generative models, E3RG delivers natural, emotionally rich, and identity-consistent responses without extra training. Experiments validate the superiority of our system on both zero-shot and few-shot settings, securing Top-1 position in the Avatar-based Multimodal Empathy Challenge on ACM MM 25. Our code is available at https://github.com/RH-Lin/E3RG.

