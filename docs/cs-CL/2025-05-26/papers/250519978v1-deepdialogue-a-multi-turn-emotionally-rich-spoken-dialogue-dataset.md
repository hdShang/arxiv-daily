---
layout: default
title: "DeepDialogue: A Multi-Turn Emotionally-Rich Spoken Dialogue Dataset"
---

# DeepDialogue: A Multi-Turn Emotionally-Rich Spoken Dialogue Dataset

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.19978" class="toolbar-btn" target="_blank">📄 arXiv: 2505.19978v1</a>
  <a href="https://arxiv.org/pdf/2505.19978.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.19978v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.19978v1', 'DeepDialogue: A Multi-Turn Emotionally-Rich Spoken Dialogue Dataset')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Alkis Koudounas, Moreno La Quatra, Elena Baralis

**分类**: cs.CL, cs.SD, eess.AS

**发布日期**: 2025-05-26

**备注**: Currently under review. See the official website: https://salt-research.github.io/DeepDialogue

---

## 💡 一句话要点

**提出DeepDialogue以解决多轮对话情感表达不足问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多轮对话` `情感计算` `多模态数据集` `对话系统` `语音合成` `人工智能` `自然语言处理`

## 📋 核心要点

1. 现有对话系统在多轮对话中难以保持情感连贯性，尤其是在情感表达和领域多样性方面存在不足。
2. DeepDialogue通过生成多轮对话数据集，结合多种语言模型和情感语音合成，解决了现有数据集的局限性。
3. 实验结果表明，小模型在对话连贯性上存在明显短板，而具体领域的对话更具深度，跨模型对话效果更佳。

## 📝 摘要（中文）

近年来，尽管对话AI在单轮响应方面取得了显著进展，但多轮对话仍然是一个挑战。现有对话数据集在情感范围、领域多样性和轮次深度上存在局限，且主要为文本形式，限制了更人性化对话系统的开发。为了解决这些问题，本文提出了DeepDialogue，一个包含40,150个高质量多轮对话的大规模多模态数据集，涵盖41个领域和20种情感。通过与9种不同语言模型的结合，生成了65,600个初始对话，并通过人工标注和LLM质量过滤进行评估。研究发现，小模型在6轮对话后难以保持连贯性，具体领域的对话比抽象领域更具意义，跨模型互动比同模型对话更连贯。DeepDialogue的一个关键贡献是其语音组件，为所有对话合成情感一致的声音，创造了首个大规模开源多模态对话数据集，真实保留了多轮对话中的情感背景。

## 🔬 方法详解

**问题定义**：本文旨在解决现有对话数据集在情感表达、领域多样性和多轮对话连贯性方面的不足，尤其是文本数据的局限性。

**核心思路**：通过构建一个包含多种情感和领域的大规模多模态对话数据集，DeepDialogue旨在提供更丰富的对话场景，促进对话系统的情感理解和表达。

**技术框架**：整体流程包括使用9种不同参数的语言模型生成初始对话，随后通过人工标注和LLM质量过滤进行评估，最终合成情感一致的语音。

**关键创新**：DeepDialogue的主要创新在于其多模态特性，结合了文本和语音数据，首次实现了情感一致的多轮对话数据集，显著提升了对话系统的情感表达能力。

**关键设计**：在数据生成过程中，采用了多种语言模型，确保生成对话的多样性和连贯性，同时在语音合成中保持情感一致性，确保数据集的高质量。

## 📊 实验亮点

实验结果显示，较小的语言模型在超过6轮对话后难以保持连贯性，而具体领域（如汽车、旅行）的对话比抽象领域（如哲学）更具深度。此外，跨模型对话的连贯性明显优于同模型对话，展示了DeepDialogue的有效性和实用性。

## 🎯 应用场景

DeepDialogue可广泛应用于情感计算、智能客服、虚拟助手等领域，提升对话系统的情感理解和交互能力。其多模态特性为未来的对话系统研究提供了新的数据基础，推动人机交互的自然性和人性化发展。

## 📄 摘要（原文）

> Recent advances in conversational AI have demonstrated impressive capabilities in single-turn responses, yet multi-turn dialogues remain challenging for even the most sophisticated language models. Current dialogue datasets are limited in their emotional range, domain diversity, turn depth, and are predominantly text-only, hindering progress in developing more human-like conversational systems across modalities. To address these limitations, we present DeepDialogue, a large-scale multimodal dataset containing 40,150 high-quality multi-turn dialogues spanning 41 domains and incorporating 20 distinct emotions with coherent emotional progressions. Our approach pairs 9 different language models (4B-72B parameters) to generate 65,600 initial conversations, which we then evaluate through a combination of human annotation and LLM-based quality filtering. The resulting dataset reveals fundamental insights: smaller models fail to maintain coherence beyond 6 dialogue turns; concrete domains (e.g., "cars," "travel") yield more meaningful conversations than abstract ones (e.g., "philosophy"); and cross-model interactions produce more coherent dialogues than same-model conversations. A key contribution of DeepDialogue is its speech component, where we synthesize emotion-consistent voices for all 40,150 dialogues, creating the first large-scale open-source multimodal dialogue dataset that faithfully preserves emotional context across multi-turn conversations.

