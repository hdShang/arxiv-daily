---
layout: default
title: Hearing to Translate: The Effectiveness of Speech Modality Integration into LLMs
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

**关键词**: `语音翻译` `SpeechLLM` `级联系统` `端到端模型` `语音基础模型`

## 📋 核心要点

1. 现有语音翻译方法依赖级联架构，但端到端SpeechLLM的潜力尚不明确，缺乏系统性对比。
2. 论文构建全面测试集，对比SpeechLLM与级联系统，评估不同噪声、语速等条件下的翻译质量。
3. 实验表明，级联系统整体更可靠，SpeechLLM仅在特定场景表现相当，语音基础模型性能仍有差距。

## 📝 摘要（中文）

随着大型语言模型（LLM）超越文本领域，将语音作为原生模态集成催生了SpeechLLM，旨在直接翻译口语，从而绕过传统的基于转录的流程。然而，这种集成是否能提高语音到文本的翻译质量，优于已建立的级联架构，仍然是一个悬而未决的问题。我们提出了Hearing to Translate，这是第一个综合测试套件，严格地将5个最先进的SpeechLLM与16个强大的直接和级联系统进行基准测试，这些系统将领先的语音基础模型（SFM）与多语言LLM相结合。我们的分析跨越16个基准、13个语言对和9个具有挑战性的条件，包括口齿不清、嘈杂和长篇语音。通过这项广泛的评估，我们发现级联系统仍然是最可靠的，而当前的SpeechLLM仅在选定的设置中与级联系统相匹配，并且SFM落后于两者，这突出了集成LLM（无论是在模型内部还是在流程中）对于高质量语音翻译至关重要。

## 🔬 方法详解

**问题定义**：论文旨在解决语音翻译领域中，端到端SpeechLLM与传统级联系统孰优孰劣的问题。现有级联系统依赖语音识别和机器翻译两个独立模块，可能存在误差累积和信息损失。而新兴的SpeechLLM试图直接从语音生成目标语言文本，理论上可以避免上述问题，但其性能优势尚未得到充分验证。因此，论文致力于通过全面的实验评估，明确两种架构的优缺点，为未来的语音翻译系统设计提供指导。

**核心思路**：论文的核心思路是通过构建一个全面的测试基准，系统性地比较端到端SpeechLLM和级联系统的语音翻译性能。该基准覆盖多种语言对、噪声条件、语速和口语风格，力求模拟真实应用场景。通过在相同条件下评估不同系统的翻译质量，从而客观地评估它们的优劣。

**技术框架**：论文采用对比实验的研究框架。首先，收集并整理了包含多种语言对和噪声条件的语音翻译数据集。然后，选取了5个最先进的SpeechLLM和16个基于领先语音基础模型（SFM）的级联系统作为评估对象。最后，在构建的测试基准上，使用标准的机器翻译评估指标（如BLEU）对各个系统的翻译质量进行评估和比较。通过分析实验结果，得出关于不同架构优缺点的结论。

**关键创新**：论文的关键创新在于构建了首个全面评估SpeechLLM的测试基准Hearing to Translate。该基准覆盖了多种语言对、噪声条件、语速和口语风格，能够更全面地评估语音翻译系统的性能。此外，论文还对当前最先进的SpeechLLM和级联系统进行了系统的对比分析，揭示了两种架构的优缺点，为未来的语音翻译系统设计提供了有价值的参考。

**关键设计**：论文在实验设计中考虑了多种因素，以保证评估的客观性和全面性。例如，在选择评估对象时，选取了当前最先进的SpeechLLM和基于领先SFM的级联系统。在构建测试基准时，覆盖了多种语言对、噪声条件、语速和口语风格。在评估翻译质量时，使用了标准的机器翻译评估指标（如BLEU）。此外，论文还对实验结果进行了详细的统计分析，以确保结论的可靠性。

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

实验结果表明，在大多数情况下，级联系统在语音翻译任务中表现更可靠。虽然SpeechLLM在特定场景下可以与级联系统媲美，但语音基础模型（SFM）的性能相对落后。这表明，无论是在模型内部还是流程中，集成大型语言模型（LLM）对于实现高质量的语音翻译至关重要。

## 🎯 应用场景

该研究成果可应用于语音翻译相关的多个领域，如国际会议同声传译、跨语言语音搜索、多语言客服机器人等。通过选择合适的语音翻译架构，可以提升跨语言交流的效率和准确性。未来的研究可以进一步探索如何结合端到端和级联架构的优点，设计更强大的语音翻译系统。

## 📄 摘要（原文）

> As Large Language Models (LLMs) expand beyond text, integrating speech as a native modality has given rise to SpeechLLMs, which aim to translate spoken language directly, thereby bypassing traditional transcription-based pipelines. Whether this integration improves speech-to-text translation quality over established cascaded architectures, however, remains an open question. We present Hearing to Translate, the first comprehensive test suite rigorously benchmarking 5 state-of-the-art SpeechLLMs against 16 strong direct and cascade systems that couple leading speech foundation models (SFM), with multilingual LLMs. Our analysis spans 16 benchmarks, 13 language pairs, and 9 challenging conditions, including disfluent, noisy, and long-form speech. Across this extensive evaluation, we find that cascaded systems remain the most reliable overall, while current SpeechLLMs only match cascades in selected settings and SFMs lag behind both, highlighting that integrating an LLM, either within the model or in a pipeline, is essential for high-quality speech translation.

