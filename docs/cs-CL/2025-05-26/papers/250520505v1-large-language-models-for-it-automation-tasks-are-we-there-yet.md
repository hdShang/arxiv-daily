---
layout: default
title: "Large Language Models for IT Automation Tasks: Are We There Yet?"
---

# Large Language Models for IT Automation Tasks: Are We There Yet?

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.20505" class="toolbar-btn" target="_blank">📄 arXiv: 2505.20505v1</a>
  <a href="https://arxiv.org/pdf/2505.20505.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.20505v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.20505v1', 'Large Language Models for IT Automation Tasks: Are We There Yet?')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Md Mahadi Hassan, John Salvador, Akond Rahman, Santu Karmaker

**分类**: cs.CL, cs.SE

**发布日期**: 2025-05-26

**备注**: 8 pages

---

## 💡 一句话要点

**提出ITAB基准以评估LLM在IT自动化任务中的表现**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `IT自动化` `Ansible` `基准测试` `状态协调` `语义错误` `执行知识`

## 📋 核心要点

1. 现有的LLMs在IT自动化任务中的应用效果不佳，尤其是在实际工具如Ansible的使用场景中。
2. 本文提出ITAB基准，专注于评估LLMs在生成Ansible自动化脚本时的能力，涵盖多样化的实际任务。
3. 实验结果显示，14个开源LLMs的pass@10表现均未超过12%，揭示了其在状态推理和模块知识应用方面的不足。

## 📝 摘要（中文）

大型语言模型（LLMs）在代码生成方面展现出潜力，但其在IT自动化任务中的有效性，尤其是针对Ansible等工具，仍未得到充分研究。现有基准主要依赖合成任务，无法满足实际从业者的需求。本文提出了ITAB（IT自动化任务基准），涵盖126个多样化任务（如服务器配置、文件管理），每个任务都考虑状态协调这一IT自动化工具的独特属性。ITAB通过在受控环境中动态执行，评估LLMs生成功能性Ansible自动化脚本的能力。我们评估了14个开源LLMs，发现其在pass@10的表现均未超过12%。通过分析1411次执行失败，识别出两类主要的语义错误：状态协调相关推理失败和模块特定执行知识不足。研究表明，开源LLMs在状态变化跟踪和应用专业模块知识方面存在关键限制，可靠的IT自动化需要在状态推理和领域特定执行理解上取得重大进展。

## 🔬 方法详解

**问题定义**：本文旨在解决现有LLMs在IT自动化任务中表现不佳的问题，尤其是它们在生成Ansible脚本时的有效性不足。现有方法主要依赖合成任务，无法真实反映从业者的需求。

**核心思路**：论文提出ITAB基准，通过126个多样化的实际任务来评估LLMs的能力，特别关注状态协调这一IT自动化工具的独特需求。

**技术框架**：ITAB基准的整体架构包括任务定义、动态执行和结果评估三个主要模块。每个任务都经过精心设计，以确保涵盖实际应用中的各种情况。

**关键创新**：最重要的创新在于引入状态协调的概念，使得评估更加贴近实际应用场景，填补了现有基准的空白。

**关键设计**：在实验中，使用了动态执行环境来测试生成的脚本，并分析了1411次执行失败的原因，识别出状态协调和模块知识的不足。

## 📊 实验亮点

实验结果显示，14个开源LLMs在IT自动化任务中的pass@10表现均未超过12%。通过对1411次执行失败的分析，发现44.87%的错误与状态协调相关推理失败有关，24.37%的错误源于模块特定执行知识的不足，揭示了LLMs在实际应用中的关键限制。

## 🎯 应用场景

该研究的潜在应用领域包括IT运维、自动化部署和系统管理等。通过提升LLMs在IT自动化任务中的表现，可以显著提高运维效率，降低人为错误，推动智能化运维的发展。未来，随着技术的进步，LLMs有望在更广泛的自动化场景中发挥作用。

## 📄 摘要（原文）

> LLMs show promise in code generation, yet their effectiveness for IT automation tasks, particularly for tools like Ansible, remains understudied. Existing benchmarks rely primarily on synthetic tasks that fail to capture the needs of practitioners who use IT automation tools, such as Ansible. We present ITAB (IT Automation Task Benchmark), a benchmark of 126 diverse tasks (e.g., configuring servers, managing files) where each task accounts for state reconciliation: a property unique to IT automation tools. ITAB evaluates LLMs' ability to generate functional Ansible automation scripts via dynamic execution in controlled environments. We evaluate 14 open-source LLMs, none of which accomplish pass@10 at a rate beyond 12%. To explain these low scores, we analyze 1,411 execution failures across the evaluated LLMs and identify two main categories of prevalent semantic errors: failures in state reconciliation related reasoning (44.87% combined from variable (11.43%), host (11.84%), path(11.63%), and template (9.97%) issues) and deficiencies in module-specific execution knowledge (24.37% combined from Attribute and parameter (14.44%) and module (9.93%) errors). Our findings reveal key limitations in open-source LLMs' ability to track state changes and apply specialized module knowledge, indicating that reliable IT automation will require major advances in state reasoning and domain-specific execution understanding.

