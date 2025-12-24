---
layout: default
title: "SafeEvalAgent: Toward Agentic and Self-Evolving Safety Evaluation of LLMs"
---

# SafeEvalAgent: Toward Agentic and Self-Evolving Safety Evaluation of LLMs

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.26100" class="toolbar-btn" target="_blank">📄 arXiv: 2509.26100v1</a>
  <a href="https://arxiv.org/pdf/2509.26100.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.26100v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.26100v1', 'SafeEvalAgent: Toward Agentic and Self-Evolving Safety Evaluation of LLMs')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yixu Wang, Xin Wang, Yang Yao, Xinyuan Li, Yan Teng, Xingjun Ma, Yingchun Wang

**分类**: cs.AI

**发布日期**: 2025-09-30

---

## 💡 一句话要点

**提出SafeEvalAgent，实现LLM安全评估的自主进化与动态基准生成**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `安全评估` `动态基准` `多智能体系统` `自我进化` `AI安全` `合规性` `Agentic评估`

## 📋 核心要点

1. 现有静态安全基准难以应对LLM安全风险的动态变化和法规演进，无法有效评估LLM的真实安全水平。
2. SafeEvalAgent将安全评估重构为持续自我进化的过程，利用多智能体协同生成并优化安全基准。
3. 实验表明，SafeEvalAgent能有效降低LLM的安全率，揭示静态评估遗漏的深层漏洞，验证了动态评估的必要性。

## 📝 摘要（中文）

大型语言模型（LLMs）正迅速融入高风险领域，这需要可靠的安全性和合规性评估。然而，现有的静态基准不足以应对AI风险的动态性和不断变化的法规，造成了严重的安全漏洞。本文提出了一种新的agentic安全评估范式，将评估重新定义为一个持续和自我进化的过程，而非一次性审计。我们提出了一个新颖的多智能体框架SafeEvalAgent，它可以自主地摄取非结构化的策略文档，以生成并永久进化一个全面的安全基准。SafeEvalAgent利用专门智能体的协同管道，并结合了自我进化的评估循环，系统从评估结果中学习，从而制定出越来越复杂和有针对性的测试用例。实验表明SafeEvalAgent的有效性，随着评估的加强，模型安全性持续下降。例如，GPT-5在欧盟AI法案上的安全率在连续迭代中从72.50%降至36.36%。这些发现揭示了静态评估的局限性，并强调了我们的框架发现传统方法遗漏的深层漏洞的能力，突显了对动态评估生态系统的迫切需求，以确保高级AI的安全和负责任的部署。

## 🔬 方法详解

**问题定义**：论文旨在解决大型语言模型（LLMs）安全评估中，现有静态基准无法有效应对AI风险动态变化和法规演进的问题。现有方法的痛点在于无法持续更新测试用例，难以发现LLMs潜在的安全漏洞，导致高风险领域应用存在安全隐患。

**核心思路**：论文的核心思路是将安全评估过程转变为一个持续自我进化的过程。通过构建一个多智能体系统，该系统能够自主学习并生成更具挑战性的测试用例，从而不断提高评估的严格性和准确性。这种动态评估方法能够更好地适应LLMs的快速发展和不断变化的安全风险。

**技术框架**：SafeEvalAgent框架包含以下主要模块：1) **策略文档摄取模块**：负责从非结构化的策略文档中提取相关信息。2) **测试用例生成模块**：利用提取的信息生成初始测试用例。3) **评估执行模块**：执行生成的测试用例，并记录LLM的响应。4) **自我进化模块**：分析评估结果，识别LLM的弱点，并生成更具针对性的测试用例。整个流程形成一个闭环，不断迭代优化测试用例，提高评估的有效性。

**关键创新**：最重要的技术创新点在于将安全评估从静态的一次性过程转变为动态的、自我进化的过程。与传统的静态基准相比，SafeEvalAgent能够自主学习并生成更具挑战性的测试用例，从而更全面地评估LLMs的安全风险。这种动态评估方法能够更好地适应LLMs的快速发展和不断变化的安全风险。

**关键设计**：SafeEvalAgent的关键设计包括：1) 使用专门的智能体来执行不同的任务，例如策略文档解析、测试用例生成和评估结果分析。2) 设计自我进化循环，使系统能够从评估结果中学习，并生成更具针对性的测试用例。3) 采用合适的评估指标来衡量LLM的安全水平，例如安全率和漏洞发现率。具体参数设置和网络结构等技术细节在论文中未详细描述，属于未知信息。

## 📊 实验亮点

实验结果表明，SafeEvalAgent能够有效降低LLM的安全率。例如，GPT-5在欧盟AI法案上的安全率在连续迭代中从72.50%降至36.36%。这表明SafeEvalAgent能够发现传统静态评估方法遗漏的深层漏洞，验证了动态评估的有效性。实验结果还表明，随着评估的加强，SafeEvalAgent能够生成更具挑战性的测试用例，从而更全面地评估LLM的安全风险。

## 🎯 应用场景

SafeEvalAgent可应用于金融、医疗、法律等高风险领域，帮助开发者和监管机构更全面地评估LLM的安全性和合规性。通过持续的动态评估，可以及时发现和修复LLM的潜在安全漏洞，降低AI应用的安全风险，促进AI技术的安全可靠发展。未来，该框架可扩展到其他类型的AI系统，并与其他安全评估工具集成，构建更完善的AI安全生态系统。

## 📄 摘要（原文）

> The rapid integration of Large Language Models (LLMs) into high-stakes domains necessitates reliable safety and compliance evaluation. However, existing static benchmarks are ill-equipped to address the dynamic nature of AI risks and evolving regulations, creating a critical safety gap. This paper introduces a new paradigm of agentic safety evaluation, reframing evaluation as a continuous and self-evolving process rather than a one-time audit. We then propose a novel multi-agent framework SafeEvalAgent, which autonomously ingests unstructured policy documents to generate and perpetually evolve a comprehensive safety benchmark. SafeEvalAgent leverages a synergistic pipeline of specialized agents and incorporates a Self-evolving Evaluation loop, where the system learns from evaluation results to craft progressively more sophisticated and targeted test cases. Our experiments demonstrate the effectiveness of SafeEvalAgent, showing a consistent decline in model safety as the evaluation hardens. For instance, GPT-5's safety rate on the EU AI Act drops from 72.50% to 36.36% over successive iterations. These findings reveal the limitations of static assessments and highlight our framework's ability to uncover deep vulnerabilities missed by traditional methods, underscoring the urgent need for dynamic evaluation ecosystems to ensure the safe and responsible deployment of advanced AI.

