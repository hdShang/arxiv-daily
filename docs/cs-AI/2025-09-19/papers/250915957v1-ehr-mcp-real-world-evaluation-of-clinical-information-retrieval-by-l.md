---
layout: default
title: "EHR-MCP: Real-world Evaluation of Clinical Information Retrieval by Large Language Models via Model Context Protocol"
---

# EHR-MCP: Real-world Evaluation of Clinical Information Retrieval by Large Language Models via Model Context Protocol

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.15957" class="toolbar-btn" target="_blank">📄 arXiv: 2509.15957v1</a>
  <a href="https://arxiv.org/pdf/2509.15957.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.15957v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.15957v1', 'EHR-MCP: Real-world Evaluation of Clinical Information Retrieval by Large Language Models via Model Context Protocol')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Kanato Masayoshi, Masahiro Hashimoto, Ryoichi Yokoyama, Naoki Toda, Yoshifumi Uwamino, Shogo Fukuda, Ho Namkoong, Masahiro Jinzaki

**分类**: cs.AI, cs.CL, cs.HC, cs.IR

**发布日期**: 2025-09-19

---

## 💡 一句话要点

**EHR-MCP：通过模型上下文协议，在真实医院环境中评估大型语言模型在临床信息检索中的应用**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `电子健康记录` `模型上下文协议` `临床信息检索` `医院AI代理`

## 📋 核心要点

1. 现有方法难以将大型语言模型应用于医院场景，主要挑战在于电子健康记录系统的访问限制。
2. 论文提出EHR-MCP框架，通过模型上下文协议连接LLM和EHR数据库，实现LLM自主检索临床信息。
3. 实验结果表明，EHR-MCP在简单任务中表现出色，但在复杂任务中仍存在挑战，为未来研究奠定基础。

## 📝 摘要（中文）

背景：大型语言模型(LLMs)在医学领域展现出潜力，但由于电子健康记录(EHR)系统的访问限制，其在医院的部署受到限制。模型上下文协议(MCP)实现了LLMs与外部工具的集成。目的：评估通过MCP连接到EHR数据库的LLM是否能在真实的医院环境中自主检索临床相关信息。方法：我们开发了EHR-MCP，这是一个与医院EHR数据库集成的自定义MCP工具框架，并使用LangGraph ReAct agent通过GPT-4.1与之交互。测试了六项任务，这些任务源于感染控制团队(ICT)的使用案例。回顾性分析了ICT会议上讨论的八名患者。测量了与医生生成的黄金标准的协议度。结果：LLM始终如一地选择和执行正确的MCP工具。除了两项任务外，所有任务都达到了接近完美的准确率。在需要时间相关计算的复杂任务中，性能较低。大多数错误源于不正确的参数或对工具结果的误解。来自EHR-MCP的响应是可靠的，但冗长和重复的数据有超出上下文窗口的风险。结论：LLMs可以通过MCP工具从真实医院环境中的EHR检索临床数据，在简单任务中实现接近完美的性能，同时也突出了复杂任务中的挑战。EHR-MCP为安全、一致的数据访问提供了一个基础设施，并可能成为医院AI代理的基础。未来的工作应该扩展到检索之外，包括推理、生成和临床影响评估，为生成式AI有效集成到临床实践中铺平道路。

## 🔬 方法详解

**问题定义**：论文旨在解决大型语言模型(LLMs)在实际医院环境中应用受限的问题，核心痛点在于LLMs难以直接访问和利用电子健康记录(EHR)系统中的临床数据。现有方法缺乏有效的桥梁，无法将LLMs的强大能力与EHR系统连接起来，导致LLMs在临床决策支持等方面的潜力无法充分发挥。

**核心思路**：论文的核心思路是利用模型上下文协议(MCP)作为LLMs与EHR系统之间的桥梁。MCP允许LLMs通过预定义的工具与外部系统进行交互，从而实现对EHR数据的安全、可控访问。通过构建自定义的MCP工具，LLMs可以自主地检索、分析EHR数据，并为临床医生提供有价值的信息。

