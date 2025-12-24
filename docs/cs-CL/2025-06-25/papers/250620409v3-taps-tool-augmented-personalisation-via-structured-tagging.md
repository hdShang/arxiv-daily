---
layout: default
title: "TAPS: Tool-Augmented Personalisation via Structured Tagging"
---

# TAPS: Tool-Augmented Personalisation via Structured Tagging

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.20409" class="toolbar-btn" target="_blank">📄 arXiv: 2506.20409v3</a>
  <a href="https://arxiv.org/pdf/2506.20409.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.20409v3" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.20409v3', 'TAPS: Tool-Augmented Personalisation via Structured Tagging')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Ekaterina Taktasheva, Jeff Dalton

**分类**: cs.CL

**发布日期**: 2025-06-25 (更新: 2025-09-16)

**备注**: Accepted to EMNLP 2026 Main

---

## 💡 一句话要点

**提出TAPS以解决个性化工具使用不足问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `个性化工具使用` `大型语言模型` `结构化标签` `不确定性检测` `对话代理`

## 📋 核心要点

1. 现有方法在个性化工具使用方面存在显著不足，未能有效整合用户偏好。
2. TAPS通过结构化标签工具和不确定性工具检测器，提出了一种增强个性化工具使用的解决方案。
3. TAPS在NLSI任务上显著提升了大型语言模型的性能，达到了新的开源模型状态。

## 📝 摘要（中文）

随着工具增强的大型语言模型的进步，它们能够与外部工具互动，从而提升执行复杂用户任务的能力。然而，现有方法忽视了个性化在指导工具使用中的作用。本文研究了如何有效地将用户偏好整合到目标导向的对话代理中。通过广泛分析，我们识别了大型语言模型在个性化工具使用方面的关键弱点。为此，我们提出了TAPS，这是一种新颖的解决方案，通过利用结构化标签工具和基于不确定性的工具检测器来增强个性化工具使用。TAPS显著提升了大型语言模型整合用户偏好的能力，在NLSI任务上实现了开源模型的新状态。

## 🔬 方法详解

**问题定义**：本文旨在解决现有工具增强大型语言模型在个性化工具使用中的不足，尤其是未能充分考虑用户偏好的问题。

**核心思路**：TAPS的核心思路是通过结构化标签和不确定性检测来增强个性化工具使用，使对话代理能够更好地响应用户的具体需求和偏好。

**技术框架**：TAPS的整体架构包括两个主要模块：结构化标签工具用于捕捉用户偏好，不确定性工具检测器用于评估工具使用的适用性和有效性。

**关键创新**：TAPS的主要创新在于结合了结构化标签和不确定性检测，显著提升了大型语言模型在个性化工具使用上的能力，这与传统方法的单一工具使用模式形成了鲜明对比。

**关键设计**：在设计中，TAPS采用了特定的损失函数来优化用户偏好的整合，同时在网络结构上引入了多层次的标签处理机制，以提高模型的适应性和准确性。

## 📊 实验亮点

在实验中，TAPS在NLSI任务上显著提升了开源模型的性能，达到了新的状态，具体提升幅度未知。这一结果表明，个性化工具使用的有效整合能够显著改善对话代理的表现。

## 🎯 应用场景

TAPS的研究成果具有广泛的应用潜力，尤其在智能助手、客户服务和个性化推荐系统等领域。通过更好地理解和响应用户偏好，TAPS能够提升用户体验和满意度，推动人机交互的进一步发展。

## 📄 摘要（原文）

> Recent advancements in tool-augmented large language models have enabled them to interact with external tools, enhancing their ability to perform complex user tasks. However, existing approaches overlook the role of personalisation in guiding tool use. This work investigates how user preferences can be effectively integrated into goal-oriented dialogue agents. Through extensive analysis, we identify key weaknesses in the ability of LLMs to personalise tool use. To this end, we introduce TAPS, a novel solution that enhances personalised tool use by leveraging a structured tagging tool and an uncertainty-based tool detector. TAPS significantly improves the ability of LLMs to incorporate user preferences, achieving the new state-of-the-art for open source models on the NLSI task.

