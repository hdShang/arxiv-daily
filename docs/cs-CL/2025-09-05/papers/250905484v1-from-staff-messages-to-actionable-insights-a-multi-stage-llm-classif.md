---
layout: default
title: "From Staff Messages to Actionable Insights: A Multi-Stage LLM Classification Framework for Healthcare Analytics"
---

# From Staff Messages to Actionable Insights: A Multi-Stage LLM Classification Framework for Healthcare Analytics

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.05484" class="toolbar-btn" target="_blank">📄 arXiv: 2509.05484v1</a>
  <a href="https://arxiv.org/pdf/2509.05484.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.05484v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.05484v1', 'From Staff Messages to Actionable Insights: A Multi-Stage LLM Classification Framework for Healthcare Analytics')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Hajar Sakai, Yi-En Tseng, Mohammadsadegh Mikaeili, Joshua Bosire, Franziska Jovin

**分类**: cs.CL

**发布日期**: 2025-09-05

---

## 💡 一句话要点

**提出多阶段LLM分类框架，从医院员工消息中提取可执行的医疗分析洞见。**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `医疗分析` `文本分类` `多阶段框架` `医院呼叫中心`

## 📋 核心要点

1. 医院呼叫中心产生大量未被充分利用的员工消息，传统方法依赖标注数据和模型调优，效率低下。
2. 提出多阶段LLM框架，利用推理、通用和轻量级模型，识别消息主题并分类原因，提取洞见。
3. 实验表明，最佳模型o3达到78.4%的加权F1分数和79.2%的准确率，优于其他模型，具有实际应用价值。

## 📝 摘要（中文）

医院呼叫中心是患者与医院系统联系的主要入口，同时也产生了大量的员工消息。这些消息记录了导航员处理患者请求并与医院办公室沟通的过程。积累的大量文本数据可以被挖掘和处理以获取洞见。然而，传统的监督学习方法需要标注数据、大量的训练和模型调优。大型语言模型（LLMs）为医疗分析提供了一种更具计算效率的方法。本文提出了一种基于多阶段LLM的框架，该框架识别员工消息的主题，并以多类方式对消息的原因进行分类。在此过程中，评估了多种LLM类型，包括推理模型、通用模型和轻量级模型。性能最佳的模型是o3，实现了78.4%的加权F1分数和79.2%的准确率，其次是gpt-5（75.3%的加权F1分数和76.2%的准确率）。该方法结合了数据安全措施和HIPAA合规性要求，这对于医疗环境至关重要。处理后的LLM输出被集成到一个可视化决策支持工具中，该工具将员工消息转化为可供医疗专业人员访问的可执行洞见。这种方法能够更有效地利用收集到的员工消息数据，识别导航员培训机会，并支持改善患者体验和护理质量。

## 🔬 方法详解

**问题定义**：论文旨在解决医院呼叫中心员工消息数据利用率低的问题。现有方法，如传统的监督学习，需要大量标注数据和模型调优，成本高昂且效率低下。此外，医疗数据的隐私性和安全性要求也增加了数据处理的难度。

**核心思路**：论文的核心思路是利用大型语言模型（LLMs）的强大文本理解和生成能力，构建一个多阶段的分类框架，自动识别员工消息的主题和原因，从而将原始消息转化为可执行的洞见。这种方法旨在减少对人工标注数据的依赖，提高数据处理效率，并确保数据安全和合规性。

**技术框架**：该框架包含多个阶段，具体流程未知。整体架构利用不同类型的LLM，包括推理模型、通用模型和轻量级模型，以适应不同的任务需求。框架还集成了数据安全措施和HIPAA合规性要求，以确保医疗数据的安全性和合规性。最终，处理后的LLM输出被集成到一个可视化决策支持工具中，方便医疗专业人员访问和使用。

**关键创新**：该论文的关键创新在于提出了一个多阶段的LLM分类框架，用于从医院员工消息中提取可执行的洞见。该框架结合了不同类型的LLM，并集成了数据安全措施和HIPAA合规性要求，使其能够安全有效地处理医疗数据。与传统的监督学习方法相比，该框架减少了对人工标注数据的依赖，提高了数据处理效率。

**关键设计**：论文中没有详细描述关键的参数设置、损失函数、网络结构等技术细节。具体LLM的选择和配置，以及多阶段框架的各个阶段的具体任务和实现方式，有待进一步研究。

## 📊 实验亮点

实验结果表明，提出的多阶段LLM框架能够有效地识别员工消息的主题和原因。其中，模型o3表现最佳，达到了78.4%的加权F1分数和79.2%的准确率，优于其他模型，包括gpt-5（75.3%的加权F1分数和76.2%的准确率）。这些结果表明，该框架具有实际应用价值。

## 🎯 应用场景

该研究成果可应用于医院管理、患者服务改进和医疗质量提升等领域。通过分析员工消息，医院可以更好地了解患者需求，优化服务流程，识别培训需求，并最终改善患者体验和护理质量。该方法还可推广到其他医疗机构，提高医疗数据的利用率和决策效率。

## 📄 摘要（原文）

> Hospital call centers serve as the primary contact point for patients within a hospital system. They also generate substantial volumes of staff messages as navigators process patient requests and communicate with the hospital offices following the established protocol restrictions and guidelines. This continuously accumulated large amount of text data can be mined and processed to retrieve insights; however, traditional supervised learning approaches require annotated data, extensive training, and model tuning. Large Language Models (LLMs) offer a paradigm shift toward more computationally efficient methodologies for healthcare analytics. This paper presents a multi-stage LLM-based framework that identifies staff message topics and classifies messages by their reasons in a multi-class fashion. In the process, multiple LLM types, including reasoning, general-purpose, and lightweight models, were evaluated. The best-performing model was o3, achieving 78.4% weighted F1-score and 79.2% accuracy, followed closely by gpt-5 (75.3% Weighted F1-score and 76.2% accuracy). The proposed methodology incorporates data security measures and HIPAA compliance requirements essential for healthcare environments. The processed LLM outputs are integrated into a visualization decision support tool that transforms the staff messages into actionable insights accessible to healthcare professionals. This approach enables more efficient utilization of the collected staff messaging data, identifies navigator training opportunities, and supports improved patient experience and care quality.

