---
layout: default
title: Breaking the Ceiling: Exploring the Potential of Jailbreak Attacks through Expanding Strategy Space
---

# Breaking the Ceiling: Exploring the Potential of Jailbreak Attacks through Expanding Strategy Space

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.21277" class="toolbar-btn" target="_blank">📄 arXiv: 2505.21277v2</a>
  <a href="https://arxiv.org/pdf/2505.21277.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.21277v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.21277v2', 'Breaking the Ceiling: Exploring the Potential of Jailbreak Attacks through Expanding Strategy Space')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yao Huang, Yitong Sun, Shouwei Ruan, Yichi Zhang, Yinpeng Dong, Xingxing Wei

**分类**: cs.CR, cs.AI, cs.CL

**发布日期**: 2025-05-27 (更新: 2025-05-28)

**备注**: 19 pages, 20 figures, accepted by ACL 2025, Findings

**🔗 代码/项目**: [GITHUB](https://github.com/Aries-iai/CL-GSO)

---

## 💡 一句话要点

**提出扩展策略空间以解决监狱突破攻击问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `监狱突破攻击` `大型语言模型` `安全性测试` `遗传算法` `对抗性攻击` `模型鲁棒性` `策略空间扩展`

## 📋 核心要点

1. 现有方法在应对安全对齐模型时效果有限，未能有效解决监狱突破攻击的根本问题。
2. 本文提出了一种新框架，通过将监狱突破策略分解为基本组件，结合遗传算法优化与意图评估机制，扩展策略空间。
3. 实验结果显示，扩展策略空间后在Claude-3.5上实现超过90%的成功率，显著提高了模型的攻击能力和跨模型迁移性。

## 📝 摘要（中文）

大型语言模型（LLMs）尽管具备先进的通用能力，但仍面临诸多安全风险，尤其是监狱突破攻击，这类攻击能够绕过安全协议。通过黑箱监狱突破攻击理解这些脆弱性，能够为模型的鲁棒性提供重要见解。现有方法虽然通过各种提示工程技术有所改进，但在安全对齐模型面前效果有限，且未能解决一个更根本的问题：有效性本质上受限于预定义的策略空间。扩展这一空间面临系统捕捉关键攻击模式和高效导航复杂性的重大挑战。为此，本文提出了一种新框架，基于阐述可能性模型（ELM）理论将监狱突破策略分解为基本组件，并开发了基于遗传算法的优化与意图评估机制。实验结果显示，通过扩展策略空间，我们在Claude-3.5上实现了超过90%的成功率，超越了专门的安全模型，展现出强大的跨模型迁移能力。

## 🔬 方法详解

**问题定义**：本文旨在解决大型语言模型在面对监狱突破攻击时的脆弱性，现有方法在安全对齐模型面前效果有限，未能有效捕捉攻击模式。

**核心思路**：通过扩展策略空间，本文将监狱突破策略分解为基本组件，结合遗传算法优化与意图评估机制，以更全面地探索攻击潜力。

**技术框架**：整体架构包括策略空间扩展模块、攻击模式捕捉模块和优化评估模块，系统性地捕捉和评估不同攻击策略的有效性。

**关键创新**：最重要的创新在于将监狱突破策略分解为基本组件，并通过遗传算法优化与意图评估机制来提升攻击成功率，这与现有方法的预定义策略空间形成鲜明对比。

**关键设计**：在设计中，采用了基于遗传算法的优化策略，设置了多种损失函数以评估攻击效果，并优化了网络结构以提高模型的适应性和鲁棒性。

## 📊 实验亮点

实验结果显示，扩展策略空间后在Claude-3.5上实现超过90%的成功率，显著高于现有方法的表现，且在跨模型迁移性和评估准确性上超越了专门的安全模型，展现出前所未有的攻击能力。

## 🎯 应用场景

该研究的潜在应用领域包括安全性测试、模型评估以及对抗性攻击研究。通过深入理解监狱突破攻击的机制，可以为大型语言模型的安全性提升提供重要参考，未来可能在AI安全领域产生深远影响。

## 📄 摘要（原文）

> Large Language Models (LLMs), despite advanced general capabilities, still suffer from numerous safety risks, especially jailbreak attacks that bypass safety protocols. Understanding these vulnerabilities through black-box jailbreak attacks, which better reflect real-world scenarios, offers critical insights into model robustness. While existing methods have shown improvements through various prompt engineering techniques, their success remains limited against safety-aligned models, overlooking a more fundamental problem: the effectiveness is inherently bounded by the predefined strategy spaces. However, expanding this space presents significant challenges in both systematically capturing essential attack patterns and efficiently navigating the increased complexity. To better explore the potential of expanding the strategy space, we address these challenges through a novel framework that decomposes jailbreak strategies into essential components based on the Elaboration Likelihood Model (ELM) theory and develops genetic-based optimization with intention evaluation mechanisms. To be striking, our experiments reveal unprecedented jailbreak capabilities by expanding the strategy space: we achieve over 90% success rate on Claude-3.5 where prior methods completely fail, while demonstrating strong cross-model transferability and surpassing specialized safeguard models in evaluation accuracy. The code is open-sourced at: https://github.com/Aries-iai/CL-GSO.

