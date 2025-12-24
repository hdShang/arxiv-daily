---
layout: default
title: "Backprompting: Leveraging Synthetic Production Data for Health Advice Guardrails"
---

# Backprompting: Leveraging Synthetic Production Data for Health Advice Guardrails

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.18384" class="toolbar-btn" target="_blank">📄 arXiv: 2508.18384v1</a>
  <a href="https://arxiv.org/pdf/2508.18384.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.18384v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.18384v1', 'Backprompting: Leveraging Synthetic Production Data for Health Advice Guardrails')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Kellen Tan Cheng, Anna Lisa Gentile, Chad DeLuca, Guang-Jie Ren

**分类**: cs.CL, cs.AI

**发布日期**: 2025-08-25

---

## 💡 一句话要点

**提出反向提示技术以生成健康建议的标注数据**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `反向提示` `健康建议` `数据标注` `护栏技术` `大型语言模型` `人机协作` `合成数据`

## 📋 核心要点

1. 现有护栏技术在开发和维护强大的检测器时面临获取高质量标注数据的挑战。
2. 本文提出反向提示技术，通过生成生产环境相似的标注数据来支持健康建议护栏的开发。
3. 实验结果表明，所提检测器在健康建议识别任务中超越了GPT-4o，提升幅度达到3.73%。

## 📝 摘要（中文）

大型语言模型（LLMs）在企业环境中的广泛应用带来了显著的风险。为了降低这些风险，护栏技术通过各种检测器过滤LLMs的输入/输出文本。然而，开发和维护强大的检测器面临许多挑战，其中之一是难以获取高质量的标注数据。本文提出了一种简单直观的解决方案——反向提示（backprompting），用于生成类似生产环境的标注数据，以支持健康建议护栏的开发。我们将反向提示方法与稀疏的人机协作聚类技术结合，标注生成的数据。我们的目标是构建一个与原始数据集大致相似的平行语料库，并将合成示例注入现有数据集中，以生成强大的训练数据。我们在识别LLM输出中的健康建议这一复杂护栏上测试了该技术，并展示了相较于其他解决方案的改进。尽管参数量少达400倍，我们的检测器仍能超越GPT-4o，提升幅度达到3.73%。

## 🔬 方法详解

**问题定义**：本文旨在解决在大型语言模型输出中识别健康建议的难题，现有方法在获取高质量标注数据方面存在不足，限制了检测器的性能。

**核心思路**：提出反向提示技术，通过生成与真实生产环境相似的标注数据，来增强健康建议护栏的开发和训练。该方法简单直观，易于实现。

**技术框架**：整体流程包括反向提示生成合成数据、稀疏人机协作聚类标注生成的数据，以及将合成数据与现有数据集结合以增强训练数据。

**关键创新**：反向提示技术是本文的核心创新点，它通过生成生产环境相似的标注数据，解决了获取真实标注数据的困难，与传统方法相比具有显著优势。

**关键设计**：在技术实现中，采用了稀疏人机协作聚类技术来标注生成的数据，确保数据的质量和多样性，同时保持了较低的参数量，使得检测器在性能上具备竞争力。

## 📊 实验亮点

实验结果显示，所提出的检测器在健康建议识别任务中超越了GPT-4o，提升幅度达到3.73%。尽管参数量减少了400倍，检测器仍能保持较高的性能，证明了反向提示技术的有效性和实用性。

## 🎯 应用场景

该研究的潜在应用领域包括医疗健康、在线咨询和智能客服等场景。通过生成高质量的标注数据，能够有效提升大型语言模型在健康建议领域的安全性和可靠性，降低误导性信息的风险，具有重要的实际价值和未来影响。

## 📄 摘要（原文）

> The pervasiveness of large language models (LLMs) in enterprise settings has also brought forth a significant amount of risks associated with their usage. Guardrails technologies aim to mitigate this risk by filtering LLMs' input/output text through various detectors. However, developing and maintaining robust detectors faces many challenges, one of which is the difficulty in acquiring production-quality labeled data on real LLM outputs prior to deployment. In this work, we propose backprompting, a simple yet intuitive solution to generate production-like labeled data for health advice guardrails development. Furthermore, we pair our backprompting method with a sparse human-in-the-loop clustering technique to label the generated data. Our aim is to construct a parallel corpus roughly representative of the original dataset yet resembling real LLM output. We then infuse existing datasets with our synthetic examples to produce robust training data for our detector. We test our technique in one of the most difficult and nuanced guardrails: the identification of health advice in LLM output, and demonstrate improvement versus other solutions. Our detector is able to outperform GPT-4o by up to 3.73%, despite having 400x less parameters.

