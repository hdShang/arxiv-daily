---
layout: default
title: "StolenLoRA: Exploring LoRA Extraction Attacks via Synthetic Data"
---

# StolenLoRA: Exploring LoRA Extraction Attacks via Synthetic Data

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.23594" class="toolbar-btn" target="_blank">📄 arXiv: 2509.23594v1</a>
  <a href="https://arxiv.org/pdf/2509.23594.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.23594v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.23594v1', 'StolenLoRA: Exploring LoRA Extraction Attacks via Synthetic Data')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yixu Wang, Yan Teng, Yingchun Wang, Xingjun Ma

**分类**: cs.CR, cs.CV

**发布日期**: 2025-09-28

**备注**: ICCV 2025

---

## 💡 一句话要点

**提出StolenLoRA，利用合成数据实现对LoRA适配模型的提取攻击。**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `LoRA提取` `模型提取攻击` `参数高效微调` `合成数据` `半监督学习` `大型语言模型` `模型安全` `视觉模型适配`

## 📋 核心要点

1. LoRA等PEFT方法虽然高效，但其紧凑性使其易受模型提取攻击，存在安全隐患。
2. StolenLoRA利用LLM生成合成数据，并结合分歧半监督学习，高效提取LoRA适配模型的功能。
3. 实验表明，StolenLoRA在低查询次数下具有高攻击成功率，揭示了LoRA适配模型的脆弱性。

## 📝 摘要（中文）

参数高效微调（PEFT）方法如LoRA已经改变了视觉模型的适配方式，实现了定制模型的快速部署。然而，LoRA适配的紧凑性引入了新的安全问题，特别是它们容易受到模型提取攻击。本文提出了一种新的模型提取攻击，名为LoRA提取，它基于公共预训练模型提取LoRA适配模型。然后，我们提出了一种新的提取方法，称为StolenLoRA，它训练一个替代模型，利用合成数据提取LoRA适配模型的功能。StolenLoRA利用大型语言模型来制作有效的数据生成提示，并结合基于分歧的半监督学习（DSL）策略，以最大限度地从有限的查询中获取信息。我们的实验表明了StolenLoRA的有效性，即使在攻击者和受害者模型使用不同预训练骨干网络的跨骨干场景中，仅使用1万次查询即可达到高达96.60%的攻击成功率。这些发现揭示了LoRA适配模型对此类提取的特定脆弱性，并强调了迫切需要针对PEFT方法量身定制的强大防御机制。我们还探索了一种基于多样化LoRA部署的初步防御策略，突出了其减轻此类攻击的潜力。

## 🔬 方法详解

**问题定义**：论文旨在解决LoRA适配模型容易受到模型提取攻击的问题。现有的模型提取攻击方法通常针对完整模型，而忽略了PEFT方法（如LoRA）的特殊性，缺乏针对LoRA适配模型的有效攻击手段。因此，如何高效地提取LoRA适配模型的功能成为一个重要的研究问题。

**核心思路**：论文的核心思路是训练一个替代模型，使其能够模仿LoRA适配模型的行为。通过使用合成数据训练替代模型，攻击者可以在不直接访问受害者模型参数的情况下，提取其功能。利用大型语言模型（LLM）生成高质量的合成数据，并采用基于分歧的半监督学习（DSL）策略，可以提高提取效率和攻击成功率。

**技术框架**：StolenLoRA的整体框架包括以下几个主要阶段：1) **提示生成**：利用LLM生成用于合成数据的提示。2) **数据合成**：使用生成的提示，通过查询受害者LoRA适配模型，生成合成数据集。3) **替代模型训练**：使用合成数据集训练替代模型，使其模仿受害者模型的功能。4) **分歧半监督学习**：利用DSL策略，选择信息量最大的未标记数据进行查询，以提高训练效率。

**关键创新**：StolenLoRA的关键创新在于：1) **针对LoRA适配模型的提取攻击**：专注于提取LoRA适配模型的功能，而非整个模型。2) **基于LLM的提示生成**：利用LLM生成高质量的合成数据，提高了数据质量和多样性。3) **基于分歧的半监督学习（DSL）**：通过选择信息量最大的未标记数据进行查询，提高了训练效率和攻击成功率。

**关键设计**：在提示生成阶段，论文使用了精心设计的提示模板，以引导LLM生成多样化的数据。在DSL阶段，论文采用了基于模型预测分歧的采样策略，选择预测结果差异最大的样本进行查询。替代模型的结构与受害者模型类似，但参数是随机初始化的。损失函数采用交叉熵损失，优化器采用Adam。

## 📊 实验亮点

StolenLoRA在实验中表现出显著的攻击效果，即使在跨骨干网络的情况下，仅使用1万次查询即可达到高达96.60%的攻击成功率。与没有使用LLM生成prompt的方法相比，攻击成功率有显著提升。实验结果表明，LoRA适配模型容易受到基于合成数据的提取攻击，并验证了StolenLoRA的有效性。

## 🎯 应用场景

该研究成果可应用于评估和增强基于LoRA等PEFT方法的模型的安全性。通过模拟攻击，可以发现LoRA适配模型的潜在漏洞，并开发相应的防御机制。此外，该研究还可以促进对PEFT方法安全性的更深入理解，并推动更安全的模型部署实践。

## 📄 摘要（原文）

> Parameter-Efficient Fine-Tuning (PEFT) methods like LoRA have transformed vision model adaptation, enabling the rapid deployment of customized models. However, the compactness of LoRA adaptations introduces new safety concerns, particularly their vulnerability to model extraction attacks. This paper introduces a new focus of model extraction attacks named LoRA extraction that extracts LoRA-adaptive models based on a public pre-trained model. We then propose a novel extraction method called StolenLoRA which trains a substitute model to extract the functionality of a LoRA-adapted model using synthetic data. StolenLoRA leverages a Large Language Model to craft effective prompts for data generation, and it incorporates a Disagreement-based Semi-supervised Learning (DSL) strategy to maximize information gain from limited queries. Our experiments demonstrate the effectiveness of StolenLoRA, achieving up to a 96.60% attack success rate with only 10k queries, even in cross-backbone scenarios where the attacker and victim models utilize different pre-trained backbones. These findings reveal the specific vulnerability of LoRA-adapted models to this type of extraction and underscore the urgent need for robust defense mechanisms tailored to PEFT methods. We also explore a preliminary defense strategy based on diversified LoRA deployments, highlighting its potential to mitigate such attacks.

