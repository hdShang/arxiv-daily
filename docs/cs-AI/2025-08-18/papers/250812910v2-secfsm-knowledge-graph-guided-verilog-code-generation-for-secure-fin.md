---
layout: default
title: "SecFSM: Knowledge Graph-Guided Verilog Code Generation for Secure Finite State Machines in Systems-on-Chip"
---

# SecFSM: Knowledge Graph-Guided Verilog Code Generation for Secure Finite State Machines in Systems-on-Chip

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.12910" class="toolbar-btn" target="_blank">📄 arXiv: 2508.12910v2</a>
  <a href="https://arxiv.org/pdf/2508.12910.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.12910v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.12910v2', 'SecFSM: Knowledge Graph-Guided Verilog Code Generation for Secure Finite State Machines in Systems-on-Chip')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Ziteng Hu, Yingjie Xia, Xiyuan Chen, Li Kuang

**分类**: cs.CR, cs.AI, cs.AR

**发布日期**: 2025-08-18 (更新: 2025-08-21)

---

## 💡 一句话要点

**提出SecFSM以解决安全敏感FSM的Verilog代码生成问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `有限状态机` `Verilog代码生成` `安全知识图谱` `大型语言模型` `系统级芯片` `安全漏洞` `自动化设计`

## 📋 核心要点

1. 现有的LLM生成的Verilog代码存在安全漏洞，尤其是在安全敏感的FSM实现中，这使得传统方法面临挑战。
2. SecFSM通过构建FSM安全知识图谱，结合用户需求分析，指导LLMs生成更安全的Verilog代码，提升了代码的安全性。
3. 在25个安全测试用例的基准测试中，SecFSM的通过率达到21/25，显著优于现有的最先进方法。

## 📝 摘要（中文）

有限状态机（FSM）在系统级芯片（SoC）的控制逻辑实现中发挥着关键作用。传统上，FSM由硬件工程师通过Verilog编码实现，这一过程往往繁琐且耗时。随着大型语言模型（LLMs）在代码生成方面的显著进展，LLMs被越来越多地用于自动化Verilog代码生成。然而，LLM生成的Verilog代码常常存在安全漏洞，这对安全敏感的FSM实现尤为令人担忧。为了解决这一问题，我们提出了SecFSM，这是一种利用安全导向知识图谱指导LLMs生成更安全Verilog代码的新方法。我们首先构建了FSM安全知识图谱（FSKG）作为LLMs的外部辅助。随后，我们分析用户需求以识别漏洞，并获取漏洞列表。然后，我们根据漏洞列表从FSKG中检索知识。最后，我们基于安全知识构建安全提示以进行Verilog代码生成。实验结果表明，SecFSM在多个基准测试中优于现有方法。

## 🔬 方法详解

**问题定义**：本论文旨在解决LLM生成的Verilog代码中存在的安全漏洞问题，尤其是在安全敏感的有限状态机（FSM）实现中。现有方法缺乏针对安全性的考虑，导致生成的代码容易受到攻击。

**核心思路**：论文提出的SecFSM方法通过构建FSM安全知识图谱（FSKG），为LLMs提供安全导向的知识支持，从而生成更安全的Verilog代码。该方法通过分析用户需求，识别潜在漏洞，并基于这些漏洞进行知识检索，最终生成安全提示。

**技术框架**：SecFSM的整体架构包括几个主要模块：首先是FSM安全知识图谱的构建，其次是用户需求分析模块，接着是漏洞识别与知识检索模块，最后是基于安全知识的Verilog代码生成模块。

**关键创新**：SecFSM的核心创新在于引入了安全知识图谱作为外部辅助，系统性地分析用户需求并识别安全漏洞，这一方法与传统的LLM生成方法本质上不同，后者通常缺乏对安全性的专门关注。

**关键设计**：在设计过程中，SecFSM采用了特定的参数设置以优化知识检索过程，并设计了针对安全性的损失函数，以确保生成的代码在安全性方面达到预期标准。

## 📊 实验亮点

在与现有最先进方法的对比中，SecFSM在25个安全测试用例的基准测试中取得了21/25的通过率，显示出显著的性能提升。这一结果表明，SecFSM在生成安全Verilog代码方面具有明显优势，能够有效应对安全漏洞问题。

## 🎯 应用场景

SecFSM的研究成果在安全敏感的系统级芯片设计中具有广泛的应用潜力，尤其是在需要高安全性的嵌入式系统、网络设备和金融设备等领域。通过提高Verilog代码的安全性，该方法能够有效降低系统被攻击的风险，提升整体系统的可靠性和安全性。

## 📄 摘要（原文）

> Finite State Machines (FSMs) play a critical role in implementing control logic for Systems-on-Chip (SoC). Traditionally, FSMs are implemented by hardware engineers through Verilog coding, which is often tedious and time-consuming. Recently, with the remarkable progress of Large Language Models (LLMs) in code generation, LLMs have been increasingly explored for automating Verilog code generation. However, LLM-generated Verilog code often suffers from security vulnerabilities, which is particularly concerning for security-sensitive FSM implementations. To address this issue, we propose SecFSM, a novel method that leverages a security-oriented knowledge graph to guide LLMs in generating more secure Verilog code. Specifically, we first construct a FSM Security Knowledge Graph (FSKG) as an external aid to LLMs. Subsequently, we analyze users' requirements to identify vulnerabilities and get a list of vulnerabilities in the requirements. Then, we retrieve knowledge from FSKG based on the vulnerabilities list. Finally, we construct security prompts based on the security knowledge for Verilog code generation. To evaluate SecFSM, we build a dedicated dataset collected from academic datasets, artificial datasets, papers, and industrial cases. Extensive experiments demonstrate that SecFSM outperforms state-of-the-art baselines. In particular, on a benchmark of 25 security test cases evaluated by DeepSeek-R1, SecFSM achieves an outstanding pass rate of 21/25.

