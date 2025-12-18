---
layout: default
title: How Do Semantically Equivalent Code Transformations Impact Membership Inference on LLMs for Code?
---

# How Do Semantically Equivalent Code Transformations Impact Membership Inference on LLMs for Code?

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.15468" class="toolbar-btn" target="_blank">📄 arXiv: 2512.15468v1</a>
  <a href="https://arxiv.org/pdf/2512.15468.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.15468v1" onclick="toggleFavorite(this, '2512.15468v1', 'How Do Semantically Equivalent Code Transformations Impact Membership Inference on LLMs for Code?')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Hua Yang, Alejandro Velasco, Thanh Le-Cong, Md Nazmul Haque, Bowen Xu, Denys Poshyvanyk

**分类**: cs.SE, cs.AI, cs.CR

**发布日期**: 2025-12-17

**备注**: 13 pages, 3 figures

---

## 💡 一句话要点

**语义等价代码变换削弱代码大语言模型成员推理攻击的有效性**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `代码大语言模型` `成员推理攻击` `语义等价变换` `知识产权保护` `因果分析`

## 📋 核心要点

1. 代码大语言模型训练依赖大量代码，存在侵犯知识产权的风险，需要成员推理技术进行检测。
2. 论文研究语义等价的代码变换能否绕过成员推理检测，保护私有代码不被泄露。
3. 实验表明，变量重命名等变换能有效降低成员推理的成功率，但组合多种变换效果不佳。

## 📝 摘要（中文）

代码大语言模型的成功依赖于海量的代码数据，包括公共开源仓库和公司私有代码。这引发了关于知识产权合规和未经授权使用受限许可代码的担忧。成员推理（MI）技术已被用于检测此类未经授权的使用，但其有效性可能被语义等价代码变换技术削弱，这些技术在保持语义不变的同时修改代码语法。本文系统地研究了语义等价代码变换规则是否可以用于规避MI检测。结果表明，对于每个规则，模型准确率在最坏情况下仅下降1.5%，表明转换后的数据集可以有效地替代微调。此外，我们发现其中一个规则（RenameVariable）将MI成功率降低了10.19%，突显了其隐藏受限代码存在的潜力。为了验证这些发现，我们进行了因果分析，证实变量重命名在破坏MI检测方面具有最强的因果效应。值得注意的是，我们发现组合多个转换并不能进一步降低MI的有效性。我们的结果揭示了训练代码大语言模型在许可合规执行方面的一个关键漏洞，表明基于转换的混淆技术可以大大削弱MI检测。

## 🔬 方法详解

**问题定义**：论文旨在解决代码大语言模型训练过程中，如何防止模型记忆训练数据，特别是私有或受版权保护的代码，从而避免潜在的知识产权侵犯问题。现有成员推理（MI）技术可以检测模型是否使用了特定代码进行训练，但这些技术容易受到语义等价代码变换的攻击，即攻击者可以通过修改代码的语法结构，同时保持其语义不变，来规避MI检测。现有方法缺乏对这种攻击手段的有效防御。

**核心思路**：论文的核心思路是系统性地研究各种语义等价的代码变换规则对MI检测的影响。通过分析不同变换规则对MI成功率的削弱程度，找出最有效的混淆手段，从而揭示MI检测的脆弱性，并为未来的防御方法提供指导。研究重点在于评估不同变换规则的独立效果以及组合效果，并进行因果分析以验证其影响。

**技术框架**：论文的技术框架主要包括以下几个步骤：1）选择一组具有代表性的语义等价代码变换规则，例如变量重命名、循环展开、条件语句替换等。2）使用这些规则对训练数据集进行变换，生成多个变换后的数据集。3）使用原始数据集和变换后的数据集分别训练代码大语言模型。4）使用MI攻击方法检测这些模型是否记忆了原始训练数据。5）分析不同变换规则对MI成功率的影响，并进行因果分析以验证其因果关系。

**关键创新**：论文最重要的技术创新点在于系统性地研究了多种语义等价代码变换对代码大语言模型成员推理攻击的影响。以往的研究可能只关注单一的变换方法，而本文则全面地评估了多种变换规则，并分析了它们之间的相互作用。此外，论文还通过因果分析验证了变量重命名等变换规则对MI检测的因果效应，为理解MI攻击的原理提供了新的视角。

**关键设计**：论文的关键设计包括：1）选择合适的代码变换规则，确保变换后的代码在语义上与原始代码等价。2）使用标准的成员推理攻击方法，例如基于置信度的攻击或基于损失的攻击。3）使用合适的代码大语言模型作为实验对象，例如基于Transformer的模型。4）采用合适的评估指标，例如MI攻击的准确率或成功率。5）使用因果推断方法，例如DoWhy库，来验证变换规则对MI检测的因果效应。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.15468v1/x1.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.15468v1/x2.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.15468v1/x3.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

实验结果表明，语义等价代码变换可以有效降低成员推理攻击的成功率。其中，变量重命名规则（RenameVariable）能够将MI成功率降低10.19%。然而，组合多种变换规则并不能进一步降低MI的有效性。模型准确率在最坏情况下仅下降1.5%，表明转换后的数据集可以有效地替代微调。

## 🎯 应用场景

该研究成果可应用于代码大语言模型的安全评估和防御。通过了解语义等价代码变换对成员推理攻击的影响，可以设计更鲁棒的成员推理检测方法，从而更好地保护私有代码和知识产权。此外，该研究还可以指导开发者在训练代码大语言模型时，采取合适的混淆技术，以降低模型记忆训练数据的风险。

## 📄 摘要（原文）

> The success of large language models for code relies on vast amounts of code data, including public open-source repositories, such as GitHub, and private, confidential code from companies. This raises concerns about intellectual property compliance and the potential unauthorized use of license-restricted code. While membership inference (MI) techniques have been proposed to detect such unauthorized usage, their effectiveness can be undermined by semantically equivalent code transformation techniques, which modify code syntax while preserving semantic.
>   In this work, we systematically investigate whether semantically equivalent code transformation rules might be leveraged to evade MI detection. The results reveal that model accuracy drops by only 1.5% in the worst case for each rule, demonstrating that transformed datasets can effectively serve as substitutes for fine-tuning. Additionally, we find that one of the rules (RenameVariable) reduces MI success by 10.19%, highlighting its potential to obscure the presence of restricted code. To validate these findings, we conduct a causal analysis confirming that variable renaming has the strongest causal effect in disrupting MI detection. Notably, we find that combining multiple transformations does not further reduce MI effectiveness. Our results expose a critical loophole in license compliance enforcement for training large language models for code, showing that MI detection can be substantially weakened by transformation-based obfuscation techniques.

