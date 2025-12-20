---
layout: default
title: Multimodal RewardBench 2: Evaluating Omni Reward Models for Interleaved Text and Image
---

# Multimodal RewardBench 2: Evaluating Omni Reward Models for Interleaved Text and Image

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.16899" class="toolbar-btn" target="_blank">📄 arXiv: 2512.16899v1</a>
  <a href="https://arxiv.org/pdf/2512.16899.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.16899v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.16899v1', 'Multimodal RewardBench 2: Evaluating Omni Reward Models for Interleaved Text and Image')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yushi Hu, Reyhane Askari-Hemmat, Melissa Hall, Emily Dinan, Luke Zettlemoyer, Marjan Ghazvininejad

**分类**: cs.CL, cs.CV

**发布日期**: 2025-12-18

**备注**: Code and data available at https://github.com/facebookresearch/MMRB2

---

## 💡 一句话要点

**提出Multimodal RewardBench 2，用于评估处理交错文本和图像的Omni Reward模型。**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多模态学习` `奖励模型` `基准测试` `图像文本交错` `大型语言模型`

## 📋 核心要点

1. 现有奖励模型在处理交错文本和图像的多模态任务中表现不足，缺乏专门的评估基准。
2. 提出Multimodal RewardBench 2 (MMRB2)，包含四个任务，提供专家标注的偏好对，用于全面评估多模态奖励模型。
3. 实验表明，Gemini 3 Pro在MMRB2上表现最佳，但与人类水平仍有差距，开源模型Qwen3-VL-32B表现接近Gemini 2.5 Flash。

## 📝 摘要（中文）

奖励模型(RMs)对于训练大型语言模型(LLMs)至关重要，但对于处理交错图像和文本序列的Omni模型，奖励模型的研究仍然不足。本文提出了Multimodal RewardBench 2 (MMRB2)，这是第一个全面的基准，用于评估多模态理解和（交错）生成方面的奖励模型。MMRB2涵盖四个任务：文本到图像、图像编辑、交错生成和多模态推理（“用图像思考”），每个任务提供1000个专家标注的偏好对，这些数据来自21个源任务中的23个模型和代理。MMRB2的设计特点包括：（1）实用但具有挑战性的提示；（2）来自最先进模型和代理的响应；（3）通过集成过滤策略策划的具有强烈人类专家共识的偏好对。使用MMRB2，我们研究了每个子任务的现有评判器，包括多模态LLM-as-a-judge和使用人类偏好训练的模型。最新的Gemini 3 Pro达到了75-80%的准确率。GPT-5和Gemini 2.5 Pro达到了66-75%的准确率，而人类的准确率超过90%，但它们超过了广泛使用的GPT-4o（59%）。性能最佳的开源模型Qwen3-VL-32B实现了与Gemini 2.5 Flash（64%）相似的准确率。我们还表明，MMRB2的性能与使用Best-of-N抽样的下游任务成功率密切相关，并进行了深入分析，揭示了未来改进奖励模型的关键领域。

## 🔬 方法详解

**问题定义**：论文旨在解决多模态奖励模型评估不足的问题，尤其是在处理交错文本和图像序列时。现有的奖励模型和评估方法主要集中在文本或图像的单模态任务上，缺乏对多模态交互和推理能力的有效评估。这导致了在多模态场景下，奖励模型难以准确衡量生成内容的质量和符合人类偏好的程度。

**核心思路**：论文的核心思路是构建一个全面的多模态奖励模型评估基准，即Multimodal RewardBench 2 (MMRB2)。该基准包含多个具有挑战性的多模态任务，并提供高质量的人工标注偏好数据，用于训练和评估奖励模型。通过在MMRB2上进行评估，可以更准确地了解奖励模型在多模态场景下的性能，并指导模型的改进。

**技术框架**：MMRB2基准包含四个主要任务：（1）文本到图像生成；（2）图像编辑；（3）交错文本和图像生成；（4）多模态推理（“用图像思考”）。每个任务都包含1000个专家标注的偏好对，这些数据来自21个源任务中的23个模型和代理。数据的收集和标注过程采用了集成过滤策略，以确保偏好对具有高度的人类专家共识。

**关键创新**：MMRB2的关键创新在于它是第一个专门针对多模态奖励模型评估的综合性基准。它不仅包含了多种具有挑战性的多模态任务，还提供了高质量的人工标注偏好数据，并采用了严格的质量控制流程。此外，MMRB2还研究了现有评判器（包括多模态LLM-as-a-judge和使用人类偏好训练的模型）的性能，为未来的研究提供了重要的参考。

**关键设计**：MMRB2的关键设计包括：(1) 实用但具有挑战性的提示，旨在模拟真实应用场景；(2) 来自最先进模型和代理的响应，确保评估的代表性；(3) 通过集成过滤策略策划的具有强烈人类专家共识的偏好对，保证数据的质量。此外，论文还分析了MMRB2性能与下游任务成功率之间的相关性，验证了基准的有效性。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.16899v1/x1.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.16899v1/x2.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.16899v1/x3.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

实验结果表明，最新的Gemini 3 Pro在MMRB2上达到了75-80%的准确率，GPT-5和Gemini 2.5 Pro达到了66-75%的准确率，超过了GPT-4o（59%）。开源模型Qwen3-VL-32B实现了与Gemini 2.5 Flash（64%）相似的准确率。MMRB2性能与下游任务成功率高度相关，验证了基准的有效性。

## 🎯 应用场景

该研究成果可应用于训练和评估多模态大型语言模型，提升模型在图像生成、图像编辑、多模态对话和推理等任务中的性能。高质量的奖励模型能够更好地对齐模型输出与人类偏好，从而提高用户体验和应用价值，例如智能助手、内容创作工具等。

## 📄 摘要（原文）

> Reward models (RMs) are essential for training large language models (LLMs), but remain underexplored for omni models that handle interleaved image and text sequences. We introduce Multimodal RewardBench 2 (MMRB2), the first comprehensive benchmark for reward models on multimodal understanding and (interleaved) generation. MMRB2 spans four tasks: text-to-image, image editing, interleaved generation, and multimodal reasoning ("thinking-with-images"), providing 1,000 expert-annotated preference pairs per task from 23 models and agents across 21 source tasks. MMRB2 is designed with: (1) practical but challenging prompts; (2) responses from state-of-the-art models and agents; and (3) preference pairs with strong human-expert consensus, curated via an ensemble filtering strategy. Using MMRB2, we study existing judges for each subtask, including multimodal LLM-as-a-judge and models trained with human preferences. The latest Gemini 3 Pro attains 75-80% accuracy. GPT-5 and Gemini 2.5 Pro reach 66-75% accuracy, compared to >90% for humans, yet surpass the widely used GPT-4o (59%). The best performing open-source model Qwen3-VL-32B achieves similar accuracies as Gemini 2.5 Flash (64%). We also show that MMRB2 performance strongly correlates with downstream task success using Best-of-N sampling and conduct an in-depth analysis that shows key areas to improve the reward models going forward.

