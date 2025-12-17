---
layout: default
title: Adjudicator: Correcting Noisy Labels with a KG-Informed Council of LLM Agents
---

# Adjudicator: Correcting Noisy Labels with a KG-Informed Council of LLM Agents

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.13704" class="toolbar-btn" target="_blank">📄 arXiv: 2512.13704</a>
  <a href="https://arxiv.org/pdf/2512.13704.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.13704" onclick="toggleFavorite(this, '2512.13704', 'Adjudicator: Correcting Noisy Labels with a KG-Informed Council of LLM Agents')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Doohee You, Sundeep Paul

**分类**: cs.AI

**发布日期**: 2025-12-18

---

## 💡 一句话要点

**Adjudicator：利用知识图谱增强的大语言模型智能体委员会纠正噪声标签**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `噪声标签纠正` `知识图谱` `大语言模型` `多智能体系统` `神经符号学习`

## 📋 核心要点

1. 生产环境中机器学习模型受噪声标签影响，降低性能和用户信任，现有方法难以有效识别和纠正。
2. Adjudicator构建动态知识图谱，并利用其指导多智能体大语言模型委员会进行标签有效性投票。
3. 实验表明，Adjudicator在AlleNoise数据集上F1分数达到0.99，显著优于单一大语言模型和非知识图谱委员会。

## 📝 摘要（中文）

生产机器学习系统的性能受到训练数据质量的根本限制。在高风险工业应用中，噪声标签会降低性能并削弱用户信任。本文提出了Adjudicator，一个解决自动识别和纠正标签噪声这一关键数据挖掘挑战的系统，并已验证可用于生产部署。Adjudicator将其建模为一个神经符号任务，首先构建一个动态知识图谱（KG）来统一项目上下文。然后，该知识图谱为“智能体委员会”提供信息，这是一个新颖的多智能体大语言模型架构，其中专门的智能体就标签的有效性进行辩论和投票。我们在AlleNoise基准测试的1000项平衡子集上验证了我们的系统。我们的知识图谱模型实现了0.99的F1分数，显著优于单个大语言模型基线（0.48 F1）和非知识图谱委员会（0.59 F1）。我们的分析表明，这归功于一种新颖的覆盖逻辑所实现的精确度，该逻辑使用知识图谱来完美地识别复杂的结构性错误（完全召回率）——基线无法找到的一类错误。这一结果展示了一个强大且可解释的自动化、高精度数据验证系统，为在严格管理的工业环境中生成黄金数据集提供了一个重要的概念验证。

## 🔬 方法详解

**问题定义**：论文旨在解决机器学习训练数据中噪声标签的问题，特别是在高风险工业应用中。现有方法在处理复杂、结构性噪声标签时表现不佳，导致模型性能下降和用户信任降低。这些噪声标签难以被传统方法识别和纠正，严重影响了模型的泛化能力和可靠性。

**核心思路**：论文的核心思路是利用知识图谱（KG）来增强大语言模型（LLM）在识别和纠正噪声标签方面的能力。通过构建一个动态的知识图谱，将项目上下文信息整合起来，为LLM提供更丰富的背景知识。然后，利用一个多智能体委员会，每个智能体都基于知识图谱的信息对标签的有效性进行辩论和投票。这种方法模拟了专家评审的过程，可以更准确地识别和纠正噪声标签。

**技术框架**：Adjudicator系统的整体架构包括以下几个主要模块：1) **知识图谱构建模块**：负责从各种数据源中提取实体和关系，构建动态的知识图谱。2) **智能体委员会模块**：包含多个专门的LLM智能体，每个智能体负责从不同的角度评估标签的有效性。3) **辩论和投票模块**：智能体之间进行辩论，分享各自的观点和证据，最终通过投票决定标签的有效性。4) **覆盖逻辑模块**：利用知识图谱的信息，对智能体委员会的投票结果进行修正，特别是针对复杂的结构性错误。

**关键创新**：该论文最重要的技术创新点在于将知识图谱与多智能体大语言模型委员会相结合，用于识别和纠正噪声标签。与传统的单一大语言模型或非知识图谱方法相比，Adjudicator能够更有效地利用上下文信息，识别和纠正复杂的结构性错误。此外，覆盖逻辑模块的设计也使得系统能够完美地识别这类错误，实现了完全召回率。

**关键设计**：知识图谱的构建方式，包括实体和关系的提取规则，以及知识图谱的更新策略。智能体委员会中每个智能体的角色和职责，以及智能体之间的辩论和投票机制。覆盖逻辑模块的具体实现方式，包括如何利用知识图谱的信息来识别和纠正结构性错误。论文中没有明确指出具体的参数设置、损失函数或网络结构等细节，这些可能是根据具体应用场景进行调整的。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.13704/x1.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.13704/x2.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.13704/graph_kgLLM.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

Adjudicator在AlleNoise数据集上取得了显著的性能提升，F1分数达到0.99，远超单一大语言模型基线（0.48 F1）和非知识图谱委员会（0.59 F1）。该系统能够完美识别复杂的结构性错误，实现完全召回率，这归功于其新颖的覆盖逻辑和知识图谱的有效利用。实验结果表明，Adjudicator是一个强大且可解释的自动化、高精度数据验证系统。

## 🎯 应用场景

Adjudicator可应用于各种需要高质量训练数据的工业场景，例如电商产品分类、金融风险评估、医疗诊断等。通过自动识别和纠正噪声标签，可以提高机器学习模型的性能和可靠性，降低运营成本，并增强用户信任。该系统为在严格管理的工业环境中生成黄金数据集提供了一个重要的概念验证，具有广阔的应用前景。

## 📄 摘要（原文）

> The performance of production machine learning systems is fundamentally limited by the quality of their training data. In high-stakes industrial applications, noisy labels can degrade performance and erode user trust. This paper presents Adjudicator, a system that addresses the critical data mining challenge of automatically identifying and correcting label noise and has been validated for production deployment. Adjudicator models this as a neuro-symbolic task, first constructing a dynamic Knowledge Graph (KG) to unify item context. This KG then informs a "Council of Agents," a novel multi-agent Large Language Model architecture where specialized agents debate and vote on a label's validity. We validate our system on a 1,000-item balanced subset of the AlleNoise benchmark. Our KG-informed model achieves a 0.99 F1-score, significantly outperforming a single-LLM baseline (0.48 F1) and a non-KG council (0.59 F1). Our analysis reveals this is due to a Precision, achieved by a novel override logic that uses the KG to perfectly identify complex, structural errors (complete Recall) -- a class of errors that baselines fail to find. This result demonstrates a robust and explainable system for automated, high-precision data verification, serving as a vital proof-of-concept for generating golden datasets in strictly governed industrial environments.

