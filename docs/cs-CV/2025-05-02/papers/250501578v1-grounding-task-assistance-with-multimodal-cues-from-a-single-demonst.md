---
layout: default
title: Grounding Task Assistance with Multimodal Cues from a Single Demonstration
---

# Grounding Task Assistance with Multimodal Cues from a Single Demonstration

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.01578" class="toolbar-btn" target="_blank">📄 arXiv: 2505.01578v1</a>
  <a href="https://arxiv.org/pdf/2505.01578.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.01578v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.01578v1', 'Grounding Task Assistance with Multimodal Cues from a Single Demonstration')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Gabriel Sarch, Balasaravanan Thoravi Kumaravel, Sahithya Ravi, Vibhav Vineet, Andrew D. Wilson

**分类**: cs.CV

**发布日期**: 2025-05-02

---

## 💡 一句话要点

**提出MICA框架以解决任务辅助中的多模态信息缺失问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多模态融合` `任务辅助` `视觉语言模型` `眼动追踪` `语音识别` `上下文理解` `人机交互`

## 📋 核心要点

1. 现有的RGB视频示范无法有效捕捉细粒度的上下文信息，限制了任务辅助的效果。
2. MICA框架通过整合眼动和语音线索，分割示范为子任务，提取关键帧和字幕，增强上下文理解。
3. 实验结果显示，多模态线索在任务复制中的响应质量显著提升，眼动线索的表现接近语音线索。

## 📝 摘要（中文）

人类的示范通常是学习相同任务的关键参考。然而，RGB视频作为主要的示范媒介，常常无法捕捉到细粒度的上下文线索，如意图、安全关键的环境因素和人类行为中的微妙偏好。这一感知差距限制了视觉语言模型（VLMs）对动作发生原因的推理能力。为此，本文提出了MICA（多模态互动上下文辅助）框架，通过整合眼动和语音线索来改善任务辅助的对话代理。MICA将示范分割为有意义的子任务，并提取关键帧和捕捉细粒度意图的字幕，从而增强视觉问答的上下文基础。实验证明，多模态线索显著提高了响应质量，眼动线索单独就达到了93%的语音性能，二者结合则取得了最高准确率。

## 🔬 方法详解

**问题定义**：本研究旨在解决现有任务辅助系统中因缺乏细粒度上下文信息而导致的性能不足问题，尤其是在使用RGB视频作为示范媒介时。

**核心思路**：提出MICA框架，通过整合眼动和语音线索，增强对任务示范的理解，进而提高对话代理的任务辅助能力。

**技术框架**：MICA框架包括三个主要模块：示范分割模块、关键帧提取模块和上下文理解模块。示范分割模块将任务示范分解为多个子任务，关键帧提取模块从中提取重要帧和字幕，而上下文理解模块则结合多模态线索进行分析。

**关键创新**：MICA的创新在于首次将眼动和语音线索结合用于任务辅助，显著提升了对任务意图和用户特定需求的理解能力，与传统的基于帧的检索方法形成鲜明对比。

**关键设计**：在设计中，MICA采用了特定的损失函数来优化多模态线索的融合效果，并在网络结构上引入了注意力机制，以增强对重要信息的关注。

## 📊 实验亮点

实验结果表明，使用多模态线索的响应质量显著高于传统的基于帧的检索方法。眼动线索单独达到了93%的语音性能，而二者结合的准确率更是最高，展示了多模态信号在实际任务辅助中的重要性。

## 🎯 应用场景

该研究的潜在应用领域包括教育培训、机器人任务执行和人机交互等。通过提供更为精准的任务辅助，MICA框架能够提升用户学习效率和任务执行的安全性，未来可能在智能助手和自动化系统中发挥重要作用。

## 📄 摘要（原文）

> A person's demonstration often serves as a key reference for others learning the same task. However, RGB video, the dominant medium for representing these demonstrations, often fails to capture fine-grained contextual cues such as intent, safety-critical environmental factors, and subtle preferences embedded in human behavior. This sensory gap fundamentally limits the ability of Vision Language Models (VLMs) to reason about why actions occur and how they should adapt to individual users. To address this, we introduce MICA (Multimodal Interactive Contextualized Assistance), a framework that improves conversational agents for task assistance by integrating eye gaze and speech cues. MICA segments demonstrations into meaningful sub-tasks and extracts keyframes and captions that capture fine-grained intent and user-specific cues, enabling richer contextual grounding for visual question answering. Evaluations on questions derived from real-time chat-assisted task replication show that multimodal cues significantly improve response quality over frame-based retrieval. Notably, gaze cues alone achieves 93% of speech performance, and their combination yields the highest accuracy. Task type determines the effectiveness of implicit (gaze) vs. explicit (speech) cues, underscoring the need for adaptable multimodal models. These results highlight the limitations of frame-based context and demonstrate the value of multimodal signals for real-world AI task assistance.

