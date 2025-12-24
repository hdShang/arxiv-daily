---
layout: default
title: "Hearing to Translate: The Effectiveness of Speech Modality Integration into LLMs"
---

# Hearing to Translate: The Effectiveness of Speech Modality Integration into LLMs

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.16378" class="toolbar-btn" target="_blank">📄 arXiv: 2512.16378v1</a>
  <a href="https://arxiv.org/pdf/2512.16378.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.16378v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.16378v1', 'Hearing to Translate: The Effectiveness of Speech Modality Integration into LLMs')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Sara Papi, Javier Garcia Gilabert, Zachary Hopton, Vilém Zouhar, Carlos Escolano, Gerard I. Gállego, Jorge Iranzo-Sánchez, Ahrii Kim, Dominik Macháček, Patricia Schmidtova, Maike Züfle

**分类**: cs.CL, cs.AI, cs.SD

**发布日期**: 2025-12-18

**备注**: Project available at https://github.com/sarapapi/hearing2translate

---

## 💡 一句话要点

**首个SpeechLLM综合评测：对比端到端与级联架构语音翻译性能**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `语音翻译` `SpeechLLM` `级联系统` `端到端模型` `性能评测`

## 📋 核心要点

1. 现有端到端SpeechLLM语音翻译能力有待考量，缺乏与传统级联架构的系统性对比。
2. 提出Hearing to Translate测试套件，全面评估SpeechLLM与级联系统的语音翻译性能。
3. 实验表明，级联系统总体上更可靠，SpeechLLM仅在特定场景下可媲美，SFM表现最差。

## 📝 摘要（中文）

随着大型语言模型(LLMs)超越文本领域，将语音作为原生模态集成催生了SpeechLLMs，旨在直接翻译口语，从而绕过传统的基于转录的流程。然而，这种集成是否能提高语音到文本的翻译质量，优于已建立的级联架构，仍然是一个悬而未决的问题。我们提出了Hearing to Translate，这是第一个综合测试套件，严格地将5个最先进的SpeechLLMs与16个强大的直接和级联系统进行基准测试，这些系统将领先的语音基础模型(SFM)与多语言LLMs结合。我们的分析跨越16个基准、13个语言对和9个具有挑战性的条件，包括口齿不清、嘈杂和长篇语音。通过这项广泛的评估，我们发现级联系统仍然是最可靠的，而当前的SpeechLLMs仅在选定的设置中与级联系统相匹配，并且SFMs落后于两者，这突出了集成LLM（无论是在模型内部还是在pipeline中）对于高质量语音翻译至关重要。

## 🔬 方法详解

**问题定义**：论文旨在解决语音翻译领域中，端到端SpeechLLM与传统级联架构孰优孰劣的问题。现有端到端模型虽然简化了流程，但其性能是否能超越经过充分优化的级联系统，尤其是在复杂场景下，仍缺乏充分的实验验证。级联系统虽然流程复杂，但每个模块都可以独立优化，性能上限较高。因此，需要一个全面的评测体系来客观比较两者的优劣。

**核心思路**：论文的核心思路是通过构建一个全面的评测基准，在多种语言对和复杂场景下，系统性地比较端到端SpeechLLM和级联系统的语音翻译性能。通过大量实验数据，分析不同架构的优势和劣势，为未来的语音翻译模型设计提供指导。

**技术框架**：论文构建的Hearing to Translate测试套件包含以下几个关键部分：
1.  **数据集**：涵盖16个基准数据集，13个语言对，以及9种具有挑战性的语音条件，包括口齿不清、噪声和长篇语音。
2.  **模型选择**：选取了5个最先进的SpeechLLM模型，以及16个强大的直接和级联系统，这些系统结合了领先的语音基础模型(SFM)和多语言LLM。
3.  **评估指标**：采用标准的语音翻译评估指标，如BLEU等，来衡量不同模型的翻译质量。
4.  **实验流程**：在统一的实验环境下，对所有模型进行评估，并进行详细的性能分析。

**关键创新**：论文的主要创新在于构建了首个全面的SpeechLLM评测基准Hearing to Translate。该基准覆盖了多种语言对、复杂语音条件和模型架构，能够更客观地评估不同语音翻译系统的性能。此外，论文还深入分析了端到端SpeechLLM和级联系统在不同场景下的优劣，为未来的模型设计提供了有价值的参考。

**关键设计**：论文的关键设计在于数据集的选择和实验场景的构建。为了更全面地评估模型的性能，论文选择了涵盖多种语言对和复杂语音条件的数据集。此外，论文还设计了9种具有挑战性的语音条件，包括口齿不清、噪声和长篇语音，以模拟真实的语音翻译场景。在模型选择方面，论文选取了最先进的SpeechLLM模型和级联系统，保证了评估结果的代表性。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.16378v1/x1.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.16378v1/x2.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.16378v1/figs/pearmut_screenshot_1.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

实验结果表明，在大多数情况下，级联系统仍然是最可靠的语音翻译方案。虽然当前的SpeechLLM在特定场景下可以与级联系统相媲美，但在整体性能上仍有差距。此外，实验还发现，单独使用SFM进行语音翻译的效果较差，集成LLM（无论是在模型内部还是在pipeline中）对于高质量语音翻译至关重要。

## 🎯 应用场景

该研究成果可应用于多种语音翻译场景，如国际会议同声传译、跨语言语音助手、多语言客服系统等。通过对比不同架构的优劣，可以指导未来语音翻译系统的设计和优化，提升跨语言交流的效率和质量。此外，该评测基准的发布，也将促进语音翻译领域的研究进展。

## 📄 摘要（原文）

> As Large Language Models (LLMs) expand beyond text, integrating speech as a native modality has given rise to SpeechLLMs, which aim to translate spoken language directly, thereby bypassing traditional transcription-based pipelines. Whether this integration improves speech-to-text translation quality over established cascaded architectures, however, remains an open question. We present Hearing to Translate, the first comprehensive test suite rigorously benchmarking 5 state-of-the-art SpeechLLMs against 16 strong direct and cascade systems that couple leading speech foundation models (SFM), with multilingual LLMs. Our analysis spans 16 benchmarks, 13 language pairs, and 9 challenging conditions, including disfluent, noisy, and long-form speech. Across this extensive evaluation, we find that cascaded systems remain the most reliable overall, while current SpeechLLMs only match cascades in selected settings and SFMs lag behind both, highlighting that integrating an LLM, either within the model or in a pipeline, is essential for high-quality speech translation.

