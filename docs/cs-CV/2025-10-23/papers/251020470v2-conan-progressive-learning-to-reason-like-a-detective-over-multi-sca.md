---
layout: default
title: Conan: Progressive Learning to Reason Like a Detective over Multi-Scale Visual Evidence
---

# Conan: Progressive Learning to Reason Like a Detective over Multi-Scale Visual Evidence

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2510.20470" class="toolbar-btn" target="_blank">📄 arXiv: 2510.20470v2</a>
  <a href="https://arxiv.org/pdf/2510.20470.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.20470v2" onclick="toggleFavorite(this, '2510.20470v2', 'Conan: Progressive Learning to Reason Like a Detective over Multi-Scale Visual Evidence')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Kun Ouyang, Yuanxin Liu, Linli Yao, Yishuo Cai, Hao Zhou, Jie Zhou, Fandong Meng, Xu Sun

**分类**: cs.CV

**发布日期**: 2025-10-23 (更新: 2025-11-20)

---

## 💡 一句话要点

**Conan：提出基于多尺度视觉证据的渐进式学习框架，提升多模态大语言模型在视频推理任务上的性能。**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `视频推理` `多模态大语言模型` `强化学习` `视觉证据` `渐进式学习`

## 📋 核心要点

1. 多模态大语言模型在视频推理中面临挑战，现有方法或依赖无依据的文本链，或难以精确定位视觉证据。
2. Conan框架通过识别上下文和证据帧，进行跨帧线索推理，并自适应决定推理步骤，实现基于视觉证据的多步推理。
3. Conan在多个基准测试中超越了现有模型，并在长视频理解任务中表现出良好的泛化能力和鲁棒性。

## 📝 摘要（中文）

视频推理需要在帧之间进行多步骤推导，这对多模态大语言模型（MLLMs）来说仍然是一个主要的挑战。虽然基于强化学习（RL）的方法增强了推理能力，但它们通常依赖于纯文本链，导致结论缺乏依据或产生幻觉。相反，帧检索方法引入了视觉基础，但仍然难以准确定位证据。为了解决这些限制，我们提出了Conan，一个基于证据的多步骤视频推理框架。Conan识别上下文和证据帧，推理跨帧线索，并自适应地决定何时结束或进一步探索。为此，我们1）构建了Conan-91K，一个大规模的自动生成的推理轨迹数据集，包括帧识别、证据推理和动作决策，以及2）设计了一个多阶段渐进式冷启动策略，结合识别-推理-行动（AIR）RLVR训练框架，以逐步激励多步骤视觉推理。在六个多步骤推理基准上的大量实验表明，Conan的准确率平均超过基线Qwen2.5-VL-7B-Instruct 10%以上，实现了最先进的性能。此外，Conan有效地推广到长视频理解任务，验证了其强大的可扩展性和鲁棒性。

## 🔬 方法详解

**问题定义**：视频推理任务需要模型具备在多个帧之间进行推理的能力，现有方法要么依赖于纯文本推理链，容易产生幻觉；要么依赖于帧检索，但难以准确定位关键证据帧。这些问题限制了模型在复杂视频场景下的推理性能。

**核心思路**：Conan的核心思路是通过渐进式学习，引导模型逐步学习识别关键帧、进行证据推理和做出行动决策。通过强化学习，模型能够自适应地探索和利用视觉证据，从而提高推理的准确性和可靠性。

**技术框架**：Conan框架包含以下几个主要模块：1) 帧识别模块，用于识别与推理相关的上下文帧和证据帧；2) 证据推理模块，用于基于识别的帧进行跨帧线索推理；3) 行动决策模块，用于决定何时结束推理或进一步探索。整个框架采用多阶段渐进式冷启动策略，逐步训练模型的各个模块。

**关键创新**：Conan的关键创新在于其AIR (Identification-Reasoning-Action) 强化学习训练框架和多阶段渐进式冷启动策略。AIR框架将推理过程分解为识别、推理和行动三个步骤，并使用强化学习来优化每个步骤的策略。渐进式冷启动策略则通过逐步增加训练难度，帮助模型更好地学习复杂的推理过程。

**关键设计**：Conan-91K数据集的构建是关键设计之一，它提供了大规模的自动生成的推理轨迹，包括帧识别、证据推理和行动决策。此外，损失函数的设计也至关重要，它需要平衡识别、推理和行动三个步骤的优化目标。具体的网络结构细节在论文中应该有更详细的描述（未知）。

## 📊 实验亮点

Conan在六个多步骤推理基准测试中，平均准确率超过基线模型Qwen2.5-VL-7B-Instruct 10%以上，取得了state-of-the-art的性能。此外，Conan在长视频理解任务中也表现出良好的泛化能力和鲁棒性，验证了其在复杂视频场景下的推理能力。

## 🎯 应用场景

Conan框架可应用于智能监控、视频内容理解、智能客服等领域。例如，在智能监控中，Conan可以用于分析监控视频，识别异常行为并进行预警。在视频内容理解中，Conan可以用于理解视频内容，提取关键信息并生成摘要。在智能客服中，Conan可以用于回答用户关于视频内容的问题。

## 📄 摘要（原文）

> Video reasoning, which requires multi-step deduction across frames, remains a major challenge for multimodal large language models (MLLMs). While reinforcement learning (RL)-based methods enhance reasoning capabilities, they often rely on text-only chains that yield ungrounded or hallucinated conclusions. Conversely, frame-retrieval approaches introduce visual grounding, yet still struggle with inaccurate evidence localization. To address these limitations, we present Conan, a framework for evidence-grounded multi-step video reasoning. Conan identifies context and evidence frames, reasons over cross-frame clues, and adaptively decides when to conclude or explore further. To achieve this, we 1) construct Conan-91K, a large-scale dataset of automatically generated reasoning traces that include frame identification, evidence reasoning, and action decision, and 2) design a multi-stage progressive cold-start strategy combined with an Identification-Reasoning-Action (AIR) RLVR training framework to progressively incentivize multi-step visual reasoning. Extensive experiments on six multi-step reasoning benchmarks demonstrate that Conan surpasses the baseline Qwen2.5-VL-7B-Instruct by an average of over 10% in accuracy, achieving state-of-the-art performance. Furthermore, Conan generalizes effectively to long video understanding tasks, validating its strong scalability and robustness.

