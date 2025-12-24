---
layout: default
title: "Stream-Omni: Simultaneous Multimodal Interactions with Large Language-Vision-Speech Model"
---

# Stream-Omni: Simultaneous Multimodal Interactions with Large Language-Vision-Speech Model

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.13642" class="toolbar-btn" target="_blank">📄 arXiv: 2506.13642v2</a>
  <a href="https://arxiv.org/pdf/2506.13642.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.13642v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.13642v2', 'Stream-Omni: Simultaneous Multimodal Interactions with Large Language-Vision-Speech Model')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Shaolei Zhang, Shoutao Guo, Qingkai Fang, Yan Zhou, Yang Feng

**分类**: cs.AI, cs.CL, cs.CV, cs.SD, eess.AS

**发布日期**: 2025-06-16 (更新: 2025-06-22)

**备注**: Code: https://github.com/ictnlp/Stream-Omni , Model: https://huggingface.co/ICTNLP/stream-omni-8b

---

## 💡 一句话要点

**提出Stream-Omni以实现多模态高效交互**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多模态模型` `语言-视觉-语音` `模态对齐` `高效交互` `智能助手` `自动语音识别` `视觉问答`

## 📋 核心要点

1. 现有多模态模型在模态对齐上依赖于大规模数据，导致效率低下，尤其是在语音模态上。
2. 本文提出Stream-Omni，通过更有目的地建模模态之间的关系，实现高效的模态对齐。
3. 实验结果显示，Stream-Omni在多个基准测试中表现优异，尤其在视觉理解和语音交互任务上有显著提升。

## 📝 摘要（中文）

随着类似GPT-4o的大型多模态模型（LMM）的出现，探索文本、视觉和语音模态的整合以支持更灵活的多模态交互变得尤为重要。现有LMM通常沿序列维度连接模态表示，并将其输入大型语言模型（LLM）主干。尽管序列维度连接在模态整合上较为直接，但往往依赖于大规模数据来学习模态对齐。本文提出Stream-Omni，一个具有高效模态对齐的大型语言-视觉-语音模型，能够同时支持多种模态组合下的交互。Stream-Omni利用LLM作为主干，并基于模态之间的关系对视觉和语音进行对齐。实验结果表明，Stream-Omni在视觉理解、语音交互和视觉引导的语音交互任务上表现出色。

## 🔬 方法详解

**问题定义**：本文旨在解决现有多模态模型在模态对齐上依赖大规模数据的问题，尤其是在语音模态的效率低下。

**核心思路**：Stream-Omni通过更有目的地建模模态之间的关系，采用不同的对齐策略来实现高效的模态整合，减少对数据的依赖。

**技术框架**：Stream-Omni的整体架构包括一个大型语言模型作为主干，视觉模态通过序列维度连接与文本对齐，而语音模态则通过CTC（Connectionist Temporal Classification）层维度映射与文本对齐。

**关键创新**：Stream-Omni的核心创新在于引入了层维度映射的机制，使得语音模态能够在较少的数据下实现与文本的有效对齐，这与现有方法的简单序列连接方式有本质区别。

**关键设计**：在设计上，Stream-Omni采用了CTC-based层维度映射技术，并在损失函数中考虑了模态之间的关系，以优化模态对齐的效果。

## 📊 实验亮点

在多个基准测试中，Stream-Omni在视觉理解、语音交互和视觉引导的语音交互任务上均表现出色，尤其在语音模态的对齐效率上显著提升，减少了对大规模数据的依赖，展示了其强大的多模态处理能力。

## 🎯 应用场景

Stream-Omni的研究成果在智能助手、自动语音识别、视觉问答等领域具有广泛的应用潜力。通过高效的模态对齐，用户可以获得更流畅的多模态交互体验，提升人机交互的自然性和智能性。

## 📄 摘要（原文）

> The emergence of GPT-4o-like large multimodal models (LMMs) has raised the exploration of integrating text, vision, and speech modalities to support more flexible multimodal interaction. Existing LMMs typically concatenate representation of modalities along the sequence dimension and feed them into a large language model (LLM) backbone. While sequence-dimension concatenation is straightforward for modality integration, it often relies heavily on large-scale data to learn modality alignments. In this paper, we aim to model the relationships between modalities more purposefully, thereby achieving more efficient and flexible modality alignments. To this end, we propose Stream-Omni, a large language-vision-speech model with efficient modality alignments, which can simultaneously support interactions under various modality combinations. Stream-Omni employs LLM as the backbone and aligns the vision and speech to the text based on their relationships. For vision that is semantically complementary to text, Stream-Omni uses sequence-dimension concatenation to achieve vision-text alignment. For speech that is semantically consistent with text, Stream-Omni introduces a CTC-based layer-dimension mapping to achieve speech-text alignment. In this way, Stream-Omni can achieve modality alignments with less data (especially speech), enabling the transfer of text capabilities to other modalities. Experiments on various benchmarks demonstrate that Stream-Omni achieves strong performance on visual understanding, speech interaction, and vision-grounded speech interaction tasks. Owing to the layer-dimensional mapping, Stream-Omni can simultaneously provide intermediate text outputs (such as ASR transcriptions and model responses) during speech interaction, offering users a comprehensive multimodal experience.

