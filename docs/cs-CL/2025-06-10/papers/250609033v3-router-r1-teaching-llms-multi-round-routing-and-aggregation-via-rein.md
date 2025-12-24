---
layout: default
title: "Router-R1: Teaching LLMs Multi-Round Routing and Aggregation via Reinforcement Learning"
---

# Router-R1: Teaching LLMs Multi-Round Routing and Aggregation via Reinforcement Learning

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.09033" class="toolbar-btn" target="_blank">📄 arXiv: 2506.09033v3</a>
  <a href="https://arxiv.org/pdf/2506.09033.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.09033v3" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.09033v3', 'Router-R1: Teaching LLMs Multi-Round Routing and Aggregation via Reinforcement Learning')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Haozhen Zhang, Tao Feng, Jiaxuan You

**分类**: cs.CL, cs.AI, cs.LG

**发布日期**: 2025-06-10 (更新: 2025-10-24)

**备注**: Accepted by NeurIPS 2025. Code is available at https://github.com/ulab-uiuc/Router-R1. Models and Datasets are available at https://huggingface.co/collections/ulab-ai/router-r1-6851bbe099c7a56914b5db03

---

## 💡 一句话要点

**提出Router-R1以解决多轮路由与聚合问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `强化学习` `多轮路由` `模型聚合` `性能优化` `成本管理` `智能系统`

## 📋 核心要点

1. 现有的LLM路由器通常仅支持单轮、一对一的映射，无法有效处理需要多模型协作的复杂任务。
2. Router-R1通过强化学习将多LLM路由和聚合建模为序列决策过程，增强了模型的推理和动态调用能力。
3. 实验结果表明，Router-R1在多个基准测试中超越了多个强基线，展现了更好的性能和成本管理能力。

## 📝 摘要（中文）

随着多样化的大型语言模型（LLMs）的快速出现，LLM路由器的发展也随之加速。现有的LLM路由器通常采用单轮、一对一的映射方式，这限制了其处理复杂任务的能力。本文提出了Router-R1，一个基于强化学习的框架，将多LLM路由和聚合视为一个序列决策过程。Router-R1将路由器本身实例化为一个强大的LLM，利用其推理能力将“思考”动作与“路由”动作交替进行，并将每个响应整合到其不断演变的上下文中。通过采用轻量级的基于规则的奖励机制，Router-R1在性能与成本之间优化平衡，展示了在七个通用和多跳问答基准上的优越性能。

## 🔬 方法详解

**问题定义**：本文旨在解决现有LLM路由器在处理复杂任务时的局限性，尤其是单轮、一对一的映射方式无法充分利用多个LLM的互补优势。

**核心思路**：Router-R1通过强化学习将多LLM路由和聚合视为序列决策过程，利用LLM的推理能力交替进行内部思考与动态路由，从而实现更高效的模型调用和响应整合。

**技术框架**：Router-R1的整体架构包括路由器本身作为LLM的实例，结合轻量级的基于规则的奖励机制，分为思考、路由和响应整合三个主要模块。

**关键创新**：Router-R1的核心创新在于将路由和聚合过程视为一个动态的决策过程，允许模型在执行过程中进行自我调整，显著提升了性能与成本的平衡能力。

**关键设计**：在设计上，Router-R1采用了简单的模型描述作为条件，如定价、延迟和示例性能，并引入了格式奖励、最终结果奖励和新颖的成本奖励，以优化性能与成本之间的权衡。

## 📊 实验亮点

在七个通用和多跳问答基准测试中，Router-R1的表现超越了多个强基线，展现出更优的性能和更强的泛化能力，尤其在成本管理方面也取得了显著进展，展示了其在实际应用中的潜力。

## 🎯 应用场景

Router-R1的研究成果在多种应用场景中具有潜在价值，尤其是在需要高效处理复杂查询的智能客服、信息检索和多模态交互等领域。通过优化模型选择和调用策略，Router-R1能够显著提升系统的响应速度和准确性，推动智能系统的进一步发展。

## 📄 摘要（原文）

> The rapid emergence of diverse large language models (LLMs) has spurred the development of LLM routers that assign user queries to the most suitable model. However, existing LLM routers typically perform a single-round, one-to-one mapping (\textit{i.e.}, assigning each query to a single model in isolation), which limits their capability to tackle complex tasks that demand the complementary strengths of multiple LLMs. In this paper, we present \textbf{Router-R1}, a reinforcement learning (RL)-based framework that formulates multi-LLM routing and aggregation as a sequential decision process. Router-R1 instantiates the router itself as a capable LLM, leveraging its reasoning ability to interleave "think" actions (internal deliberation) with "route" actions (dynamic model invocation), and integrates each response into its evolving context. To facilitate learning, we employ a lightweight rule-based reward comprising format rewards, final outcome rewards, and a novel cost reward for optimizing the balance between performance and cost, opening a pathway toward enhancing performance-cost trade-offs via RL. Router-R1 also conditions only on simple model descriptors such as pricing, latency, and example performance, enabling strong generalization to unseen model selection. Experiments on seven general and multi-hop QA benchmarks show that Router-R1 outperforms several strong baselines, achieving superior performance while maintaining robust generalization and cost management.

