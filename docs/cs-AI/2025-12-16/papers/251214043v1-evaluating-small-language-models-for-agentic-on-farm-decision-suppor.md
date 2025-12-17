---
layout: default
title: Evaluating Small Language Models for Agentic On-Farm Decision Support Systems
---

# Evaluating Small Language Models for Agentic On-Farm Decision Support Systems

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.14043" class="toolbar-btn" target="_blank">📄 arXiv: 2512.14043v1</a>
  <a href="https://arxiv.org/pdf/2512.14043.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.14043v1" onclick="toggleFavorite(this, '2512.14043v1', 'Evaluating Small Language Models for Agentic On-Farm Decision Support Systems')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Enhong Liu, Haiyu Yang, Miel Hostens

**分类**: cs.AI

**发布日期**: 2025-12-16

---

## 💡 一句话要点

**评估小型语言模型在农场决策支持系统中的应用潜力，Qwen-4B表现突出。**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `小型语言模型` `农场决策支持` `Agentic AI` `奶牛养殖` `Qwen-4B`

## 📋 核心要点

1. 现有大型语言模型计算需求高，难以在农场本地部署，限制了其在奶牛养殖决策支持中的应用。
2. 论文构建了一个基于小型语言模型的agentic AI系统，包含文献、网络搜索等五个任务代理，用于农场决策支持。
3. 实验评估了20个小型语言模型，Qwen-4B在多数任务中表现优异，验证了小型语言模型在农场决策中的潜力。

## 📝 摘要（中文）

大型语言模型(LLM)有潜力通过支持决策制定和扩大技术知识有限的利益相关者的知识获取，来支持奶业学者和农民。然而，巨大的计算需求几乎完全限制了通过云服务访问LLM，这使得基于LLM的决策支持工具对于奶牛养殖来说是不切实际的。为了解决这一差距，需要能够在农场硬件上本地运行的轻量级替代方案。在这项工作中，我们对HuggingFace上可用的20个开源小型语言模型(SLM)在农场实际计算约束下进行了基准测试。基于我们之前的工作，我们开发了一个agentic AI系统，该系统集成了五个特定于任务的代理：文献搜索、网络搜索、SQL数据库交互、NoSQL数据库交互以及遵循预测模型的图形生成。评估分两个阶段进行。在第一阶段，使用五个测试问题进行初步筛选，以识别能够在计算受限环境中遵循基本的乳制品相关指令并可靠执行的模型。通过此初步阶段的模型随后在第二阶段使用30个问题（每个任务类别五个，加上一个解决完整性和不当行为的类别）进行评估。结果表明，Qwen-4B在大多数任务类别中都取得了优异的性能，尽管在通过PySpark进行的NoSQL数据库交互中表现出不稳定的有效性。据我们所知，这是第一项明确评估SLM作为奶牛养殖决策引擎可行性的工作，其中心重点是隐私和计算效率。虽然结果突出了SLM辅助工具在奶牛养殖中实际部署的前景，但仍然存在挑战，并且仍然需要进行微调以完善SLM在奶牛特定问题中的性能。

## 🔬 方法详解

**问题定义**：论文旨在解决大型语言模型（LLM）计算资源需求高，难以在资源受限的农场环境中部署的问题。现有基于LLM的决策支持工具主要依赖云服务，存在隐私和成本问题，无法满足奶牛养殖的实际需求。因此，需要寻找能够在本地运行、计算效率高的小型语言模型（SLM）作为替代方案。

**核心思路**：论文的核心思路是评估和选择适合农场环境的小型语言模型，并构建一个基于该模型的agentic AI系统，以支持奶牛养殖的决策过程。通过将复杂的决策任务分解为多个子任务，并为每个子任务设计专门的代理，从而降低了对单个模型性能的要求，提高了整体系统的可靠性和效率。

**技术框架**：该agentic AI系统包含五个主要模块，每个模块对应一个特定任务的代理：1) 文献搜索代理：用于检索相关学术文献；2) 网络搜索代理：用于从互联网获取信息；3) SQL数据库交互代理：用于查询结构化数据；4) NoSQL数据库交互代理：用于查询非结构化数据；5) 图形生成代理：用于根据预测模型生成可视化图表。整个系统通过协调这些代理的工作，完成复杂的决策支持任务。

**关键创新**：论文的关键创新在于明确评估了小型语言模型在农场决策支持中的可行性，并构建了一个集成了多个任务代理的agentic AI系统。与以往的研究不同，该研究特别关注隐私和计算效率，旨在开发能够在本地运行的实用工具。此外，该研究还针对奶牛养殖领域的问题进行了专门的评估和优化。

**关键设计**：论文采用两阶段评估方法。第一阶段使用少量问题进行初步筛选，选择能够满足基本要求的模型。第二阶段使用更全面的问题集进行详细评估，包括五个任务类别和一个完整性和不当行为类别。评估指标包括准确率、效率和稳定性。在NoSQL数据库交互中，使用了PySpark进行数据处理。Qwen-4B模型在多数任务中表现出色，但NoSQL数据库交互的稳定性有待提高。

## 📊 实验亮点

实验结果表明，Qwen-4B在多数任务类别中表现优异，证明了小型语言模型在农场决策支持中的潜力。尽管在NoSQL数据库交互中存在不稳定性，但整体性能优于其他参评模型。该研究首次明确评估了小型语言模型在奶牛养殖决策中的可行性，为后续研究提供了重要的参考。

## 🎯 应用场景

该研究成果可应用于开发低成本、高隐私的农场决策支持系统，帮助农民进行更科学的饲养管理、疾病预防和资源优化。未来，可进一步扩展到其他农业领域，例如作物种植、畜牧养殖等，促进农业智能化发展，提高生产效率和可持续性。

## 📄 摘要（原文）

> Large Language Models (LLM) hold potential to support dairy scholars and farmers by supporting decision-making and broadening access to knowledge for stakeholders with limited technical expertise. However, the substantial computational demand restricts access to LLM almost exclusively through cloud-based service, which makes LLM-based decision support tools impractical for dairy farming. To address this gap, lightweight alternatives capable of running locally on farm hardware are required. In this work, we benchmarked 20 open-source Small Language Models (SLM) available on HuggingFace under farm-realistic computing constraints. Building on our prior work, we developed an agentic AI system that integrates five task-specific agents: literature search, web search, SQL database interaction, NoSQL database interaction, and graph generation following predictive models. Evaluation was conducted in two phases. In the first phase, five test questions were used for the initial screening to identify models capable of following basic dairy-related instructions and performing reliably in a compute-constrained environment. Models that passed this preliminary stage were then evaluated using 30 questions (five per task category mentioned above, plus one category addressing integrity and misconduct) in phase two. In results, Qwen-4B achieved superior performance across most of task categories, although showed unstable effectiveness in NoSQL database interactions through PySpark. To our knowledge, this is the first work explicitly evaluating the feasibility of SLM as engines for dairy farming decision-making, with central emphases on privacy and computational efficiency. While results highlight the promise of SLM-assisted tools for practical deployment in dairy farming, challenges remain, and fine-tuning is still needed to refine SLM performance in dairy-specific questions.

