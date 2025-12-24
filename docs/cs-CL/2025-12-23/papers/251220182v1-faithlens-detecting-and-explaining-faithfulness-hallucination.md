---
layout: default
title: FaithLens: Detecting and Explaining Faithfulness Hallucination
---

# FaithLens: Detecting and Explaining Faithfulness Hallucination

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.20182" class="toolbar-btn" target="_blank">📄 arXiv: 2512.20182v1</a>
  <a href="https://arxiv.org/pdf/2512.20182.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.20182v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.20182v1', 'FaithLens: Detecting and Explaining Faithfulness Hallucination')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Shuzheng Si, Qingyi Wang, Haozhe Zhao, Yuzhuo Bai, Guanqiao Chen, Kangyang Luo, Gang Chen, Fanchao Qi, Minjia Zhang, Baobao Chang, Maosong Sun

**分类**: cs.CL, cs.AI

**发布日期**: 2025-12-23

---

## 💡 一句话要点

**提出FaithLens，用于检测并解释大语言模型中的忠实性幻觉。**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `忠实性幻觉检测` `大语言模型` `可解释性` `强化学习` `数据合成`

## 📋 核心要点

1. 大型语言模型（LLM）的幻觉问题严重影响其在实际应用中的可靠性，尤其是在检索增强生成和摘要等任务中。
2. FaithLens通过合成带有解释的训练数据，并结合数据过滤和强化学习，实现了对幻觉的有效检测和解释。
3. 实验结果表明，FaithLens在多个任务上超越了GPT-4.1等先进模型，同时提供了高质量的解释，提升了模型的可信度。

## 📝 摘要（中文）

本文介绍FaithLens，一种经济高效且有效的忠实性幻觉检测模型，它可以联合提供二元预测和相应的解释，以提高可信度。为了实现这一目标，我们首先通过先进的大语言模型合成带有解释的训练数据，并应用明确定义的数据过滤策略，以确保标签正确性、解释质量和数据多样性。随后，我们使用这些精心策划的训练数据对模型进行冷启动微调，并使用基于规则的强化学习进一步优化它，使用预测正确性和解释质量的奖励。在12个不同任务上的结果表明，80亿参数的FaithLens优于GPT-4.1和o3等先进模型。此外，FaithLens可以产生高质量的解释，从而在可信度、效率和有效性之间实现独特的平衡。

## 🔬 方法详解

**问题定义**：论文旨在解决大型语言模型（LLM）中普遍存在的“忠实性幻觉”问题。现有方法要么无法有效检测幻觉，要么缺乏对幻觉原因的解释，导致用户难以信任LLM的输出。因此，需要一种既能准确检测幻觉，又能提供可信解释的解决方案。

**核心思路**：FaithLens的核心思路是训练一个能够联合预测幻觉存在与否，并提供相应解释的模型。通过高质量的训练数据和强化学习，模型能够学习到幻觉的模式，并生成人类可理解的解释，从而提高模型的可信度。

**技术框架**：FaithLens的整体框架包括以下几个主要阶段：1) **数据合成**：使用先进的LLM生成带有解释的训练数据。2) **数据过滤**：应用数据过滤策略，确保数据的标签正确性、解释质量和数据多样性。3) **冷启动微调**：在过滤后的数据上对模型进行微调，作为模型的初始状态。4) **强化学习优化**：使用基于规则的强化学习，根据预测正确性和解释质量对模型进行优化。

**关键创新**：FaithLens的关键创新在于其联合预测和解释的能力，以及其训练数据的生成和优化方法。通过合成高质量的训练数据，并使用强化学习进行优化，FaithLens能够学习到幻觉的复杂模式，并生成可信的解释。此外，基于规则的强化学习奖励函数的设计也是一个创新点，它能够同时考虑预测的准确性和解释的质量。

**关键设计**：在数据合成阶段，论文使用了先进的LLM来生成训练数据，并设计了特定的prompt来引导LLM生成高质量的解释。在数据过滤阶段，论文定义了一系列规则来过滤掉标签错误、解释质量差或数据多样性不足的数据。在强化学习阶段，论文设计了基于规则的奖励函数，该函数根据预测的准确性和解释的质量来奖励模型。具体的参数设置和网络结构细节在论文中未详细描述，属于未知信息。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.20182v1/x3.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.20182v1/x4.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.20182v1/x5.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

FaithLens在12个不同的任务上进行了评估，结果表明，80亿参数的FaithLens优于GPT-4.1和o3等先进模型。此外，FaithLens能够生成高质量的解释，从而在可信度、效率和有效性之间实现独特的平衡。具体的性能提升幅度在论文中未给出明确的量化数据，属于未知信息。

## 🎯 应用场景

FaithLens可应用于各种需要LLM提供可靠输出的场景，例如检索增强生成、文本摘要、问答系统等。通过检测和解释幻觉，FaithLens可以提高LLM输出的可信度，减少错误信息的传播，并帮助用户更好地理解LLM的推理过程。未来，FaithLens可以进一步扩展到其他类型的LLM和任务中，成为提高LLM可靠性的重要工具。

## 📄 摘要（原文）

> Recognizing whether outputs from large language models (LLMs) contain faithfulness hallucination is crucial for real-world applications, e.g., retrieval-augmented generation and summarization. In this paper, we introduce FaithLens, a cost-efficient and effective faithfulness hallucination detection model that can jointly provide binary predictions and corresponding explanations to improve trustworthiness. To achieve this, we first synthesize training data with explanations via advanced LLMs and apply a well-defined data filtering strategy to ensure label correctness, explanation quality, and data diversity. Subsequently, we fine-tune the model on these well-curated training data as a cold start and further optimize it with rule-based reinforcement learning, using rewards for both prediction correctness and explanation quality. Results on 12 diverse tasks show that the 8B-parameter FaithLens outperforms advanced models such as GPT-4.1 and o3. Also, FaithLens can produce high-quality explanations, delivering a distinctive balance of trustworthiness, efficiency, and effectiveness.

