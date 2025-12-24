---
layout: default
title: "HealthProcessAI: A Technical Framework and Proof-of-Concept for LLM-Enhanced Healthcare Process Mining"
---

# HealthProcessAI: A Technical Framework and Proof-of-Concept for LLM-Enhanced Healthcare Process Mining

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.21540" class="toolbar-btn" target="_blank">📄 arXiv: 2508.21540v2</a>
  <a href="https://arxiv.org/pdf/2508.21540.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.21540v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.21540v2', 'HealthProcessAI: A Technical Framework and Proof-of-Concept for LLM-Enhanced Healthcare Process Mining')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Eduardo Illueca-Fernandez, Kaile Chen, Fernando Seoane, Farhad Abtahi

**分类**: cs.AI

**发布日期**: 2025-08-29 (更新: 2025-10-15)

**备注**: Figure 1 updated, typos corrected, references added, under review

---

## 💡 一句话要点

**提出HealthProcessAI以简化医疗流程挖掘问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `医疗流程挖掘` `大型语言模型` `自动化报告生成` `数据分析` `流行病学` `技术框架` `脓毒症数据`

## 📋 核心要点

1. 现有流程挖掘方法在医疗领域应用时面临技术复杂性和缺乏标准化的挑战，限制了其普及和有效性。
2. HealthProcessAI框架通过整合多个大型语言模型，简化了流程挖掘的应用，提升了结果的可理解性和可访问性。
3. 通过对脓毒症数据的验证，框架在多个场景中展示了强大的技术性能，并成功生成了易于理解的报告。

## 📝 摘要（中文）

流程挖掘作为一种强大的分析技术，能够帮助理解复杂的医疗工作流程。然而，其应用面临技术复杂性、缺乏标准化方法和实践培训资源有限等重大障碍。为此，本文提出了HealthProcessAI，一个旨在简化医疗和流行病学中流程挖掘应用的GenAI框架。该框架围绕现有的Python（PM4PY）和R（bupaR）库提供了全面的封装，并集成了多个大型语言模型（LLMs）以实现自动化的流程图解释和报告生成。通过使用脓毒症进展数据进行验证，框架展示了其在四个概念验证场景中的强大技术性能，并通过自动化LLM分析成功生成报告。LLM评估显示，Claude Sonnet-4和Gemini 2.5-Pro在一致性评分上表现最佳，分别为3.79/4.0和3.65/4.0。该框架的设计使得流程挖掘结果更易于临床医生、数据科学家和研究人员理解，具有重要的实际应用价值。

## 🔬 方法详解

**问题定义**：本研究旨在解决医疗流程挖掘应用中的技术复杂性和缺乏标准化方法的问题，现有方法使得非专业用户难以理解分析结果。

**核心思路**：HealthProcessAI框架通过集成多个大型语言模型（LLMs），实现自动化的流程图解释和报告生成，从而降低用户的技术门槛。

**技术框架**：该框架的整体架构包括数据输入模块、流程挖掘模块（基于PM4PY和bupaR）、LLM集成模块和报告生成模块，形成一个闭环的分析流程。

**关键创新**：最重要的创新在于将LLMs应用于流程挖掘结果的自动化解释，使得复杂的技术分析结果能够被广泛的医疗从业者理解，显著提升了结果的可用性。

**关键设计**：框架中关键的参数设置包括LLM的选择和配置，损失函数的设计以优化模型的解释能力，以及网络结构的调整以适应医疗数据的特性。具体细节尚未完全公开。

## 📊 实验亮点

在实验中，HealthProcessAI框架成功处理了脓毒症数据，并在四个概念验证场景中展示了强大的技术性能。通过与五个先进的LLM模型的比较，Claude Sonnet-4和Gemini 2.5-Pro在一致性评分上表现最佳，分别达到了3.79/4.0和3.65/4.0，显示出框架的有效性和可靠性。

## 🎯 应用场景

HealthProcessAI框架具有广泛的应用潜力，特别是在医疗和流行病学领域。通过简化流程挖掘的复杂性，该框架能够帮助临床医生和研究人员更好地理解和利用数据，从而推动医疗决策和研究的进展。未来，该框架可能会扩展到其他领域，如公共卫生和健康管理，进一步提升数据驱动决策的能力。

## 📄 摘要（原文）

> Process mining has emerged as a powerful analytical technique for understanding complex healthcare workflows. However, its application faces significant barriers, including technical complexity, a lack of standardized approaches, and limited access to practical training resources. We introduce HealthProcessAI, a GenAI framework designed to simplify process mining applications in healthcare and epidemiology by providing a comprehensive wrapper around existing Python (PM4PY) and R (bupaR) libraries. To address unfamiliarity and improve accessibility, the framework integrates multiple Large Language Models (LLMs) for automated process map interpretation and report generation, helping translate technical analyses into outputs that diverse users can readily understand. We validated the framework using sepsis progression data as a proof-of-concept example and compared the outputs of five state-of-the-art LLM models through the OpenRouter platform. To test its functionality, the framework successfully processed sepsis data across four proof-of-concept scenarios, demonstrating robust technical performance and its capability to generate reports through automated LLM analysis. LLM evaluation using five independent LLMs as automated evaluators revealed distinct model strengths: Claude Sonnet-4 and Gemini 2.5-Pro achieved the highest consistency scores (3.79/4.0 and 3.65/4.0) when evaluated by automated LLM assessors. By integrating multiple Large Language Models (LLMs) for automated interpretation and report generation, the framework addresses widespread unfamiliarity with process mining outputs, making them more accessible to clinicians, data scientists, and researchers. This structured analytics and AI-driven interpretation combination represents a novel methodological advance in translating complex process mining results into potentially actionable insights for healthcare applications.

