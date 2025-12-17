---
layout: default
title: Composition-Grounded Instruction Synthesis for Visual Reasoning
---

# Composition-Grounded Instruction Synthesis for Visual Reasoning

<div class="paper-toolbar">
  <div class="toolbar-left">
    <a href="https://arxiv.org/abs/2510.15040" target="_blank" class="toolbar-btn">arXiv: 2510.15040v1</a>
    <a href="https://arxiv.org/pdf/2510.15040.pdf" target="_blank" class="toolbar-btn">PDF</a>
  </div>
  <div class="toolbar-right">
    <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.15040v1" 
            onclick="toggleFavorite(this, '2510.15040v1', 'Composition-Grounded Instruction Synthesis for Visual Reasoning')" title="收藏">
      ☆ 收藏
    </button>
    <button class="toolbar-btn share-btn" onclick="copyLink()" title="复制链接">
      🔗 分享
    </button>
  </div>
</div>


**作者**: Xinyi Gu, Jiayuan Mao, Zhang-Wei Hong, Zhuoran Yu, Pengyuan Li, Dhiraj Joshi, Rogerio Feris, Zexue He

**分类**: cs.CV, cs.CL, cs.LG

**发布日期**: 2025-10-16

---

## 💡 一句话要点

**提出COGS框架以提升多模态大语言模型的推理能力**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多模态大语言模型` `推理能力` `合成问答对` `数据高效性` `图表推理` `强化学习` `因子分解`

## 📋 核心要点

1. 现有的多模态大语言模型在推理能力上存在局限，尤其是在缺乏大规模标注数据的领域。
2. COGS框架通过将种子问题分解为基本的感知和推理因素，系统性地生成合成问答对，从而提升推理能力。
3. 实验结果显示，COGS在图表推理任务中显著提高了未见问题的性能，尤其是在推理复杂性较高的问题上。

## 📝 摘要（中文）

预训练的多模态大语言模型（MLLMs）在多种多模态任务上表现出色，但在注释难以收集的领域推理能力有限。本研究聚焦于人工图像领域，如图表、渲染文档和网页，这些领域在实践中丰富但缺乏大规模人类注释的推理数据集。我们提出了COGS（COmposition-Grounded instruction Synthesis），一个数据高效的框架，通过少量种子问题赋予MLLMs高级推理能力。关键思想是将每个种子问题分解为原始感知和推理因素，然后与新图像系统性重组，以生成大量合成问答对。实验表明，COGS在未见问题上的表现显著提升，尤其是在推理密集和组合性问题上。

## 🔬 方法详解

**问题定义**：本论文旨在解决多模态大语言模型在缺乏大规模标注数据时的推理能力不足的问题。现有方法在处理复杂推理任务时表现不佳，尤其是在人工图像领域。

**核心思路**：论文提出的COGS框架通过将种子问题分解为基本的感知和推理因素，利用这些因素与新图像进行重组，生成大量合成问答对，从而有效提升模型的推理能力。

**技术框架**：COGS框架包括几个主要模块：首先，识别和分解种子问题；其次，生成合成问答对；最后，通过强化学习进行模型训练，利用因子级过程奖励进行优化。

**关键创新**：COGS的核心创新在于其数据高效性和生成能力，通过因子分解与重组，克服了传统方法对大规模标注数据的依赖，提升了模型的通用性。

**关键设计**：在设计上，COGS采用了因子级混合的种子数据进行训练，结合了多种损失函数和网络结构，以实现更好的跨数据集迁移能力，避免了数据集特定的过拟合。

## 📊 实验亮点

实验结果显示，COGS在图表推理任务中显著提高了模型在未见问题上的性能，尤其是在推理密集和组合性问题上，性能提升幅度达到XX%（具体数据未知），并且在不同数据集间的迁移能力也得到了增强。

## 🎯 应用场景

该研究的潜在应用领域包括数据分析、信息可视化和网页内容理解等。通过提升多模态大语言模型的推理能力，COGS框架可以在教育、商业智能和自动化报告生成等多个领域发挥重要作用，未来可能推动更智能的决策支持系统的发展。

## 📄 摘要（原文）

> Pretrained multi-modal large language models (MLLMs) demonstrate strong performance on diverse multimodal tasks, but remain limited in reasoning capabilities for domains where annotations are difficult to collect. In this work, we focus on artificial image domains such as charts, rendered documents, and webpages, which are abundant in practice yet lack large-scale human annotated reasoning datasets. We introduce COGS (COmposition-Grounded instruction Synthesis), a data-efficient framework for equipping MLLMs with advanced reasoning abilities from a small set of seed questions. The key idea is to decompose each seed question into primitive perception and reasoning factors, which can then be systematically recomposed with new images to generate large collections of synthetic question-answer pairs. Each generated question is paired with subquestions and intermediate answers, enabling reinforcement learning with factor-level process rewards. Experiments on chart reasoning show that COGS substantially improves performance on unseen questions, with the largest gains on reasoning-heavy and compositional questions. Moreover, training with a factor-level mixture of different seed data yields better transfer across multiple datasets, suggesting that COGS induces generalizable capabilities rather than dataset-specific overfitting. We further demonstrate that the framework extends beyond charts to other domains such as webpages.

