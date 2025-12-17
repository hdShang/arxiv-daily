---
layout: default
title: Spoken DialogSum: An Emotion-Rich Conversational Dataset for Spoken Dialogue Summarization
---

# Spoken DialogSum: An Emotion-Rich Conversational Dataset for Spoken Dialogue Summarization

**arXiv**: [2512.14687v1](https://arxiv.org/abs/2512.14687) | [PDF](https://arxiv.org/pdf/2512.14687.pdf)

**作者**: Yen-Ju Lu, Kunxiao Gao, Mingrui Liang, Helin Wang, Thomas Thebaud, Laureano Moro-Velazquez, Najim Dehak, Jesus Villalba

**分类**: cs.CL, cs.AI, cs.LG, eess.AS

**发布日期**: 2025-12-16

**备注**: 12 pages, 2 figures

**🔗 代码/项目**: [PROJECT_PAGE](https://fatfat-emosum.github.io/EmoDialog-Sum-Audio-Samples/)

---

## 💡 一句话要点

**提出Spoken DialogSum数据集以解决语音对话摘要中缺乏情感和副语言信息对齐数据的问题。**

**关键词**: `语音对话摘要` `情感计算` `副语言信息` `数据集构建` `端到端语音建模` `多模态对齐` `文本转语音合成` `大型语言模型`

## 📋 核心要点

1. 核心问题：现有语音对话摘要研究缺乏同时包含语音、摘要和副语言信息（如情感、音高）的数据集，限制了情感感知模型的发展。
2. 方法要点：通过两阶段方法构建Spoken DialogSum数据集，先使用LLM重写脚本并标记情感等副语言信息，再用TTS合成对齐语音。
3. 实验或效果：基线实验表明，端到端音频-LLM模型在情感摘要任务上比级联ASR-LLM系统在ROUGE-L分数上相对提升28%。

## 📝 摘要（中文）

当前的音频语言模型能够处理长对话，但情感感知或语音对话摘要的研究因缺乏将语音、摘要和副语言线索关联的数据而受限。我们引入了Spoken DialogSum，这是首个将原始对话音频与事实摘要、情感丰富摘要以及说话者年龄、性别和情感的语句级标签对齐的语料库。该数据集通过两个阶段构建：首先，使用大型语言模型重写DialogSum脚本，添加Switchboard风格的填充词和反馈词，并为每个语句标记情感、音高和语速；其次，通过富有表现力的文本转语音引擎从标记脚本合成语音，并与副语言标签对齐。Spoken DialogSum包含13,460个情感多样的对话，每个对话都配有事实摘要和情感聚焦摘要。数据集在线可用。基线实验显示，与级联的ASR-LLM系统相比，音频-LLM将情感摘要的ROUGE-L分数相对提升了28%，证实了端到端语音建模的价值。

## 🔬 方法详解

论文的核心方法是构建Spoken DialogSum数据集的框架。整体框架包括两个阶段：第一阶段，利用大型语言模型（LLM）对DialogSum文本脚本进行改写，添加Switchboard风格的填充词和反馈词以模拟真实对话，并为每个语句自动标记情感、音高和语速等副语言信息；第二阶段，使用富有表现力的文本转语音（TTS）引擎，基于标记脚本合成语音，确保语音与副语言标签精确对齐。关键技术创新点在于首次将原始音频、事实摘要、情感摘要和语句级副语言标签集成到一个统一数据集中。与现有方法的主要区别是，现有数据集通常仅包含文本或语音，缺乏情感和副语言信息的系统对齐，而本方法通过自动化流程实现了多模态数据的协同生成。

## 📊 实验亮点

最重要的实验结果是，使用Spoken DialogSum数据集训练的端到端音频-LLM模型，在情感摘要任务上，ROUGE-L分数比级联ASR-LLM系统相对提升了28%，显著证明了直接处理语音信号在情感感知任务中的优势。

## 🎯 应用场景

该研究在语音助手、客户服务对话分析、情感计算和心理健康监测等领域具有潜在应用价值。通过提供情感丰富的语音对话数据，可支持开发更智能的对话系统，提升人机交互的自然性和情感理解能力。

## 📄 摘要（原文）

> Recent audio language models can follow long conversations. However, research on emotion-aware or spoken dialogue summarization is constrained by the lack of data that links speech, summaries, and paralinguistic cues. We introduce Spoken DialogSum, the first corpus aligning raw conversational audio with factual summaries, emotion-rich summaries, and utterance-level labels for speaker age, gender, and emotion. The dataset is built in two stages: first, an LLM rewrites DialogSum scripts with Switchboard-style fillers and back-channels, then tags each utterance with emotion, pitch, and speaking rate. Second, an expressive TTS engine synthesizes speech from the tagged scripts, aligned with paralinguistic labels. Spoken DialogSum comprises 13,460 emotion-diverse dialogues, each paired with both a factual and an emotion-focused summary. The dataset is available online at https://fatfat-emosum.github.io/EmoDialog-Sum-Audio-Samples/. Baselines show that an Audio-LLM raises emotional-summary ROUGE-L by 28% relative to a cascaded ASR-LLM system, confirming the value of end-to-end speech modeling.

