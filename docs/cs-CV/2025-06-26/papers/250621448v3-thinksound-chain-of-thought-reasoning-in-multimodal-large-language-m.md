---
layout: default
title: "ThinkSound: Chain-of-Thought Reasoning in Multimodal Large Language Models for Audio Generation and Editing"
---

# ThinkSound: Chain-of-Thought Reasoning in Multimodal Large Language Models for Audio Generation and Editing

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.21448" class="toolbar-btn" target="_blank">📄 arXiv: 2506.21448v3</a>
  <a href="https://arxiv.org/pdf/2506.21448.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.21448v3" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.21448v3', 'ThinkSound: Chain-of-Thought Reasoning in Multimodal Large Language Models for Audio Generation and Editing')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Huadai Liu, Kaicheng Luo, Jialei Wang, Wen Wang, Qian Chen, Zhou Zhao, Wei Xue

**分类**: eess.AS, cs.CV, cs.SD

**发布日期**: 2025-06-26 (更新: 2025-11-05)

**备注**: Accepted by NeurIPS 2025 Main

---

## 💡 一句话要点

**提出ThinkSound框架以解决视频音频生成中的高保真挑战**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `视频音频生成` `链式思维推理` `多模态大语言模型` `音效设计` `自然语言处理`

## 📋 核心要点

1. 现有的视频到音频生成方法在高保真音频生成上存在挑战，难以真实捕捉视觉内容的细微差别。
2. 本文提出的ThinkSound框架通过链式思维推理，分阶段实现音频的生成与编辑，增强了用户交互体验。
3. 实验结果显示，ThinkSound在音频指标和链式思维指标上均达到了最先进的性能，并在Movie Gen Audio基准测试中表现优异。

## 📝 摘要（中文）

尽管端到端的视频到音频生成技术已显著提升，但高保真音频的生成仍然面临挑战，尤其是在捕捉视觉内容细微差别方面。本文提出了ThinkSound，一个利用链式思维推理的框架，支持视频的逐步、交互式音频生成与编辑。该方法将过程分为三个互补阶段：基础音效生成、交互式对象中心精细化和基于自然语言指令的目标编辑。每个阶段都通过多模态大语言模型生成上下文对齐的链式思维推理，指导统一的音频基础模型。此外，我们引入了AudioCoT，一个具有结构化推理注释的综合数据集，建立视觉内容、文本描述与声音合成之间的联系。实验表明，ThinkSound在视频到音频生成方面达到了最先进的性能。

## 🔬 方法详解

**问题定义**：本文旨在解决视频到音频生成中高保真音频的生成问题。现有方法在捕捉视觉内容的细微差别和复杂的音频环境方面存在不足。

**核心思路**：ThinkSound框架利用链式思维推理，分阶段实现音频生成与编辑，通过用户交互提升生成质量和准确性。

**技术框架**：该框架分为三个主要阶段：基础音效生成、交互式对象中心精细化和基于自然语言的目标编辑。每个阶段都依赖于多模态大语言模型生成的上下文对齐推理。

**关键创新**：最重要的创新在于引入链式思维推理，允许逐步生成和编辑音频，显著提升了生成的准确性和用户交互的灵活性。

**关键设计**：在技术细节上，框架采用了结构化推理注释的数据集AudioCoT，确保视觉内容、文本描述与音频合成之间的有效连接。

## 📊 实验亮点

实验结果显示，ThinkSound在视频到音频生成任务中达到了最先进的性能，在音频质量和链式思维推理指标上均优于现有基线，尤其在Movie Gen Audio基准测试中表现突出，提升幅度显著。

## 🎯 应用场景

ThinkSound框架在影视制作、游戏音效设计和虚拟现实等领域具有广泛的应用潜力。通过提供高保真音频生成与编辑能力，能够显著提升创作效率和音频质量，推动相关行业的发展。

## 📄 摘要（原文）

> While end-to-end video-to-audio generation has greatly improved, producing high-fidelity audio that authentically captures the nuances of visual content remains challenging. Like professionals in the creative industries, this generation requires sophisticated reasoning about items such as visual dynamics, acoustic environments, and temporal relationships. We present ThinkSound, a novel framework that leverages Chain-of-Thought (CoT) reasoning to enable stepwise, interactive audio generation and editing for videos. Our approach decomposes the process into three complementary stages: foundational foley generation that creates semantically coherent soundscapes, interactive object-centric refinement through precise user interactions, and targeted editing guided by natural language instructions. At each stage, a multimodal large language model generates contextually aligned CoT reasoning that guides a unified audio foundation model. Furthermore, we introduce AudioCoT, a comprehensive dataset with structured reasoning annotations that establishes connections between visual content, textual descriptions, and sound synthesis. Experiments demonstrate that ThinkSound achieves state-of-the-art performance in video-to-audio generation across both audio metrics and CoT metrics, and excels in the out-of-distribution Movie Gen Audio benchmark. The project page is available at https://ThinkSound-Project.github.io.

