---
layout: default
title: "MemoryVLA: Perceptual-Cognitive Memory in Vision-Language-Action Models for Robotic Manipulation"
---

# MemoryVLA: Perceptual-Cognitive Memory in Vision-Language-Action Models for Robotic Manipulation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.19236" class="toolbar-btn" target="_blank">📄 arXiv: 2508.19236v1</a>
  <a href="https://arxiv.org/pdf/2508.19236.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.19236v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.19236v1', 'MemoryVLA: Perceptual-Cognitive Memory in Vision-Language-Action Models for Robotic Manipulation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Hao Shi, Bin Xie, Yingfei Liu, Lin Sun, Fengrong Liu, Tiancai Wang, Erjin Zhou, Haoqiang Fan, Xiangyu Zhang, Gao Huang

**分类**: cs.RO, cs.CV

**发布日期**: 2025-08-26

**备注**: The project is available at https://shihao1895.github.io/MemoryVLA

**🔗 代码/项目**: [PROJECT_PAGE](https://shihao1895.github.io/MemoryVLA)

---

## 💡 一句话要点

**提出MemoryVLA以解决机器人操作中的时间上下文问题**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `机器人操作` `视觉-语言-行动` `时间上下文` `认知科学` `长时间依赖` `感知-认知记忆库` `决策能力` `智能机器人`

## 📋 核心要点

1. 现有的视觉-语言-行动模型通常忽视时间上下文，导致在长时间依赖的机器人操作任务中表现不佳。
2. 本文提出MemoryVLA框架，通过工作记忆和感知-认知记忆库来处理时间上下文，提升机器人操作的决策能力。
3. 在多个模拟和现实任务中，MemoryVLA的成功率超过现有基线，特别是在长时间任务中表现出显著提升。

## 📝 摘要（中文）

时间上下文对于机器人操作至关重要，但主流的视觉-语言-行动（VLA）模型通常忽视这一点，导致在长时间依赖任务中表现不佳。认知科学表明，人类依赖工作记忆来缓冲短期表征以进行即时控制，而海马系统则保存过去经验的详细和语义信息。基于这些机制，本文提出了MemoryVLA，一个用于长时间机器人操作的认知-记忆-行动框架。该框架通过预训练的视觉语言模型（VLM）将观察编码为感知和认知标记，形成工作记忆，同时建立感知-认知记忆库以存储低级细节和高级语义。工作记忆从记忆库中检索决策相关条目，并与当前标记自适应融合，更新记忆库。通过这些标记，记忆条件扩散行动专家生成时间感知的行动序列。实验结果表明，MemoryVLA在150多个模拟和现实任务中表现优异，成功率显著高于现有基线。

## 🔬 方法详解

**问题定义**：本文旨在解决机器人操作中的时间上下文问题，现有的VLA模型在处理长时间依赖任务时表现不足，无法有效利用历史信息进行决策。

**核心思路**：MemoryVLA框架结合了认知科学中的工作记忆和长时记忆机制，通过感知-认知记忆库存储和检索信息，以增强机器人在复杂任务中的表现。

**技术框架**：该框架包括三个主要模块：预训练的视觉语言模型（VLM）用于编码观察信息，感知-认知记忆库用于存储信息，记忆条件扩散行动专家用于生成时间感知的行动序列。

**关键创新**：MemoryVLA的创新在于引入了感知-认知记忆库，能够有效整合短期和长期记忆，显著提升了机器人在长时间依赖任务中的决策能力。

**关键设计**：在设计中，工作记忆通过自适应融合当前标记和记忆库中的信息来更新，采用了特定的损失函数以优化记忆的检索和更新过程。

## 📊 实验亮点

MemoryVLA在SimperEnv-Bridge、Fractal和LIBERO-5等任务中分别取得了71.9%、72.7%和96.5%的成功率，显著超越了现有的CogACT和pi-0基线，尤其在Bridge任务上提升了14.6个百分点。在12个现实任务中，MemoryVLA的成功率达到84.0%，长时间任务的表现比现有基线提升了26个百分点。

## 🎯 应用场景

MemoryVLA的研究成果可广泛应用于机器人操作、自动化生产线、智能家居等领域，提升机器人在复杂环境中的自主决策能力。未来，该框架有望推动更高层次的智能机器人发展，使其在动态和不确定的环境中表现更加出色。

## 📄 摘要（原文）

> Temporal context is essential for robotic manipulation because such tasks are inherently non-Markovian, yet mainstream VLA models typically overlook it and struggle with long-horizon, temporally dependent tasks. Cognitive science suggests that humans rely on working memory to buffer short-lived representations for immediate control, while the hippocampal system preserves verbatim episodic details and semantic gist of past experience for long-term memory. Inspired by these mechanisms, we propose MemoryVLA, a Cognition-Memory-Action framework for long-horizon robotic manipulation. A pretrained VLM encodes the observation into perceptual and cognitive tokens that form working memory, while a Perceptual-Cognitive Memory Bank stores low-level details and high-level semantics consolidated from it. Working memory retrieves decision-relevant entries from the bank, adaptively fuses them with current tokens, and updates the bank by merging redundancies. Using these tokens, a memory-conditioned diffusion action expert yields temporally aware action sequences. We evaluate MemoryVLA on 150+ simulation and real-world tasks across three robots. On SimplerEnv-Bridge, Fractal, and LIBERO-5 suites, it achieves 71.9%, 72.7%, and 96.5% success rates, respectively, all outperforming state-of-the-art baselines CogACT and pi-0, with a notable +14.6 gain on Bridge. On 12 real-world tasks spanning general skills and long-horizon temporal dependencies, MemoryVLA achieves 84.0% success rate, with long-horizon tasks showing a +26 improvement over state-of-the-art baseline. Project Page: https://shihao1895.github.io/MemoryVLA

