---
layout: default
title: Optimizing Large Language Models for ESG Activity Detection in Financial Texts
---

# Optimizing Large Language Models for ESG Activity Detection in Financial Texts

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2502.21112" class="toolbar-btn" target="_blank">📄 arXiv: 2502.21112</a>
  <a href="https://arxiv.org/pdf/2502.21112.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2502.21112" onclick="toggleFavorite(this, '2502.21112', 'Optimizing Large Language Models for ESG Activity Detection in Financial Texts')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Mattia Birti, Andrea Maurino, Francesco Osborne

**分类**: cs.AI, cs.CE, cs.CL, cs.CY, cs.IR

**发布日期**: 2025-12-18

---

## 💡 一句话要点

**通过微调大型语言模型，提升金融文本中ESG活动检测的准确性。**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `ESG活动检测` `大型语言模型` `金融文本` `微调` `合成数据` `可持续金融` `自然语言处理`

## 📋 核心要点

1. 通用大语言模型在特定领域的表现受限，且缺乏高质量的结构化ESG数据集，导致金融文本中ESG活动检测任务面临挑战。
2. 该论文通过微调大语言模型，结合原始数据和合成数据，提升模型在ESG活动识别方面的性能，从而更好地对齐可持续性报告与监管框架。
3. 实验结果表明，在ESG-Activities数据集上微调后，Llama 7B和Gemma 7B等开源模型在特定配置下优于大型商业模型。

## 📝 摘要（中文）

将环境、社会和治理（ESG）因素整合到企业决策中是可持续金融的一个基本方面。然而，确保商业实践与不断发展的监管框架保持一致仍然是一个持续的挑战。用于自动评估可持续性报告和非财务披露与特定ESG活动的一致性的人工智能驱动解决方案，可以极大地支持这一过程。然而，由于通用大型语言模型（LLM）在特定领域环境中的局限性以及结构化、高质量数据集的稀缺性，这项任务仍然很复杂。本文研究了当前一代LLM识别与环境活动相关的文本的能力。此外，我们证明了通过对原始和合成生成的数据组合进行微调，可以显著提高其性能。为此，我们引入了ESG-Activities，这是一个基准数据集，包含1,325个标记的文本片段，这些片段根据欧盟ESG分类法进行分类。我们的实验结果表明，在ESG-Activities上进行微调可以显著提高分类准确性，在特定配置中，Llama 7B和Gemma 7B等开放模型优于大型专有解决方案。这些发现对于金融分析师、政策制定者和人工智能研究人员具有重要意义，他们希望通过先进的自然语言处理技术来提高ESG透明度和合规性。

## 🔬 方法详解

**问题定义**：论文旨在解决金融文本中自动检测与识别ESG（环境、社会和治理）活动的问题。现有方法，特别是通用大语言模型，在处理领域特定任务时存在局限性，并且缺乏高质量的标注数据来训练模型，导致检测精度不高。

**核心思路**：论文的核心思路是通过在特定领域的ESG数据集上对大型语言模型进行微调，使其更好地适应金融文本的特点，从而提高ESG活动检测的准确性。同时，利用合成数据增强训练集，缓解数据稀缺问题。

**技术框架**：整体框架包括以下几个步骤：1) 构建ESG-Activities数据集，包含人工标注的金融文本片段；2) 利用原始数据和合成数据组合对预训练的大型语言模型进行微调；3) 在测试集上评估微调后模型的性能，并与基线模型进行比较。主要模块包括数据预处理、模型微调和性能评估。

**关键创新**：论文的关键创新在于：1) 构建了一个高质量的ESG-Activities基准数据集，为该领域的研究提供了数据基础；2) 证明了通过微调和合成数据增强，可以显著提升大型语言模型在ESG活动检测任务中的性能，甚至超越一些大型商业模型。

**关键设计**：论文的关键设计包括：1) 数据集的构建，需要仔细设计标注规范，确保数据质量；2) 微调策略的选择，包括选择合适的预训练模型、调整学习率等超参数；3) 合成数据的生成方法，需要保证合成数据的真实性和多样性，避免引入噪声。

## 📊 实验亮点

实验结果表明，通过在ESG-Activities数据集上进行微调，Llama 7B和Gemma 7B等开源模型在特定配置下优于大型商业模型，显著提高了ESG活动检测的准确性。该研究验证了微调和合成数据增强在提升领域特定任务性能方面的有效性。

## 🎯 应用场景

该研究成果可应用于金融分析、政策制定和企业合规等领域。金融分析师可以利用该技术自动评估企业的ESG表现，政策制定者可以监测企业是否符合相关法规，企业可以自查自纠，提高ESG透明度和合规性。该研究有助于推动可持续金融的发展。

## 📄 摘要（原文）

> The integration of Environmental, Social, and Governance (ESG) factors into corporate decision-making is a fundamental aspect of sustainable finance. However, ensuring that business practices align with evolving regulatory frameworks remains a persistent challenge. AI-driven solutions for automatically assessing the alignment of sustainability reports and non-financial disclosures with specific ESG activities could greatly support this process. Yet, this task remains complex due to the limitations of general-purpose Large Language Models (LLMs) in domain-specific contexts and the scarcity of structured, high-quality datasets. In this paper, we investigate the ability of current-generation LLMs to identify text related to environmental activities. Furthermore, we demonstrate that their performance can be significantly enhanced through fine-tuning on a combination of original and synthetically generated data. To this end, we introduce ESG-Activities, a benchmark dataset containing 1,325 labelled text segments classified according to the EU ESG taxonomy. Our experimental results show that fine-tuning on ESG-Activities significantly enhances classification accuracy, with open models such as Llama 7B and Gemma 7B outperforming large proprietary solutions in specific configurations. These findings have important implications for financial analysts, policymakers, and AI researchers seeking to enhance ESG transparency and compliance through advanced natural language processing techniques.

