---
layout: default
title: "MATP-BENCH: Can MLLM Be a Good Automated Theorem Prover for Multimodal Problems?"
---

# MATP-BENCH: Can MLLM Be a Good Automated Theorem Prover for Multimodal Problems?

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.06034" class="toolbar-btn" target="_blank">📄 arXiv: 2506.06034v1</a>
  <a href="https://arxiv.org/pdf/2506.06034.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.06034v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.06034v1', 'MATP-BENCH: Can MLLM Be a Good Automated Theorem Prover for Multimodal Problems?')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Zhitao He, Zongwei Lyu, Dazhong Chen, Dadi Guo, Yi R. Fung

**分类**: cs.CL

**发布日期**: 2025-06-06

**备注**: 29 pages

---

## 💡 一句话要点

**提出MATP-BENCH以评估多模态大语言模型在自动定理证明中的能力**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多模态大语言模型` `自动定理证明` `数学问题` `基准评估` `视觉推理` `形式化语言` `机器学习`

## 📋 核心要点

1. 现有方法在多模态定理证明领域的能力有限，无法有效解决复杂的多模态数学问题。
2. 论文提出MATP-BENCH基准，旨在评估多模态大语言模型在自动定理证明中的表现，涵盖多种数学层次和形式化语言。
3. 实验结果显示，现有模型在MATP-BENCH上的表现不佳，表明该基准为未来的研究提供了重要挑战和方向。

## 📝 摘要（中文）

许多定理，特别是在几何学中，常以多模态形式呈现（如图示）。人类在这种情况下通过视觉推理获得直觉并指导证明过程。现代多模态大语言模型（MLLMs）在解决各种数学问题方面表现出色，但作为自动定理证明器（ATPs）的潜力仍未得到充分探索。本文提出了多模态自动定理证明基准（MATP-BENCH），这是一个新的多模态、多层次和多语言的基准，旨在评估MLLMs在这一角色中的表现。MATP-BENCH包含1056个来自高中、大学及竞赛级别的多模态定理，所有问题均附有Lean 4、Coq和Isabelle的形式化描述，使基准与多种定理证明框架兼容。该基准要求模型将复杂的视觉理解与广泛的数学知识和严谨的符号推理相结合，以生成正式证明。我们利用MATP-BENCH评估多种先进的多模态语言模型，现有方法仅能解决有限数量的问题，表明该基准为自动定理证明研究提出了开放挑战。

## 🔬 方法详解

**问题定义**：本文旨在解决多模态定理证明中的评估问题，现有方法在处理复杂的多模态数学问题时表现不足，无法有效整合视觉信息与数学推理。

**核心思路**：论文的核心思路是构建MATP-BENCH基准，通过提供多模态定理及其形式化描述，评估MLLMs在自动定理证明中的能力，促进该领域的研究进展。

**技术框架**：MATP-BENCH的整体架构包括三个主要模块：多模态定理生成、形式化描述生成和模型评估。每个模块相互关联，确保模型能够处理多种输入形式并生成有效的证明。

**关键创新**：最重要的技术创新在于引入了一个综合性的基准，涵盖多种数学层次和形式化语言，使得MLLMs在多模态定理证明中的应用得以系统评估，这在现有研究中尚属首次。

**关键设计**：在设计中，论文使用了Lean 4、Coq和Isabelle等多种形式化语言，确保基准的广泛适用性。同时，模型需要在视觉理解和符号推理之间建立有效的联系，以生成准确的证明。

## 📊 实验亮点

实验结果表明，现有的多模态语言模型在MATP-BENCH上的解决能力有限，能够成功解决的问题仅占基准的少数。这一发现突显了MATP-BENCH作为一个开放挑战的重要性，并为未来的研究指明了方向。

## 🎯 应用场景

该研究的潜在应用领域包括教育、自动化证明系统以及数学软件开发。通过提高多模态大语言模型在定理证明中的能力，可以为数学教育提供更智能的辅助工具，并推动自动化定理证明技术的发展，具有重要的实际价值和未来影响。

## 📄 摘要（原文）

> Numerous theorems, such as those in geometry, are often presented in multimodal forms (e.g., diagrams). Humans benefit from visual reasoning in such settings, using diagrams to gain intuition and guide the proof process. Modern Multimodal Large Language Models (MLLMs) have demonstrated remarkable capabilities in solving a wide range of mathematical problems. However, the potential of MLLMs as Automated Theorem Provers (ATPs), specifically in the multimodal domain, remains underexplored. In this paper, we introduce the Multimodal Automated Theorem Proving benchmark (MATP-BENCH), a new Multimodal, Multi-level, and Multi-language benchmark designed to evaluate MLLMs in this role as multimodal automated theorem provers. MATP-BENCH consists of 1056 multimodal theorems drawn from high school, university, and competition-level mathematics. All these multimodal problems are accompanied by formalizations in Lean 4, Coq and Isabelle, thus making the benchmark compatible with a wide range of theorem-proving frameworks. MATP-BENCH requires models to integrate sophisticated visual understanding with mastery of a broad spectrum of mathematical knowledge and rigorous symbolic reasoning to generate formal proofs. We use MATP-BENCH to evaluate a variety of advanced multimodal language models. Existing methods can only solve a limited number of the MATP-BENCH problems, indicating that this benchmark poses an open challenge for research on automated theorem proving.

