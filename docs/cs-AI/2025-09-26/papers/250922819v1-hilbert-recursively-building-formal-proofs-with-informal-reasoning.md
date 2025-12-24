---
layout: default
title: "Hilbert: Recursively Building Formal Proofs with Informal Reasoning"
---

# Hilbert: Recursively Building Formal Proofs with Informal Reasoning

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.22819" class="toolbar-btn" target="_blank">📄 arXiv: 2509.22819v1</a>
  <a href="https://arxiv.org/pdf/2509.22819.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.22819v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.22819v1', 'Hilbert: Recursively Building Formal Proofs with Informal Reasoning')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Sumanth Varambally, Thomas Voice, Yanchao Sun, Zhifeng Chen, Rose Yu, Ke Ye

**分类**: cs.AI, cs.FL, cs.LG

**发布日期**: 2025-09-26

---

## 💡 一句话要点

**Hilbert：结合非形式推理与形式验证，递归构建数学证明**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `形式化验证` `定理证明` `大型语言模型` `递归分解` `数学推理`

## 📋 核心要点

1. 现有证明器LLM在解决数学问题方面能力不足，远低于通用LLM的水平，难以生成可验证的数学证明。
2. Hilbert框架结合非形式推理和形式验证，利用递归分解将复杂问题拆解为子目标，分别由推理器或证明器LLM解决。
3. 实验表明，Hilbert在miniF2F和PutnamBench等基准测试中显著优于现有方法，大幅提升了问题解决的成功率。

## 📝 摘要（中文）

大型语言模型（LLMs）在数学推理方面表现出色，但其解决方案常包含无法自动验证的错误。形式化定理证明系统（如Lean 4）提供完全精确的自动验证，这促使人们构建专门的证明器LLM，以生成形式语言的可验证证明。然而，存在一个显著差距：当前证明器LLM解决的问题远少于在自然语言中运行的通用LLM。我们引入Hilbert，一个agent框架，通过结合非形式推理和形式验证的互补优势来弥合这一差距。我们的系统协调四个组件：擅长数学推理的非形式LLM、针对Lean 4策略优化的专用证明器LLM、形式验证器和语义定理检索器。对于证明器无法解决的问题，Hilbert采用递归分解将其分解为子目标，并使用证明器或推理器LLM解决这些子目标。它利用验证器的反馈来根据需要改进不正确的证明。实验结果表明，Hilbert在关键基准测试中显著优于现有方法，在miniF2F上达到99.2%，比最佳公开方法高出6.6个百分点。Hilbert在PutnamBench上取得了已知的最佳结果，解决了660个问题中的462个（70.0%），优于SeedProver等专有方法（50.4%），并且比最佳公开基线提高了422%。因此，Hilbert有效地缩小了非形式推理和形式证明生成之间的差距。

## 🔬 方法详解

**问题定义**：论文旨在解决现有证明器LLM在数学问题求解能力上的不足，特别是它们在生成形式化、可验证的数学证明方面的局限性。现有方法要么依赖于通用LLM，但其结果难以验证；要么依赖于专门的证明器LLM，但其解决问题的能力远低于通用LLM。因此，如何结合两者的优势，生成既具有推理能力又可验证的数学证明，是本文要解决的核心问题。

**核心思路**：Hilbert的核心思路是结合非形式推理和形式验证的优势。它利用通用LLM强大的数学推理能力进行问题分解和求解，同时利用形式验证器确保结果的正确性。通过递归分解问题，将复杂问题分解为更小的、易于解决的子问题，并使用专门的证明器LLM或推理器LLM解决这些子问题。

**技术框架**：Hilbert框架包含四个主要组件：1) 非形式LLM：负责数学推理和问题分解；2) 专用证明器LLM：针对Lean 4策略进行优化，生成形式化证明；3) 形式验证器：验证证明的正确性；4) 语义定理检索器：检索相关的定理和引理，辅助证明过程。整体流程是：给定一个问题，如果证明器LLM无法直接解决，则非形式LLM将其分解为子目标。然后，系统尝试使用证明器LLM或推理器LLM解决这些子目标。验证器对生成的证明进行验证，如果验证失败，则系统会根据验证器的反馈进行调整和改进。

**关键创新**：Hilbert的关键创新在于其递归分解和验证的框架。它不是简单地依赖于单个LLM来解决问题，而是将问题分解为更小的、易于管理的子问题，并利用不同的工具来解决这些子问题。这种递归分解和验证的策略能够有效地利用不同工具的优势，提高问题解决的成功率。

**关键设计**：论文中没有详细描述关键参数设置、损失函数或网络结构的具体细节。但框架的关键设计在于递归分解的策略和验证器的反馈机制。递归分解的深度和子问题的粒度需要根据具体问题进行调整。验证器的反馈信息需要足够详细，以便系统能够有效地调整和改进证明。

## 📊 实验亮点

Hilbert在miniF2F基准测试中达到了99.2%的准确率，比最佳公开方法高出6.6个百分点。在PutnamBench基准测试中，Hilbert解决了660个问题中的462个（70.0%），优于SeedProver等专有方法（50.4%），并且比最佳公开基线提高了422%。这些结果表明，Hilbert在数学问题求解方面取得了显著的进展。

## 🎯 应用场景

Hilbert框架可应用于自动化定理证明、数学教育、软件验证等领域。通过结合非形式推理和形式验证，可以提高数学问题求解的效率和准确性，并为软件系统的正确性提供更强的保障。未来，该框架有望扩展到其他需要严格推理和验证的领域，例如人工智能安全和金融建模。

## 📄 摘要（原文）

> Large Language Models (LLMs) demonstrate impressive mathematical reasoning abilities, but their solutions frequently contain errors that cannot be automatically verified. Formal theorem proving systems such as Lean 4 offer automated verification with complete accuracy, motivating recent efforts to build specialized prover LLMs that generate verifiable proofs in formal languages. However, a significant gap remains: current prover LLMs solve substantially fewer problems than general-purpose LLMs operating in natural language. We introduce Hilbert, an agentic framework that bridges this gap by combining the complementary strengths of informal reasoning and formal verification. Our system orchestrates four components: an informal LLM that excels at mathematical reasoning, a specialized prover LLM optimized for Lean 4 tactics, a formal verifier, and a semantic theorem retriever. Given a problem that the prover is unable to solve, Hilbert employs recursive decomposition to split the problem into subgoals that it solves with the prover or reasoner LLM. It leverages verifier feedback to refine incorrect proofs as necessary. Experimental results demonstrate that Hilbert substantially outperforms existing approaches on key benchmarks, achieving 99.2% on miniF2F, 6.6% points above the best publicly available method. Hilbert achieves the best known result on PutnamBench. It solves 462/660 problems (70.0%), outperforming proprietary approaches like SeedProver (50.4%) and achieving a 422% improvement over the best publicly available baseline. Thus, Hilbert effectively narrows the gap between informal reasoning and formal proof generation.

