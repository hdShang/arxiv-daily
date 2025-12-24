---
layout: default
title: "EgoInstruct: An Egocentric Video Dataset of Face-to-face Instructional Interactions with Multi-modal LLM Benchmarking"
---

# EgoInstruct: An Egocentric Video Dataset of Face-to-face Instructional Interactions with Multi-modal LLM Benchmarking

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.22019" class="toolbar-btn" target="_blank">📄 arXiv: 2509.22019v1</a>
  <a href="https://arxiv.org/pdf/2509.22019.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.22019v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.22019v1', 'EgoInstruct: An Egocentric Video Dataset of Face-to-face Instructional Interactions with Multi-modal LLM Benchmarking')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yuki Sakai, Ryosuke Furuta, Juichun Yen, Yoichi Sato

**分类**: cs.CV

**发布日期**: 2025-09-26

**备注**: Accepted to the I-HFM Workshop at ICCV 2025

---

## 💡 一句话要点

**EgoInstruct：用于人际教学交互的自中心视频数据集与多模态LLM基准测试**

🎯 **匹配领域**: **支柱六：视频提取与匹配 (Video Extraction)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `自中心视频` `人际教学` `多模态学习` `大型语言模型` `数据集` `程序步骤分割` `会话状态分类`

## 📋 核心要点

1. 现有方法缺乏对人际教学场景的系统研究，主要原因是缺少合适的数据集和有效的分析技术。
2. 论文构建了一个新的自中心视频数据集EgoInstruct，并标注了程序步骤分割和会话状态分类两个任务。
3. 实验表明，多模态大型语言模型（MLLM）在理解人际教学场景方面优于专门的基线模型，无需特定任务微调。

## 📝 摘要（中文）

分析教师和学习者在同一物理空间中进行的人际教学互动，对于教育支持和技能转移至关重要。然而，计算机视觉领域尚未系统地研究这种面对面的教学场景。我们认为存在两个主要原因：i) 缺乏合适的数据集；ii) 分析技术有限。为了解决这一差距，我们提出了一个新的自中心视频数据集，用于人际教学，并为两个基本任务提供了真实标注，作为全面理解教学互动的第一步：程序步骤分割和会话状态分类。我们使用该数据集，以传统任务特定模型为基准，评估多模态大型语言模型（MLLM）。由于人际教学涉及多种模态（语音内容和韵律、注视和身体运动以及视觉上下文），因此有效的理解需要以集成方式处理口头和非口头交流的方法。因此，我们评估了最近引入的联合处理图像、音频和文本的MLLM。该评估量化了当前机器学习模型理解人际教学场景的程度。在实验中，MLLM即使没有经过特定任务的微调，也优于专门的基线模型，表明它们在全面理解教学互动方面具有潜力。

## 🔬 方法详解

**问题定义**：论文旨在解决计算机视觉领域对人际教学场景理解不足的问题。现有方法缺乏对教师和学习者之间复杂交互的建模能力，并且缺少高质量的数据集来支持相关研究。因此，现有的方法难以有效地进行程序步骤分割和会话状态分类等任务。

**核心思路**：论文的核心思路是构建一个包含多种模态信息（视频、音频、文本）的自中心视角数据集，并利用多模态大型语言模型（MLLM）来学习和理解人际教学场景中的复杂交互。通过联合处理不同模态的信息，MLLM能够更好地捕捉教师和学习者之间的口头和非口头交流。

**技术框架**：该研究的技术框架主要包括以下几个部分：1) 数据集构建：收集并标注自中心视角的教学视频，包含程序步骤分割和会话状态分类的标注信息。2) 基线模型：选择传统的任务特定模型作为基线，例如用于程序步骤分割的序列模型和用于会话状态分类的分类器。3) 多模态LLM：使用预训练的多模态LLM，例如能够同时处理图像、音频和文本的模型。4) 评估：在构建的数据集上评估MLLM和基线模型的性能，并进行比较分析。

**关键创新**：该论文的关键创新在于：1) 构建了一个新的自中心视角的人际教学数据集EgoInstruct，填补了该领域的数据空白。2) 证明了多模态大型语言模型（MLLM）在理解人际教学场景方面具有潜力，即使没有经过特定任务的微调，也能取得优于传统基线模型的效果。

**关键设计**：论文的关键设计包括：1) 数据集的标注方案，针对程序步骤分割和会话状态分类两个任务进行标注，保证了数据的质量和可用性。2) 多模态LLM的选择，选择了能够同时处理图像、音频和文本的模型，以便充分利用不同模态的信息。3) 实验评估方案，通过与传统基线模型进行比较，验证了MLLM的有效性。

## 📊 实验亮点

实验结果表明，多模态大型语言模型（MLLM）在EgoInstruct数据集上，即使没有经过特定任务的微调，也优于专门的基线模型。这表明MLLM在理解人际教学场景方面具有强大的潜力，能够有效地捕捉和利用不同模态的信息。

## 🎯 应用场景

该研究成果可应用于在线教育、技能培训、远程协作等领域。通过理解人际教学互动，可以开发更智能的教学辅助系统，提升教学效果和学习体验。未来，该研究可以扩展到更复杂的教学场景，例如多人协作教学、个性化教学等。

## 📄 摘要（原文）

> Analyzing instructional interactions between an instructor and a learner who are co-present in the same physical space is a critical problem for educational support and skill transfer. Yet such face-to-face instructional scenes have not been systematically studied in computer vision. We identify two key reasons: i) the lack of suitable datasets and ii) limited analytical techniques. To address this gap, we present a new egocentric video dataset of face-to-face instruction and provide ground-truth annotations for two fundamental tasks that serve as a first step toward a comprehensive understanding of instructional interactions: procedural step segmentation and conversation-state classification. Using this dataset, we benchmark multimodal large language models (MLLMs) against conventional task-specific models. Since face-to-face instruction involves multiple modalities (speech content and prosody, gaze and body motion, and visual context), effective understanding requires methods that handle verbal and nonverbal communication in an integrated manner. Accordingly, we evaluate recently introduced MLLMs that jointly process images, audio, and text. This evaluation quantifies the extent to which current machine learning models understand face-to-face instructional scenes. In experiments, MLLMs outperform specialized baselines even without task-specific fine-tuning, suggesting their promise for holistic understanding of instructional interactions.

