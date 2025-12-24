---
layout: default
title: "R1-Code-Interpreter: LLMs Reason with Code via Supervised and Multi-stage Reinforcement Learning"
---

# R1-Code-Interpreter: LLMs Reason with Code via Supervised and Multi-stage Reinforcement Learning

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.21668" class="toolbar-btn" target="_blank">📄 arXiv: 2505.21668v2</a>
  <a href="https://arxiv.org/pdf/2505.21668.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.21668v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.21668v2', 'R1-Code-Interpreter: LLMs Reason with Code via Supervised and Multi-stage Reinforcement Learning')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yongchao Chen, Yueying Liu, Junwei Zhou, Yilun Hao, Jingquan Wang, Yang Zhang, Na Li, Chuchu Fan

**分类**: cs.AI, cs.CL, cs.SC

**发布日期**: 2025-05-27 (更新: 2025-09-29)

**备注**: 26 pages, 10 figures

**🔗 代码/项目**: [GITHUB](https://github.com/yongchao98/R1-Code-Interpreter) | [HUGGINGFACE](https://huggingface.co/yongchao98)

---

## 💡 一句话要点

**提出R1-Code-Interpreter以解决LLMs在代码推理中的挑战**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `代码解释器` `强化学习` `多阶段课程学习` `推理任务` `模型训练`

## 📋 核心要点

1. 现有方法在训练通用代码解释器时面临任务异质性和有效样本稀缺的挑战。
2. 提出了一种多阶段课程学习方法，优先选择高潜力样本进行强化学习训练，逐步转向低潜力样本。
3. 最终模型R1-CI-14B在37个测试任务上的平均准确率从44.1%提升至72.4%，超越了文本模型GPT-4o和带代码解释器的GPT-4o。

## 📝 摘要（中文）

在训练大型语言模型（LLMs）以利用代码解释器进行多任务推理方面，缺乏实用指导。本文提出R1-Code-Interpreter，这是一个通过多轮监督微调和强化学习训练的文本模型扩展，能够在逐步推理中自主生成多个代码查询。与以往集中于狭窄领域的RL + 工具使用方法不同，我们策划了144个多样化的推理与规划任务，并展示了在任务异质性和有效样本稀缺性下，训练通用代码解释器所面临的重大挑战。为此，我们引入了一种多阶段课程学习方法，通过测量改进潜力来划分训练样本，显著提高了模型的性能。

## 🔬 方法详解

**问题定义**：本文旨在解决大型语言模型在多样化推理任务中如何有效利用代码解释器的问题。现有方法在处理任务异质性和样本稀缺性时表现不佳，限制了模型的通用性和准确性。

**核心思路**：提出了一种多阶段课程学习方法，通过对训练样本的改进潜力进行测量，优先选择高潜力样本进行强化学习训练，逐步引入低潜力样本，以提升模型的学习效率和效果。

**技术框架**：整体架构包括多轮监督微调和强化学习两个主要阶段。首先，通过监督微调对模型进行初步训练，然后在强化学习阶段，依据样本的潜力进行动态调整，逐步优化模型的推理能力。

**关键创新**：最重要的创新点在于引入了多阶段课程学习策略，使得模型能够在面对多样化任务时，逐步适应并提升性能。这一方法与传统的单一训练策略有本质区别，能够更有效地应对任务的复杂性。

**关键设计**：在模型训练中，采用了动态样本选择机制，损失函数设计上注重强化学习的收益最大化，网络结构则基于现有的LLM架构进行优化，以适应代码生成的需求。具体参数设置和训练细节在实验部分进行了详细描述。

## 📊 实验亮点

在实验中，R1-CI-14B模型在37个测试任务上的平均准确率从44.1%提升至72.4%，相比文本模型GPT-4o（58.6%）和带代码解释器的GPT-4o（70.9%）均有显著提升，强化学习的平均收益从+3.4%提升至+9.3%。

## 🎯 应用场景

该研究的潜在应用领域包括教育、编程辅助、自动化测试等。通过提升大型语言模型在代码推理任务中的表现，R1-Code-Interpreter能够为开发者提供更智能的编程支持，促进软件开发的效率和质量，未来可能在各类编程相关的AI应用中发挥重要作用。

## 📄 摘要（原文）

> Practical guidance on training Large Language Models (LLMs) to leverage Code Interpreter across diverse tasks remains lacking. We present R1-Code-Interpreter, an extension of a text-only LLM trained via multi-turn supervised fine-tuning (SFT) and reinforcement learning (RL) to autonomously generate multiple code queries during step-by-step reasoning. Unlike prior RL + tool-use efforts focused on narrow domains such as math or retrieval, we curate 144 diverse reasoning and planning tasks and show that training a general-purpose Code Interpreter across them presents significant challenges due to task heterogeneity and scarcity of effective samples. To address this, we introduce a multi-stage curriculum learning approach that partitions training samples by measured improvement potential. The RL training prioritizes samples with higher potential and gradually shifts to lower-potential ones, increasing the average RL gains from merely +3.4% to +9.3% across Qwen-2.5 models (3/7/14B). Our final model, R1-CI-14B, improves average accuracy on the 37 test tasks from 44.1% to 72.4%, outperforming text-only GPT-4o (58.6%) and GPT-4o with Code Interpreter (70.9%). Notably, R1-CI-14B also exhibits emergent self-checking behavior through code generation. Datasets, Codes, and Models are available at https://github.com/yongchao98/R1-Code-Interpreter and https://huggingface.co/yongchao98.

