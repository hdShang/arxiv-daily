---
layout: default
title: "FASTRIC: Prompt Specification Language for Verifiable LLM Interactions"
---

# FASTRIC: Prompt Specification Language for Verifiable LLM Interactions

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.18940" class="toolbar-btn" target="_blank">📄 arXiv: 2512.18940v1</a>
  <a href="https://arxiv.org/pdf/2512.18940.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.18940v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.18940v1', 'FASTRIC: Prompt Specification Language for Verifiable LLM Interactions')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Wen-Long Jin

**分类**: cs.CL, cs.SE

**发布日期**: 2025-12-22

**备注**: 13 pages, 3 figures. Supplementary materials at https://doi.org/10.17605/OSF.IO/PV6R3

---

## 💡 一句话要点

**FASTRIC：一种用于可验证LLM交互的提示规范语言**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `提示工程` `有限状态机` `多轮交互` `形式化验证` `程序一致性` `规范语言`

## 📋 核心要点

1. 现有大型语言模型在多轮交互中缺乏形式化规范，难以验证其执行是否符合设计意图。
2. FASTRIC通过在提示中显式定义有限状态机，使LLM能够作为智能代理执行规范化的交互行为。
3. 实验表明，模型容量与最佳提示形式化程度之间存在关联，存在一个“金发姑娘区”能实现最佳性能。

## 📝 摘要（中文）

大型语言模型(LLMs)执行复杂的多轮交互协议，但缺乏正式规范来验证执行是否符合设计者的意图。我们引入FASTRIC，一种提示规范语言，它在自然语言提示中显式地表达隐式的有限状态机(FSM)，从而能够通过执行轨迹分析进行一致性验证。LLM充当智能执行代理：解释设计者编码的FSM以执行指定的行为角色。与需要解析器和编译器的符号规范语言不同，FASTRIC利用LLM作为统一的基础设施——同时充当解析器、解释器、运行时环境和开发助手。FASTRIC指导设计者阐明七个FSM元素(最终状态、代理、状态、触发器、角色、初始状态、约束)，从而构建多轮交互。规范的形式化程度——从前沿模型推断的隐式描述到为较弱模型提供的逐步指令——充当设计参数。我们引入程序一致性作为衡量执行是否符合FSM规范的验证指标。在一个包含四个形式化级别和三个模型规模(14.7B、685B、1T+参数)的三状态幼儿园辅导FSM的测试中，结果表明最佳规范形式化程度是模型容量的函数。DeepSeek-V3.2 (685B)在L2-L4级别上实现了完美的一致性(1.00)；ChatGPT-5 (~1T)在L3级别达到峰值(0.90)，然后在L4级别崩溃(0.39)；Phi4 (14.7B)没有显示出稳定的最优值，且方差较高(SD=0.16-0.36)。这些发现揭示了特定于模型的形式化范围——“金发姑娘区”——其中规范提供了足够的结构而没有过度约束，从而建立了提示规范工程，用于创建可验证的交互协议，将多轮交互设计从启发式艺术转变为具有可衡量的程序保证的系统工程。

## 🔬 方法详解

**问题定义**：论文旨在解决大型语言模型（LLMs）在多轮交互中缺乏可验证性的问题。现有的LLM交互设计主要依赖启发式方法，缺乏形式化的规范，导致难以保证LLM的执行符合设计者的意图，也难以进行有效的调试和优化。

**核心思路**：论文的核心思路是利用提示工程，将有限状态机（FSM）的概念融入到自然语言提示中，从而显式地定义LLM在多轮交互中的行为规范。通过这种方式，LLM可以被视为一个智能执行代理，根据预定义的FSM执行交互协议。这种方法避免了传统符号规范语言所需的解析器和编译器，直接利用LLM自身的能力进行解析、解释和执行。

