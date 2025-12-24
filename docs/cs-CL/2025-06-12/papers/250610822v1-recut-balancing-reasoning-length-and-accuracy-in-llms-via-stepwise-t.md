---
layout: default
title: "ReCUT: Balancing Reasoning Length and Accuracy in LLMs via Stepwise Trails and Preference Optimization"
---

# ReCUT: Balancing Reasoning Length and Accuracy in LLMs via Stepwise Trails and Preference Optimization

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.10822" class="toolbar-btn" target="_blank">📄 arXiv: 2506.10822v1</a>
  <a href="https://arxiv.org/pdf/2506.10822.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.10822v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.10822v1', 'ReCUT: Balancing Reasoning Length and Accuracy in LLMs via Stepwise Trails and Preference Optimization')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Zhensheng Jin, Xinze Li, Yifan Ji, Chunyi Peng, Zhenghao Liu, Qi Shi, Yukun Yan, Shuo Wang, Furong Peng, Ge Yu

**分类**: cs.CL

**发布日期**: 2025-06-12

**🔗 代码/项目**: [GITHUB](https://github.com/NEUIR/ReCUT)

---

## 💡 一句话要点

**提出ReCUT以解决大语言模型推理长度与准确性平衡问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大语言模型` `推理优化` `链式思维` `逐步试验` `长短切换采样` `数学推理` `模型集成` `偏好学习`

## 📋 核心要点

1. 现有的链式思维提示法在推理过程中容易导致冗长和重复的推理轨迹，影响效率和准确性。
2. 本文提出的ReCUT方法通过逐步探索和长短切换采样策略，优化推理路径的生成，平衡准确性与长度。
3. 实验结果显示，ReCUT在多个数学推理数据集上将推理长度减少约30-50%，同时保持或提升了推理准确性。

## 📝 摘要（中文）

近年来，链式思维（CoT）提示法显著提升了大语言模型（LLMs）的推理能力。然而，这些方法常常导致过度思考，生成冗长或重复的推理轨迹。现有方法通过策划多个推理链来训练LLMs，但效果受限于生成数据的质量，且易于过拟合。为了解决这一挑战，本文提出了推理压缩通过逐步试验（ReCUT）的方法，旨在平衡推理轨迹的准确性和长度。具体而言，ReCUT采用逐步探索机制和长短切换采样策略，使LLMs能够逐步生成多样的推理路径。这些路径经过评估后用于构建偏好对，以训练两个专门的模型（Gemini LLMs）——一个优化推理准确性，另一个优化短推理。最终通过插值这两个模型的参数获得集成模型。实验结果表明，ReCUT在多个数学推理数据集和基础模型上显著减少推理长度约30-50%，同时保持或提高推理准确性。

## 🔬 方法详解

**问题定义**：本文旨在解决大语言模型在推理过程中产生冗长和重复轨迹的问题。现有方法依赖于多个推理链的策划，效果受限于生成数据质量，且易导致过拟合。

**核心思路**：ReCUT通过逐步试验的方式生成多样化的推理路径，并利用长短切换采样策略来优化推理的准确性与长度，旨在实现更高效的推理过程。

**技术框架**：ReCUT的整体架构包括逐步探索机制和偏好对构建模块。首先，模型生成多条推理路径，然后评估这些路径的质量，最后构建偏好对以训练两个优化模型。

**关键创新**：ReCUT的核心创新在于其逐步探索机制和长短切换采样策略，这与传统方法的单一推理链生成方式有本质区别，能够有效减少推理长度。

**关键设计**：在模型训练中，采用了特定的损失函数来平衡准确性和推理长度，同时设计了两个专门的Gemini LLMs模型，分别优化推理的准确性和简洁性。模型参数的插值方法也为最终集成模型提供了新的思路。

## 📊 实验亮点

实验结果表明，ReCUT在多个数学推理数据集上将推理长度减少了约30-50%，同时在准确性上与多种基线模型相比保持或提升了性能。这一显著的改进展示了ReCUT在推理效率和效果上的双重优势。

## 🎯 应用场景

ReCUT方法在教育、自动化问答和智能助手等领域具有广泛的应用潜力。通过优化推理过程，该方法可以提高用户体验，减少计算资源消耗，并在复杂问题求解中提供更高效的支持。未来，ReCUT的思路也可能被应用于其他类型的生成模型和推理任务中。

## 📄 摘要（原文）

> Recent advances in Chain-of-Thought (CoT) prompting have substantially improved the reasoning capabilities of Large Language Models (LLMs). However, these methods often suffer from overthinking, leading to unnecessarily lengthy or redundant reasoning traces. Existing approaches attempt to mitigate this issue through curating multiple reasoning chains for training LLMs, but their effectiveness is often constrained by the quality of the generated data and prone to overfitting. To address the challenge, we propose Reasoning Compression ThroUgh Stepwise Trials (ReCUT), a novel method aimed at balancing the accuracy and length of reasoning trajectory. Specifically, ReCUT employs a stepwise exploration mechanism and a long-short switched sampling strategy, enabling LLMs to incrementally generate diverse reasoning paths. These paths are evaluated and used to construct preference pairs to train two specialized models (Gemini LLMs)-one optimized for reasoning accuracy, the other for shorter reasoning. A final integrated model is obtained by interpolating the parameters of these two models. Experimental results across multiple math reasoning datasets and backbone models demonstrate that ReCUT significantly reduces reasoning lengths by approximately 30-50%, while maintaining or improving reasoning accuracy compared to various baselines. All codes and data will be released via https://github.com/NEUIR/ReCUT.