**技术框架**：EHR-MCP框架包含以下主要组成部分：1) 医院EHR数据库；2) 一组自定义的MCP工具，用于访问和操作EHR数据；3) LangGraph ReAct agent，作为LLM的控制中心，负责选择和执行MCP工具；4) GPT-4.1，作为LLM的核心，负责理解用户请求、生成查询、解析工具结果并生成最终答案。整个流程如下：用户发起请求 -> LangGraph ReAct agent分析请求并选择合适的MCP工具 -> MCP工具从EHR数据库检索数据 -> GPT-4.1解析工具结果并生成响应 -> 返回给用户。

**关键创新**：论文的关键创新在于将MCP应用于EHR数据访问，并构建了EHR-MCP框架，实现了LLMs在真实医院环境中自主检索临床信息。与现有方法相比，EHR-MCP提供了一种安全、可控、可扩展的方式，将LLMs与EHR系统集成起来，为临床应用开辟了新的可能性。

**关键设计**：EHR-MCP的关键设计包括：1) 自定义MCP工具的设计，需要根据具体的EHR数据结构和临床需求进行定制；2) LangGraph ReAct agent的配置，需要仔细调整参数，以确保LLM能够正确地选择和执行MCP工具；3) 上下文窗口的管理，由于EHR数据可能非常庞大，需要采取措施避免超出LLM的上下文窗口限制，例如对数据进行摘要或筛选。

## 📊 实验亮点

实验结果表明，EHR-MCP在六项感染控制团队(ICT)的使用案例中，除了两项复杂任务外，均达到了接近完美的准确率。LLM能够始终如一地选择和执行正确的MCP工具，证明了EHR-MCP在真实医院环境中的可行性和有效性。虽然在需要时间相关计算的复杂任务中性能有所下降，但这也为未来的研究方向提供了启示。

## 🎯 应用场景

该研究成果可应用于临床决策支持、患者风险评估、疾病预测和药物研发等领域。EHR-MCP为构建医院AI代理奠定了基础，未来有望实现更智能化的临床服务，例如自动生成病历摘要、辅助诊断、个性化治疗方案推荐等。该研究也为其他医疗机构提供了借鉴，促进生成式AI在医疗领域的广泛应用。

## 📄 摘要（原文）

> Background: Large language models (LLMs) show promise in medicine, but their deployment in hospitals is limited by restricted access to electronic health record (EHR) systems. The Model Context Protocol (MCP) enables integration between LLMs and external tools.
>   Objective: To evaluate whether an LLM connected to an EHR database via MCP can autonomously retrieve clinically relevant information in a real hospital setting.
>   Methods: We developed EHR-MCP, a framework of custom MCP tools integrated with the hospital EHR database, and used GPT-4.1 through a LangGraph ReAct agent to interact with it. Six tasks were tested, derived from use cases of the infection control team (ICT). Eight patients discussed at ICT conferences were retrospectively analyzed. Agreement with physician-generated gold standards was measured.
>   Results: The LLM consistently selected and executed the correct MCP tools. Except for two tasks, all tasks achieved near-perfect accuracy. Performance was lower in the complex task requiring time-dependent calculations. Most errors arose from incorrect arguments or misinterpretation of tool results. Responses from EHR-MCP were reliable, though long and repetitive data risked exceeding the context window.
>   Conclusions: LLMs can retrieve clinical data from an EHR via MCP tools in a real hospital setting, achieving near-perfect performance in simple tasks while highlighting challenges in complex ones. EHR-MCP provides an infrastructure for secure, consistent data access and may serve as a foundation for hospital AI agents. Future work should extend beyond retrieval to reasoning, generation, and clinical impact assessment, paving the way for effective integration of generative AI into clinical practice.

