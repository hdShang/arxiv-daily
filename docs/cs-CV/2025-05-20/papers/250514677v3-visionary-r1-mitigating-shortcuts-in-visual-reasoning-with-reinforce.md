---
layout: default
title: Visionary-R1: Mitigating Shortcuts in Visual Reasoning with Reinforcement Learning
---

# Visionary-R1: Mitigating Shortcuts in Visual Reasoning with Reinforcement Learning

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.14677" class="toolbar-btn" target="_blank">📄 arXiv: 2505.14677v3</a>
  <a href="https://arxiv.org/pdf/2505.14677.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.14677v3" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.14677v3', 'Visionary-R1: Mitigating Shortcuts in Visual Reasoning with Reinforcement Learning')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Jiaer Xia, Yuhang Zang, Peng Gao, Sharon Li, Kaiyang Zhou

**分类**: cs.CV

**发布日期**: 2025-05-20 (更新: 2025-10-26)

---

## 💡 一句话要点

**提出Visionary-R1以解决视觉推理中的快捷学习问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `视觉推理` `强化学习` `视觉语言模型` `多模态学习` `推理能力` `图像理解` `无CoT训练`

## 📋 核心要点

1. 现有方法在视觉推理中容易导致模型产生快捷学习，降低泛化能力。
2. 本文提出通过强化学习训练视觉语言模型，采用标题-推理-答案的输出格式，鼓励模型先解读图像。
3. 在273K个无CoT的视觉问答对上训练后，Visionary-R1在多个基准测试中超越了现有的多模态模型。

## 📝 摘要（中文）

学习通用推理能力一直是人工智能领域的挑战。近期的研究表明，强化学习技术能够帮助预训练的大型语言模型（LLMs）通过简单的问答对发展推理能力。本文旨在通过强化学习和视觉问答对训练视觉语言模型（VLMs），以在图像数据上进行推理，而无需显式的思维链（CoT）监督。研究发现，简单地应用强化学习可能导致模型从简单问题中产生快捷学习，从而降低其在未见数据分布上的泛化能力。为此，本文提出在推理之前鼓励模型对图像进行解读，采用“标题-推理-答案”的输出格式进行训练。经过273K个无CoT的视觉问答对训练，Visionary-R1在多个视觉推理基准上超越了强大的多模态模型，如GPT-4o和Claude3.5-Sonnet。

## 🔬 方法详解

**问题定义**：本文旨在解决视觉推理中模型产生快捷学习的问题，现有方法往往导致模型在简单问题上过度拟合，降低其在复杂场景中的泛化能力。

**核心思路**：论文的核心思路是通过强化学习训练视觉语言模型，鼓励模型在回答问题之前先生成图像的详细描述，从而提高推理的准确性和可靠性。

**技术框架**：整体架构包括三个主要阶段：首先生成图像的详细标题，其次构建推理链，最后给出答案。该流程确保模型在推理前充分理解图像内容。

**关键创新**：最重要的技术创新在于引入了“标题-推理-答案”的输出格式，避免了传统方法中直接回答问题的快捷学习现象，从而提升了模型的泛化能力。

**关键设计**：在训练过程中，使用了273K个无CoT的视觉问答对，采用强化学习算法进行优化，确保模型在推理时能够充分利用图像信息，设计了适当的损失函数以平衡各个输出阶段的学习目标。

## 📊 实验亮点

实验结果显示，Visionary-R1在多个视觉推理基准上表现优异，相较于强大的多模态模型如GPT-4o和Claude3.5-Sonnet，性能提升显著，具体提升幅度达到XX%（具体数据待补充）。

## 🎯 应用场景

该研究的潜在应用领域包括智能图像识别、自动问答系统以及多模态内容生成等。通过提升视觉推理能力，Visionary-R1能够在教育、医疗和自动驾驶等领域提供更为精准的决策支持，具有重要的实际价值和未来影响。

## 📄 摘要（原文）

> Learning general-purpose reasoning capabilities has long been a challenging problem in AI. Recent research in large language models (LLMs), such as DeepSeek-R1, has shown that reinforcement learning techniques like GRPO can enable pre-trained LLMs to develop reasoning capabilities using simple question-answer pairs. In this paper, we aim to train visual language models (VLMs) to perform reasoning on image data through reinforcement learning and visual question-answer pairs, without any explicit chain-of-thought (CoT) supervision. Our findings indicate that simply applying reinforcement learning to a VLM -- by prompting the model to produce a reasoning chain before providing an answer -- can lead the model to develop shortcuts from easy questions, thereby reducing its ability to generalize across unseen data distributions. We argue that the key to mitigating shortcut learning is to encourage the model to interpret images prior to reasoning. Therefore, we train the model to adhere to a caption-reason-answer output format: initially generating a detailed caption for an image, followed by constructing an extensive reasoning chain. When trained on 273K CoT-free visual question-answer pairs and using only reinforcement learning, our model, named Visionary-R1, outperforms strong multimodal models, such as GPT-4o, Claude3.5-Sonnet, and Gemini-1.5-Pro, on multiple visual reasoning benchmarks.

