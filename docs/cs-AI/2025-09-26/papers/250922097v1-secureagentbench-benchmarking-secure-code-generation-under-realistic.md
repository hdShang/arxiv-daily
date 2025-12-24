---
layout: default
title: "SecureAgentBench: Benchmarking Secure Code Generation under Realistic Vulnerability Scenarios"
---

# SecureAgentBench: Benchmarking Secure Code Generation under Realistic Vulnerability Scenarios

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.22097" class="toolbar-btn" target="_blank">📄 arXiv: 2509.22097v1</a>
  <a href="https://arxiv.org/pdf/2509.22097.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.22097v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.22097v1', 'SecureAgentBench: Benchmarking Secure Code Generation under Realistic Vulnerability Scenarios')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Junkai Chen, Huihui Huang, Yunbo Lyu, Junwen An, Jieke Shi, Chengran Yang, Ting Zhang, Haoye Tian, Yikun Li, Zhenhao Li, Xin Zhou, Xing Hu, David Lo

**分类**: cs.SE, cs.AI, cs.CL, cs.CR

**发布日期**: 2025-09-26

---

## 💡 一句话要点

**SecureAgentBench：在真实漏洞场景下评估代码Agent的安全代码生成能力**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `代码生成` `安全漏洞` `大型语言模型` `基准测试` `软件安全`

## 📋 核心要点

1. 现有代码生成基准测试忽略了漏洞引入的真实上下文，且评估协议无法全面捕捉功能正确性和新引入的漏洞。
2. SecureAgentBench通过构建包含真实漏洞场景的105个编码任务，全面评估代码Agent的安全代码生成能力。
3. 实验结果表明，现有代码Agent难以生成安全代码，即使添加安全指令也无法显著提高安全编码能力。

## 📝 摘要（中文）

大型语言模型（LLM）驱动的代码Agent正在通过自动化测试、调试和修复等任务迅速改变软件工程，但其生成的代码的安全风险已成为一个关键问题。现有的基准测试提供了一些有价值的见解，但仍然不足：它们常常忽略了漏洞引入的真实上下文，或者采用狭隘的评估协议，无法捕捉功能正确性或新引入的漏洞。因此，我们引入了SecureAgentBench，这是一个包含105个编码任务的基准，旨在严格评估代码Agent在安全代码生成方面的能力。每个任务包括（i）需要大型存储库中多文件编辑的真实任务设置，（ii）基于真实世界开源漏洞并精确识别引入点的对齐上下文，以及（iii）结合功能测试、通过概念验证漏洞利用进行漏洞检查以及使用静态分析检测新引入漏洞的综合评估。我们评估了三个具有代表性的Agent（SWE-agent、OpenHands和Aider）以及三个最先进的LLM（Claude 3.7 Sonnet、GPT-4.1和DeepSeek-V3.1）。结果表明：（i）当前的Agent难以生成安全代码，即使是性能最佳的SWE-agent（由DeepSeek-V3.1支持）也仅实现了15.2%的正确且安全的解决方案，（ii）一些Agent生成了功能正确的代码，但仍然引入了漏洞，包括以前未记录的新漏洞，以及（iii）为Agent添加明确的安全指令并不能显著提高安全编码能力，这突显了进一步研究的必要性。这些发现将SecureAgentBench确立为一个严格的安全代码生成基准，也是利用LLM实现更可靠软件开发的一步。

## 🔬 方法详解

**问题定义**：现有代码生成基准测试在评估代码Agent的安全性时存在不足，主要体现在无法模拟真实漏洞引入的上下文，并且评估指标不够全面，难以同时衡量功能正确性和安全性。现有方法难以有效识别和避免代码Agent生成含有漏洞的代码，阻碍了LLM在软件开发中的安全应用。

