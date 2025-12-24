---
layout: default
title: Fusing Bidirectional Chains of Thought and Reward Mechanisms A Method for Enhancing Question-Answering Capabilities of Large Language Models for Chinese Intangible Cultural Heritage
---

# Fusing Bidirectional Chains of Thought and Reward Mechanisms A Method for Enhancing Question-Answering Capabilities of Large Language Models for Chinese Intangible Cultural Heritage

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.08167" class="toolbar-btn" target="_blank">📄 arXiv: 2505.08167v4</a>
  <a href="https://arxiv.org/pdf/2505.08167.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.08167v4" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.08167v4', 'Fusing Bidirectional Chains of Thought and Reward Mechanisms A Method for Enhancing Question-Answering Capabilities of Large Language Models for Chinese Intangible Cultural Heritage')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Ruilin Liu, Zhixiao Zhao, Jieqiong Li, Chang Liu, Dongbo Wang

**分类**: cs.CL, cs.AI

**发布日期**: 2025-05-13 (更新: 2025-06-10)

**备注**: We want to withdraw this paper due to data usage permission issues identified after submission. We discovered that our use of certain intangible cultural heritage materials required additional community permissions and institutional ethical approvals that were not obtained

---

## 💡 一句话要点

**提出双向思维链与奖励机制以提升大语言模型在非物质文化遗产领域的问答能力**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `非物质文化遗产` `大语言模型` `双向思维链` `奖励机制` `问答系统` `模型微调` `知识蒸馏` `领域适应`

## 📋 核心要点

1. 现有方法在使用非物质文化遗产数据微调大语言模型时，面临偏见和知识继承错误等挑战。
2. 本文提出了一种结合双向思维链和奖励机制的新训练方法，以提高模型的问答能力和答案准确性。
3. 实验结果显示，该方法在问答任务中优于多种基线方法，且在多个领域的数据集上具有良好的泛化能力。

## 📝 摘要（中文）

随着大语言模型（LLMs）的快速发展，为领域特定的LLMs提供了重要支持和机会。然而，使用非物质文化遗产（ICH）数据对这些大模型进行微调时，面临偏见、知识继承错误和灾难性遗忘等挑战。为了解决这些问题，本文提出了一种新颖的训练方法，结合了双向思维链和奖励机制。该方法基于专为非物质文化遗产领域设计的ICH-Qwen模型，能够通过反向提问和推理激活模型的潜在知识，从而提高生成答案的准确性。此外，在训练过程中引入奖励机制，通过结构和内容评估优化决策过程。实验结果表明，该方法在问答任务上优于0-shot、逐步推理、知识蒸馏和问题增强方法，展示了其在多个领域的适应性和价值。

## 🔬 方法详解

**问题定义**：本文旨在解决在非物质文化遗产数据上微调大语言模型时出现的偏见、知识继承错误和灾难性遗忘等问题。现有方法在处理这些问题时效果不佳，导致模型的问答能力受限。

**核心思路**：论文提出的核心思路是结合双向思维链与奖励机制，通过反向推理激活模型的潜在知识，从而提升生成答案的准确性和质量。这样的设计旨在优化模型的推理过程，增强其在特定领域的表现。

**技术框架**：整体架构包括双向思维链模块和奖励机制模块。双向思维链模块负责前向推理和反向推理，而奖励机制模块则通过结构和内容评估来优化模型的决策过程。训练过程中，模型会根据不同的权重方案进行评估和调整。

**关键创新**：最重要的技术创新点在于将双向思维链与奖励机制相结合，这一方法在现有技术中尚属首次，显著提升了模型的推理能力和答案生成质量。

**关键设计**：在训练过程中，设置了特定的损失函数和评估标准，以确保模型在不同阶段的输出质量。此外，奖励机制的设计允许根据模型输出的结构和内容进行动态调整，从而进一步优化模型性能。

## 📊 实验亮点

实验结果表明，所提方法在问答任务中相较于0-shot、逐步推理、知识蒸馏和问题增强方法，准确率、Bleu-4和Rouge-L得分均有显著提升，展示了其在多个领域的有效性和适应性。

## 🎯 应用场景

该研究的潜在应用领域包括非物质文化遗产的保护与传播、教育领域的知识传授以及文化研究等。通过提升大语言模型在特定领域的问答能力，该方法为未来在多样化领域的模型训练提供了有价值的思路和方法，具有广泛的实际价值和影响。

## 📄 摘要（原文）

> The rapid development of large language models (LLMs) has provided significant support and opportunities for the advancement of domain-specific LLMs. However, fine-tuning these large models using Intangible Cultural Heritage (ICH) data inevitably faces challenges such as bias, incorrect knowledge inheritance, and catastrophic forgetting. To address these issues, we propose a novel training method that integrates a bidirectional chains of thought and a reward mechanism. This method is built upon ICH-Qwen, a large language model specifically designed for the field of intangible cultural heritage. The proposed method enables the model to not only perform forward reasoning but also enhances the accuracy of the generated answers by utilizing reverse questioning and reverse reasoning to activate the model's latent knowledge. Additionally, a reward mechanism is introduced during training to optimize the decision-making process. This mechanism improves the quality of the model's outputs through structural and content evaluations with different weighting schemes. We conduct comparative experiments on ICH-Qwen, with results demonstrating that our method outperforms 0-shot, step-by-step reasoning, knowledge distillation, and question augmentation methods in terms of accuracy, Bleu-4, and Rouge-L scores on the question-answering task. Furthermore, the paper highlights the effectiveness of combining the bidirectional chains of thought and reward mechanism through ablation experiments. In addition, a series of generalizability experiments are conducted, with results showing that the proposed method yields improvements on various domain-specific datasets and advanced models in areas such as Finance, Wikidata, and StrategyQA. This demonstrates that the method is adaptable to multiple domains and provides a valuable approach for model training in future applications across diverse fields.

