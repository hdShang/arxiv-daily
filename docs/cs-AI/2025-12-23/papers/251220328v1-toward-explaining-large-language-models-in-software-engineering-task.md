---
layout: default
title: Toward Explaining Large Language Models in Software Engineering Tasks
---

# Toward Explaining Large Language Models in Software Engineering Tasks

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.20328" class="toolbar-btn" target="_blank">📄 arXiv: 2512.20328v1</a>
  <a href="https://arxiv.org/pdf/2512.20328.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.20328v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.20328v1', 'Toward Explaining Large Language Models in Software Engineering Tasks')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Antonio Vitale, Khai-Nguyen Nguyen, Denys Poshyvanyk, Rocco Oliveto, Simone Scalabrino, Antonio Mastropaolo

**分类**: cs.SE, cs.AI, cs.LG

**发布日期**: 2025-12-23

**🔗 代码/项目**: [GITHUB](https://github.com/deviserlab/FeatureSHAP)

---

## 💡 一句话要点

**提出FeatureSHAP，用于解释软件工程任务中的大型语言模型**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `可解释AI` `大型语言模型` `软件工程` `Shapley值` `代码生成` `代码摘要` `模型解释` `特征重要性`

## 📋 核心要点

1. 现有LLM在软件工程任务中表现出色，但其黑盒特性限制了在高风险领域的应用，缺乏领域特定的解释。
2. FeatureSHAP基于Shapley值，通过输入扰动和任务相似性比较，将模型输出归因于高级输入特征。
3. 实验表明，FeatureSHAP能有效区分相关和不相关特征，提供高保真解释，并帮助从业者做出更明智的决策。

## 📝 摘要（中文）

大型语言模型（LLMs）在软件工程（SE）任务自动化方面取得了显著进展，例如代码生成和代码摘要。然而，LLMs的黑盒特性严重阻碍了其在高风险和安全关键领域的应用，在这些领域，可解释性和透明度对于信任、责任和有效的人工监督至关重要。尽管人们对软件工程领域的可解释AI越来越感兴趣，但现有方法缺乏与从业者对SE工件的推理方式相一致的领域特定解释。为了解决这一差距，我们引入了FeatureSHAP，这是第一个完全自动化、模型无关的可解释性框架，专为软件工程任务量身定制。FeatureSHAP基于Shapley值，通过系统的输入扰动和任务特定的相似性比较，将模型输出归因于高级输入特征，同时与开源和专有LLMs兼容。我们在两个双模态SE任务（代码生成和代码摘要）上评估了FeatureSHAP。结果表明，FeatureSHAP对不相关的输入特征赋予较低的重要性，并产生比基线方法更高保真度的解释。一项涉及37名参与者的从业者调查表明，FeatureSHAP有助于从业者更好地解释模型输出并做出更明智的决策。总而言之，FeatureSHAP代表了在软件工程中实现实用可解释AI的有意义的一步。FeatureSHAP可在https://github.com/deviserlab/FeatureSHAP上获得。

## 🔬 方法详解

**问题定义**：论文旨在解决大型语言模型（LLMs）在软件工程（SE）任务中应用时缺乏可解释性的问题。现有方法无法提供领域特定的解释，难以让从业者理解模型决策过程，阻碍了LLMs在安全关键领域的应用。现有方法无法有效区分输入特征的重要性，导致解释结果不准确。

**核心思路**：论文的核心思路是利用Shapley值来量化每个输入特征对模型输出的贡献。通过系统地扰动输入并比较不同扰动下的模型输出，可以估计每个特征的重要性。 这种方法是模型无关的，可以应用于各种LLMs，无需修改模型结构或训练过程。 结合任务特定的相似性比较，能够更好地对软件工程领域的工件进行解释。

**技术框架**：FeatureSHAP框架包含以下主要阶段：1) 输入特征提取：将输入数据分解为高级特征。2) 输入扰动：系统地扰动输入特征，生成多个扰动后的输入样本。3) 模型预测：使用LLM对原始输入和扰动后的输入进行预测。4) Shapley值计算：基于Shapley值理论，计算每个特征对模型输出的贡献。5) 解释生成：根据Shapley值，生成对模型决策的解释。

**关键创新**：FeatureSHAP的关键创新在于其完全自动化和模型无关的特性，以及针对软件工程任务的定制化设计。它能够自动提取输入特征，并使用Shapley值来量化特征的重要性，无需人工干预。与现有方法相比，FeatureSHAP能够提供更准确、更易于理解的解释，并与开源和专有LLMs兼容。

**关键设计**：FeatureSHAP的关键设计包括：1) 任务特定的相似性度量：用于比较不同扰动后的输入样本，以更准确地估计特征的重要性。2) 高级特征提取：将输入数据分解为更易于理解的高级特征，例如代码中的函数名、变量名等。3) Shapley值计算的优化：采用高效的算法来计算Shapley值，以降低计算复杂度。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.20328v1/x1.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.20328v1/x2.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.20328v1/x3.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

实验结果表明，FeatureSHAP在代码生成和代码摘要任务中均优于基线方法。FeatureSHAP能够更准确地识别重要的输入特征，并生成更高保真度的解释。从业者调查表明，FeatureSHAP能够帮助开发人员更好地理解模型输出，并做出更明智的决策。例如，在代码生成任务中，FeatureSHAP能够突出显示与生成代码相关的关键代码片段。

## 🎯 应用场景

FeatureSHAP可应用于各种软件工程任务，例如代码生成、代码摘要、代码缺陷预测等。它可以帮助开发人员理解LLMs的决策过程，提高对模型输出的信任度，并进行有效的错误诊断和修复。该研究对于推动LLMs在安全关键领域的应用具有重要意义，例如航空航天、医疗保健等。

## 📄 摘要（原文）

> Recent progress in Large Language Models (LLMs) has substantially advanced the automation of software engineering (SE) tasks, enabling complex activities such as code generation and code summarization. However, the black-box nature of LLMs remains a major barrier to their adoption in high-stakes and safety-critical domains, where explainability and transparency are vital for trust, accountability, and effective human supervision. Despite increasing interest in explainable AI for software engineering, existing methods lack domain-specific explanations aligned with how practitioners reason about SE artifacts. To address this gap, we introduce FeatureSHAP, the first fully automated, model-agnostic explainability framework tailored to software engineering tasks. Based on Shapley values, FeatureSHAP attributes model outputs to high-level input features through systematic input perturbation and task-specific similarity comparisons, while remaining compatible with both open-source and proprietary LLMs. We evaluate FeatureSHAP on two bi-modal SE tasks: code generation and code summarization. The results show that FeatureSHAP assigns less importance to irrelevant input features and produces explanations with higher fidelity than baseline methods. A practitioner survey involving 37 participants shows that FeatureSHAP helps practitioners better interpret model outputs and make more informed decisions. Collectively, FeatureSHAP represents a meaningful step toward practical explainable AI in software engineering. FeatureSHAP is available at https://github.com/deviserlab/FeatureSHAP.

