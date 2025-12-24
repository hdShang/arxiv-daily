---
layout: default
title: "VideoJudge: Bootstrapping Enables Scalable Supervision of MLLM-as-a-Judge for Video Understanding"
---

# VideoJudge: Bootstrapping Enables Scalable Supervision of MLLM-as-a-Judge for Video Understanding

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.21451" class="toolbar-btn" target="_blank">📄 arXiv: 2509.21451v1</a>
  <a href="https://arxiv.org/pdf/2509.21451.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.21451v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.21451v1', 'VideoJudge: Bootstrapping Enables Scalable Supervision of MLLM-as-a-Judge for Video Understanding')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Abdul Waheed, Zhen Wu, Dareen Alharthi, Seungone Kim, Bhiksha Raj

**分类**: cs.CV, cs.CL

**发布日期**: 2025-09-25

**备注**: Work in progress

---

## 💡 一句话要点

**VideoJudge：通过自举法实现MLLM作为视频理解评判器的可扩展监督**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `视频理解` `多模态学习` `大型语言模型` `自举学习` `模型评估`

## 📋 核心要点

1. 现有视频理解模型的评估指标（如BLEU）无法准确反映人类的细微判断，人工评估成本高昂。
2. VideoJudge通过生成器和评估器之间的自举方法，训练专门用于视频理解评估的MLLM评判器。
3. 实验表明，VideoJudge-7B在多个元评估基准上优于更大的MLLM评判器基线，证明了其有效性。

## 📝 摘要（中文）

精确评估视频理解模型仍然具有挑战性：常用的指标如BLEU、ROUGE和BERTScore无法捕捉人类判断的细微之处，而通过人工评估获得此类判断的成本很高。最近的工作探索了使用大型语言模型（LLM）或多模态LLM（MLLM）作为评估器，但它们在视频理解中的扩展仍然相对未被探索。在这项工作中，我们介绍了VideoJudge，一个3B和7B大小的MLLM评判器，专门用于评估视频理解模型的输出（即，以视频为条件的文本响应）。为了训练VideoJudge，我们的方法建立在生成器和评估器之间的相互作用上：提示生成器产生以目标评级为条件的响应，并丢弃与评估器的评级不匹配的响应。在四个元评估基准中的三个上，VideoJudge-7B优于更大的MLLM评判器基线，如Qwen2.5-VL（32B和72B）。值得注意的是，我们发现LLM评判器（Qwen3）模型的性能比MLLM评判器（Qwen2.5-VL）更差，并且长链式思维推理并没有提高性能，这表明提供视频输入对于评估视频理解任务至关重要。

## 🔬 方法详解

**问题定义**：论文旨在解决视频理解模型评估不准确且成本高昂的问题。现有评估方法，如BLEU、ROUGE等，无法捕捉人类判断的细微差别。人工评估虽然准确，但耗时耗力，难以大规模应用。因此，需要一种能够自动、准确且高效地评估视频理解模型的方法。

**核心思路**：论文的核心思路是利用多模态大型语言模型（MLLM）作为评判器，并采用自举方法进行训练。通过生成器生成带有目标评分的响应，然后由MLLM评判器进行评估，不匹配的响应将被丢弃。这种方法可以有效地训练MLLM评判器，使其能够准确地评估视频理解模型的输出。

**技术框架**：VideoJudge的训练框架包含两个主要模块：生成器和评估器。生成器负责根据给定的视频和目标评分生成文本响应。评估器是一个MLLM，负责评估生成器生成的响应与目标评分是否一致。训练过程中，生成器和评估器相互作用，不断优化各自的性能。具体流程如下：1) 给定视频和目标评分，生成器生成文本响应；2) 评估器评估生成的响应与目标评分是否一致；3) 如果一致，则保留该样本；否则，丢弃该样本；4) 使用保留的样本训练生成器和评估器。

**关键创新**：论文的关键创新在于提出了基于自举法的MLLM评判器训练方法。该方法无需大量人工标注数据，即可训练出能够准确评估视频理解模型的MLLM评判器。此外，论文还发现，对于视频理解任务的评估，MLLM评判器的性能优于LLM评判器，并且长链式思维推理并没有显著提高性能，这表明提供视频输入对于评估至关重要。

**关键设计**：VideoJudge使用了3B和7B两种尺寸的MLLM作为评估器。生成器可以使用各种视频理解模型，例如，可以采用预训练的视频编码器和文本解码器。训练过程中，可以使用交叉熵损失函数来优化生成器和评估器的性能。此外，还可以采用各种正则化技术来防止过拟合。

## 📊 实验亮点

实验结果表明，VideoJudge-7B在四个元评估基准中的三个上优于更大的MLLM评判器基线，如Qwen2.5-VL（32B和72B）。这表明，通过自举法训练的VideoJudge能够有效地评估视频理解模型的输出，并且具有良好的泛化能力。此外，实验还发现，LLM评判器（Qwen3）的性能不如MLLM评判器（Qwen2.5-VL），表明视频输入对于评估视频理解任务至关重要。

## 🎯 应用场景

VideoJudge可应用于视频理解模型的自动评估和性能监控，加速模型开发迭代过程。它还可用于构建自动化的视频内容审核系统，提高审核效率和准确性。此外，该技术还可应用于教育领域，自动评估学生对视频内容的理解程度。

## 📄 摘要（原文）

> Precisely evaluating video understanding models remains challenging: commonly used metrics such as BLEU, ROUGE, and BERTScore fail to capture the fineness of human judgment, while obtaining such judgments through manual evaluation is costly. Recent work has explored using large language models (LLMs) or multimodal LLMs (MLLMs) as evaluators, but their extension to video understanding remains relatively unexplored. In this work, we introduce VideoJudge, a 3B and 7B-sized MLLM judge specialized to evaluate outputs from video understanding models (\textit{i.e.}, text responses conditioned on videos). To train VideoJudge, our recipe builds on the interplay between a generator and an evaluator: the generator is prompted to produce responses conditioned on a target rating, and responses not matching the evaluator's rating are discarded. Across three out of four meta-evaluation benchmarks, VideoJudge-7B outperforms larger MLLM judge baselines such as Qwen2.5-VL (32B and 72B). Notably, we find that LLM judges (Qwen3) models perform worse than MLLM judges (Qwen2.5-VL) and long chain-of-thought reasoning does not improve performance, indicating that providing video inputs is crucial for evaluation of video understanding tasks.

