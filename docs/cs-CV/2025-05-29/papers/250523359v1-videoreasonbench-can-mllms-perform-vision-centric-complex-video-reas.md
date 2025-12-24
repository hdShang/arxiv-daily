---
layout: default
title: "VideoReasonBench: Can MLLMs Perform Vision-Centric Complex Video Reasoning?"
---

# VideoReasonBench: Can MLLMs Perform Vision-Centric Complex Video Reasoning?

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.23359" class="toolbar-btn" target="_blank">📄 arXiv: 2505.23359v1</a>
  <a href="https://arxiv.org/pdf/2505.23359.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.23359v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.23359v1', 'VideoReasonBench: Can MLLMs Perform Vision-Centric Complex Video Reasoning?')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yuanxin Liu, Kun Ouyang, Haoning Wu, Yi Liu, Lin Sui, Xinhao Li, Yan Zhong, Y. Charles, Xinyu Zhou, Xu Sun

**分类**: cs.CV

**发布日期**: 2025-05-29

**备注**: Project Page: https://llyx97.github.io/video_reason_bench/

---

## 💡 一句话要点

**提出VideoReasonBench以解决视频理解中的复杂推理问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `视频理解` `复杂推理` `长链推理` `多模态LLMs` `基准测试` `视觉内容` `推理能力`

## 📋 核心要点

1. 现有视频理解基准缺乏足够的推理深度，无法充分展示长链推理的优势。
2. 提出VideoReasonBench基准，专注于视觉内容的复杂视频推理，设计了多层次的问题以评估推理能力。
3. 通过对18个多模态LLMs的评估，发现大多数模型在复杂推理上表现不佳，Gemini-2.5-Pro的表现显著优于其他模型。

## 📝 摘要（中文）

近期研究表明，长链推理（CoT）能够显著提升大型语言模型（LLMs）在复杂任务上的表现。然而，在视频理解领域，这一优势尚未得到验证，因为现有基准缺乏足够的推理深度。为此，本文提出了VideoReasonBench，一个旨在评估以视觉为中心的复杂视频推理的基准。每个视频展示了一系列细致的操作，问题则评估了三个逐步提升的视频推理技能。通过对18个最先进的多模态LLMs的评估，发现大多数在复杂视频推理上表现不佳，而思维增强的Gemini-2.5-Pro显著优于其他模型。研究还揭示了在测试时扩展思维预算对提升性能的重要性。

## 🔬 方法详解

**问题定义**：本文旨在解决现有视频理解基准在推理深度上的不足，尤其是在复杂视频推理任务中，现有方法往往依赖知识而非视觉内容。

**核心思路**：提出VideoReasonBench基准，通过设计包含细致操作的视频，确保视觉丰富性和高推理复杂性，以评估模型的推理能力。

**技术框架**：VideoReasonBench包含多个视频，每个视频展示一系列操作，问题分为三个层次：回忆观察到的视觉信息、推断潜在状态内容、预测超出视频的信息。

**关键创新**：最重要的创新在于引入了以视觉为中心的复杂推理任务，强调了长链推理在视频理解中的重要性，与现有基准的知识驱动方法形成鲜明对比。

**关键设计**：在设计中，视频内容的选择和问题的层次化设置是关键，确保模型需要进行逐步推理以得出正确答案。

## 📊 实验亮点

实验结果显示，18个多模态LLMs在VideoReasonBench上的表现普遍较差，例如GPT-4o仅达到6.9%的准确率，而思维增强的Gemini-2.5-Pro则以56.0%的准确率显著领先，展示了长链推理在复杂视频推理中的重要性。

## 🎯 应用场景

该研究的潜在应用领域包括视频分析、智能监控、自动驾驶等，能够帮助模型更好地理解和推理视频内容，提升人机交互的智能化水平。未来，该基准可能推动视频理解领域的进一步研究和技术进步。

## 📄 摘要（原文）

> Recent studies have shown that long chain-of-thought (CoT) reasoning can significantly enhance the performance of large language models (LLMs) on complex tasks. However, this benefit is yet to be demonstrated in the domain of video understanding, since most existing benchmarks lack the reasoning depth required to demonstrate the advantages of extended CoT chains. While recent efforts have proposed benchmarks aimed at video reasoning, the tasks are often knowledge-driven and do not rely heavily on visual content. To bridge this gap, we introduce VideoReasonBench, a benchmark designed to evaluate vision-centric, complex video reasoning. To ensure visual richness and high reasoning complexity, each video in VideoReasonBench depicts a sequence of fine-grained operations on a latent state that is only visible in part of the video. The questions evaluate three escalating levels of video reasoning skills: recalling observed visual information, inferring the content of latent states, and predicting information beyond the video. Under such task setting, models have to precisely recall multiple operations in the video, and perform step-by-step reasoning to get correct final answers for these questions. Using VideoReasonBench, we comprehensively evaluate 18 state-of-the-art multimodal LLMs (MLLMs), finding that most perform poorly on complex video reasoning, e.g., GPT-4o achieves only 6.9% accuracy, while the thinking-enhanced Gemini-2.5-Pro significantly outperforms others with 56.0% accuracy. Our investigations on "test-time scaling" further reveal that extended thinking budget, while offering none or minimal benefits on existing video benchmarks, is essential for improving the performance on VideoReasonBench.

