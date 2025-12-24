---
layout: default
title: "SEC-bench: Automated Benchmarking of LLM Agents on Real-World Software Security Tasks"
---

# SEC-bench: Automated Benchmarking of LLM Agents on Real-World Software Security Tasks

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.11791" class="toolbar-btn" target="_blank">📄 arXiv: 2506.11791v2</a>
  <a href="https://arxiv.org/pdf/2506.11791.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.11791v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.11791v2', 'SEC-bench: Automated Benchmarking of LLM Agents on Real-World Software Security Tasks')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Hwiwon Lee, Ziqi Zhang, Hanxiao Lu, Lingming Zhang

**分类**: cs.LG, cs.CR

**发布日期**: 2025-06-13 (更新: 2025-10-22)

---

## 💡 一句话要点

**提出SEC-bench以解决LLM代理在软件安全任务中的评估问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `软件安全` `自动化评估` `漏洞检测` `补丁生成`

## 📋 核心要点

1. 现有的LLM代理评估方法主要依赖合成数据，无法真实反映软件安全工程中的复杂性和挑战。
2. SEC-bench框架通过自动构建代码库和重现漏洞，提供了一个全面的评估LLM代理在真实安全任务中的能力的方法。
3. 在使用SEC-bench进行的评估中，LLM代理在概念验证生成和漏洞修补任务中的成功率分别仅为18.0%和34.0%，显示出显著的性能差距。

## 📝 摘要（中文）

对大型语言模型（LLM）代理进行严格的安全评估对于确保其在软件开发生命周期中的安全部署至关重要。然而，现有基准测试主要依赖于合成挑战或简化的漏洞数据集，无法捕捉安全工程师在实际工作中遇到的复杂性和模糊性。我们提出SEC-bench，这是第一个完全自动化的基准测试框架，用于评估LLM代理在真实安全工程任务中的表现。SEC-bench采用一种新颖的多代理框架，自动构建代码库，重现漏洞，并生成高质量的补丁以进行可靠评估。使用SEC-bench，我们实施了两个关键的软件安全任务，结果显示现有LLM代码代理在这些任务中的表现存在显著差距。

## 🔬 方法详解

**问题定义**：本论文旨在解决现有LLM代理在软件安全任务评估中的不足，尤其是缺乏真实世界复杂性和模糊性的挑战。现有方法往往依赖于合成数据，无法有效评估LLM在实际应用中的表现。

**核心思路**：我们提出SEC-bench，一个自动化的基准测试框架，能够在真实的安全工程任务中评估LLM代理的能力。通过自动构建代码库和重现漏洞，SEC-bench提供了一个可靠的评估环境。

**技术框架**：SEC-bench的整体架构包括多个模块：自动构建代码库、漏洞重现、生成高质量补丁和评估LLM代理的能力。每个模块协同工作，以确保评估的全面性和准确性。

**关键创新**：SEC-bench的主要创新在于其完全自动化的特性和多代理框架设计，使得评估过程高效且可重复。这与传统方法的手动评估方式形成鲜明对比。

**关键设计**：在设计中，我们关注于高质量漏洞数据集的生成，确保每个实例的成本仅为0.87美元。此外，评估过程中采用了标准化的评估指标，以确保结果的可靠性和可比性。

## 📊 实验亮点

在SEC-bench的评估中，现有的LLM代码代理在概念验证生成任务中的成功率仅为18.0%，而在漏洞修补任务中为34.0%。这些结果表明，当前技术在实际应用中仍存在显著的性能差距，强调了进一步研究和改进的必要性。

## 🎯 应用场景

SEC-bench的研究成果具有广泛的应用潜力，特别是在软件安全领域。它可以帮助开发者和安全工程师更好地评估和选择LLM代理，从而提高软件开发过程中的安全性和效率。未来，该框架还可以扩展到其他领域的自动化评估，推动智能系统的安全应用。

## 📄 摘要（原文）

> Rigorous security-focused evaluation of large language model (LLM) agents is imperative for establishing trust in their safe deployment throughout the software development lifecycle. However, existing benchmarks largely rely on synthetic challenges or simplified vulnerability datasets that fail to capture the complexity and ambiguity encountered by security engineers in practice. We introduce SEC-bench, the first fully automated benchmarking framework for evaluating LLM agents on authentic security engineering tasks. SEC-bench employs a novel multi-agent scaffold that automatically constructs code repositories with harnesses, reproduces vulnerabilities in isolated environments, and generates gold patches for reliable evaluation. Our framework automatically creates high-quality software vulnerability datasets with reproducible artifacts at a cost of only $0.87 per instance. Using SEC-bench, we implement two critical software security tasks to rigorously evaluate LLM agents' capabilities: proof-of-concept (PoC) generation and vulnerability patching. A comprehensive evaluation of state-of-the-art LLM code agents reveals significant performance gaps, achieving at most 18.0% success in PoC generation and 34.0% in vulnerability patching on our complete dataset. These results highlight the crucial steps needed toward developing LLM agents that are more practical, intelligent, and autonomous for security engineering.