**技术框架**：FASTRIC的技术框架主要包括以下几个部分：1) 提示规范语言：定义了七个FSM元素（最终状态、代理、状态、触发器、角色、初始状态、约束），用于结构化多轮交互。2) 形式化程度：允许设计者根据模型的能力调整提示的详细程度，从隐式描述到显式指令。3) 程序一致性：作为验证指标，衡量LLM的执行轨迹与FSM规范的符合程度。整体流程是：设计者使用FASTRIC定义FSM规范，然后将规范嵌入到提示中，LLM根据提示执行交互，最后通过程序一致性指标评估执行结果。

**关键创新**：FASTRIC的关键创新在于将形式化规范与自然语言提示相结合，利用LLM自身的能力进行规范的解析和执行，从而实现可验证的LLM交互。与传统的符号规范语言相比，FASTRIC更加灵活和易于使用，无需额外的工具链。此外，FASTRIC还提出了程序一致性这一新的验证指标，用于衡量LLM执行的规范性。

**关键设计**：FASTRIC的关键设计包括：1) FSM元素的定义：明确了多轮交互中需要考虑的关键要素，为设计者提供了结构化的指导。2) 形式化程度的控制：允许设计者根据模型的能力调整提示的详细程度，从而实现最佳的性能。3) 程序一致性的计算：定义了如何衡量LLM的执行轨迹与FSM规范的符合程度，为验证LLM的交互行为提供了量化的指标。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.18940v1/deepthink-figure1_fsm_structure.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.18940v1/FASTRIC-figure2_conformance.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.18940v1/FASTRIC-figure3_conformance_boxplots.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

实验结果表明，最佳的提示形式化程度与模型容量有关。DeepSeek-V3.2 (685B)在L2-L4级别上实现了完美的一致性(1.00)，ChatGPT-5 (~1T)在L3级别达到峰值(0.90)，然后在L4级别崩溃(0.39)，Phi4 (14.7B)没有显示出稳定的最优值，且方差较高(SD=0.16-0.36)。这些结果揭示了存在一个模型特定的“金发姑娘区”，在该区域内，规范提供了足够的结构而没有过度约束。

## 🎯 应用场景

FASTRIC可应用于各种需要可验证多轮交互的场景，例如智能客服、教育辅导、任务导向对话系统等。通过FASTRIC，开发者可以更加可靠地控制LLM的行为，减少意外情况的发生，并提高交互系统的稳定性和可预测性。未来，FASTRIC有望推动LLM在安全敏感领域的应用，例如医疗诊断、金融服务等。

## 📄 摘要（原文）

> Large Language Models (LLMs) execute complex multi-turn interaction protocols but lack formal specifications to verify execution against designer intent. We introduce FASTRIC, a Prompt Specification Language that makes implicit Finite State Machines (FSMs) explicit in natural language prompts, enabling conformance verification through execution trace analysis. The LLM serves as intelligent execution agent: interpreting designer-encoded FSMs to execute specified behavioral roles. Unlike symbolic specification languages requiring parsers and compilers, FASTRIC leverages LLMs as unified infrastructure-simultaneously parser, interpreter, runtime environment, and development assistant. FASTRIC guides designers to articulate seven FSM elements (Final States, Agents, States, Triggers, Roles, Initial State, Constraints) structuring multi-turn interactions. Specification formality-ranging from implicit descriptions that frontier models infer to explicit step-by-step instructions for weaker models-serves as a design parameter. We introduce procedural conformance as verification metric measuring execution adherence to FSM specifications. Testing a 3-state kindergarten tutoring FSM across four formality levels and three model scales (14.7B, 685B, 1T+ parameters) reveals optimal specification formality is a function of model capacity. DeepSeek-V3.2 (685B) achieves perfect conformance (1.00) at L2-L4; ChatGPT-5 (~1T) peaks at L3 (0.90) before collapsing at L4 (0.39); Phi4 (14.7B) shows no stable optimum with high variance (SD=0.16-0.36). These findings reveal model-specific formality ranges-"Goldilocks zones"-where specifications provide sufficient structure without over-constraint, establishing Prompt Specification Engineering for creating verifiable interaction protocols, transforming multi-turn interaction design from heuristic art to systematic engineering with measurable procedural guarantees.

