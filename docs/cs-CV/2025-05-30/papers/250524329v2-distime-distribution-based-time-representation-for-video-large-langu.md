---
layout: default
title: DisTime: Distribution-based Time Representation for Video Large Language Models
---

# DisTime: Distribution-based Time Representation for Video Large Language Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.24329" class="toolbar-btn" target="_blank">📄 arXiv: 2505.24329v2</a>
  <a href="https://arxiv.org/pdf/2505.24329.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.24329v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.24329v2', 'DisTime: Distribution-based Time Representation for Video Large Language Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yingsen Zeng, Zepeng Huang, Yujie Zhong, Chengjian Feng, Jie Hu, Lin Ma, Yang Liu

**分类**: cs.CV

**发布日期**: 2025-05-30 (更新: 2025-07-31)

**备注**: Accepted by ICCV 2025

**🔗 代码/项目**: [GITHUB](https://github.com/josephzpng/DisTime)

---

## 💡 一句话要点

**提出DisTime以解决视频大语言模型的时间表示问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `视频理解` `时间表示` `大语言模型` `自动标注` `多模态学习` `数据集构建` `时间定位` `深度学习`

## 📋 核心要点

1. 现有视频大语言模型在时间定位上存在精度不足的问题，主要受限于离散时间表示和数据集的时间感知能力。
2. 论文提出DisTime框架，通过可学习的时间嵌入和基于分布的时间解码器，增强视频大语言模型的时间理解能力。
3. 实验结果显示，DisTime在多个基准测试中实现了最先进的性能，并在视频问答任务中保持了竞争力。

## 📝 摘要（中文）

尽管视频理解技术已有所进展，视频大语言模型（Video-LLMs）在精确的时间定位上仍面临挑战，主要由于离散的时间表示和有限的时间感知数据集。现有的时间表达方法要么将时间与基于文本的数值混淆，要么添加一系列专用的时间标记，或使用专门的时间定位头进行回归。为了解决这些问题，本文提出了DisTime，一个轻量级框架，旨在增强Video-LLMs的时间理解能力。DisTime采用可学习的标记创建连续的时间嵌入空间，并结合基于分布的时间解码器生成时间概率分布，有效减轻边界模糊性并保持时间连续性。此外，基于分布的时间编码器重新编码时间戳，为Video-LLMs提供时间标记。为克服现有数据集中时间粒度的限制，本文提出了一种自动标注范式，结合了Video-LLMs的字幕能力与专用时间模型的定位专长，创建了InternVid-TG数据集，包含125万条时间定位事件，超越ActivityNet-Caption 55倍。大量实验表明，DisTime在三个时间敏感任务上实现了最先进的性能，同时在视频问答任务中保持了竞争力。

## 🔬 方法详解

**问题定义**：本文旨在解决视频大语言模型在时间定位中的精确性不足，现有方法往往依赖于离散的时间表示，导致时间理解的模糊性和不连续性。

**核心思路**：DisTime通过引入可学习的时间嵌入和基于分布的时间解码器，创建一个连续的时间表示空间，从而提高时间理解的准确性和连续性。

**技术框架**：DisTime的整体架构包括两个主要模块：基于分布的时间编码器和时间解码器。时间编码器负责将时间戳重新编码为时间标记，而时间解码器则生成时间概率分布，确保时间信息的连续性。

**关键创新**：DisTime的核心创新在于引入了基于分布的时间解码器，能够有效减轻时间边界的模糊性，并通过学习的方式提升时间表示的连续性，这与传统方法形成鲜明对比。

**关键设计**：在设计中，DisTime使用了可学习的时间标记和特定的损失函数，以优化时间嵌入的学习过程，确保时间信息的准确传递。

## 📊 实验亮点

在实验中，DisTime在三个时间敏感任务上实现了最先进的性能，超越了现有基准，特别是在时间定位精度上，表现出显著的提升。同时，在视频问答任务中，DisTime也保持了竞争力，展示了其广泛的适用性。

## 🎯 应用场景

DisTime的研究成果在视频理解、自动字幕生成和视频问答等领域具有广泛的应用潜力。通过提高视频大语言模型的时间理解能力，能够更好地支持多模态内容的分析和处理，推动智能视频分析技术的发展。

## 📄 摘要（原文）

> Despite advances in general video understanding, Video Large Language Models (Video-LLMs) face challenges in precise temporal localization due to discrete time representations and limited temporally aware datasets. Existing methods for temporal expression either conflate time with text-based numerical values, add a series of dedicated temporal tokens, or regress time using specialized temporal grounding heads. To address these issues, we introduce DisTime, a lightweight framework designed to enhance temporal comprehension in Video-LLMs. DisTime employs a learnable token to create a continuous temporal embedding space and incorporates a Distribution-based Time Decoder that generates temporal probability distributions, effectively mitigating boundary ambiguities and maintaining temporal continuity. Additionally, the Distribution-based Time Encoder re-encodes timestamps to provide time markers for Video-LLMs. To overcome temporal granularity limitations in existing datasets, we propose an automated annotation paradigm that combines the captioning capabilities of Video-LLMs with the localization expertise of dedicated temporal models. This leads to the creation of InternVid-TG, a substantial dataset with 1.25M temporally grounded events across 179k videos, surpassing ActivityNet-Caption by 55 times. Extensive experiments demonstrate that DisTime achieves state-of-the-art performance across benchmarks in three time-sensitive tasks while maintaining competitive performance in Video QA tasks. Code and data are released at https://github.com/josephzpng/DisTime.

