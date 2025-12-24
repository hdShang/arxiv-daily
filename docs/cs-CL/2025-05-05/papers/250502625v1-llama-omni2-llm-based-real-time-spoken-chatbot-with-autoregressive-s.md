---
layout: default
title: "LLaMA-Omni2: LLM-based Real-time Spoken Chatbot with Autoregressive Streaming Speech Synthesis"
---

# LLaMA-Omni2: LLM-based Real-time Spoken Chatbot with Autoregressive Streaming Speech Synthesis

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.02625" class="toolbar-btn" target="_blank">📄 arXiv: 2505.02625v1</a>
  <a href="https://arxiv.org/pdf/2505.02625.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.02625v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.02625v1', 'LLaMA-Omni2: LLM-based Real-time Spoken Chatbot with Autoregressive Streaming Speech Synthesis')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Qingkai Fang, Yan Zhou, Shoutao Guo, Shaolei Zhang, Yang Feng

**分类**: cs.CL, cs.AI, cs.SD, eess.AS

**发布日期**: 2025-05-05

**备注**: Preprint. Project: https://github.com/ictnlp/LLaMA-Omni2

---

## 💡 一句话要点

**提出LLaMA-Omni2以实现实时智能语音聊天机器人**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `语音交互` `大型语言模型` `自回归解码` `智能聊天机器人` `实时语音合成`

## 📋 核心要点

1. 现有的语音聊天机器人在实时性和自然交互方面存在不足，难以满足用户的需求。
2. LLaMA-Omni 2通过集成语音编码器和自回归流式语音解码器，提供高效的实时语音交互解决方案。
3. 在仅使用20万多轮对话样本的情况下，LLaMA-Omni 2在语音问答和指令跟随任务中超越了之前的最先进模型。

## 📝 摘要（中文）

实时、智能和自然的语音交互是下一代人机交互的重要组成部分。近期的研究表明，基于大型语言模型（LLMs）构建智能语音聊天机器人的潜力。本文介绍了LLaMA-Omni 2，这是一系列参数从0.5B到14B的语音语言模型（SpeechLMs），能够实现高质量的实时语音交互。LLaMA-Omni 2基于Qwen2.5系列模型，集成了语音编码器和自回归流式语音解码器。尽管仅在20万多轮语音对话样本上进行训练，LLaMA-Omni 2在多个语音问答和语音指令跟随基准测试中表现出色，超越了以数百万小时语音数据训练的GLM-4-Voice等现有最先进的SpeechLMs。

## 🔬 方法详解

**问题定义**：本文旨在解决现有语音聊天机器人在实时性和自然交互方面的不足，尤其是在训练数据量有限的情况下，如何实现高效的语音交互。

**核心思路**：LLaMA-Omni 2通过结合语音编码器与自回归流式解码器，优化了语音生成过程，使其能够在较少的训练数据下仍然实现高质量的语音交互。

**技术框架**：LLaMA-Omni 2的整体架构包括语音编码器和自回归解码器两个主要模块，前者负责将输入语音转换为特征表示，后者则生成相应的语音输出。

**关键创新**：LLaMA-Omni 2的最大创新在于其在较少的训练样本下仍能超越传统模型，展示了在有限数据条件下的强大性能，尤其是在语音问答和指令跟随任务中。

**关键设计**：模型参数设置从0.5B到14B不等，采用了适应性损失函数和优化的网络结构，以提高训练效率和生成质量。

## 📊 实验亮点

LLaMA-Omni 2在多个语音问答和指令跟随基准测试中表现优异，超越了GLM-4-Voice等最先进模型，展示了在仅使用20万多轮对话样本下的强大性能，体现了其在语音交互领域的显著提升。

## 🎯 应用场景

LLaMA-Omni 2在智能语音助手、客户服务、教育培训等多个领域具有广泛的应用潜力。其高效的实时语音交互能力能够提升用户体验，推动人机交互的自然化进程，未来可能会在更多智能设备中得到应用。

## 📄 摘要（原文）

> Real-time, intelligent, and natural speech interaction is an essential part of the next-generation human-computer interaction. Recent advancements have showcased the potential of building intelligent spoken chatbots based on large language models (LLMs). In this paper, we introduce LLaMA-Omni 2, a series of speech language models (SpeechLMs) ranging from 0.5B to 14B parameters, capable of achieving high-quality real-time speech interaction. LLaMA-Omni 2 is built upon the Qwen2.5 series models, integrating a speech encoder and an autoregressive streaming speech decoder. Despite being trained on only 200K multi-turn speech dialogue samples, LLaMA-Omni 2 demonstrates strong performance on several spoken question answering and speech instruction following benchmarks, surpassing previous state-of-the-art SpeechLMs like GLM-4-Voice, which was trained on millions of hours of speech data.

