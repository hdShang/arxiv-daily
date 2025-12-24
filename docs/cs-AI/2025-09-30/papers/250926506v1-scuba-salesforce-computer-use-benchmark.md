---
layout: default
title: "SCUBA: Salesforce Computer Use Benchmark"
---

# SCUBA: Salesforce Computer Use Benchmark

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.26506" class="toolbar-btn" target="_blank">📄 arXiv: 2509.26506v1</a>
  <a href="https://arxiv.org/pdf/2509.26506.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.26506v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.26506v1', 'SCUBA: Salesforce Computer Use Benchmark')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yutong Dai, Krithika Ramakrishnan, Jing Gu, Matthew Fernandez, Yanqi Luo, Viraj Prabhu, Zhenyu Hu, Silvio Savarese, Caiming Xiong, Zeyuan Chen, Ran Xu

**分类**: cs.AI

**发布日期**: 2025-09-30

---

## 💡 一句话要点

**SCUBA：Salesforce平台计算机使用基准测试，评估CRM工作流自动化智能体**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)**

**关键词**: `计算机使用智能体` `Salesforce` `CRM` `基准测试` `企业软件自动化`

## 📋 核心要点

1. 现有方法在企业级软件（如Salesforce）的自动化任务中表现不佳，缺乏真实场景的基准测试。
2. SCUBA基准测试通过模拟真实用户在Salesforce CRM中的工作流程，评估智能体的企业软件使用能力。
3. 实验表明，开源模型在SCUBA上的零样本性能远低于闭源模型，演示增强能显著提升任务成功率。

## 📝 摘要（中文）

本文提出了SCUBA，一个旨在评估计算机使用智能体在Salesforce平台客户关系管理(CRM)工作流中表现的基准测试。SCUBA包含300个任务实例，来源于真实用户访谈，覆盖平台管理员、销售代表和服务专员三种主要角色。这些任务测试了一系列企业关键能力，包括企业软件UI导航、数据操作、工作流自动化、信息检索和故障排除。为了确保真实性，SCUBA在Salesforce沙箱环境中运行，支持并行执行和细粒度的评估指标以捕捉里程碑进度。本文对各种智能体在零样本和演示增强设置下进行了基准测试。结果表明，不同智能体设计范式之间存在巨大性能差距，开源模型和闭源模型之间也存在差距。在零样本设置中，在OSWorld等相关基准测试中表现良好的开源模型驱动的计算机使用智能体在SCUBA上的成功率低于5%，而基于闭源模型的方法仍然可以达到高达39%的任务成功率。在演示增强设置中，任务成功率可以提高到50%，同时分别降低13%和16%的时间和成本。这些发现突出了企业任务自动化的挑战以及智能体解决方案的前景。通过提供具有可解释评估的真实基准，SCUBA旨在加速构建用于复杂业务软件生态系统的可靠计算机使用智能体的进展。

## 🔬 方法详解

**问题定义**：现有计算机使用智能体在通用任务上表现良好，但在复杂的企业软件（如Salesforce）中的自动化任务中面临挑战。现有方法缺乏针对企业软件的真实场景基准测试，难以评估和提升智能体在实际业务环境中的能力。现有方法难以处理企业软件复杂的UI导航、数据操作、工作流自动化、信息检索和故障排除等任务。

**核心思路**：SCUBA的核心思路是构建一个基于真实用户访谈的、在Salesforce沙箱环境中运行的基准测试，以评估智能体在CRM工作流中的表现。通过模拟真实用户在Salesforce中的操作，SCUBA能够更准确地反映智能体在实际业务场景中的能力。通过提供细粒度的评估指标，SCUBA能够捕捉智能体在任务执行过程中的里程碑进度。

**技术框架**：SCUBA基准测试包含以下主要组成部分：1) 300个任务实例，来源于真实用户访谈，覆盖平台管理员、销售代表和服务专员三种主要角色。2) Salesforce沙箱环境，用于模拟真实的企业软件环境。3) 并行执行支持，允许同时运行多个任务实例。4) 细粒度的评估指标，用于捕捉智能体在任务执行过程中的里程碑进度。5) 零样本和演示增强设置，用于评估不同智能体在不同设置下的表现。

**关键创新**：SCUBA的关键创新在于其真实性和细粒度的评估。SCUBA基于真实用户访谈构建任务实例，并在Salesforce沙箱环境中运行，从而确保了基准测试的真实性。SCUBA提供细粒度的评估指标，能够捕捉智能体在任务执行过程中的里程碑进度，从而更全面地评估智能体的能力。与现有方法相比，SCUBA更能够反映智能体在实际业务场景中的能力。

**关键设计**：SCUBA的关键设计包括：1) 任务实例的设计，确保任务实例覆盖了企业软件使用的各种关键能力，如UI导航、数据操作、工作流自动化、信息检索和故障排除。2) 评估指标的设计，确保评估指标能够捕捉智能体在任务执行过程中的里程碑进度。3) 零样本和演示增强设置的设计，用于评估不同智能体在不同设置下的表现。具体参数设置和损失函数取决于被测试的智能体模型。

## 📊 实验亮点

实验结果表明，在零样本设置下，开源模型驱动的智能体在SCUBA上的成功率低于5%，而基于闭源模型的方法可以达到39%的任务成功率。在演示增强设置中，任务成功率可以提高到50%，同时分别降低13%和16%的时间和成本。这些结果突出了企业任务自动化的挑战以及智能体解决方案的潜力。

## 🎯 应用场景

SCUBA基准测试可用于评估和改进计算机使用智能体在企业软件自动化领域的应用。潜在应用包括自动化客户关系管理(CRM)工作流程、提高销售效率、改善客户服务质量、降低企业运营成本。该研究将推动企业软件自动化技术的发展，并为企业提供更智能、更高效的解决方案。

## 📄 摘要（原文）

> We introduce SCUBA, a benchmark designed to evaluate computer-use agents on customer relationship management (CRM) workflows within the Salesforce platform. SCUBA contains 300 task instances derived from real user interviews, spanning three primary personas, platform administrators, sales representatives, and service agents. The tasks test a range of enterprise-critical abilities, including Enterprise Software UI navigation, data manipulation, workflow automation, information retrieval, and troubleshooting. To ensure realism, SCUBA operates in Salesforce sandbox environments with support for parallel execution and fine-grained evaluation metrics to capture milestone progress. We benchmark a diverse set of agents under both zero-shot and demonstration-augmented settings. We observed huge performance gaps in different agent design paradigms and gaps between the open-source model and the closed-source model. In the zero-shot setting, open-source model powered computer-use agents that have strong performance on related benchmarks like OSWorld only have less than 5\% success rate on SCUBA, while methods built on closed-source models can still have up to 39% task success rate. In the demonstration-augmented settings, task success rates can be improved to 50\% while simultaneously reducing time and costs by 13% and 16%, respectively. These findings highlight both the challenges of enterprise tasks automation and the promise of agentic solutions. By offering a realistic benchmark with interpretable evaluation, SCUBA aims to accelerate progress in building reliable computer-use agents for complex business software ecosystems.

