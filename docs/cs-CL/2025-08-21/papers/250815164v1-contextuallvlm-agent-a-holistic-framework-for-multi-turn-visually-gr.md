---
layout: default
title: "ContextualLVLM-Agent: A Holistic Framework for Multi-Turn Visually-Grounded Dialogue and Complex Instruction Following"
---

# ContextualLVLM-Agent: A Holistic Framework for Multi-Turn Visually-Grounded Dialogue and Complex Instruction Following

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.15164" class="toolbar-btn" target="_blank">📄 arXiv: 2508.15164v1</a>
  <a href="https://arxiv.org/pdf/2508.15164.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.15164v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.15164v1', 'ContextualLVLM-Agent: A Holistic Framework for Multi-Turn Visually-Grounded Dialogue and Complex Instruction Following')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Seungmin Han, Haeun Kwon, Ji-jun Park, Taeyang Yoon

**分类**: cs.CL

**发布日期**: 2025-08-21

---

## 💡 一句话要点

**提出CoLVLM-Agent以解决复杂多轮视觉对话问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多轮对话` `视觉语言模型` `推理能力` `指令遵循` `多模态交互`

## 📋 核心要点

1. 现有模型在处理复杂多轮视觉任务时，面临上下文丢失和视觉幻觉等问题，难以进行深度推理和持续的上下文理解。
2. 提出MMDR-Bench数据集和CoLVLM Agent框架，通过迭代的“记忆-感知-规划-执行”循环，增强推理和指令遵循能力。
3. CoLVLM Agent在MMDR-Bench上表现优异，平均人类评估得分为4.03，超越了GPT-4o和Gemini 1.5 Pro等现有模型。

## 📝 摘要（中文）

尽管大规模语言模型（LLMs）和大规模视觉语言模型（LVLMs）取得了显著进展，但当前模型在处理复杂的多轮视觉任务时仍面临重大挑战。现有基准往往无法捕捉真实世界多模态交互的动态性和复杂性，导致上下文丢失和视觉幻觉等问题。为此，本文提出了MMDR-Bench（多模态对话推理基准），包含300个精心设计的复杂多轮对话场景，并提出CoLVLM Agent（上下文LVLM代理），通过迭代的“记忆-感知-规划-执行”循环增强现有LVLM的推理和指令遵循能力。实验结果表明，CoLVLM Agent在MMDR-Bench上表现优异，平均人类评估得分为4.03，显著超越了现有的商业模型，如GPT-4o（3.92）和Gemini 1.5 Pro（3.85）。

## 🔬 方法详解

**问题定义**：本文旨在解决现有多轮视觉对话模型在复杂任务中面临的上下文丢失和视觉幻觉等问题，现有方法难以有效处理多模态交互的动态性和复杂性。

**核心思路**：提出CoLVLM Agent框架，通过迭代的“记忆-感知-规划-执行”循环，增强模型的推理能力和指令遵循能力，无需对底层模型进行大规模重训练。

**技术框架**：CoLVLM Agent的整体架构包括四个主要模块：记忆模块用于存储上下文信息，感知模块用于处理视觉输入，规划模块负责生成响应，执行模块则实现指令的执行。

**关键创新**：最重要的创新在于提出了MMDR-Bench数据集和CoLVLM Agent框架，显著提升了模型在复杂多轮对话中的推理深度和指令遵循能力，与现有方法相比具有本质的改进。

**关键设计**：在模型设计中，采用了特定的损失函数以优化推理深度，并通过模块化设计确保在多轮对话中保持上下文的一致性和准确性。实验中还对参数设置进行了细致调整，以提升模型的整体性能。

## 📊 实验亮点

在MMDR-Bench上的实验结果显示，CoLVLM Agent的平均人类评估得分为4.03，显著高于现有的商业模型GPT-4o（3.92）和Gemini 1.5 Pro（3.85），在推理深度、指令遵循和错误抑制方面表现出显著优势。

## 🎯 应用场景

该研究的潜在应用领域包括智能客服、虚拟助手和教育领域等，能够在复杂的多模态交互中提供更为精准和自然的对话体验。未来，该框架有望推动多模态人工智能的发展，提升人机交互的智能化水平。

## 📄 摘要（原文）

> Despite significant advancements in Large Language Models (LLMs) and Large Vision-Language Models (LVLMs), current models still face substantial challenges in handling complex, multi-turn, and visually-grounded tasks that demand deep reasoning, sustained contextual understanding, entity tracking, and multi-step instruction following. Existing benchmarks often fall short in capturing the dynamism and intricacies of real-world multi-modal interactions, leading to issues such as context loss and visual hallucinations. To address these limitations, we introduce MMDR-Bench (Multi-Modal Dialogue Reasoning Benchmark), a novel dataset comprising 300 meticulously designed complex multi-turn dialogue scenarios, each averaging 5-7 turns and evaluated across six core dimensions including visual entity tracking and reasoning depth. Furthermore, we propose CoLVLM Agent (Contextual LVLM Agent), a holistic framework that enhances existing LVLMs with advanced reasoning and instruction following capabilities through an iterative "memory-perception-planning-execution" cycle, requiring no extensive re-training of the underlying models. Our extensive experiments on MMDR-Bench demonstrate that CoLVLM Agent consistently achieves superior performance, attaining an average human evaluation score of 4.03, notably surpassing state-of-the-art commercial models like GPT-4o (3.92) and Gemini 1.5 Pro (3.85). The framework exhibits significant advantages in reasoning depth, instruction adherence, and error suppression, and maintains robust performance over extended dialogue turns, validating the effectiveness of its modular design and iterative approach for complex multi-modal interactions.

