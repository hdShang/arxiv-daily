---
layout: default
title: "UML-CoT: Structured Reasoning and Planning with Unified Modeling Language for Robotic Room Cleaning"
---

# UML-CoT: Structured Reasoning and Planning with Unified Modeling Language for Robotic Room Cleaning

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.22628" class="toolbar-btn" target="_blank">📄 arXiv: 2509.22628v2</a>
  <a href="https://arxiv.org/pdf/2509.22628.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.22628v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.22628v2', 'UML-CoT: Structured Reasoning and Planning with Unified Modeling Language for Robotic Room Cleaning')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Hongyu Chen, Guangrun Wang

**分类**: cs.CV, cs.AI, cs.LG

**发布日期**: 2025-09-26 (更新: 2025-09-29)

---

## 💡 一句话要点

**提出UML-CoT框架，利用UML进行机器人房间清洁任务的结构化推理与规划**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `机器人` `统一建模语言` `思维链` `结构化推理` `具身智能`

## 📋 核心要点

1. 现有思维链方法依赖非结构化文本，缺乏可解释性和在具身任务中的可执行性。
2. UML-CoT利用UML类图和活动图进行结构化推理和规划，生成符号化CoT和可执行计划。
3. 在MRoom-30k基准测试中，UML-CoT在可解释性、规划连贯性和执行成功率方面均优于非结构化方法。

## 📝 摘要（中文）

本文提出了一种名为UML-CoT的结构化推理与规划框架，旨在利用统一建模语言（UML）为机器人房间清洁任务生成符号化的思维链（CoT）和可执行的行动计划。UML类图用于捕获组合式的对象语义，而活动图则用于建模过程化的控制流。该框架采用三阶段训练流程，结合了监督式微调和群体相对策略优化（GRPO），包括从仅有答案的数据中进行奖励学习。在新的MRoom-30k杂乱房间清洁场景基准测试中，UML-CoT在可解释性、规划连贯性和执行成功率方面均优于非结构化的CoT方法，突显了UML作为一种更具表现力和可操作性的结构化推理形式。

## 🔬 方法详解

**问题定义**：现有的大语言模型（LLMs）在具身任务中，虽然可以通过思维链（CoT）提示进行推理，但其非结构化的文本输出限制了可解释性和可执行性。已有的结构化CoT方法，如场景图或逻辑图，仅能建模低阶关系，缺乏继承或行为抽象等高级特性，并且缺乏用于序列或条件规划的标准语义。因此，如何构建一种更具表达力、可解释性和可执行性的结构化推理框架是本文要解决的核心问题。

**核心思路**：本文的核心思路是利用统一建模语言（UML）的强大表达能力，将复杂任务分解为结构化的符号表示。通过UML类图来描述环境中对象的组成和关系，利用UML活动图来建模任务的流程和控制逻辑。这种结构化的表示方式不仅提高了推理过程的可解释性，也使得生成的行动计划更易于执行。

**技术框架**：UML-CoT框架包含三个主要阶段：1) **UML图生成**：利用LLM生成UML类图和活动图，描述环境和任务。2) **符号化CoT生成**：基于UML图，LLM生成符号化的思维链，用于指导任务执行。3) **行动计划生成与执行**：将符号化的CoT转化为可执行的行动计划，并由机器人执行。该框架采用三阶段训练流程，首先进行监督式微调，然后使用群体相对策略优化（GRPO）进行强化学习，并从仅有答案的数据中学习奖励函数。

**关键创新**：本文最重要的技术创新在于将UML引入到机器人任务的推理和规划中。与以往的结构化CoT方法相比，UML具有更强的表达能力，可以建模更复杂的对象关系和行为模式。此外，UML作为一种标准化的建模语言，也提高了框架的可解释性和通用性。

**关键设计**：在UML图生成阶段，使用了特定的prompt模板来引导LLM生成符合规范的UML类图和活动图。在GRPO训练阶段，设计了合适的奖励函数，鼓励生成更连贯和有效的行动计划。具体参数设置和网络结构等技术细节在论文中有详细描述，此处不再赘述。

## 📊 实验亮点

UML-CoT在MRoom-30k基准测试中取得了显著的成果。与非结构化的CoT方法相比，UML-CoT在规划连贯性和执行成功率方面均有显著提升。实验结果表明，UML作为一种结构化推理形式，可以有效地提高机器人在复杂环境中的任务执行能力。

## 🎯 应用场景

UML-CoT框架具有广泛的应用前景，可应用于各种需要复杂推理和规划的机器人任务中，例如家庭服务机器人、工业自动化机器人、医疗机器人等。该框架通过提高任务的可解释性和可执行性，有望提升机器人的智能化水平和自主性，从而更好地服务于人类。

## 📄 摘要（原文）

> Chain-of-Thought (CoT) prompting improves reasoning in large language models (LLMs), but its reliance on unstructured text limits interpretability and executability in embodied tasks. Prior work has explored structured CoTs using scene or logic graphs, yet these remain fundamentally limited: they model only low-order relations, lack constructs like inheritance or behavioral abstraction, and provide no standardized semantics for sequential or conditional planning. We propose UML-CoT, a structured reasoning and planning framework that leverages Unified Modeling Language (UML) to generate symbolic CoTs and executable action plans. UML class diagrams capture compositional object semantics, while activity diagrams model procedural control flow. Our three-stage training pipeline combines supervised fine-tuning with Group Relative Policy Optimization (GRPO), including reward learning from answer-only data. We evaluate UML-CoT on MRoom-30k, a new benchmark of cluttered room-cleaning scenarios. UML-CoT outperforms unstructured CoTs in interpretability, planning coherence, and execution success, highlighting UML as a more expressive and actionable structured reasoning formalism.

