---
layout: default
title: MESS+: Dynamically Learned Inference-Time LLM Routing in Model Zoos with Service Level Guarantees
---

# MESS+: Dynamically Learned Inference-Time LLM Routing in Model Zoos with Service Level Guarantees

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.19947" class="toolbar-btn" target="_blank">📄 arXiv: 2505.19947v3</a>
  <a href="https://arxiv.org/pdf/2505.19947.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.19947v3" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.19947v3', 'MESS+: Dynamically Learned Inference-Time LLM Routing in Model Zoos with Service Level Guarantees')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Herbert Woisetschläger, Ryan Zhang, Shiqiang Wang, Hans-Arno Jacobsen

**分类**: cs.LG, cs.AI, eess.SY

**发布日期**: 2025-05-26 (更新: 2025-10-23)

**备注**: NeurIPS 2025. Code: https://github.com/laminair/mess-plus

---

## 💡 一句话要点

**提出MESS+以优化LLM请求路由并确保服务质量**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `请求路由` `服务水平协议` `随机优化` `成本优化`

## 📋 核心要点

1. 现有的LLM路由方法在选择适合特定任务的模型时缺乏灵活性，且难以满足用户和服务提供商的不同需求。
2. MESS+通过实时学习LLM的请求满意度概率，解决了模型选择的优化问题，确保了服务质量与成本的平衡。
3. 在多项LLM基准测试中，MESS+实现了平均2倍的成本节省，显著提升了路由效率。

## 📝 摘要（中文）

开放权重的大型语言模型（LLM）库提供了多种高质量模型的访问，但选择适合特定任务的模型仍然具有挑战性，且需要技术专长。大多数用户希望获得事实正确、安全且令人满意的响应，而推理服务提供商则优先考虑降低运营成本。这些相互竞争的利益通常通过服务水平协议（SLA）进行调解，以保证最低服务质量。我们提出了MESS+，一种随机优化算法，用于在提供严格SLA合规保证的同时实现成本最优的LLM请求路由。MESS+在用户与系统交互时实时学习LLM的请求满意度概率，并基于此解决每个请求的优化问题。我们的算法结合了虚拟队列和请求满意度预测的创新方法，并进行了成本最优性和约束满足的理论分析。在一系列最先进的LLM基准测试中，MESS+相比现有的LLM路由技术实现了平均2倍的成本节省。

## 🔬 方法详解

**问题定义**：本论文旨在解决在开放权重LLM库中，如何高效选择适合特定任务的模型的问题。现有方法往往无法兼顾用户的需求和服务提供商的成本控制，导致服务质量和运营效率下降。

**核心思路**：MESS+的核心思路是通过实时学习LLM的请求满意度概率，动态优化模型选择。该方法通过解决每个请求的优化问题，确保在满足服务水平协议（SLA）的前提下实现成本最优。

**技术框架**：MESS+的整体架构包括虚拟队列和请求满意度预测模块。系统在用户发起请求时，实时评估不同模型的满意度，并根据预测结果进行模型选择。

**关键创新**：MESS+的主要创新在于结合了虚拟队列与请求满意度预测的机制，能够在动态环境中快速适应用户需求，确保服务质量与成本的最优平衡。这与传统的静态模型选择方法形成了鲜明对比。

**关键设计**：在设计中，MESS+使用了特定的损失函数来优化请求满意度的预测，并通过调整虚拟队列的参数来提高系统的响应速度和准确性。

## 📊 实验亮点

在实验中，MESS+在多项LLM基准测试中实现了平均2倍的成本节省，相比于现有的LLM路由技术，展现了显著的性能提升。这一结果表明MESS+在优化模型选择和满足服务质量方面的有效性。

## 🎯 应用场景

该研究的潜在应用领域包括智能客服、在线教育、内容生成等多个需要高效模型选择的场景。通过优化LLM请求路由，MESS+能够帮助服务提供商降低运营成本，同时提升用户体验，具有重要的实际价值和广泛的应用前景。

## 📄 摘要（原文）

> Open-weight large language model (LLM) zoos provide access to numerous high-quality models, but selecting the appropriate model for specific tasks remains challenging and requires technical expertise. Most users simply want factually correct, safe, and satisfying responses without concerning themselves with model technicalities, while inference service providers prioritize minimizing operating costs. These competing interests are typically mediated through service level agreements (SLAs) that guarantee minimum service quality. We introduce MESS+, a stochastic optimization algorithm for cost-optimal LLM request routing while providing rigorous SLA compliance guarantees. MESS+ learns request satisfaction probabilities of LLMs in real-time as users interact with the system, based on which model selection decisions are made by solving a per-request optimization problem. Our algorithm includes a novel combination of virtual queues and request satisfaction prediction, along with a theoretical analysis of cost optimality and constraint satisfaction. Across a wide range of state-of-the-art LLM benchmarks, MESS+ achieves an average of $2\times$ cost savings compared to existing LLM routing techniques.

