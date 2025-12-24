---
layout: default
title: "Automating Modelica Module Generation Using Large Language Models: A Case Study on Building Control Description Language"
---

# Automating Modelica Module Generation Using Large Language Models: A Case Study on Building Control Description Language

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.14623" class="toolbar-btn" target="_blank">📄 arXiv: 2509.14623v1</a>
  <a href="https://arxiv.org/pdf/2509.14623.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.14623v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.14623v1', 'Automating Modelica Module Generation Using Large Language Models: A Case Study on Building Control Description Language')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Hanlong Wan, Xing Lu, Yan Chen, Karthik Devaprasad, Laura Hinkle

**分类**: cs.SE, cs.AI, cs.PL, eess.SY

**发布日期**: 2025-09-18

**备注**: This is the pre-peer-review version of a journal paper; the repo is available at: https://github.com/pnnl/prompt2control

---

## 💡 一句话要点

**利用大语言模型自动化生成Modelica模块，提升建筑控制描述语言开发效率。**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大语言模型` `Modelica` `代码生成` `自动化` `建筑控制` `能源系统` `人机协同` `提示工程`

## 📋 核心要点

1. Modelica控制模块开发耗时且依赖专家知识，现有方法难以满足快速迭代的需求。
2. 利用大语言模型，结合结构化提示、库感知、自动编译和人机协同，实现Modelica模块的自动化生成。
3. 实验表明，该方法能显著减少开发时间（40%-60%），但仍需人工干预以保证代码质量和行为正确性。

## 📝 摘要（中文）

动态能源系统和控制需要先进的建模框架来设计和测试监管和容错策略。Modelica是一种广泛使用的基于方程的语言，但开发控制模块需要大量的人工和专业的知识。本文研究了使用大型语言模型（LLM）来自动化生成建筑Modelica库中的控制描述语言模块。我们开发了一个结构化的工作流程，该流程结合了标准化的提示支架、库感知基础、使用OpenModelica的自动编译以及人机协同评估。实验在四个基本逻辑任务（And、Or、Not和Switch）和五个控制模块（冷却器启用/禁用、旁通阀控制、冷却塔风扇速度、工厂请求和泄压风门控制）上进行。结果表明，GPT 4o在零样本模式下未能生成可执行的Modelica代码，而Claude Sonnet 4通过精心设计的提示，在基本逻辑块上实现了完全成功。对于控制模块，成功率达到83%，失败的输出需要中等程度的人工修复（估计1到8小时）。检索增强生成通常会在模块选择中产生不匹配（例如，And检索为Or），而确定性的硬规则搜索策略避免了这些错误。人工评估也优于AI评估，因为当前的LLM无法评估仿真结果或验证行为正确性。尽管存在这些限制，但LLM辅助的工作流程将每个模块的平均开发时间从10到20小时减少到4到6小时，相当于节省了40%到60%的时间。这些结果突出了LLM辅助Modelica生成的潜力和当前局限性，并指出了预仿真验证、更强的基础和闭环评估方面的未来研究方向。

## 🔬 方法详解

**问题定义**：论文旨在解决Modelica控制模块开发效率低下的问题。现有方法依赖于人工编写，耗时且需要专业的Modelica知识，难以快速适应动态能源系统和控制的需求。

**核心思路**：论文的核心思路是利用大语言模型（LLM）的强大代码生成能力，通过结构化的提示和库感知，自动化生成Modelica控制模块。通过人机协同的方式，弥补LLM在代码正确性和行为验证方面的不足。

**技术框架**：整体流程包括以下几个阶段：1) **提示工程**：设计标准化的提示模板，引导LLM生成Modelica代码。2) **库感知**：利用检索增强生成或硬规则搜索策略，使LLM能够访问和利用现有的Modelica库。3) **自动编译**：使用OpenModelica自动编译生成的代码，检测语法错误。4) **人机协同评估**：人工评估生成的代码，修复错误并验证行为正确性。

**关键创新**：论文的关键创新在于将LLM应用于Modelica模块的自动化生成，并提出了一个结构化的工作流程，结合了提示工程、库感知、自动编译和人机协同。这种方法能够显著提高开发效率，降低对专业知识的依赖。

**关键设计**：论文中，提示工程的设计至关重要，需要精心设计提示模板，明确指定LLM需要生成的代码类型、输入输出和功能描述。库感知的实现方式包括检索增强生成和硬规则搜索，后者避免了模块选择错误。人机协同评估需要人工检查生成的代码，并进行仿真验证，确保代码的正确性和行为符合预期。

## 📊 实验亮点

实验结果表明，使用LLM辅助的工作流程可以将每个模块的平均开发时间从10到20小时减少到4到6小时，相当于节省了40%到60%的时间。Claude Sonnet 4在基本逻辑块上实现了完全成功，控制模块的成功率达到83%。人工评估优于AI评估，能够更准确地评估仿真结果和验证行为正确性。

## 🎯 应用场景

该研究成果可应用于动态能源系统、建筑控制系统等领域，加速控制策略的设计、测试和部署。通过降低Modelica模块开发的门槛，促进更广泛的能源系统建模和仿真，为节能减排提供技术支持。未来可扩展到其他领域，例如机器人控制、电力系统等。

## 📄 摘要（原文）

> Dynamic energy systems and controls require advanced modeling frameworks to design and test supervisory and fault tolerant strategies. Modelica is a widely used equation based language, but developing control modules is labor intensive and requires specialized expertise. This paper examines the use of large language models (LLMs) to automate the generation of Control Description Language modules in the Building Modelica Library as a case study. We developed a structured workflow that combines standardized prompt scaffolds, library aware grounding, automated compilation with OpenModelica, and human in the loop evaluation. Experiments were carried out on four basic logic tasks (And, Or, Not, and Switch) and five control modules (chiller enable/disable, bypass valve control, cooling tower fan speed, plant requests, and relief damper control). The results showed that GPT 4o failed to produce executable Modelica code in zero shot mode, while Claude Sonnet 4 achieved up to full success for basic logic blocks with carefully engineered prompts. For control modules, success rates reached 83 percent, and failed outputs required medium level human repair (estimated one to eight hours). Retrieval augmented generation often produced mismatches in module selection (for example, And retrieved as Or), while a deterministic hard rule search strategy avoided these errors. Human evaluation also outperformed AI evaluation, since current LLMs cannot assess simulation results or validate behavioral correctness. Despite these limitations, the LLM assisted workflow reduced the average development time from 10 to 20 hours down to 4 to 6 hours per module, corresponding to 40 to 60 percent time savings. These results highlight both the potential and current limitations of LLM assisted Modelica generation, and point to future research in pre simulation validation, stronger grounding, and closed loop evaluation.

