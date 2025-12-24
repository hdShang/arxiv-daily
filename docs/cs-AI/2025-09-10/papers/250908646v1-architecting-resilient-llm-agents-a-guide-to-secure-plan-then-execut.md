---
layout: default
title: "Architecting Resilient LLM Agents: A Guide to Secure Plan-then-Execute Implementations"
---

# Architecting Resilient LLM Agents: A Guide to Secure Plan-then-Execute Implementations

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.08646" class="toolbar-btn" target="_blank">📄 arXiv: 2509.08646v1</a>
  <a href="https://arxiv.org/pdf/2509.08646.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.08646v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.08646v1', 'Architecting Resilient LLM Agents: A Guide to Secure Plan-then-Execute Implementations')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Ron F. Del Rosario, Klaudia Krawiecka, Christian Schroeder de Witt

**分类**: cs.CR, cs.AI, eess.SY

**发布日期**: 2025-09-10

---

## 💡 一句话要点

**构建弹性LLM Agent：安全“计划-执行”模式的实现指南**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `LLM Agent` `计划-执行模式` `提示注入攻击` `安全架构` `LangChain` `CrewAI` `AutoGen` `人机环`

## 📋 核心要点

1. 现有LLM Agent在复杂任务自动化中面临安全风险，尤其容易受到间接提示注入攻击，影响系统稳定性和可信度。
2. 论文提出“计划-执行”（P-t-E）架构模式，将战略规划与战术执行分离，增强Agent的可预测性、成本效益和安全性。
3. 论文提供了LangChain、CrewAI和AutoGen等框架的P-t-E实现蓝图，并讨论了动态重规划、并行执行和人机环验证等高级模式。

## 📝 摘要（中文）

随着大型语言模型（LLM）Agent在自动化复杂、多步骤任务方面的能力日益增强，对稳健、安全和可预测的架构模式的需求变得至关重要。本文提供了一个关于“计划-执行”（P-t-E）模式的全面指南，这是一种将战略规划与战术执行分离的Agent设计。我们探讨了P-t-E的基本原则，详细介绍了其核心组件——规划器和执行器，以及其在可预测性、成本效率和推理质量方面相对于ReAct（推理+行动）等反应式模式的架构优势。重点关注这种设计的安全影响，特别是通过建立控制流完整性来抵御间接提示注入攻击的固有弹性。我们认为，虽然P-t-E提供了一个坚实的基础，但深度防御策略是必要的，并详细介绍了必要的补充控制，如最小权限原则、任务范围的工具访问和沙盒代码执行。为了使这些原则具有可操作性，本指南为三个领先的Agent框架：LangChain（通过LangGraph）、CrewAI和AutoGen提供了详细的实现蓝图和工作代码参考。分析了每个框架实现P-t-E模式的方法，突出了LangGraph用于重新规划的状态图、CrewAI用于安全性的声明式工具范围以及AutoGen的内置Docker沙盒等独特功能。最后，我们讨论了高级模式，包括动态重新规划循环、使用有向无环图（DAG）的并行执行以及人机环（HITL）验证的关键作用，为旨在构建生产级、弹性且值得信赖的LLM Agent的架构师、开发人员和安全工程师提供完整的战略蓝图。

## 🔬 方法详解

**问题定义**：现有LLM Agent在执行复杂任务时，容易受到恶意用户通过间接提示注入发起的攻击。这些攻击利用Agent对外部数据源的依赖，篡改数据以控制Agent的行为，导致不可预测的结果和安全漏洞。传统的反应式模式（如ReAct）缺乏对控制流的严格管理，使得攻击更容易得逞。

**核心思路**：论文的核心思路是采用“计划-执行”（P-t-E）架构，将任务分解为独立的规划和执行阶段。规划阶段负责生成详细的任务执行计划，而执行阶段则严格按照计划执行，从而限制了外部数据对Agent行为的直接影响。这种分离降低了Agent受到提示注入攻击的风险，提高了系统的可预测性和安全性。

**技术框架**：P-t-E架构包含两个主要模块：规划器（Planner）和执行器（Executor）。规划器接收用户指令，生成包含多个步骤的详细执行计划。执行器接收规划器生成的计划，并按照计划依次执行每个步骤。在执行过程中，执行器可以调用外部工具或API，但必须严格遵守计划的约束。此外，论文还讨论了动态重规划、并行执行和人机环验证等高级模式，以进一步增强Agent的鲁棒性和可靠性。

**关键创新**：P-t-E架构的关键创新在于将战略规划与战术执行分离，从而实现了控制流的完整性。与传统的反应式模式相比，P-t-E模式能够更好地抵御间接提示注入攻击，并提高Agent的可预测性和安全性。此外，论文还提供了LangChain、CrewAI和AutoGen等主流Agent框架的P-t-E实现方案，为开发者提供了实用的参考。

**关键设计**：论文强调了最小权限原则、任务范围的工具访问和沙盒代码执行等关键设计原则，以进一步增强Agent的安全性。例如，通过限制Agent对外部工具的访问权限，可以降低恶意代码执行的风险。此外，论文还讨论了如何使用LangGraph的状态图实现动态重规划，以及如何使用有向无环图（DAG）实现并行执行。

## 📊 实验亮点

论文通过分析LangChain、CrewAI和AutoGen等框架的P-t-E实现，展示了该架构在不同平台上的可行性和优势。特别地，LangGraph的状态图允许Agent进行动态重规划，CrewAI的声明式工具范围增强了安全性，AutoGen的Docker沙箱提供了隔离的执行环境。

## 🎯 应用场景

该研究成果可广泛应用于需要安全可靠的LLM Agent的场景，如金融风控、智能客服、自动化运维等。通过采用P-t-E架构，可以有效降低Agent受到恶意攻击的风险，提高系统的稳定性和可信度，从而推动LLM Agent在实际应用中的普及。

## 📄 摘要（原文）

> As Large Language Model (LLM) agents become increasingly capable of automating complex, multi-step tasks, the need for robust, secure, and predictable architectural patterns is paramount. This paper provides a comprehensive guide to the ``Plan-then-Execute'' (P-t-E) pattern, an agentic design that separates strategic planning from tactical execution. We explore the foundational principles of P-t-E, detailing its core components - the Planner and the Executor - and its architectural advantages in predictability, cost-efficiency, and reasoning quality over reactive patterns like ReAct (Reason + Act). A central focus is placed on the security implications of this design, particularly its inherent resilience to indirect prompt injection attacks by establishing control-flow integrity. We argue that while P-t-E provides a strong foundation, a defense-in-depth strategy is necessary, and we detail essential complementary controls such as the Principle of Least Privilege, task-scoped tool access, and sandboxed code execution. To make these principles actionable, this guide provides detailed implementation blueprints and working code references for three leading agentic frameworks: LangChain (via LangGraph), CrewAI, and AutoGen. Each framework's approach to implementing the P-t-E pattern is analyzed, highlighting unique features like LangGraph's stateful graphs for re-planning, CrewAI's declarative tool scoping for security, and AutoGen's built-in Docker sandboxing. Finally, we discuss advanced patterns, including dynamic re-planning loops, parallel execution with Directed Acyclic Graphs (DAGs), and the critical role of Human-in-the-Loop (HITL) verification, to offer a complete strategic blueprint for architects, developers, and security engineers aiming to build production-grade, resilient, and trustworthy LLM agents.

