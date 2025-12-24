---
layout: default
title: "InstructTTSEval: Benchmarking Complex Natural-Language Instruction Following in Text-to-Speech Systems"
---

# InstructTTSEval: Benchmarking Complex Natural-Language Instruction Following in Text-to-Speech Systems

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.16381" class="toolbar-btn" target="_blank">📄 arXiv: 2506.16381v1</a>
  <a href="https://arxiv.org/pdf/2506.16381.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.16381v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.16381v1', 'InstructTTSEval: Benchmarking Complex Natural-Language Instruction Following in Text-to-Speech Systems')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Kexin Huang, Qian Tu, Liwei Fan, Chenchen Yang, Dong Zhang, Shimin Li, Zhaoye Fei, Qinyuan Cheng, Xipeng Qiu

**分类**: cs.CL, cs.SD, eess.AS

**发布日期**: 2025-06-19

**备注**: 19 pages, 9 figures

---

## 💡 一句话要点

**提出InstructTTSEval以解决TTS系统复杂指令理解问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `文本到语音` `自然语言处理` `语音合成` `指令跟随` `基准评估` `自动评估` `复杂指令`

## 📋 核心要点

1. 现有的TTS系统在理解和执行复杂自然语言指令方面存在显著不足，限制了其灵活性和应用范围。
2. 本文提出InstructTTSEval基准，通过三个任务评估TTS系统对复杂指令的理解能力，旨在提升系统的指令跟随能力。
3. 实验结果显示，当前的指令跟随TTS系统仍有较大改进空间，InstructTTSEval将促进该领域的进一步研究和发展。

## 📝 摘要（中文）

在现代语音合成中，副语言信息如说话者的音色、情感状态和动态韵律在传达语义之外的细微差别中起着关键作用。传统的文本到语音（TTS）系统依赖固定的风格标签或插入语音提示来控制这些线索，限制了灵活性。尽管许多TTS系统现在支持通过文本描述进行定制合成，但它们对复杂指令的实际理解和执行能力仍然未得到充分探索。为了解决这些问题，本文提出了InstructTTSEval，一个用于测量复杂自然语言风格控制能力的基准，包含三个任务和总计6000个测试案例。我们利用Gemini作为自动评估工具，评估现有TTS系统的指令跟随能力，发现仍有较大改进空间。我们期望InstructTTSEval能推动更强大、灵活和准确的指令跟随TTS的发展。

## 🔬 方法详解

**问题定义**：本文旨在解决现有TTS系统在理解和执行复杂自然语言指令方面的不足，尤其是缺乏高质量基准和自动评估指标的问题。

**核心思路**：通过引入InstructTTSEval基准，设计三个具体任务来评估TTS系统对复杂指令的响应能力，从而推动模型的优化和提升。

**技术框架**：整体架构包括三个任务模块：声学参数规范、描述性风格指令和角色扮演，每个任务包含英语和中文子集，配有参考音频。评估使用Gemini作为自动评估工具。

**关键创新**：最重要的创新在于提出了InstructTTSEval基准，填补了现有TTS系统在复杂指令理解评估方面的空白，提供了系统化的测试案例和评估标准。

**关键设计**：在任务设计中，每个任务均包含1000个测试案例，确保多样性和代表性；同时，Gemini的自动评估机制提高了评估的效率和准确性。

## 📊 实验亮点

实验结果表明，当前的指令跟随TTS系统在复杂指令理解方面仍有显著提升空间，InstructTTSEval基准的引入将为后续研究提供明确的评估标准和方向，推动性能的进一步优化。

## 🎯 应用场景

该研究的潜在应用领域包括智能助手、语音导航、教育和娱乐等多个场景。通过提升TTS系统对复杂指令的理解能力，能够实现更自然和人性化的语音交互，增强用户体验。未来，InstructTTSEval有望成为TTS系统开发和评估的重要工具，推动行业标准的建立。

## 📄 摘要（原文）

> In modern speech synthesis, paralinguistic information--such as a speaker's vocal timbre, emotional state, and dynamic prosody--plays a critical role in conveying nuance beyond mere semantics. Traditional Text-to-Speech (TTS) systems rely on fixed style labels or inserting a speech prompt to control these cues, which severely limits flexibility. Recent attempts seek to employ natural-language instructions to modulate paralinguistic features, substantially improving the generalization of instruction-driven TTS models. Although many TTS systems now support customized synthesis via textual description, their actual ability to interpret and execute complex instructions remains largely unexplored. In addition, there is still a shortage of high-quality benchmarks and automated evaluation metrics specifically designed for instruction-based TTS, which hinders accurate assessment and iterative optimization of these models. To address these limitations, we introduce InstructTTSEval, a benchmark for measuring the capability of complex natural-language style control. We introduce three tasks, namely Acoustic-Parameter Specification, Descriptive-Style Directive, and Role-Play, including English and Chinese subsets, each with 1k test cases (6k in total) paired with reference audio. We leverage Gemini as an automatic judge to assess their instruction-following abilities. Our evaluation of accessible instruction-following TTS systems highlights substantial room for further improvement. We anticipate that InstructTTSEval will drive progress toward more powerful, flexible, and accurate instruction-following TTS.

