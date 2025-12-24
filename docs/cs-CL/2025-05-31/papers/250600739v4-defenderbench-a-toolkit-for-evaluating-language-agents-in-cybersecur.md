---
layout: default
title: DefenderBench: A Toolkit for Evaluating Language Agents in Cybersecurity Environments
---

# DefenderBench: A Toolkit for Evaluating Language Agents in Cybersecurity Environments

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.00739" class="toolbar-btn" target="_blank">📄 arXiv: 2506.00739v4</a>
  <a href="https://arxiv.org/pdf/2506.00739.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.00739v4" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.00739v4', 'DefenderBench: A Toolkit for Evaluating Language Agents in Cybersecurity Environments')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Chiyu Zhang, Marc-Alexandre Cote, Michael Albada, Anush Sankaran, Jack W. Stokes, Tong Wang, Amir Abdi, William Blum, Muhammad Abdul-Mageed

**分类**: cs.CL

**发布日期**: 2025-05-31 (更新: 2025-10-14)

**备注**: Accepted by NeurIPS 2025 Workshop Scaling Environments for Agents (SEA)

**🔗 代码/项目**: [GITHUB](https://github.com/microsoft/DefenderBench)

---

## 💡 一句话要点

**提出DefenderBench工具包以评估网络安全环境中的语言代理**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `网络安全` `语言模型` `评估工具` `开源工具` `模块化设计`

## 📋 核心要点

1. 现有的语言模型在网络安全领域的应用尚处于探索阶段，缺乏系统的评估工具。
2. DefenderBench提供了一个模块化的评估框架，支持多种网络安全任务的评估，便于研究人员进行公平比较。
3. 实验结果表明，Claude-3.7-sonnet在DefenderBench中表现最佳，得分为81.65，展示了该工具包的有效性。

## 📝 摘要（中文）

大型语言模型（LLM）在自然语言理解和推理方面展现了令人印象深刻的能力，但其在网络安全领域的潜力尚未得到充分探索。本文介绍了DefenderBench，这是一个实用的开源工具包，用于评估语言代理在攻击、防御和基于知识的网络安全任务中的表现。DefenderBench包括网络入侵、恶意内容检测、代码漏洞分析和网络安全知识评估等环境，旨在为研究人员提供经济实惠且易于访问的评估平台，同时确保评估的公正性和严谨性。我们对多种最先进的LLM进行了基准测试，结果显示Claude-3.7-sonnet在DefenderBench中得分最高，为81.65。

## 🔬 方法详解

**问题定义**：本文旨在解决现有语言代理在网络安全任务评估中的不足，尤其是缺乏标准化和系统化的评估工具。现有方法往往无法全面评估语言模型在网络安全中的应用能力。

**核心思路**：DefenderBench通过提供一个开放源代码的评估工具包，涵盖攻击、防御及知识评估任务，旨在为研究人员提供一个公平、可重复的评估平台。

**技术框架**：DefenderBench的整体架构包括多个模块，分别用于网络入侵检测、恶意内容识别、代码漏洞分析和网络安全知识评估。每个模块都设计为可独立运行，便于集成自定义的LLM和任务。

**关键创新**：DefenderBench的最大创新在于其模块化设计，允许用户根据需求添加新的任务和模型，从而促进了研究的可重复性和公平性。

**关键设计**：在设计上，DefenderBench采用标准化的评估框架，确保不同模型的评估结果具有可比性，同时提供了详细的任务描述和评估指标，以便于研究人员理解和使用。

## 📊 实验亮点

实验结果显示，Claude-3.7-sonnet在DefenderBench中得分最高，达到81.65，明显优于其他模型，如Claude-3.7-sonnet-think得分78.40，开源模型Llama 3.3 70B得分71.81，展示了DefenderBench在评估语言模型性能方面的有效性和可靠性。

## 🎯 应用场景

DefenderBench的潜在应用领域包括网络安全研究、教育和工业界。它可以帮助研究人员和从业者评估和比较不同语言模型在网络安全任务中的表现，从而推动该领域的技术进步和应用落地。未来，DefenderBench可能成为网络安全领域语言模型评估的标准工具，促进更多创新的出现。

## 📄 摘要（原文）

> Large language model (LLM) agents have shown impressive capabilities in human language comprehension and reasoning, yet their potential in cybersecurity remains underexplored. We introduce DefenderBench, a practical, open-source toolkit for evaluating language agents across offense, defense, and cybersecurity knowledge-based tasks. DefenderBench includes environments for network intrusion, malicious content detection, code vulnerability analysis, and cybersecurity knowledge assessment. It is intentionally designed to be affordable and easily accessible for researchers while providing fair and rigorous assessment. We benchmark several state-of-the-art (SoTA) and popular LLMs, including both open- and closed-weight models, using a standardized agentic framework. Our results show that Claude-3.7-sonnet performs best with a DefenderBench score of 81.65, followed by Claude-3.7-sonnet-think with 78.40, while the best open-weight model, Llama 3.3 70B, is not far behind with a DefenderBench score of 71.81. DefenderBench's modular design allows seamless integration of custom LLMs and tasks, promoting reproducibility and fair comparisons. An anonymized version of DefenderBench is available at https://github.com/microsoft/DefenderBench.

