---
layout: default
title: Evaluating Small Language Models for Agentic On-Farm Decision Support Systems
---

# Evaluating Small Language Models for Agentic On-Farm Decision Support Systems

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.14043" class="toolbar-btn" target="_blank">📄 arXiv: 2512.14043</a>
  <a href="https://arxiv.org/pdf/2512.14043.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.14043" onclick="toggleFavorite(this, '2512.14043', 'Evaluating Small Language Models for Agentic On-Farm Decision Support Systems')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Enhong Liu, Haiyu Yang, Miel Hostens

**分类**: cs.AI

**发布日期**: 2025-12-18

---

## 💡 一句话要点

**评估小型语言模型在农场决策支持系统中的应用潜力，Qwen-4B表现突出。**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `小型语言模型` `农场决策支持` `乳业` `智能代理` `计算效率`

## 📋 核心要点

1. 大型语言模型计算需求高，难以在农场本地部署，限制了其在乳业决策支持中的应用。
2. 论文提出使用小型语言模型（SLM）构建智能代理系统，在本地硬件上运行，降低计算成本。
3. 实验评估了20个开源SLM，Qwen-4B在多个任务中表现出色，验证了SLM在乳业决策中的潜力。

## 📝 摘要（中文）

大型语言模型(LLM)有潜力通过支持决策制定和扩大技术知识有限的利益相关者获取知识的途径来支持乳业学者和农民。然而，巨大的计算需求几乎完全限制了通过云服务访问LLM，这使得基于LLM的决策支持工具对于奶牛养殖来说是不切实际的。为了解决这一差距，需要能够在农场硬件上本地运行的轻量级替代方案。在这项工作中，我们以农场实际计算约束为基准，测试了HuggingFace上可用的20个开源小型语言模型(SLM)。基于我们之前的工作，我们开发了一个智能AI系统，该系统集成了五个特定于任务的代理：文献搜索、网络搜索、SQL数据库交互、NoSQL数据库交互以及遵循预测模型的图形生成。评估分两个阶段进行。在第一阶段，使用五个测试问题进行初步筛选，以识别能够在计算受限环境中遵循基本的乳制品相关指令并可靠地执行的模型。通过此初步阶段的模型随后在第二阶段使用30个问题（每个任务类别五个，加上一个解决诚信和不当行为的类别）进行评估。结果表明，Qwen-4B在大多数任务类别中都取得了优异的性能，尽管在通过PySpark进行的NoSQL数据库交互中表现出不稳定的有效性。据我们所知，这是第一项明确评估SLM作为乳业决策引擎可行性的工作，重点是隐私和计算效率。虽然结果突出了SLM辅助工具在乳业实际部署中的前景，但仍然存在挑战，并且仍然需要进行微调以完善SLM在乳业特定问题中的性能。

## 🔬 方法详解

**问题定义**：论文旨在解决大型语言模型（LLM）计算资源需求高，难以在资源受限的农场环境中部署的问题。现有基于LLM的决策支持系统主要依赖云服务，存在隐私和成本问题，无法满足乳业的实际需求。

**核心思路**：论文的核心思路是探索使用小型语言模型（SLM）替代LLM，构建能够在农场本地硬件上运行的智能代理系统。通过选择合适的SLM并进行针对性优化，可以在保证一定性能的前提下，显著降低计算成本和提高隐私性。

**技术框架**：论文构建了一个包含五个任务特定代理的智能AI系统：1) 文献搜索；2) 网络搜索；3) SQL数据库交互；4) NoSQL数据库交互；5) 基于预测模型的图生成。该系统首先使用五个测试问题进行初步筛选，然后使用30个问题（包括诚信和不当行为）进行更全面的评估。

**关键创新**：论文的关键创新在于首次明确评估了SLM作为乳业决策引擎的可行性，并强调了隐私和计算效率。通过构建包含多个代理的智能系统，实现了对乳业决策过程的全面支持。

**关键设计**：论文选择了HuggingFace上可用的20个开源SLM进行评估。评估过程分为两个阶段，第一阶段进行初步筛选，第二阶段进行全面评估。评估指标包括模型在各个任务上的准确性和稳定性。Qwen-4B在大多数任务类别中表现出色，但在NoSQL数据库交互中表现出不稳定性。

## 📊 实验亮点

实验结果表明，Qwen-4B在大多数任务类别中表现优异，证明了SLM在乳业决策支持中的潜力。尽管在NoSQL数据库交互中存在不稳定性，但整体性能优于其他SLM。该研究首次明确评估了SLM在乳业领域的应用，为后续研究提供了重要参考。

## 🎯 应用场景

该研究成果可应用于构建低成本、高隐私的农场决策支持系统，帮助农民和乳业学者更高效地获取知识和做出决策。未来，可以通过微调和优化SLM，进一步提升其在乳业特定问题上的性能，并将其推广到其他农业领域。

## 📄 摘要（原文）

> Large Language Models (LLM) hold potential to support dairy scholars and farmers by supporting decision-making and broadening access to knowledge for stakeholders with limited technical expertise. However, the substantial computational demand restricts access to LLM almost exclusively through cloud-based service, which makes LLM-based decision support tools impractical for dairy farming. To address this gap, lightweight alternatives capable of running locally on farm hardware are required. In this work, we benchmarked 20 open-source Small Language Models (SLM) available on HuggingFace under farm-realistic computing constraints. Building on our prior work, we developed an agentic AI system that integrates five task-specific agents: literature search, web search, SQL database interaction, NoSQL database interaction, and graph generation following predictive models. Evaluation was conducted in two phases. In the first phase, five test questions were used for the initial screening to identify models capable of following basic dairy-related instructions and performing reliably in a compute-constrained environment. Models that passed this preliminary stage were then evaluated using 30 questions (five per task category mentioned above, plus one category addressing integrity and misconduct) in phase two. In results, Qwen-4B achieved superior performance across most of task categories, although showed unstable effectiveness in NoSQL database interactions through PySpark. To our knowledge, this is the first work explicitly evaluating the feasibility of SLM as engines for dairy farming decision-making, with central emphases on privacy and computational efficiency. While results highlight the promise of SLM-assisted tools for practical deployment in dairy farming, challenges remain, and fine-tuning is still needed to refine SLM performance in dairy-specific questions.

