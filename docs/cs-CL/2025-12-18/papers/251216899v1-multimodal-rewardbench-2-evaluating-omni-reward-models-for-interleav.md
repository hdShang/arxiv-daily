---
layout: default
title: "Multimodal RewardBench 2: Evaluating Omni Reward Models for Interleaved Text and Image"
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

**提出Multimodal RewardBench 2，用于评估处理交错文本和图像的通用奖励模型。**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多模态学习` `奖励模型` `基准测试` `图像文本交错` `大型语言模型` `多模态推理` `人类偏好`

## 📋 核心要点

1. 现有奖励模型在处理交错文本和图像的多模态任务中表现不足，缺乏专门的评估基准。
2. 提出Multimodal RewardBench 2 (MMRB2)，一个全面的多模态奖励模型评估基准，包含四个具有挑战性的任务。
3. 实验表明，即使是强大的模型如Gemini 3 Pro，在MMRB2上的表现仍与人类专家存在差距，开源模型Qwen3-VL-32B表现接近Gemini 2.5 Flash。

## 📝 摘要（中文）

奖励模型（RMs）对于训练大型语言模型（LLMs）至关重要，但对于处理交错图像和文本序列的通用模型仍未得到充分探索。我们推出了Multimodal RewardBench 2（MMRB2），这是第一个全面的奖励模型基准，用于多模态理解和（交错）生成。MMRB2涵盖四个任务：文本到图像、图像编辑、交错生成和多模态推理（“用图像思考”），每个任务提供1000个专家标注的偏好对，这些数据来自23个模型和代理，涵盖21个源任务。MMRB2的设计特点包括：（1）实用但具有挑战性的提示；（2）来自最先进模型和代理的响应；（3）通过集成过滤策略策划的具有强烈人类专家共识的偏好对。使用MMRB2，我们研究了每个子任务的现有评判标准，包括多模态LLM-as-a-judge和使用人类偏好训练的模型。最新的Gemini 3 Pro达到了75-80%的准确率。GPT-5和Gemini 2.5 Pro达到了66-75%的准确率，而人类的准确率超过90%，但超过了广泛使用的GPT-4o（59%）。性能最佳的开源模型Qwen3-VL-32B实现了与Gemini 2.5 Flash（64%）相似的准确率。我们还表明，MMRB2的性能与使用Best-of-N抽样的下游任务成功率密切相关，并进行了深入分析，揭示了未来改进奖励模型的关键领域。

## 🔬 方法详解

**问题定义**：论文旨在解决多模态奖励模型评估标准缺失的问题，尤其是在处理交错文本和图像的任务中。现有的奖励模型在评估多模态内容理解和生成方面存在不足，缺乏一个全面、具有挑战性的基准来衡量其性能。这阻碍了多模态LLM的进一步发展。

**核心思路**：论文的核心思路是构建一个高质量、多样化的多模态奖励模型评估基准MMRB2。通过收集来自多个模型和代理的响应，并由人类专家进行标注，形成偏好对，以此来评估奖励模型在不同多模态任务中的表现。这种方法能够更全面地反映奖励模型在实际应用中的能力。

**技术框架**：MMRB2基准包含四个主要任务：文本到图像生成、图像编辑、交错生成和多模态推理。每个任务都包含1000个专家标注的偏好对，这些数据来自23个模型和代理，涵盖21个源任务。数据的收集和标注过程采用了集成过滤策略，以确保偏好对具有高度的人类专家共识。

**关键创新**：MMRB2的关键创新在于其全面性和高质量。它不仅涵盖了多种多模态任务，而且使用了来自最先进模型和代理的响应，并由人类专家进行标注。此外，MMRB2还采用了集成过滤策略，以确保偏好对的质量和一致性。这是首个针对多模态奖励模型的综合性基准。

**关键设计**：MMRB2的设计考虑了实际应用场景，使用了实用但具有挑战性的提示。偏好对的生成过程包括多个步骤，首先是收集来自不同模型和代理的响应，然后由人类专家对这些响应进行排序和标注。为了确保标注的质量，采用了集成过滤策略，即只有当多个专家对同一偏好对达成一致时，该偏好对才会被纳入基准。

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

MMRB2基准测试结果显示，Gemini 3 Pro在多模态任务上达到了75-80%的准确率，GPT-5和Gemini 2.5 Pro达到了66-75%的准确率，但仍低于人类专家的90%以上。开源模型Qwen3-VL-32B的性能与Gemini 2.5 Flash相当，达到了64%的准确率。MMRB2性能与下游任务成功率高度相关。

## 🎯 应用场景

该研究成果可应用于训练和评估多模态大型语言模型，提升模型在图像生成、图像编辑、多模态推理等任务中的性能。MMRB2基准的发布将促进多模态奖励模型的研究和发展，推动相关技术的进步，并最终提升多模态AI应用的质量和用户体验。

## 📄 摘要（原文）

> Reward models (RMs) are essential for training large language models (LLMs), but remain underexplored for omni models that handle interleaved image and text sequences. We introduce Multimodal RewardBench 2 (MMRB2), the first comprehensive benchmark for reward models on multimodal understanding and (interleaved) generation. MMRB2 spans four tasks: text-to-image, image editing, interleaved generation, and multimodal reasoning ("thinking-with-images"), providing 1,000 expert-annotated preference pairs per task from 23 models and agents across 21 source tasks. MMRB2 is designed with: (1) practical but challenging prompts; (2) responses from state-of-the-art models and agents; and (3) preference pairs with strong human-expert consensus, curated via an ensemble filtering strategy. Using MMRB2, we study existing judges for each subtask, including multimodal LLM-as-a-judge and models trained with human preferences. The latest Gemini 3 Pro attains 75-80% accuracy. GPT-5 and Gemini 2.5 Pro reach 66-75% accuracy, compared to >90% for humans, yet surpass the widely used GPT-4o (59%). The best performing open-source model Qwen3-VL-32B achieves similar accuracies as Gemini 2.5 Flash (64%). We also show that MMRB2 performance strongly correlates with downstream task success using Best-of-N sampling and conduct an in-depth analysis that shows key areas to improve the reward models going forward.

