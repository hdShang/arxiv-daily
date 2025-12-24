---
layout: default
title: "From Legacy to Standard: LLM-Assisted Transformation of Cybersecurity Playbooks into CACAO Format"
---

# From Legacy to Standard: LLM-Assisted Transformation of Cybersecurity Playbooks into CACAO Format

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.03342" class="toolbar-btn" target="_blank">📄 arXiv: 2508.03342v1</a>
  <a href="https://arxiv.org/pdf/2508.03342.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.03342v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.03342v1', 'From Legacy to Standard: LLM-Assisted Transformation of Cybersecurity Playbooks into CACAO Format')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Mehdi Akbari Gurabi, Lasse Nitz, Radu-Mihai Castravet, Roman Matzutt, Avikarsha Mandal, Stefan Decker

**分类**: cs.CR, cs.AI

**发布日期**: 2025-08-05

**备注**: 20 pages, including appendices, 32 references, 4 tables, 7 main figures (some of them has sub-figures)

---

## 💡 一句话要点

**提出基于大语言模型的自动化网络安全剧本转化方法**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `网络安全` `大语言模型` `提示工程` `自动化转换` `CACAO格式` `事件响应` `语法检查`

## 📋 核心要点

1. 现有的网络安全剧本格式多样且不可机器读取，导致自动化和互操作性受限。
2. 本文提出利用大语言模型和提示工程自动将传统剧本转换为CACAO格式，提升转换效率和准确性。
3. 实验表明，该方法在准确性上显著优于基线模型，有效捕捉复杂工作流并减少错误。

## 📝 摘要（中文）

现有的网络安全剧本通常采用异构且不可机器读取的格式，这限制了其在安全编排、自动化和响应平台中的自动化和互操作性。本文探讨了结合提示工程的大语言模型在将传统事件响应剧本自动转换为标准化的机器可读CACAO格式中的适用性。我们系统地研究了各种提示工程技术，并精心设计了旨在最大化语法准确性和语义保真度的提示，以保持控制流的完整性。我们的模块化转换管道集成了语法检查器，以确保语法正确性，并具有迭代优化机制，逐步减少语法错误。实验结果表明，我们的方法显著提高了剧本转换的准确性，有效捕捉复杂的工作流结构，并大幅减少错误，展示了在自动化网络安全剧本转换任务中的实际应用潜力。

## 🔬 方法详解

**问题定义**：本文旨在解决现有网络安全剧本格式异构且不可机器读取的问题，这导致其在自动化和互操作性方面的局限性。

**核心思路**：通过结合大语言模型和提示工程，自动将传统事件响应剧本转换为标准化的CACAO格式，以提高转换的准确性和效率。

**技术框架**：整体架构包括多个模块：首先是提示设计模块，针对不同剧本设计优化提示；其次是语法检查模块，确保生成内容的语法正确；最后是迭代优化模块，通过反馈机制逐步减少语法错误。

**关键创新**：最重要的创新在于将大语言模型与提示工程相结合，形成了一种新的自动化转换方法，显著提高了剧本转换的准确性和复杂工作流的捕捉能力。

**关键设计**：在提示设计中，采用了多种提示工程技术，确保语法和语义的准确性；语法检查器的集成确保了生成内容的质量；迭代优化机制则通过反馈循环不断改进生成结果。

## 📊 实验亮点

实验结果显示，提出的方法在剧本转换的准确性上显著优于基线模型，具体提升幅度达到XX%。此外，该方法有效捕捉了复杂的工作流结构，减少了语法错误，展示了其在实际应用中的潜力。

## 🎯 应用场景

该研究的潜在应用领域包括网络安全事件响应、自动化安全编排和安全管理平台。通过将传统剧本转化为标准化格式，能够提高安全响应的效率和准确性，降低人工干预的需求，进而提升整体安全防护能力。未来，该方法可能在更广泛的安全领域得到应用，推动自动化技术的发展。

## 📄 摘要（原文）

> Existing cybersecurity playbooks are often written in heterogeneous, non-machine-readable formats, which limits their automation and interoperability across Security Orchestration, Automation, and Response platforms. This paper explores the suitability of Large Language Models, combined with Prompt Engineering, to automatically translate legacy incident response playbooks into the standardized, machine-readable CACAO format. We systematically examine various Prompt Engineering techniques and carefully design prompts aimed at maximizing syntactic accuracy and semantic fidelity for control flow preservation. Our modular transformation pipeline integrates a syntax checker to ensure syntactic correctness and features an iterative refinement mechanism that progressively reduces syntactic errors. We evaluate the proposed approach on a custom-generated dataset comprising diverse legacy playbooks paired with manually created CACAO references. The results demonstrate that our method significantly improves the accuracy of playbook transformation over baseline models, effectively captures complex workflow structures, and substantially reduces errors. It highlights the potential for practical deployment in automated cybersecurity playbook transformation tasks.

