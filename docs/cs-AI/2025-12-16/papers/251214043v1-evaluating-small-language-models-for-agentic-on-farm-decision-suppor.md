---
layout: default
title: Evaluating Small Language Models for Agentic On-Farm Decision Support Systems
---

# Evaluating Small Language Models for Agentic On-Farm Decision Support Systems

**arXiv**: [2512.14043v1](https://arxiv.org/abs/2512.14043) | [PDF](https://arxiv.org/pdf/2512.14043.pdf)

**作者**: Enhong Liu, Haiyu Yang, Miel Hostens

**分类**: cs.AI

**发布日期**: 2025-12-16

---

## 💡 一句话要点

**评估小型语言模型在农场决策支持系统中的应用潜力，Qwen-4B表现突出。**

🎯 **匹配领域**: **强化学习与模仿学习 (RL & IL)** **世界模型与预测 (World Models)**

**关键词**: `小型语言模型` `农场决策支持` `乳品农业` `智能代理` `Qwen-4B`

## 📋 核心要点

1. 大型语言模型计算需求高，难以在农场本地部署，限制了其在乳业决策支持中的应用。
2. 论文提出使用小型语言模型（SLM）构建智能AI系统，包含文献、网络搜索和数据库交互等多个代理。
3. 实验评估了20个开源SLM在农场计算约束下的性能，Qwen-4B在多数任务中表现出色。

## 📝 摘要（中文）

大型语言模型（LLM）有潜力通过支持决策制定和扩大技术知识有限的利益相关者的知识获取，从而为乳业学者和农民提供支持。然而，巨大的计算需求几乎完全限制了通过云服务访问LLM，这使得基于LLM的决策支持工具对于乳品农业来说是不切实际的。为了解决这一差距，需要能够在农场硬件上本地运行的轻量级替代方案。在这项工作中，我们对HuggingFace上可用的20个开源小型语言模型（SLM）在农场实际计算约束下进行了基准测试。在我们之前工作的基础上，我们开发了一个智能AI系统，该系统集成了五个特定于任务的代理：文献搜索、网络搜索、SQL数据库交互、NoSQL数据库交互以及遵循预测模型的图形生成。评估分两个阶段进行。在第一阶段，使用五个测试问题进行初步筛选，以识别能够在计算受限环境中遵循基本的乳制品相关指令并可靠执行的模型。通过此初步阶段的模型然后在第二阶段使用30个问题（每个任务类别五个，加上一个解决完整性和不当行为的类别）进行评估。结果表明，Qwen-4B在大多数任务类别中都取得了优异的性能，尽管在通过PySpark进行的NoSQL数据库交互中表现出不稳定的有效性。据我们所知，这是第一项明确评估SLM作为乳品农业决策引擎可行性的工作，其中心重点是隐私和计算效率。虽然结果突出了SLM辅助工具在乳品农业中实际部署的前景，但仍然存在挑战，并且仍然需要进行微调以完善SLM在乳品特定问题中的性能。

## 🔬 方法详解

**问题定义**：论文旨在解决大型语言模型（LLM）计算资源需求高，难以在资源受限的农场环境中部署的问题。现有基于LLM的决策支持工具主要依赖云服务，这限制了农民和乳业学者在本地使用这些工具，并且存在隐私问题。

**核心思路**：论文的核心思路是探索使用小型语言模型（SLM）替代大型语言模型，构建轻量级的、可在本地部署的智能AI系统。通过选择合适的SLM并集成多个特定任务的代理，实现农场决策支持功能，同时保证计算效率和数据隐私。

**技术框架**：该智能AI系统包含五个主要代理：1) 文献搜索代理；2) 网络搜索代理；3) SQL数据库交互代理；4) NoSQL数据库交互代理；5) 图形生成代理。系统首先接收用户的问题，然后根据问题类型选择合适的代理进行处理。代理之间可以协同工作，例如，文献搜索代理可以为其他代理提供信息。最后，系统将结果返回给用户。

**关键创新**：该研究的关键创新在于明确评估了SLM在乳品农业决策支持中的可行性，并构建了一个集成了多个任务代理的智能AI系统。这是首次针对该领域进行如此全面的SLM性能评估，并强调了隐私和计算效率的重要性。

**关键设计**：论文中，SLM的选择基于HuggingFace上可用的开源模型，并针对农场实际计算约束进行了基准测试。评估过程分为两个阶段：第一阶段进行初步筛选，第二阶段进行更全面的评估。评估指标包括模型在各个任务上的准确性和可靠性。NoSQL数据库交互代理使用了PySpark进行数据处理。

## 📊 实验亮点

实验结果表明，Qwen-4B在大多数任务类别中表现优异，证明了SLM在农场决策支持中的潜力。尽管Qwen-4B在NoSQL数据库交互中表现出不稳定性，但整体性能优于其他SLM。该研究为后续SLM在农业领域的应用提供了重要的参考。

## 🎯 应用场景

该研究成果可应用于构建本地部署的农场决策支持系统，帮助农民和乳业学者更高效地获取信息、分析数据和制定决策。该系统可以应用于饲料配方优化、疾病预测、产量预测等方面，提高农业生产效率和可持续性，并降低对云服务的依赖，保护数据隐私。

## 📄 摘要（原文）

> Large Language Models (LLM) hold potential to support dairy scholars and farmers by supporting decision-making and broadening access to knowledge for stakeholders with limited technical expertise. However, the substantial computational demand restricts access to LLM almost exclusively through cloud-based service, which makes LLM-based decision support tools impractical for dairy farming. To address this gap, lightweight alternatives capable of running locally on farm hardware are required. In this work, we benchmarked 20 open-source Small Language Models (SLM) available on HuggingFace under farm-realistic computing constraints. Building on our prior work, we developed an agentic AI system that integrates five task-specific agents: literature search, web search, SQL database interaction, NoSQL database interaction, and graph generation following predictive models. Evaluation was conducted in two phases. In the first phase, five test questions were used for the initial screening to identify models capable of following basic dairy-related instructions and performing reliably in a compute-constrained environment. Models that passed this preliminary stage were then evaluated using 30 questions (five per task category mentioned above, plus one category addressing integrity and misconduct) in phase two. In results, Qwen-4B achieved superior performance across most of task categories, although showed unstable effectiveness in NoSQL database interactions through PySpark. To our knowledge, this is the first work explicitly evaluating the feasibility of SLM as engines for dairy farming decision-making, with central emphases on privacy and computational efficiency. While results highlight the promise of SLM-assisted tools for practical deployment in dairy farming, challenges remain, and fine-tuning is still needed to refine SLM performance in dairy-specific questions.

