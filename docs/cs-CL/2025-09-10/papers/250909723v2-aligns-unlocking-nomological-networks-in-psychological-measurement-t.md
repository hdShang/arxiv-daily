---
layout: default
title: "ALIGNS: Unlocking nomological networks in psychological measurement through a large language model"
---

# ALIGNS: Unlocking nomological networks in psychological measurement through a large language model

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.09723" class="toolbar-btn" target="_blank">📄 arXiv: 2509.09723v2</a>
  <a href="https://arxiv.org/pdf/2509.09723.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.09723v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.09723v2', 'ALIGNS: Unlocking nomological networks in psychological measurement through a large language model')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Kai R. Larsen, Sen Yan, Roland M. Mueller, Lan Sang, Mikko Rönkkö, Ravi Starzl, Donald Edmondson

**分类**: cs.CL, cs.AI, cs.LG, stat.ME

**发布日期**: 2025-09-10 (更新: 2025-09-18)

---

## 💡 一句话要点

**ALIGNS：利用大型语言模型解锁心理测量学中的因果网络。**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `心理测量学` `因果网络` `大型语言模型` `测量验证` `自然语言处理`

## 📋 核心要点

1. 心理测量学中，构建概念与测量间关系的因果网络以验证效度仍面临挑战。
2. ALIGNS利用大型语言模型，通过已验证的问卷测量训练，生成大规模因果网络。
3. 实验验证了ALIGNS的有效性，并由专家评估了其重要性、可访问性和适用性。

## 📝 摘要（中文）

心理测量学对许多学科至关重要。尽管测量技术不断进步，但构建因果网络（概念和测量之间关系的理论图，用于建立效度）仍然是一个挑战。我们介绍了“利用潜在指标生成因果结构分析”（ALIGNS），这是一个基于大型语言模型的系统，使用经过验证的问卷测量进行训练。ALIGNS提供了三个全面的因果网络，包含心理学、医学、社会政策和其他领域的超过55万个指标。这是大型语言模型首次应用于解决测量验证中的一个基础问题。我们报告了用于开发模型的分类准确性测试，以及三个评估。第一个评估表明，广泛使用的NIH PROMIS焦虑和抑郁工具会聚成一个单一的情绪困扰维度。第二个评估检查了儿童气质测量，并确定了当前框架未捕获的四个潜在维度，并质疑了一个现有维度。第三个评估是一个适用性检查，专家心理测量学家评估了该系统的重要性、可访问性和适用性。ALIGNS可在nomologicalnetwork.org免费获得，通过大规模的因果分析来补充传统的验证方法。

## 🔬 方法详解

**问题定义**：心理测量学中，验证测量工具的效度是一个长期存在的难题。传统的验证方法依赖于小规模研究和专家判断，难以处理大规模、复杂的数据关系。构建因果网络，即概念和测量之间关系的理论图，是验证效度的关键，但现有方法效率低、成本高，难以全面覆盖各个领域。

**核心思路**：ALIGNS的核心思路是利用大型语言模型（LLM）的强大语义理解和知识推理能力，自动构建和分析大规模的因果网络。通过训练LLM理解已验证的问卷测量，使其能够预测不同概念和测量之间的关系，从而生成全面的因果网络。

**技术框架**：ALIGNS的整体框架包括以下几个主要阶段：1) 数据收集：收集来自心理学、医学、社会政策等领域的已验证问卷测量数据。2) 模型训练：使用收集到的数据训练大型语言模型，使其能够理解概念和测量之间的语义关系。3) 因果网络生成：利用训练好的LLM，预测不同概念和测量之间的关系，构建大规模的因果网络。4) 评估验证：通过分类准确性测试、专家评估等方法，验证生成的因果网络的有效性和可靠性。

**关键创新**：ALIGNS的关键创新在于将大型语言模型应用于解决心理测量学中的基础问题，即构建因果网络。与传统的基于小规模研究和专家判断的方法相比，ALIGNS能够处理大规模、复杂的数据关系，自动生成全面的因果网络，大大提高了效率和覆盖范围。

**关键设计**：ALIGNS的关键设计包括：1) 选择合适的LLM架构，例如Transformer模型，以捕捉概念和测量之间的复杂语义关系。2) 设计合适的训练目标，例如预测测量工具的维度和指标，以提高模型的预测准确性。3) 采用合适的评估指标，例如分类准确性、专家评估等，以验证生成的因果网络的有效性和可靠性。

## 📊 实验亮点

实验结果表明，ALIGNS能够准确地识别NIH PROMIS焦虑和抑郁工具的情绪困扰维度，并发现了儿童气质测量中当前框架未捕获的四个潜在维度。专家评估表明，ALIGNS具有重要性、可访问性和适用性，能够有效补充传统的验证方法。

## 🎯 应用场景

ALIGNS可应用于心理学、医学、社会政策等领域，辅助研究人员进行测量工具的验证和改进，提高临床试验的有效性，并为公共政策制定提供更准确的依据。该系统能够加速因果网络的构建过程，降低验证成本，并促进跨学科的知识共享。

## 📄 摘要（原文）

> Psychological measurement is critical to many disciplines. Despite advances in measurement, building nomological networks, theoretical maps of how concepts and measures relate to establish validity, remains a challenge 70 years after Cronbach and Meehl proposed them as fundamental to validation. This limitation has practical consequences: clinical trials may fail to detect treatment effects, and public policy may target the wrong outcomes. We introduce Analysis of Latent Indicators to Generate Nomological Structures (ALIGNS), a large language model-based system trained with validated questionnaire measures. ALIGNS provides three comprehensive nomological networks containing over 550,000 indicators across psychology, medicine, social policy, and other fields. This represents the first application of large language models to solve a foundational problem in measurement validation. We report classification accuracy tests used to develop the model, as well as three evaluations. In the first evaluation, the widely used NIH PROMIS anxiety and depression instruments are shown to converge into a single dimension of emotional distress. The second evaluation examines child temperament measures and identifies four potential dimensions not captured by current frameworks, and questions one existing dimension. The third evaluation, an applicability check, engages expert psychometricians who assess the system's importance, accessibility, and suitability. ALIGNS is freely available at nomologicalnetwork.org, complementing traditional validation methods with large-scale nomological analysis.

