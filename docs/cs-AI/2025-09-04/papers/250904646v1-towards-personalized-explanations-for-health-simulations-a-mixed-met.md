---
layout: default
title: "Towards Personalized Explanations for Health Simulations: A Mixed-Methods Framework for Stakeholder-Centric Summarization"
---

# Towards Personalized Explanations for Health Simulations: A Mixed-Methods Framework for Stakeholder-Centric Summarization

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.04646" class="toolbar-btn" target="_blank">📄 arXiv: 2509.04646v1</a>
  <a href="https://arxiv.org/pdf/2509.04646.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.04646v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.04646v1', 'Towards Personalized Explanations for Health Simulations: A Mixed-Methods Framework for Stakeholder-Centric Summarization')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Philippe J. Giabbanelli, Ameeta Agrawal

**分类**: cs.AI, cs.ET

**发布日期**: 2025-09-04

**备注**: Accepted at the AAAI 2025 Fall Symposium Series. November 6-8, 2025, Arlington, VA, USA

---

## 💡 一句话要点

**提出一种混合方法框架，利用LLM为健康模拟提供个性化解释，满足不同利益相关者的需求。**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `健康模拟` `个性化解释` `大型语言模型` `利益相关者` `混合方法` `可解释性` `决策支持`

## 📋 核心要点

1. 现有健康模拟解释方法缺乏对不同利益相关者个性化需求的考虑，导致模型难以被有效利用。
2. 该论文提出一个混合方法框架，通过识别利益相关者的需求，指导LLM生成定制化的健康模拟解释。
3. 该框架通过引出需求、优化LLM生成和综合评估等步骤，提升LLM生成个性化摘要的能力。

## 📝 摘要（中文）

建模与模拟（M&S）方法，如基于Agent的模型，在支持健康决策方面具有巨大潜力，例如疫苗接种、健康饮食和身体活动行为。这些模型对不同的利益相关者群体具有潜在的可用性，可以帮助政策制定者评估潜在干预措施的后果，并指导个人在复杂环境中做出健康选择。然而，由于模型的复杂性，使得最能从中受益的利益相关者难以理解，这一潜力可能无法充分实现。虽然大型语言模型（LLM）可以将模拟输出和模型设计转化为文本，但当前的方法通常依赖于一刀切的摘要，无法反映临床医生、政策制定者、患者、护理人员和健康倡导者的不同信息需求和风格偏好。为了解决这一差距，我们提出了一个逐步框架，以识别利益相关者的需求，并指导LLM生成针对健康模拟的定制解释。我们的程序采用混合方法设计，首先引出不同健康利益相关者的解释需求和风格偏好，然后优化LLM生成定制输出的能力（例如，通过可控属性调整），然后通过一系列综合指标进行评估，以进一步改进摘要的定制生成。

## 🔬 方法详解

**问题定义**：现有的大型语言模型在解释健康模拟结果时，通常采用“一刀切”的方式，无法满足不同利益相关者（如临床医生、政策制定者、患者等）在信息需求和风格偏好上的差异。这导致模型的解释性不足，阻碍了其在实际决策中的应用。现有方法缺乏对利益相关者需求的系统性理解，难以生成个性化的解释。

**核心思路**：该论文的核心思路是采用混合方法，首先通过调研和访谈等方式，深入了解不同利益相关者对健康模拟解释的需求和偏好。然后，利用这些信息指导大型语言模型生成定制化的解释，并通过一系列指标对生成的解释进行评估和优化。通过这种方式，可以确保生成的解释既准确又易于理解，从而更好地服务于不同的利益相关者。

**技术框架**：该框架包含三个主要阶段：1) 利益相关者需求 elicitation 阶段：通过问卷调查、访谈等方式，收集不同利益相关者对健康模拟解释的需求和偏好，包括所需信息的类型、解释的风格、以及对模型透明度的要求。2) LLM 定制优化阶段：利用收集到的利益相关者需求信息，对大型语言模型进行微调或提示工程，使其能够生成符合特定利益相关者需求的解释。例如，可以通过可控属性调整来控制解释的风格和详细程度。3) 评估与改进阶段：使用一系列指标（如准确性、可理解性、满意度等）对生成的解释进行评估，并根据评估结果对LLM进行进一步的优化，以提高解释的质量和个性化程度。

**关键创新**：该论文的关键创新在于提出了一个系统化的混合方法框架，将利益相关者的需求纳入到健康模拟解释的过程中。与以往的“一刀切”方法相比，该框架能够生成更加个性化、易于理解的解释，从而更好地服务于不同的利益相关者。此外，该框架还提供了一套完整的评估指标，用于衡量解释的质量和个性化程度。

**关键设计**：在利益相关者需求 elicitation 阶段，需要设计合理的问卷调查和访谈方案，以确保能够全面地收集到不同利益相关者的需求信息。在LLM定制优化阶段，需要选择合适的微调或提示工程方法，并根据利益相关者的需求调整模型的参数。在评估与改进阶段，需要选择合适的评估指标，并根据评估结果对LLM进行迭代优化。具体的技术细节取决于所使用的LLM和健康模拟模型。

## 📊 实验亮点

论文重点在于框架的提出和设计，目前没有提供具体的实验数据。未来的工作将集中在利用该框架进行实际的健康模拟解释，并评估其在提高利益相关者理解和决策能力方面的效果。通过对比不同LLM和定制策略，可以进一步优化框架的性能。

## 🎯 应用场景

该研究成果可应用于各种健康决策支持系统，例如疫苗接种推广、健康饮食指导、慢性病管理等。通过为不同人群提供个性化的健康模拟解释，可以提高他们对健康风险的认知，从而做出更明智的健康决策。该研究还有助于提高健康模型的透明度和可信度，促进其在临床实践和政策制定中的应用。

## 📄 摘要（原文）

> Modeling & Simulation (M&S) approaches such as agent-based models hold significant potential to support decision-making activities in health, with recent examples including the adoption of vaccines, and a vast literature on healthy eating behaviors and physical activity behaviors. These models are potentially usable by different stakeholder groups, as they support policy-makers to estimate the consequences of potential interventions and they can guide individuals in making healthy choices in complex environments. However, this potential may not be fully realized because of the models' complexity, which makes them inaccessible to the stakeholders who could benefit the most. While Large Language Models (LLMs) can translate simulation outputs and the design of models into text, current approaches typically rely on one-size-fits-all summaries that fail to reflect the varied informational needs and stylistic preferences of clinicians, policymakers, patients, caregivers, and health advocates. This limitation stems from a fundamental gap: we lack a systematic understanding of what these stakeholders need from explanations and how to tailor them accordingly. To address this gap, we present a step-by-step framework to identify stakeholder needs and guide LLMs in generating tailored explanations of health simulations. Our procedure uses a mixed-methods design by first eliciting the explanation needs and stylistic preferences of diverse health stakeholders, then optimizing the ability of LLMs to generate tailored outputs (e.g., via controllable attribute tuning), and then evaluating through a comprehensive range of metrics to further improve the tailored generation of summaries.

