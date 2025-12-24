---
layout: default
title: "BatonVoice: An Operationalist Framework for Enhancing Controllable Speech Synthesis with Linguistic Intelligence from LLMs"
---

# BatonVoice: An Operationalist Framework for Enhancing Controllable Speech Synthesis with Linguistic Intelligence from LLMs

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.26514" class="toolbar-btn" target="_blank">📄 arXiv: 2509.26514v1</a>
  <a href="https://arxiv.org/pdf/2509.26514.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.26514v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.26514v1', 'BatonVoice: An Operationalist Framework for Enhancing Controllable Speech Synthesis with Linguistic Intelligence from LLMs')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yue Wang, Ruotian Ma, Xingyu Chen, Zhengliang Shi, Wanshun Chen, Huang Liu, Jiadi Yao, Qu Yang, Qingxuan Jiang, Fanghua Ye, Juntao Li, Min Zhang, Zhaopeng Tu, Xiaolong Li, Linus

**分类**: cs.CL

**发布日期**: 2025-09-30

---

## 💡 一句话要点

**BatonVoice：利用LLM语言智能增强可控语音合成的运算主义框架**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `语音合成` `文本到语音` `大型语言模型` `可控语音合成` `跨语言泛化`

## 📋 核心要点

1. 现有TTS方法未能充分利用LLM强大的指令理解能力，限制了可控语音合成的性能。
2. BatonVoice框架将指令理解与语音生成解耦，利用LLM生成语音特征的文本计划，再由TTS模型合成语音。
3. 实验表明，BatonVoice在可控语音合成和跨语言泛化方面优于现有方法，证明了其有效性。

## 📝 摘要（中文）

大型语言模型（LLM）的兴起正在重塑多模态模型，语音合成是其中一个突出的应用。然而，现有方法通常未能充分利用这些模型的语言智能，通常无法利用其强大的指令遵循能力。这种局限性阻碍了模型遵循文本指令进行可控文本到语音（TTS）的能力。为了解决这个问题，我们提出了一种受“运算主义”启发的新的范例，将指令理解与语音生成解耦。我们引入了BatonVoice，一个LLM充当“指挥”的框架，理解用户指令并生成文本“计划”——显式的声音特征（例如，音高、能量）。然后，一个单独的TTS模型，即“管弦乐队”，从这些特征生成语音。为了实现这个组件，我们开发了专门为此任务训练的BatonTTS，一个TTS模型。我们的实验表明，BatonVoice在可控和情感语音合成方面取得了强大的性能，优于强大的开源和闭源基线。值得注意的是，我们的方法实现了卓越的零样本跨语言泛化，准确地将特征控制能力应用于在后训练期间未见过的语言。这表明将语音客观化为文本声音特征可以更有效地释放LLM的语言智能。

## 🔬 方法详解

**问题定义**：现有可控语音合成方法难以充分利用大型语言模型（LLM）的语言智能，尤其是在指令遵循方面存在不足。这导致模型在根据文本指令精确控制语音特征（如音高、能量、情感等）时表现不佳。现有方法通常将指令理解和语音生成耦合在一起，难以有效利用LLM的强大能力。

**核心思路**：BatonVoice的核心思路是借鉴“运算主义”思想，将指令理解和语音生成解耦。具体而言，利用LLM作为“指挥”，负责理解用户指令并生成一个明确的文本“计划”，该计划详细描述了语音的各种特征（如音高、能量等）。然后，将这个“计划”传递给一个专门训练的TTS模型（“管弦乐队”），由其负责根据“计划”生成最终的语音。

**技术框架**：BatonVoice框架包含两个主要模块：LLM指挥模块和BatonTTS管弦乐队模块。LLM指挥模块负责接收用户指令，并将其转化为包含语音特征信息的文本计划。BatonTTS管弦乐队模块是一个专门训练的TTS模型，它接收LLM生成的文本计划作为输入，并生成相应的语音。整个流程类似于一个指挥家指挥乐队演奏音乐，指挥家（LLM）负责理解乐谱（用户指令）并给出明确的演奏指示（文本计划），乐队（BatonTTS）负责根据指示演奏出音乐（语音）。

**关键创新**：BatonVoice的关键创新在于将LLM的语言智能与TTS模型的语音生成能力有效解耦。通过将语音特征显式地表示为文本，BatonVoice能够充分利用LLM强大的指令理解和文本生成能力，从而实现更精确、更灵活的可控语音合成。此外，这种解耦的设计也使得BatonVoice具有更好的可扩展性和可维护性。

**关键设计**：BatonVoice的关键设计包括：1) 使用LLM生成包含音高、能量等语音特征的文本计划；2) 开发专门的BatonTTS模型，该模型针对文本计划到语音的转换进行优化；3) 采用合适的训练策略，使得BatonTTS能够准确地根据文本计划生成高质量的语音。具体的参数设置、损失函数和网络结构等细节在论文中进行了详细描述（未知）。

## 📊 实验亮点

实验结果表明，BatonVoice在可控语音合成和情感语音合成方面均优于现有方法。尤其值得一提的是，BatonVoice在零样本跨语言泛化方面表现出色，能够将特征控制能力应用于在训练期间未见过的语言。这证明了将语音特征显式地表示为文本能够有效提升LLM的语言智能。

## 🎯 应用场景

BatonVoice在多个领域具有广泛的应用前景，包括：个性化语音助手、情感语音合成、跨语言语音合成、语音游戏、有声读物制作等。该研究的实际价值在于提升了语音合成的可控性和表现力，使得语音合成能够更好地满足用户的个性化需求。未来，BatonVoice有望成为人机交互的重要组成部分，为人们带来更加自然、便捷的语音交互体验。

## 📄 摘要（原文）

> The rise of Large Language Models (LLMs) is reshaping multimodel models, with speech synthesis being a prominent application. However, existing approaches often underutilize the linguistic intelligence of these models, typically failing to leverage their powerful instruction-following capabilities. This limitation hinders the model's ability to follow text instructions for controllable Text-to-Speech~(TTS). To address this, we propose a new paradigm inspired by ``operationalism'' that decouples instruction understanding from speech generation. We introduce BatonVoice, a framework where an LLM acts as a ``conductor'', understanding user instructions and generating a textual ``plan'' -- explicit vocal features (e.g., pitch, energy). A separate TTS model, the ``orchestra'', then generates the speech from these features. To realize this component, we develop BatonTTS, a TTS model trained specifically for this task. Our experiments demonstrate that BatonVoice achieves strong performance in controllable and emotional speech synthesis, outperforming strong open- and closed-source baselines. Notably, our approach enables remarkable zero-shot cross-lingual generalization, accurately applying feature control abilities to languages unseen during post-training. This demonstrates that objectifying speech into textual vocal features can more effectively unlock the linguistic intelligence of LLMs.

