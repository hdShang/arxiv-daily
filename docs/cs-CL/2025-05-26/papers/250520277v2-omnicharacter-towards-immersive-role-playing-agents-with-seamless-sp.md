---
layout: default
title: OmniCharacter: Towards Immersive Role-Playing Agents with Seamless Speech-Language Personality Interaction
---

# OmniCharacter: Towards Immersive Role-Playing Agents with Seamless Speech-Language Personality Interaction

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.20277" class="toolbar-btn" target="_blank">📄 arXiv: 2505.20277v2</a>
  <a href="https://arxiv.org/pdf/2505.20277.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.20277v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.20277v2', 'OmniCharacter: Towards Immersive Role-Playing Agents with Seamless Speech-Language Personality Interaction')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Haonan Zhang, Run Luo, Xiong Liu, Yuchuan Wu, Ting-En Lin, Pengpeng Zeng, Qiang Qu, Feiteng Fang, Min Yang, Lianli Gao, Jingkuan Song, Fei Huang, Yongbin Li

**分类**: cs.CL, cs.CV

**发布日期**: 2025-05-26 (更新: 2025-06-05)

**备注**: 14 pages, 6 figures

**🔗 代码/项目**: [GITHUB](https://github.com/AlibabaResearch/DAMO-ConvAI/tree)

---

## 💡 一句话要点

**提出OmniCharacter以解决角色扮演代理的语音与语言互动问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `角色扮演代理` `语音交互` `语言模型` `沉浸式体验` `多模态响应` `深度学习` `智能代理`

## 📋 核心要点

1. 现有的角色扮演代理主要集中在文本对话的模拟，忽视了声音特征对沉浸式互动的重要性。
2. 本文提出OmniCharacter模型，旨在实现语音与语言的无缝个性互动，提升角色扮演的沉浸感。
3. 实验结果显示，OmniCharacter在响应内容和风格上优于现有方法，且响应延迟低至289毫秒。

## 📝 摘要（中文）

角色扮演代理（RPA）作为一种新兴的交互式人工智能系统，利用大型语言模型模拟多样化个性的角色。然而，现有方法主要关注文本对话的模拟，忽视了角色的声音特征（如声音风格和情感）在互动中的重要性。为此，本文提出OmniCharacter，这是一个首个无缝语音-语言个性互动模型，旨在实现低延迟的沉浸式RPA。OmniCharacter使代理在互动中持续展现角色特定的个性和声音特征，支持语音与语言响应的混合。我们构建了OmniCharacter-10K数据集，包含20个独特角色、10K丰富上下文的多轮对话和135K动态语音响应。实验结果表明，本文方法在内容和风格上均优于现有RPA和主流语音-语言模型，响应延迟低至289毫秒。

## 🔬 方法详解

**问题定义**：现有的角色扮演代理（RPA）方法主要关注文本对话的模拟，未能充分利用角色的声音特征（如声音风格和情感），导致互动体验不够沉浸。

**核心思路**：本文提出OmniCharacter模型，通过无缝结合语音和语言特征，使代理在互动中持续展现角色特定的个性和声音特征，从而提升沉浸式体验。

**技术框架**：OmniCharacter的整体架构包括数据集构建、模型训练和多模态响应生成三个主要模块。数据集OmniCharacter-10K包含多样化的角色和丰富的对话上下文，模型通过深度学习技术进行训练，最终生成语音和文本的混合响应。

**关键创新**：OmniCharacter的最大创新在于其无缝的语音-语言个性互动能力，使得角色在对话中不仅能表达文本内容，还能传达声音特征，显著提升了互动的真实感。

**关键设计**：在模型设计中，采用了特定的损失函数来平衡语音和文本的生成质量，同时优化了网络结构以降低响应延迟，确保在实际应用中能够快速响应用户的输入。

## 📊 实验亮点

实验结果表明，OmniCharacter在内容和风格的响应质量上优于现有的角色扮演代理和主流语音-语言模型，响应延迟低至289毫秒，显示出显著的性能提升。这一结果证明了无缝语音-语言个性互动的有效性。

## 🎯 应用场景

OmniCharacter的研究成果具有广泛的应用潜力，尤其在游戏、虚拟现实和教育等领域。通过提供更为真实和沉浸的角色互动体验，该技术可以提升用户的参与感和满意度，推动智能代理在多种场景中的应用。未来，随着技术的进一步发展，OmniCharacter有望在更多领域实现个性化和智能化的交互体验。

## 📄 摘要（原文）

> Role-Playing Agents (RPAs), benefiting from large language models, is an emerging interactive AI system that simulates roles or characters with diverse personalities. However, existing methods primarily focus on mimicking dialogues among roles in textual form, neglecting the role's voice traits (e.g., voice style and emotions) as playing a crucial effect in interaction, which tends to be more immersive experiences in realistic scenarios. Towards this goal, we propose OmniCharacter, a first seamless speech-language personality interaction model to achieve immersive RPAs with low latency. Specifically, OmniCharacter enables agents to consistently exhibit role-specific personality traits and vocal traits throughout the interaction, enabling a mixture of speech and language responses. To align the model with speech-language scenarios, we construct a dataset named OmniCharacter-10K, which involves more distinctive characters (20), richly contextualized multi-round dialogue (10K), and dynamic speech response (135K). Experimental results showcase that our method yields better responses in terms of both content and style compared to existing RPAs and mainstream speech-language models, with a response latency as low as 289ms. Code and dataset are available at https://github.com/AlibabaResearch/DAMO-ConvAI/tree/main/OmniCharacter.

