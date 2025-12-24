---
layout: default
title: "UI-UG: A Unified MLLM for UI Understanding and Generation"
---

# UI-UG: A Unified MLLM for UI Understanding and Generation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.24361" class="toolbar-btn" target="_blank">📄 arXiv: 2509.24361v2</a>
  <a href="https://arxiv.org/pdf/2509.24361.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.24361v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.24361v2', 'UI-UG: A Unified MLLM for UI Understanding and Generation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Hao Yang, Weijie Qiu, Ru Zhang, Zhou Fang, Ruichao Mao, Xiaoyu Lin, Maji Huang, Zhaosong Huang, Teng Guo, Shuoyang Liu, Hai Rao

**分类**: cs.CV, cs.AI, cs.HC

**发布日期**: 2025-09-29 (更新: 2025-09-30)

**🔗 代码/项目**: [GITHUB](https://github.com/neovateai/UI-UG)

---

## 💡 一句话要点

**UI-UG：统一的多模态大语言模型，用于用户界面理解与生成**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多模态大语言模型` `用户界面理解` `用户界面生成` `监督微调` `策略优化`

## 📋 核心要点

1. 现有MLLM在UI理解的准确性和UI生成质量方面面临挑战，尤其是在处理复杂UI数据时。
2. UI-UG通过SFT+GRPO提升UI理解的细粒度，并利用DPO使UI生成更符合人类偏好。
3. 实验表明，UI-UG在UI理解上达到SOTA，生成性能与更大模型相当，且整合理解与生成任务能相互促进。

## 📝 摘要（中文）

本文提出UI-UG，一个统一的多模态大语言模型（MLLM），旨在提升用户界面（UI）理解的准确性和UI生成的质量。针对UI理解任务，UI-UG采用监督微调（SFT）结合组相对策略优化（GRPO），以增强对现代复杂UI数据的细粒度理解。对于生成任务，进一步使用直接偏好优化（DPO）使模型生成更符合人类偏好的UI。此外，论文还提出了一套工业界有效的流程，包括LLM友好的领域特定语言（DSL）设计、训练策略、渲染过程和评估指标。实验结果表明，UI-UG在理解任务上达到了最先进（SOTA）的性能，优于更大的通用MLLM和类似大小的UI专用模型。在UI生成性能方面，UI-UG也与这些更大的MLLM相当，但计算成本却大大降低。同时证明了整合理解和生成任务可以提高两者的准确性和质量。

## 🔬 方法详解

**问题定义**：论文旨在解决多模态大语言模型（MLLM）在用户界面（UI）理解的准确性和UI生成质量方面存在的不足。现有方法难以准确理解复杂UI的细粒度信息，并且生成的UI可能不符合人类的偏好。

**核心思路**：论文的核心思路是将UI理解和UI生成两个任务统一到一个MLLM中，通过联合训练来提升模型在这两个任务上的表现。具体而言，通过监督微调（SFT）和组相对策略优化（GRPO）来增强模型对UI的细粒度理解能力，并通过直接偏好优化（DPO）来使模型生成更符合人类偏好的UI。

**技术框架**：UI-UG的技术框架主要包含以下几个部分：1) LLM友好的领域特定语言（DSL）设计，用于描述UI的结构和属性；2) 训练策略，包括SFT、GRPO和DPO；3) 渲染过程，用于将生成的UI描述转换为可视化的UI界面；4) 评估指标，用于评估UI理解和生成的效果。整体流程是先使用SFT和GRPO对模型进行微调，使其具备较强的UI理解能力，然后使用DPO对模型进行优化，使其能够生成更符合人类偏好的UI。

**关键创新**：论文的关键创新在于：1) 提出了一个统一的MLLM，能够同时进行UI理解和生成；2) 采用了GRPO来增强模型对UI的细粒度理解能力；3) 使用DPO来使模型生成更符合人类偏好的UI；4) 设计了一套工业界有效的流程，包括DSL设计、训练策略、渲染过程和评估指标。

**关键设计**：在训练策略方面，论文采用了SFT、GRPO和DPO三种方法。SFT使用标注数据对模型进行微调，使其具备基本的UI理解和生成能力。GRPO通过比较不同UI元素的相对重要性来优化模型的理解能力。DPO通过比较不同UI生成结果的偏好程度来优化模型的生成能力。在DSL设计方面，论文设计了一种LLM友好的DSL，能够清晰地描述UI的结构和属性。

## 📊 实验亮点

UI-UG在UI理解任务上取得了SOTA性能，超越了更大的通用MLLM和同等规模的UI专用模型。在UI生成任务上，UI-UG的性能与更大的MLLM相当，但计算成本更低。实验还证明，整合UI理解和生成任务能够相互促进，提升各自的性能。

## 🎯 应用场景

该研究成果可应用于智能UI设计、自动化UI测试、无障碍UI开发等领域。通过提升UI理解和生成能力，可以降低UI开发的成本，提高UI的质量和用户体验，并为残障人士提供更好的UI交互体验。未来，该技术有望应用于更广泛的人机交互场景。

## 📄 摘要（原文）

> Although Multimodal Large Language Models (MLLMs) have been widely applied across domains, they are still facing challenges in domain-specific tasks, such as User Interface (UI) understanding accuracy and UI generation quality. In this paper, we introduce UI-UG (a unified MLLM for UI Understanding and Generation), integrating both capabilities. For understanding tasks, we employ Supervised Fine-tuning (SFT) combined with Group Relative Policy Optimization (GRPO) to enhance fine-grained understanding on the modern complex UI data. For generation tasks, we further use Direct Preference Optimization (DPO) to make our model generate human-preferred UIs. In addition, we propose an industrially effective workflow, including the design of an LLM-friendly domain-specific language (DSL), training strategies, rendering processes, and evaluation metrics. In experiments, our model achieves state-of-the-art (SOTA) performance on understanding tasks, outperforming both larger general-purpose MLLMs and similarly-sized UI-specialized models. Our model is also on par with these larger MLLMs in UI generation performance at a fraction of the computational cost. We also demonstrate that integrating understanding and generation tasks can improve accuracy and quality for both tasks. Code and Model: https://github.com/neovateai/UI-UG

