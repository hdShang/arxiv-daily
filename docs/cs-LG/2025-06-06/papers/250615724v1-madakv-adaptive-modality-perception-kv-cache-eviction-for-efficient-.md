---
layout: default
title: "MadaKV: Adaptive Modality-Perception KV Cache Eviction for Efficient Multimodal Long-Context Inference"
---

# MadaKV: Adaptive Modality-Perception KV Cache Eviction for Efficient Multimodal Long-Context Inference

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.15724" class="toolbar-btn" target="_blank">📄 arXiv: 2506.15724v1</a>
  <a href="https://arxiv.org/pdf/2506.15724.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.15724v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.15724v1', 'MadaKV: Adaptive Modality-Perception KV Cache Eviction for Efficient Multimodal Long-Context Inference')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Kunxi Li, Zhonghua Jiang, Zhouzhou Shen, Zhaode Wang, Chengfei Lv, Shengyu Zhang, Fan Wu, Fei Wu

**分类**: cs.LG, cs.AI, cs.CL

**发布日期**: 2025-06-06

---

## 💡 一句话要点

**提出MadaKV以解决多模态长上下文推理中的KV缓存效率问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多模态长上下文` `KV缓存` `推理效率` `模态适应` `深度学习`

## 📋 核心要点

1. 现有的KV缓存驱逐方法主要针对单模态设置，无法有效捕捉多模态场景中的模态特定信息，导致性能不足。
2. MadaKV通过模态偏好适应和分层压缩补偿，动态感知模态信息并自适应保留关键标记，从而提升推理效率。
3. 实验结果表明，MadaKV在多个多模态长上下文任务中，KV缓存内存占用和解码延迟显著降低，准确率保持高水平。

## 📝 摘要（中文）

本文介绍了MadaKV，一种适应性模态感知的键值（KV）缓存驱逐策略，旨在提高多模态大语言模型（MLLMs）在长上下文推理中的效率。在多模态场景中，注意力头对不同模态的偏好存在显著差异，导致模态重要性在注意力头之间存在显著差异。传统的KV缓存驱逐方法未能捕捉模态特定信息，因此表现不佳。MadaKV通过模态偏好适应和分层压缩补偿两个关键组件来解决这些挑战。通过动态感知注意力头中的模态信息并自适应保留关键标记，MadaKV在保持高准确率的同时，实现了KV缓存内存占用和模型推理解码延迟的显著降低（提升1.3到1.5倍）。在代表性的MLLMs和MileBench基准上的大量实验表明，MadaKV相较于现有KV缓存驱逐方法具有更高的有效性。

## 🔬 方法详解

**问题定义**：本文旨在解决多模态长上下文推理中，传统KV缓存驱逐方法未能有效捕捉模态特定信息的问题。这导致在多模态场景下，模型的推理效率和性能受到限制。

**核心思路**：MadaKV的核心思路是通过模态偏好适应和分层压缩补偿，动态调整KV缓存中的信息保留策略，以适应不同模态的需求，从而提高推理效率。

**技术框架**：MadaKV的整体架构包括两个主要模块：模态偏好适应模块和分层压缩补偿模块。前者负责动态感知模态信息，后者则通过压缩不重要的标记来优化缓存使用。

**关键创新**：MadaKV的创新点在于其模态适应性设计，使得KV缓存的驱逐策略能够根据不同模态的需求进行调整，这与传统方法的静态驱逐策略形成鲜明对比。

**关键设计**：在关键设计上，MadaKV采用了动态模态感知机制，能够实时评估各模态的重要性，并根据评估结果自适应调整缓存中的标记保留策略。

## 📊 实验亮点

实验结果显示，MadaKV在多个基准测试中，相较于传统KV缓存驱逐方法，KV缓存内存占用显著降低，同时推理解码延迟提升1.3到1.5倍，且在准确率上保持高水平，展现出其优越的性能。

## 🎯 应用场景

MadaKV的研究成果在多模态大语言模型的推理任务中具有广泛的应用潜力，尤其是在需要处理长上下文的场景，如视频理解、图像描述和多模态对话系统等。通过提升推理效率，MadaKV能够为实际应用提供更快速和准确的响应，推动相关领域的发展。

## 📄 摘要（原文）

> This paper introduces MadaKV, a modality-adaptive key-value (KV) cache eviction strategy designed to enhance the efficiency of multimodal large language models (MLLMs) in long-context inference. In multimodal scenarios, attention heads exhibit varying preferences for different modalities, resulting in significant disparities in modality importance across attention heads. Traditional KV cache eviction methods, which are tailored for unimodal settings, fail to capture modality-specific information, thereby yielding suboptimal performance. MadaKV addresses these challenges through two key components: modality preference adaptation and hierarchical compression compensation. By dynamically sensing modality information within attention heads and adaptively retaining critical tokens, MadaKV achieves substantial reductions in KV cache memory footprint and model inference decoding latency (1.3 to 1.5 times improvement) while maintaining high accuracy across various multimodal long-context tasks. Extensive experiments on representative MLLMs and the MileBench benchmark demonstrate the effectiveness of MadaKV compared to existing KV cache eviction methods.

