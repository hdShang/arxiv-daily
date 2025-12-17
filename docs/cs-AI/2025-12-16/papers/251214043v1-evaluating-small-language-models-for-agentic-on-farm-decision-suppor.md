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

**评估小型语言模型作为乳业农场决策支持系统的可行性，强调隐私与计算效率**

🎯 **匹配领域**: **世界模型** **强化学习**

**关键词**: `小型语言模型` `乳业农场决策` `代理式AI系统` `计算效率` `隐私保护` `基准测试` `本地化部署` `多任务评估`

## 📋 核心要点

1. 核心问题：大型语言模型计算需求高，依赖云服务，在乳业农场中不切实际，限制了决策支持工具的部署。
2. 方法要点：开发代理式AI系统，集成五个任务特定代理，在农场硬件约束下评估20个开源小型语言模型。
3. 实验或效果：Qwen-4B在多数任务中表现优异，但NoSQL交互不稳定，证明了SLM在乳业决策中的潜力。

## 📝 摘要（中文）

大型语言模型（LLM）有潜力通过支持决策制定和扩大知识获取来帮助乳业学者和农民，特别是对那些技术专业知识有限的利益相关者。然而，巨大的计算需求使得LLM几乎只能通过基于云的服务访问，这使得基于LLM的决策支持工具在乳业农场中不切实际。为了解决这一差距，需要能够在农场硬件上本地运行的轻量级替代方案。在这项工作中，我们在农场现实计算约束下，对HuggingFace上可用的20个开源小型语言模型（SLM）进行了基准测试。基于我们之前的工作，我们开发了一个代理式AI系统，该系统集成了五个任务特定的代理：文献搜索、网络搜索、SQL数据库交互、NoSQL数据库交互以及基于预测模型的图生成。评估分两个阶段进行。在第一阶段，使用五个测试问题进行初步筛选，以识别能够遵循基本乳业相关指令并在计算受限环境中可靠运行的模型。通过初步阶段的模型随后在第二阶段使用30个问题（上述每个任务类别五个，加上一个涉及完整性和不当行为的类别）进行评估。在结果中，Qwen-4B在大多数任务类别中实现了卓越性能，尽管在通过PySpark进行NoSQL数据库交互时表现出不稳定的有效性。据我们所知，这是第一项明确评估SLM作为乳业农场决策引擎可行性的工作，重点关注隐私和计算效率。虽然结果突出了SLM辅助工具在乳业农场实际部署中的前景，但挑战仍然存在，并且仍需要微调以优化SLM在乳业特定问题中的性能。

## 🔬 方法详解

论文的核心方法是开发一个代理式AI系统，该系统集成了五个任务特定代理：文献搜索、网络搜索、SQL数据库交互、NoSQL数据库交互和基于预测模型的图生成。整体框架基于农场现实计算约束，对20个开源小型语言模型进行基准测试。关键技术创新点在于首次将SLM作为乳业农场决策引擎进行可行性评估，并构建多代理系统以模拟实际决策流程。与现有方法的主要区别在于，现有研究多关注大型语言模型在云端的应用，而本工作专注于轻量级、本地化的小型语言模型，强调隐私保护和计算效率，解决了乳业农场中资源受限环境下的实际部署问题。

## 📊 实验亮点

最重要的实验结果是Qwen-4B在大多数任务类别中表现最佳，证明了小型语言模型在乳业决策中的可行性。性能提升体现在计算效率高、隐私保护强，但NoSQL数据库交互存在不稳定性，表明仍需优化。

## 🎯 应用场景

该研究主要应用于乳业农场决策支持系统，帮助农民和学者进行数据驱动的决策制定，如疾病预测、资源管理和知识查询。潜在价值在于提供本地化、隐私保护的AI工具，降低技术门槛，提升农场运营效率。

## 📄 摘要（原文）

> Large Language Models (LLM) hold potential to support dairy scholars and farmers by supporting decision-making and broadening access to knowledge for stakeholders with limited technical expertise. However, the substantial computational demand restricts access to LLM almost exclusively through cloud-based service, which makes LLM-based decision support tools impractical for dairy farming. To address this gap, lightweight alternatives capable of running locally on farm hardware are required. In this work, we benchmarked 20 open-source Small Language Models (SLM) available on HuggingFace under farm-realistic computing constraints. Building on our prior work, we developed an agentic AI system that integrates five task-specific agents: literature search, web search, SQL database interaction, NoSQL database interaction, and graph generation following predictive models. Evaluation was conducted in two phases. In the first phase, five test questions were used for the initial screening to identify models capable of following basic dairy-related instructions and performing reliably in a compute-constrained environment. Models that passed this preliminary stage were then evaluated using 30 questions (five per task category mentioned above, plus one category addressing integrity and misconduct) in phase two. In results, Qwen-4B achieved superior performance across most of task categories, although showed unstable effectiveness in NoSQL database interactions through PySpark. To our knowledge, this is the first work explicitly evaluating the feasibility of SLM as engines for dairy farming decision-making, with central emphases on privacy and computational efficiency. While results highlight the promise of SLM-assisted tools for practical deployment in dairy farming, challenges remain, and fine-tuning is still needed to refine SLM performance in dairy-specific questions.

