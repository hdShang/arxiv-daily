---
layout: default
title: "LeanGeo: Formalizing Competitional Geometry problems in Lean"
---

# LeanGeo: Formalizing Competitional Geometry problems in Lean

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.14644" class="toolbar-btn" target="_blank">📄 arXiv: 2508.14644v1</a>
  <a href="https://arxiv.org/pdf/2508.14644.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.14644v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.14644v1', 'LeanGeo: Formalizing Competitional Geometry problems in Lean')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Chendong Song, Zihan Wang, Frederick Pu, Haiming Wang, Xiaohan Lin, Junqi Liu, Jia Li, Zhengying Liu

**分类**: cs.AI

**发布日期**: 2025-08-20

**备注**: 28 pages

**🔗 代码/项目**: [GITHUB](https://github.com/project-numina/LeanGeo/tree)

---

## 💡 一句话要点

**提出LeanGeo以解决几何问题形式化与验证挑战**

🎯 **匹配领域**: **支柱五：交互与反应 (Interaction & Reaction)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `几何问题` `形式化` `定理证明` `自动推理` `数学教育` `Lean 4` `高水平定理库`

## 📋 核心要点

1. 现有几何求解系统缺乏统一框架，难以与其他数学领域集成，且验证几何问题面临挑战。
2. LeanGeo通过在Lean 4定理证明器中形式化几何问题，提供了一个全面的高水平几何定理库，支持严格的证明验证。
3. LeanGeo-Bench展示了当前大型语言模型在几何问题上的表现，揭示了其能力和局限性，强调了未来研究的方向。

## 📝 摘要（中文）

几何问题是测试人工智能推理能力的重要领域。然而，现有的几何求解系统无法在统一框架内表达问题，导致与其他数学领域的集成困难。此外，由于大多数几何证明依赖于直观图形，验证几何问题尤其具有挑战性。为了解决这些问题，本文提出了LeanGeo，一个在Lean 4定理证明器中形式化和解决竞赛级几何问题的统一系统。LeanGeo提供了一个高水平几何定理的全面库，支持严格的证明验证，并与Mathlib无缝集成。我们还介绍了LeanGeo-Bench，这是一个包含国际数学奥林匹克（IMO）及其他高级来源问题的正式几何基准。我们的评估展示了当前大型语言模型在该基准上的能力和局限性，强调了自动几何推理进一步发展的必要性。

## 🔬 方法详解

**问题定义**：本文旨在解决现有几何求解系统无法在统一框架内表达问题的痛点，导致与其他数学领域的集成困难，以及验证几何问题的挑战。

**核心思路**：LeanGeo的核心思路是利用Lean 4定理证明器，构建一个统一的几何问题形式化系统，提供高水平几何定理库，以支持严格的证明验证和与Mathlib的集成。

**技术框架**：LeanGeo的整体架构包括高水平几何定理库、定理证明模块和与Mathlib的集成接口。用户可以通过Lean 4进行几何问题的形式化和求解。

**关键创新**：LeanGeo的主要创新在于其统一的形式化框架和高水平定理库，能够实现严格的证明验证，这在现有几何求解系统中是前所未有的。

**关键设计**：LeanGeo的设计包括高水平几何定理的系统化组织、与Lean 4的逻辑基础相结合的证明机制，以及与Mathlib的无缝集成，确保了高效的几何问题求解和验证。

## 📊 实验亮点

在LeanGeo-Bench基准测试中，当前大型语言模型的表现被评估，结果显示其在解决几何问题方面存在显著的能力和局限性。这一评估强调了在自动几何推理领域进一步研究和技术进步的必要性。

## 🎯 应用场景

LeanGeo的研究成果在教育、数学竞赛和人工智能推理等领域具有广泛的应用潜力。通过提供一个统一的几何问题求解平台，LeanGeo可以帮助学生和研究人员更好地理解几何概念，并推动自动化推理技术的发展，提升数学教育的质量和效率。

## 📄 摘要（原文）

> Geometry problems are a crucial testbed for AI reasoning capabilities. Most existing geometry solving systems cannot express problems within a unified framework, thus are difficult to integrate with other mathematical fields. Besides, since most geometric proofs rely on intuitive diagrams, verifying geometry problems is particularly challenging. To address these gaps, we introduce LeanGeo, a unified formal system for formalizing and solving competition-level geometry problems within the Lean 4 theorem prover. LeanGeo features a comprehensive library of high-level geometric theorems with Lean's foundational logic, enabling rigorous proof verification and seamless integration with Mathlib. We also present LeanGeo-Bench, a formal geometry benchmark in LeanGeo, comprising problems from the International Mathematical Olympiad (IMO) and other advanced sources. Our evaluation demonstrates the capabilities and limitations of state-of-the-art Large Language Models on this benchmark, highlighting the need for further advancements in automated geometric reasoning. We open source the theorem library and the benchmark of LeanGeo at https://github.com/project-numina/LeanGeo/tree/master.

