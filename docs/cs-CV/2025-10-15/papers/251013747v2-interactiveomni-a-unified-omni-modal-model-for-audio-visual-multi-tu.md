---
layout: default
title: InteractiveOmni: A Unified Omni-modal Model for Audio-Visual Multi-turn Dialogue
---

# InteractiveOmni: A Unified Omni-modal Model for Audio-Visual Multi-turn Dialogue

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2510.13747" class="toolbar-btn" target="_blank">📄 arXiv: 2510.13747v2</a>
  <a href="https://arxiv.org/pdf/2510.13747.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.13747v2" onclick="toggleFavorite(this, '2510.13747v2', 'InteractiveOmni: A Unified Omni-modal Model for Audio-Visual Multi-turn Dialogue')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Wenwen Tong, Hewei Guo, Dongchuan Ran, Jiangnan Chen, Jiefan Lu, Kaibin Wang, Keqiang Li, Xiaoxu Zhu, Jiakui Li, Kehan Li, Xueheng Li, Lumin Li, Chenxu Guo, Jiasheng Zhou, Jiandong Chen, Xianye Wu, Jiahao Wang, Silei Wu, Lei Chen, Hanming Deng, Yuxuan Song, Dinghao Zhou, Guiping Zhong, Ken Zheng, Shiyin Kang, Lewei Lu

**分类**: cs.CV

**发布日期**: 2025-10-15 (更新: 2025-12-03)

---

## 💡 一句话要点

**提出InteractiveOmni，一个用于音视频多轮交互的统一全模态大语言模型。**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多模态学习` `音视频交互` `大语言模型` `轻量化模型` `多轮对话` `语音生成` `跨模态理解`

## 📋 核心要点

1. 现有音视频多轮交互模型在轻量化和全模态理解能力上存在不足，难以实现高效且全面的交互。
2. InteractiveOmni通过统一的架构整合视觉、音频编码器、LLM和语音解码器，实现全模态理解和语音生成。
3. 实验表明，InteractiveOmni在多轮记忆和语音交互方面显著优于现有开源模型，且4B版本性能接近7B模型。

## 📝 摘要（中文）

本文介绍InteractiveOmni，一个统一且开源的全模态大语言模型，参数规模从4B到8B，旨在通过提供全面的全模态理解和语音生成能力，引领轻量级模型领域。为此，我们将视觉编码器、音频编码器、大型语言模型和语音解码器集成到一个统一的模型中，用于理解和生成任务。我们设计了一个多阶段训练策略，以确保强大的跨模态能力，包括全模态理解的预训练，以及语音对话和音视频交互的后训练。为了实现类似人类的长期对话能力，我们精心策划了一个多轮训练数据集，以增强模型处理复杂和多轮交互的能力。为了有效评估多轮记忆和语音交互能力，我们构建了多模态多轮记忆基准和多轮语音交互基准。实验表明，InteractiveOmni显著优于领先的开源模型，并提供了更智能的多轮音视频体验，尤其是在其长期记忆能力方面。值得注意的是，InteractiveOmni-4B在通用基准测试中与更大的模型（如Qwen2.5-Omni-7B）相当，并且仅使用50%的模型大小即可保持InteractiveOmni-8B 97%的性能。InteractiveOmni在图像、音频、视频理解和语音生成任务中取得了与同等规模模型相比最先进的结果，是下一代智能交互系统的一个可访问的开源基础。

## 🔬 方法详解

**问题定义**：现有音视频多轮交互模型通常存在模型体积大、计算资源消耗高的问题，难以在资源受限的设备上部署。此外，这些模型在处理多模态信息（如同时理解图像、音频和文本）以及进行多轮对话时，性能往往不尽如人意，缺乏长期记忆能力，无法进行流畅自然的交互。

**核心思路**：InteractiveOmni的核心思路是构建一个统一的全模态大语言模型，通过整合视觉、音频编码器、大型语言模型和语音解码器，实现对多种模态信息的理解和生成。该模型旨在通过轻量化的设计和高效的训练策略，在保证性能的同时降低计算成本，使其能够在各种设备上部署和应用。

**技术框架**：InteractiveOmni的整体架构包含以下几个主要模块：1) 视觉编码器：用于提取图像和视频的视觉特征。2) 音频编码器：用于提取音频的声学特征。3) 大型语言模型（LLM）：作为核心的语言处理模块，负责理解用户输入并生成回复。4) 语音解码器：用于将LLM生成的文本转换为语音输出。模型训练分为多个阶段：首先进行全模态理解的预训练，然后进行语音对话和音视频交互的后训练。

**关键创新**：InteractiveOmni的关键创新在于其统一的全模态架构和多阶段训练策略。传统的音视频交互模型通常需要针对不同的模态和任务进行单独设计和训练，而InteractiveOmni通过一个统一的模型实现了对多种模态信息的处理和生成，简化了模型的设计和训练流程。此外，多阶段训练策略能够有效地提升模型的跨模态理解和生成能力。

**关键设计**：在训练过程中，论文作者精心策划了一个多轮训练数据集，以增强模型处理复杂和多轮交互的能力。为了有效评估多轮记忆和语音交互能力，他们构建了多模态多轮记忆基准和多轮语音交互基准。具体的参数设置、损失函数和网络结构等技术细节在论文中未详细说明，属于未知信息。

## 📊 实验亮点

InteractiveOmni在多项基准测试中表现出色，显著优于同等规模的开源模型。例如，InteractiveOmni-4B在通用基准测试中与更大的模型（如Qwen2.5-Omni-7B）相当，并且仅使用50%的模型大小即可保持InteractiveOmni-8B 97%的性能。这表明该模型在性能和效率之间取得了良好的平衡。

## 🎯 应用场景

InteractiveOmni可应用于智能助手、虚拟客服、教育机器人等领域，实现更自然、智能的人机交互。其轻量化的设计使其能够在移动设备、智能家居等资源受限的平台上部署，为用户提供随时随地的音视频交互服务。该研究有望推动下一代智能交互系统的发展。

## 📄 摘要（原文）

> We introduce InteractiveOmni, a unified and open-source omni-modal large language model for audio-visual multi-turn interaction, ranging from 4B to 8B parameters, designed to lead the field of lightweight models by offering comprehensive omni-modal understanding and speech generation capabilities. To achieve this, we integrate the vision encoder, audio encoder, large language model, and speech decoder into a unified model for understanding and generation tasks. We design a multi-stage training strategy to ensure robust cross-modal capabilities, including pre-training for omni-modal understanding, followed by post-training with speech conversation and audio-visual interaction. To enable human-like long-term conversational ability, we meticulously curate a multi-turn training dataset that enhances the model's ability to handle complex and multi-turn interactions. To effectively evaluate the multi-turn memory and speech interaction capabilities, we construct the multi-modal multi-turn memory benchmark and the multi-turn speech interaction benchmark. Experiments demonstrate that InteractiveOmni significantly outperforms leading open-source models and provides a more intelligent multi-turn audio-visual experience, particularly in its long-term memory capabilities. Notably, InteractiveOmni-4B is comparable to the much larger model like Qwen2.5-Omni-7B on general benchmarks, and it can retain 97% of the performance of the InteractiveOmni-8B while utilizing only 50% of the model size. Achieving state-of-the-art results against similarly sized models across image, audio, video understanding, and speech generation tasks, InteractiveOmni is an accessible, open-source foundation for next-generation intelligent interactive systems.

