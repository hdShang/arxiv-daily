---
layout: default
title: "Arch-Router: Aligning LLM Routing with Human Preferences"
---

# Arch-Router: Aligning LLM Routing with Human Preferences

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.16655" class="toolbar-btn" target="_blank">📄 arXiv: 2506.16655v1</a>
  <a href="https://arxiv.org/pdf/2506.16655.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.16655v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.16655v1', 'Arch-Router: Aligning LLM Routing with Human Preferences')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Co Tran, Salman Paracha, Adil Hafeez, Shuguang Chen

**分类**: cs.CL

**发布日期**: 2025-06-19

**🔗 代码/项目**: [HUGGINGFACE](https://huggingface.co/katanemo/Arch-Router-1.5B)

---

## 💡 一句话要点

**提出Arch-Router以解决LLM路由与人类偏好不一致问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `模型路由` `人类偏好` `偏好对齐` `对话系统` `智能助手` `个性化推荐`

## 📋 核心要点

1. 现有的LLM路由方法在评估性能时未能有效捕捉人类的主观偏好，且模型选择范围有限。
2. 本文提出了一种偏好对齐的路由框架Arch-Router，通过将查询与用户定义的领域和动作类型进行匹配，优化模型选择。
3. 实验结果显示，Arch-Router在对话数据集上实现了最先进的性能，超越了多个顶级专有模型。

## 📝 摘要（中文）

随着大型语言模型（LLMs）的快速发展，路由技术已成为优化不同模型使用的重要手段。然而，现有的LLM路由方法存在两个主要局限：一是评估性能的基准往往无法捕捉基于主观评价标准的人类偏好，二是通常只从有限的模型池中进行选择。为此，本文提出了一种偏好对齐的路由框架，通过将查询与用户定义的领域或动作类型匹配，提供了一种实用的机制来编码偏好。具体而言，我们引入了Arch-Router，一个紧凑的1.5B模型，能够学习将查询映射到领域-动作偏好，从而进行模型路由决策。实验表明，我们的方法在与人类偏好的匹配上达到了最先进的结果，超越了顶级的专有模型。

## 🔬 方法详解

**问题定义**：本文旨在解决现有LLM路由方法在评估人类偏好时的不足，尤其是主观评价标准的缺失和模型选择的局限性。

**核心思路**：论文提出的Arch-Router通过将查询与用户定义的领域和动作类型进行匹配，来优化模型选择，从而更好地反映人类的偏好。

**技术框架**：Arch-Router的整体架构包括查询输入、领域-动作偏好映射和模型选择模块。该框架支持无缝添加新模型，而无需重新训练或修改架构。

**关键创新**：Arch-Router的主要创新在于其偏好对齐的路由机制，能够有效捕捉主观评价标准，使得路由决策更加透明和灵活。

**关键设计**：模型采用了1.5B参数的紧凑结构，设计了特定的损失函数以优化查询与偏好的匹配，同时确保了模型的高效性和可扩展性。

## 📊 实验亮点

在对话数据集上的实验结果显示，Arch-Router在与人类偏好的匹配上达到了最先进的水平，超越了多个顶级专有模型，具体提升幅度未知，展示了其在主观评价标准捕捉上的优势。

## 🎯 应用场景

该研究的潜在应用场景包括智能助手、个性化推荐系统和多领域对话系统等。通过更好地对齐人类偏好，Arch-Router能够提升用户体验，增强模型在实际应用中的适应性和灵活性，具有重要的实际价值和未来影响。

## 📄 摘要（原文）

> With the rapid proliferation of large language models (LLMs) -- each optimized for different strengths, style, or latency/cost profile -- routing has become an essential technique to operationalize the use of different models. However, existing LLM routing approaches are limited in two key ways: they evaluate performance using benchmarks that often fail to capture human preferences driven by subjective evaluation criteria, and they typically select from a limited pool of models. In this work, we propose a preference-aligned routing framework that guides model selection by matching queries to user-defined domains (e.g., travel) or action types (e.g., image editing) -- offering a practical mechanism to encode preferences in routing decisions. Specifically, we introduce \textbf{Arch-Router}, a compact 1.5B model that learns to map queries to domain-action preferences for model routing decisions. Our approach also supports seamlessly adding new models for routing without requiring retraining or architectural modifications. Experiments on conversational datasets demonstrate that our approach achieves state-of-the-art (SOTA) results in matching queries with human preferences, outperforming top proprietary models. Our approach captures subjective evaluation criteria and makes routing decisions more transparent and flexible. Our model is available at: \texttt{https://huggingface.co/katanemo/Arch-Router-1.5B}.

