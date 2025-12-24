---
layout: default
title: "Enhancing the Preference Extractor in Multi-turn Dialogues: From Annotating Disasters to Accurate Preference Extraction"
---

# Enhancing the Preference Extractor in Multi-turn Dialogues: From Annotating Disasters to Accurate Preference Extraction

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.01739" class="toolbar-btn" target="_blank">📄 arXiv: 2508.01739v1</a>
  <a href="https://arxiv.org/pdf/2508.01739.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.01739v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.01739v1', 'Enhancing the Preference Extractor in Multi-turn Dialogues: From Annotating Disasters to Accurate Preference Extraction')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Cheng Wang, ziru Liu, Pengcheng Tang, Mingyu Zhang, Quanyu Dai, Yue Zhu

**分类**: cs.CL

**发布日期**: 2025-08-03

---

## 💡 一句话要点

**提出IterChat框架以解决多轮对话中的偏好提取问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多轮对话` `偏好提取` `数据生成` `GPT-4` `对话系统` `标注效率` `机器学习`

## 📋 核心要点

1. 现有方法在多轮对话中偏好提取面临高质量标注数据获取困难，导致偏好转变跟踪不准确。
2. 本文提出IterChat框架，通过构建新数据格式和利用GPT-4生成对话数据，降低标注错误率，提高效率。
3. 实验结果表明，使用新格式微调或少量提示的性能优于原始多轮对话，标注效率提升28.4%。

## 📝 摘要（中文）

在对话系统中识别用户偏好是提供满意服务的关键。现有研究表明，利用大型语言模型（LLMs）微调特定任务的偏好提取器能够取得良好的准确性和泛化能力。然而，获取高质量的标注多轮对话数据的难度较大，导致偏好转变的准确跟踪面临挑战。为此，本文提出了一种新的对话数据生成框架IterChat，通过构建新的数据格式和利用GPT-4生成多样化的对话数据，显著提高了标注效率和模型性能。实验结果显示，使用新数据格式进行微调或少量提示的性能优于原始多轮对话，标注效率提升28.4%。

## 🔬 方法详解

**问题定义**：本文旨在解决多轮对话中用户偏好提取的准确性问题。现有方法在获取高质量标注数据时面临困难，导致偏好转变跟踪不准确，影响模型训练效果。

**核心思路**：论文提出的IterChat框架通过将多轮偏好提取过程分解为单轮提取的迭代执行，构建新的对话数据格式，以减少标注错误并提高标注效率。

**技术框架**：IterChat框架包括两个主要模块：第一，构建新的数据格式，将对话数据分类为带属性的历史偏好和单轮对话；第二，利用GPT-4预定义偏好槽并随机抽样生成对话数据集。

**关键创新**：最重要的技术创新在于新数据格式的构建和GPT-4的应用，使得偏好提取过程更为高效，显著降低了标注错误率。与现有方法相比，IterChat在数据生成和标注效率上具有本质区别。

**关键设计**：在新数据格式中，历史偏好与单轮对话的分离设计减少了标注复杂性，GPT-4的使用确保了生成数据的多样性和高质量，最终提升了模型的训练效果。

## 📊 实验亮点

实验结果显示，使用新对话格式进行微调或少量提示的性能显著优于原始多轮对话，标注效率提升28.4%。这一结果表明，IterChat框架在偏好提取任务中具有明显的优势。

## 🎯 应用场景

该研究的潜在应用领域包括智能客服、个性化推荐系统和人机交互等。通过提高对话系统中用户偏好的提取能力，能够显著提升用户体验和服务质量，未来可能在商业和社交领域产生深远影响。

## 📄 摘要（原文）

> Identifying user preferences in dialogue systems is a pivotal aspect of providing satisfying services. Current research shows that using large language models (LLMs) to fine-tune a task-specific preference extractor yields excellent results in terms of accuracy and generalization. However, the primary challenge stems from the inherent difficulty in obtaining high-quality labeled multi-turn dialogue data. Accurately tracking user preference transitions across turns not only demands intensive domain expertise and contextual consistency maintenance for annotators (termed \textbf{``Annotating Disaster''}) but also complicates model training due to error propagation in sequential dependency learning. Inspired by the observation that multi-turn preference extraction can be decomposed into iterative executions of one-turn extraction processes. We propose a novel dialogue data generation framework named \textbf{IterChat}. First, we construct a new data format that categorizes the dialogue data into attributed historical preferences and one-turn dialogues. This reduces the probability of annotation errors and improves annotation efficiency. Then, to generate a high-quality and diverse dialogue dataset, we adopt GPT4 to pre-define the preference slots in the target preference extractor task and then randomly sample the subset of the slots and their corresponding schema values to create the dialogue datasets. Experimental results indicate that fine-tuning or only few-shot prompting with the new dialogue format yields superior performance compared to the original multi-turn dialogues. Additionally, the new data format improves annotator efficiency with a win rate of 28.4\% higher than the original multi-turn dialogues.

