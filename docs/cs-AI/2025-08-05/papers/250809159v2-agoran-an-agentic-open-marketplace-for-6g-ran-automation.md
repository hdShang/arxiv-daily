---
layout: default
title: "Agoran: An Agentic Open Marketplace for 6G RAN Automation"
---

# Agoran: An Agentic Open Marketplace for 6G RAN Automation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.09159" class="toolbar-btn" target="_blank">📄 arXiv: 2508.09159v2</a>
  <a href="https://arxiv.org/pdf/2508.09159.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.09159v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.09159v2', 'Agoran: An Agentic Open Marketplace for 6G RAN Automation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Ilias Chatzistefanidis, Navid Nikaein, Andrea Leone, Ali Maatouk, Leandros Tassiulas, Roberto Morabito, Ioannis Pitsiorlas, Marios Kountouris

**分类**: cs.NI, cs.AI

**发布日期**: 2025-08-05 (更新: 2025-08-21)

**备注**: Pre-print submitted to Computer Networks AI-for-6G

---

## 💡 一句话要点

**提出Agoran以解决6G RAN自动化中的利益相关者协调问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `6G网络` `网络切片` `自动化管理` `多服务协调` `人工智能` `实时决策` `资源优化`

## 📋 核心要点

1. 现有网络切片控制器在多服务所有者目标协调方面存在僵化和缺乏商业背景的问题。
2. Agoran通过三个自主AI分支（立法、执行、司法）构建了一个代理市场，增强了利益相关者的参与和决策能力。
3. 在私有5G测试平台上，Agoran实现了eMBB切片吞吐量提高37%、URLLC切片延迟降低73%的显著效果。

## 📝 摘要（中文）

下一代移动网络必须调和多个服务所有者之间常常冲突的目标。然而，现有的网络切片控制器仍然僵化、受政策约束且缺乏商业背景意识。我们提出了Agoran服务和资源代理（SRB），这是一个代理市场，将利益相关者直接纳入操作环节。Agoran通过三个自主AI分支分配权力：立法分支使用增强检索的大型语言模型（LLMs）回答合规查询；执行分支通过观察者更新的向量数据库保持实时态势感知；司法分支评估每个代理消息的基于规则的信任评分，同时仲裁LLMs检测恶意行为并实时应用激励以恢复信任。在私有5G测试平台上进行部署并使用车辆移动的真实轨迹进行评估，Agoran实现了显著的增益：eMBB切片的吞吐量提高了37%，URLLC切片的延迟降低了73%，同时与静态基线相比，端到端PRB使用节省了8.3%。

## 🔬 方法详解

**问题定义**：论文旨在解决当前网络切片控制器在多服务所有者目标协调中的僵化和缺乏商业背景的问题。现有方法无法灵活应对不同利益相关者的需求，导致资源利用效率低下。

**核心思路**：Agoran通过构建一个代理市场，将利益相关者直接纳入操作环节，利用三个自主AI分支（立法、执行、司法）来增强决策的灵活性和实时性。这样的设计旨在提高网络切片的动态适应能力和资源分配效率。

**技术框架**：Agoran的整体架构包括三个主要模块：立法分支负责合规性查询，执行分支维护实时态势感知，司法分支评估信任评分并仲裁消息。各模块通过协同工作，实现利益相关者的高效沟通与决策。

**关键创新**：Agoran的最大创新在于其代理市场的构建和三分支架构，允许利益相关者在实时环境中进行灵活的协商与决策。这与传统的静态控制器形成鲜明对比，显著提升了网络的灵活性和响应能力。

**关键设计**：在技术细节上，Agoran使用了增强检索的LLMs进行合规性查询，采用观察者更新的向量数据库来维护实时数据，并通过基于规则的信任评分机制来评估代理消息的可信度。

## 📊 实验亮点

Agoran在私有5G测试平台上的实验结果显示，eMBB切片的吞吐量提高了37%，URLLC切片的延迟降低了73%，同时端到端PRB使用节省了8.3%。这些结果表明Agoran在动态资源管理和服务质量提升方面的显著优势。

## 🎯 应用场景

该研究的潜在应用领域包括下一代移动网络的自动化管理、资源优化和服务质量保障。Agoran的设计理念可以为未来的6G网络提供灵活的解决方案，促进不同服务所有者之间的高效协作，提升网络的整体性能和用户体验。

## 📄 摘要（原文）

> Next-generation mobile networks must reconcile the often-conflicting goals of multiple service owners. However, today's network slice controllers remain rigid, policy-bound, and unaware of the business context. We introduce Agoran Service and Resource Broker (SRB), an agentic marketplace that brings stakeholders directly into the operational loop. Inspired by the ancient Greek agora, Agoran distributes authority across three autonomous AI branches: a Legislative branch that answers compliance queries using retrieval-augmented Large Language Models (LLMs); an Executive branch that maintains real-time situational awareness through a watcher-updated vector database; and a Judicial branch that evaluates each agent message with a rule-based Trust Score, while arbitrating LLMs detect malicious behavior and apply real-time incentives to restore trust. Stakeholder-side Negotiation Agents and the SRB-side Mediator Agent negotiate feasible, Pareto-optimal offers produced by a multi-objective optimizer, reaching a consensus intent in a single round, which is then deployed to Open and AI RAN controllers. Deployed on a private 5G testbed and evaluated with realistic traces of vehicle mobility, Agoran achieved significant gains: (i) a 37% increase in throughput of eMBB slices, (ii) a 73% reduction in latency of URLLC slices, and concurrently (iii) an end-to-end 8.3% saving in PRB usage compared to a static baseline. An 1B-parameter Llama model, fine-tuned for five minutes on 100 GPT-4 dialogues, recovers approximately 80% of GPT-4.1's decision quality, while operating within 6 GiB of memory and converging in only 1.3 seconds. These results establish Agoran as a concrete, standards-aligned path toward ultra-flexible, stakeholder-centric 6G networks. A live demo is presented https://www.youtube.com/watch?v=h7vEyMu2f5w\&ab_channel=BubbleRAN.

