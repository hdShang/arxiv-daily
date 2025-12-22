---
layout: default
title: Deep But Reliable: Advancing Multi-turn Reasoning for Thinking with Images
---

# Deep But Reliable: Advancing Multi-turn Reasoning for Thinking with Images

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.17306" class="toolbar-btn" target="_blank">📄 arXiv: 2512.17306v1</a>
  <a href="https://arxiv.org/pdf/2512.17306.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.17306v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.17306v1', 'Deep But Reliable: Advancing Multi-turn Reasoning for Thinking with Images')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Wenhao Yang, Yu Xia, Jinlong Huang, Shiyin Lu, Qing-Guo Chen, Zhao Xu, Weihua Luo, Kaifu Zhang, Yuanyu Wan, Lijun Zhang

**分类**: cs.CV

**发布日期**: 2025-12-19

---

## 💡 一句话要点

**提出DRIM模型，提升视觉语言模型在图像推理中的多轮自反思能力**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `视觉语言模型` `多轮推理` `自反思` `强化学习` `思维链` `图像理解` `冗余惩罚`

## 📋 核心要点

1. 现有视觉语言模型在复杂视觉任务中，难以反思和纠正错误的推理轨迹。
2. DRIM模型通过数据构建、冷启动SFT和强化学习三个阶段，实现深度且可靠的多轮推理。
3. 实验表明，DRIM模型在视觉理解基准测试中取得了优越的性能。

## 📝 摘要（中文）

本文提出DRIM模型，旨在提升大型视觉语言模型(VLM)在图像推理中进行多轮自反思的能力。现有模型在进行基于图像的思维链(CoT)推理时，难以反思和纠正错误的推理轨迹。DRIM模型通过三阶段流程解决此问题：数据构建、冷启动SFT和强化学习。首先，基于高分辨率图像数据集，构建高难度且可验证的视觉问答对，每个任务需要多轮工具调用才能得到正确答案。在SFT阶段，收集工具轨迹作为冷启动数据，引导多轮推理模式。在强化学习阶段，引入冗余惩罚策略优化，激励模型发展自反思推理模式，对产生错误答案且缺乏充分多尺度探索的推理轨迹进行惩罚。实验结果表明，DRIM在视觉理解基准测试中表现出色。

## 🔬 方法详解

**问题定义**：论文旨在解决现有视觉语言模型在进行多轮图像推理时，缺乏自反思和纠错能力的问题。现有方法在推理过程中，一旦出现错误，很难回溯并修正，导致最终结果错误。这主要是因为模型缺乏对自身推理过程的评估和改进机制。

**核心思路**：论文的核心思路是让模型具备“深度”和“可靠性”的多轮推理能力。通过引入自反思机制，使模型能够评估自身的推理过程，并在发现错误时进行纠正。这种自反思能力通过冗余惩罚策略优化来实现，鼓励模型进行多尺度的探索，并对不充分的探索进行惩罚。

**技术框架**：DRIM模型包含三个主要阶段：1) 数据构建：构建高难度、可验证的视觉问答对，需要多轮工具调用才能解决。2) 冷启动SFT：利用收集到的工具轨迹数据，对模型进行监督微调，引导模型学习多轮推理模式。3) 强化学习：引入冗余惩罚策略优化，训练模型进行自反思推理。

**关键创新**：DRIM的关键创新在于引入了冗余惩罚策略优化，这是一种新型的强化学习方法，旨在激励模型发展自反思推理模式。通过对推理轨迹进行评估，并对那些产生错误答案且缺乏充分多尺度探索的轨迹进行惩罚，模型能够学会识别和纠正自身的错误。

**关键设计**：在数据构建阶段，论文设计了高难度、可验证的视觉问答对，确保模型需要进行多轮推理才能得到正确答案。在强化学习阶段，冗余惩罚策略优化的具体实现方式（例如，如何定义“多尺度探索”和“惩罚”）以及相关的超参数设置是关键的技术细节。具体的损失函数设计也至关重要，需要平衡奖励和惩罚，以引导模型学习到有效的自反思推理策略。

## 📊 实验亮点

DRIM模型在视觉理解基准测试中取得了显著的性能提升，证明了其有效性。具体的性能数据和对比基线需要在论文中查找。DRIM模型通过引入自反思机制，能够更好地理解图像内容，并进行更准确的推理，从而在各种视觉任务中表现出色。

## 🎯 应用场景

DRIM模型具有广泛的应用前景，例如智能客服、自动驾驶、医疗诊断等领域。在这些领域中，模型需要具备强大的推理能力和可靠性，才能做出准确的决策。DRIM模型通过提升视觉语言模型的多轮自反思能力，可以显著提高其在这些领域的应用效果，并推动相关技术的发展。

## 📄 摘要（原文）

> Recent advances in large Vision-Language Models (VLMs) have exhibited strong reasoning capabilities on complex visual tasks by thinking with images in their Chain-of-Thought (CoT), which is achieved by actively invoking tools to analyze visual inputs rather than merely perceiving them. However, existing models often struggle to reflect on and correct themselves when attempting incorrect reasoning trajectories. To address this limitation, we propose DRIM, a model that enables deep but reliable multi-turn reasoning when thinking with images in its multimodal CoT. Our pipeline comprises three stages: data construction, cold-start SFT and RL. Based on a high-resolution image dataset, we construct high-difficulty and verifiable visual question-answer pairs, where solving each task requires multi-turn tool calls to reach the correct answer. In the SFT stage, we collect tool trajectories as cold-start data, guiding a multi-turn reasoning pattern. In the RL stage, we introduce redundancy-penalized policy optimization, which incentivizes the model to develop a self-reflective reasoning pattern. The basic idea is to impose judgment on reasoning trajectories and penalize those that produce incorrect answers without sufficient multi-scale exploration. Extensive experiments demonstrate that DRIM achieves superior performance on visual understanding benchmarks.

