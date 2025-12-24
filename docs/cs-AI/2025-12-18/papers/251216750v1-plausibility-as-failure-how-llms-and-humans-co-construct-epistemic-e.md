---
layout: default
title: "Plausibility as Failure: How LLMs and Humans Co-Construct Epistemic Error"
---

# Plausibility as Failure: How LLMs and Humans Co-Construct Epistemic Error

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.16750" class="toolbar-btn" target="_blank">📄 arXiv: 2512.16750v1</a>
  <a href="https://arxiv.org/pdf/2512.16750.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.16750v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.16750v1', 'Plausibility as Failure: How LLMs and Humans Co-Construct Epistemic Error')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Claudia Vale Oliveira, Nelson Zagalo, Filipe Silva, Anabela Brandao, Syeda Faryal Hussain Khurrum, Joaquim Santos

**分类**: cs.HC, cs.AI

**发布日期**: 2025-12-18

**备注**: 19 pages, 2 tables, 77 references, 6 appendices

---

## 💡 一句话要点

**揭示LLM与人类交互中认知错误的共建机制，强调评估的解释性视角**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `人机交互` `认知错误` `可信度` `评估框架` `解释性判断` `认知漂移` `验证负担`

## 📋 核心要点

1. 现有LLM错误分析侧重预测指标，忽略了其对人类判断的解释性影响，导致对人机交互中认知错误的理解不足。
2. 该研究将LLM错误视为人机交互中共同构建的认知失败，强调模型生成的可信度与人类解释性判断之间的关系。
3. 通过多轮评估，揭示了LLM错误从预测性向解释性转变，以及人类评估中出现的验证负担和认知漂移现象。

## 📝 摘要（中文）

大型语言模型（LLM）日益成为日常推理中的认知伙伴，但对其错误的分析主要集中在预测指标上，而非其对人类判断的解释性影响。本研究考察了在人机交互中，不同形式的认知失败如何产生、被掩盖和被容忍。这里的失败被理解为一种关系破裂，由模型生成的可信度和人类的解释性判断共同塑造。我们进行了三轮多LLM评估，采用跨学科任务和逐步区分的评估框架，观察评估者如何从语言、认知和可信度维度解释模型响应。研究发现，LLM的错误从预测性转向解释性，语言流畅性、结构连贯性和表面上可信的引用掩盖了更深层次的意义扭曲。评估者经常混淆正确性、相关性、偏差、依据和一致性等标准，表明人类判断将分析区分简化为受形式和流畅性影响的直觉启发式。在各轮评估中，我们观察到系统的验证负担和认知漂移。随着任务变得更加密集，评估者越来越依赖表面线索，允许错误但形式良好的答案被认为是可信的。这些结果表明，错误不仅仅是模型行为的属性，而是生成的可信度和人类解释性捷径共同构建的结果。因此，理解AI的认知失败需要将评估重新定义为一个关系解释过程，其中系统失败和人类校准错误之间的界限变得模糊。该研究为LLM评估、数字素养和可信赖的人机通信设计提供了启示。

## 🔬 方法详解

**问题定义**：现有的大型语言模型（LLM）的错误评估主要集中在预测准确率等指标上，忽略了LLM的输出如何影响人类的判断和认知。这种评估方式无法充分理解人机交互中认知错误的产生机制，尤其是在LLM输出具有表面可信度的情况下，人类可能会受到误导。现有方法缺乏对人类如何解释和容忍LLM错误的深入研究。

**核心思路**：本研究的核心思路是将LLM的错误视为一种“共建”的现象，即错误并非仅仅是模型自身的属性，而是模型生成的内容与人类的解释性判断相互作用的结果。研究强调了“可信度”（plausibility）在这一过程中的作用，认为LLM生成的表面上合理的内容可能会掩盖深层次的错误，从而影响人类的判断。

**技术框架**：研究采用了一种三轮多LLM评估框架，涉及跨学科任务。每一轮评估都使用不同的评估框架，这些框架在语言、认知和可信度维度上逐步区分。评估者需要对LLM的响应进行评估，研究人员观察评估者如何解释这些响应，以及在不同任务密度下，评估者的判断标准如何变化。

**关键创新**：该研究最重要的创新在于其对LLM错误评估的视角转变。它不再将错误视为模型自身的孤立问题，而是将其视为人机交互中共同构建的认知失败。这种视角强调了人类的解释性判断在错误产生过程中的作用，并揭示了LLM生成的可信度如何影响人类的判断。

**关键设计**：研究的关键设计包括：1) 多轮评估，以便观察评估者判断标准随任务密度变化的趋势；2) 跨学科任务，以考察LLM在不同领域的表现；3) 逐步区分的评估框架，以更细致地分析LLM的错误类型和人类的判断标准。研究还关注了评估者在评估过程中出现的“验证负担”和“认知漂移”现象，即随着任务变得更加密集，评估者越来越依赖表面线索，从而更容易接受错误的答案。

## 📊 实验亮点

研究发现，LLM错误会从预测性错误转变为解释性错误，即表面流畅和连贯的回答可能掩盖深层含义的扭曲。评估者在任务密度增加时，会更多依赖表面线索，导致错误答案被接受。这些结果强调了评估LLM时，需要关注人类的解释性判断，而不仅仅是模型的预测准确率。

## 🎯 应用场景

该研究成果可应用于LLM评估体系的改进，提升数字素养教育，并指导更值得信赖的人机交互系统设计。通过理解LLM错误的共建机制，可以开发更有效的评估方法，帮助用户识别和避免LLM带来的认知偏差，从而促进负责任的AI应用。

## 📄 摘要（原文）

> Large language models (LLMs) are increasingly used as epistemic partners in everyday reasoning, yet their errors remain predominantly analyzed through predictive metrics rather than through their interpretive effects on human judgment. This study examines how different forms of epistemic failure emerge, are masked, and are tolerated in human AI interaction, where failure is understood as a relational breakdown shaped by model-generated plausibility and human interpretive judgment. We conducted a three round, multi LLM evaluation using interdisciplinary tasks and progressively differentiated assessment frameworks to observe how evaluators interpret model responses across linguistic, epistemic, and credibility dimensions. Our findings show that LLM errors shift from predictive to hermeneutic forms, where linguistic fluency, structural coherence, and superficially plausible citations conceal deeper distortions of meaning. Evaluators frequently conflated criteria such as correctness, relevance, bias, groundedness, and consistency, indicating that human judgment collapses analytical distinctions into intuitive heuristics shaped by form and fluency. Across rounds, we observed a systematic verification burden and cognitive drift. As tasks became denser, evaluators increasingly relied on surface cues, allowing erroneous yet well formed answers to pass as credible. These results suggest that error is not solely a property of model behavior but a co-constructed outcome of generative plausibility and human interpretive shortcuts. Understanding AI epistemic failure therefore requires reframing evaluation as a relational interpretive process, where the boundary between system failure and human miscalibration becomes porous. The study provides implications for LLM assessment, digital literacy, and the design of trustworthy human AI communication.