**核心思路**：SecureAgentBench的核心思路是构建一个更贴近真实软件开发场景的基准测试，包含真实的漏洞引入上下文，并采用更全面的评估方法，从而更准确地评估代码Agent的安全代码生成能力。通过提供包含真实漏洞的任务，可以促使Agent学习如何避免引入类似漏洞，并提高其生成安全代码的能力。

**技术框架**：SecureAgentBench包含以下几个主要组成部分：1) 105个编码任务，每个任务都基于真实开源项目的漏洞，并包含漏洞引入点的精确信息；2) 真实的任务设置，要求Agent在大型代码仓库中进行多文件编辑；3) 综合评估方法，包括功能测试、漏洞验证（通过概念验证漏洞利用）和静态分析，以检测新引入的漏洞。该框架旨在全面评估Agent在真实场景下的安全代码生成能力。

**关键创新**：SecureAgentBench的关键创新在于其真实性和全面性。它不是基于人工合成的漏洞，而是基于真实开源项目的漏洞，从而更贴近实际软件开发场景。此外，它采用综合评估方法，不仅关注功能正确性，还关注漏洞的存在和新漏洞的引入，从而更全面地评估代码Agent的安全性。

**关键设计**：SecureAgentBench的关键设计包括：1) 任务选择：选择具有代表性的开源项目和漏洞，确保任务的多样性和挑战性；2) 上下文对齐：精确识别漏洞引入点，并提供相关的代码上下文，帮助Agent理解漏洞的根源；3) 评估指标：采用多种评估指标，包括功能测试的通过率、漏洞验证的成功率和静态分析的告警数量，从而全面评估Agent的性能。

## 📊 实验亮点

实验结果表明，即使是最先进的代码Agent在SecureAgentBench上的表现仍然不尽如人意，最佳Agent（SWE-agent + DeepSeek-V3.1）的正确且安全解决方案的比例仅为15.2%。此外，实验还发现，一些Agent虽然能够生成功能正确的代码，但仍然会引入漏洞，甚至包括新的漏洞。添加明确的安全指令并不能显著提高安全编码能力。

## 🎯 应用场景

SecureAgentBench可用于评估和改进各种代码Agent的安全代码生成能力，从而提高软件开发的安全性。该基准测试可以帮助研究人员开发更安全的LLM驱动的软件开发工具，并促进LLM在安全关键型应用中的应用。此外，该基准测试还可以用于培训代码Agent，使其能够更好地识别和避免引入漏洞。

## 📄 摘要（原文）

> Large language model (LLM) powered code agents are rapidly transforming software engineering by automating tasks such as testing, debugging, and repairing, yet the security risks of their generated code have become a critical concern. Existing benchmarks have offered valuable insights but remain insufficient: they often overlook the genuine context in which vulnerabilities were introduced or adopt narrow evaluation protocols that fail to capture either functional correctness or newly introduced vulnerabilities. We therefore introduce SecureAgentBench, a benchmark of 105 coding tasks designed to rigorously evaluate code agents' capabilities in secure code generation. Each task includes (i) realistic task settings that require multi-file edits in large repositories, (ii) aligned contexts based on real-world open-source vulnerabilities with precisely identified introduction points, and (iii) comprehensive evaluation that combines functionality testing, vulnerability checking through proof-of-concept exploits, and detection of newly introduced vulnerabilities using static analysis. We evaluate three representative agents (SWE-agent, OpenHands, and Aider) with three state-of-the-art LLMs (Claude 3.7 Sonnet, GPT-4.1, and DeepSeek-V3.1). Results show that (i) current agents struggle to produce secure code, as even the best-performing one, SWE-agent supported by DeepSeek-V3.1, achieves merely 15.2% correct-and-secure solutions, (ii) some agents produce functionally correct code but still introduce vulnerabilities, including new ones not previously recorded, and (iii) adding explicit security instructions for agents does not significantly improve secure coding, underscoring the need for further research. These findings establish SecureAgentBench as a rigorous benchmark for secure code generation and a step toward more reliable software development with LLMs.

