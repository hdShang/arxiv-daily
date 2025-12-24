---
layout: default
title: SAMChat: Introducing Chain of Thought Reasoning and GRPO to a Multimodal Small Language Model for Small Scale Remote Sensing
---

# SAMChat: Introducing Chain of Thought Reasoning and GRPO to a Multimodal Small Language Model for Small Scale Remote Sensing

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.07984" class="toolbar-btn" target="_blank">📄 arXiv: 2505.07984v2</a>
  <a href="https://arxiv.org/pdf/2505.07984.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.07984v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.07984v2', 'SAMChat: Introducing Chain of Thought Reasoning and GRPO to a Multimodal Small Language Model for Small Scale Remote Sensing')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Aybora Koksal, A. Aydin Alatan

**分类**: cs.CV

**发布日期**: 2025-05-12 (更新: 2025-11-27)

**备注**: Accepted to Journal of Selected Topics in Applied Earth Observations and Remote Sensing (JSTARS) Special Issue on Foundation and Large Vision Models for Remote Sensing. Code and dataset are available at https://github.com/aybora/SAMChat

**DOI**: [10.1109/JSTARS.2025.3637115](https://doi.org/10.1109/JSTARS.2025.3637115)

---

## 💡 一句话要点

**提出SAMChat以解决小规模遥感图像分析问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多模态模型` `遥感分析` `链式思维推理` `群体相对策略优化` `军事设施识别` `数据集构建` `精确分析`

## 📋 核心要点

1. 现有的多模态大语言模型在特定领域应用时，尤其是资源有限的遥感图像分析中，效果不佳。
2. 本研究提出SAMChat模型，结合链式思维推理和群体相对策略优化，专注于遥感图像的精准分析。
3. 实验结果显示，SAMChat在新提出的SAMData基准上实现了超过80%的召回率和98%的精确率，显著优于现有方法。

## 📝 摘要（中文）

近年来，多模态大语言模型在理解和生成文本-图像内容方面展现了显著能力。然而，这些模型在特定领域，尤其是需要资源高效和领域特定适应的场景中，效果仍然有限。本研究提出了一种轻量级的多模态语言模型SAMChat，专门用于分析偏远地区的遥感图像，包括具有挑战性的导弹发射场。通过专家审核验证的数百张航空图像，构建了新的数据集SAMData，并通过详细的说明突出微妙的军事设施。对一个具有20亿参数的开源多模态模型进行了监督微调，结合链式思维推理注释，提升了模型的准确性和可解释性。此外，利用群体相对策略优化（GRPO）增强了模型检测关键领域特征的能力，同时减少对平民场景的误报。实验证明，SAMChat在开放式描述和分类指标上显著优于更大的一般多模态模型及现有的遥感适应方法。

## 🔬 方法详解

**问题定义**：本研究旨在解决现有多模态模型在遥感图像分析中的不足，尤其是在资源受限和领域特定的应用场景中，现有方法往往无法有效识别和分析军事设施。

**核心思路**：论文提出的SAMChat模型通过引入链式思维推理（CoT）和群体相对策略优化（GRPO），实现了对遥感图像的精确分析和解释，能够更好地捕捉领域特定的线索。

**技术框架**：SAMChat的整体架构包括数据集构建、模型微调和评估三个主要阶段。首先，构建了包含专家审核的航空图像数据集SAMData；其次，对一个20亿参数的开源多模态模型进行监督微调；最后，通过实验评估模型的性能。

**关键创新**：本研究的核心创新在于结合链式思维推理和GRPO，提升了模型在特定领域的表现，尤其是在减少误报方面，与现有方法相比具有显著优势。

**关键设计**：在模型微调过程中，采用了专门设计的损失函数和参数设置，以确保模型在识别军事设施时的高精度和高召回率，同时优化了网络结构以适应多模态输入。

## 📊 实验亮点

在实验中，SAMChat在新提出的SAMData基准上取得了超过80%的召回率和98%的精确率，显著优于现有的多模态模型和遥感适应方法。这一结果表明，针对特定领域的微调和强化学习策略能够显著提升模型性能。

## 🎯 应用场景

SAMChat模型的潜在应用领域包括军事侦察、灾后评估和环境监测等。通过精准分析遥感图像，该模型能够为决策者提供重要的情报支持，提升应对突发事件的能力。未来，该技术有望扩展到更多领域，如城市规划和资源管理，具有广泛的实际价值。

## 📄 摘要（原文）

> Remarkable capabilities in understanding and generating text-image content have been demonstrated by recent advancements in multimodal large language models (MLLMs). However, their effectiveness in specialized domains-particularly those requiring resource-efficient and domain-specific adaptations-has remained limited. In this work, a lightweight multimodal language model termed SAMChat is introduced, specifically adapted to analyze remote sensing imagery in secluded areas, including challenging missile launch sites. A new dataset, SAMData, was compiled by verifying hundreds of aerial images through expert review, and subtle military installations were highlighted via detailed captions. Supervised fine-tuning on a 2B parameter open-source MLLM with chain-of-thought (CoT) reasoning annotations was performed, enabling more accurate and interpretable explanations. Additionally, Group Relative Policy Optimization (GRPO) was leveraged to enhance the model's ability to detect critical domain-specific cues-such as defensive layouts and key military structures-while minimizing false positives on civilian scenes. Through empirical evaluations, it has been shown that SAMChat significantly outperforms both larger, general-purpose multimodal models and existing remote sensing adapted approaches on open-ended captioning and classification metrics. Over 80% recall and 98% precision were achieved on the newly proposed SAMData benchmark, underscoring the potency of targeted fine-tuning and reinforcement learning in specialized real-world applications.

