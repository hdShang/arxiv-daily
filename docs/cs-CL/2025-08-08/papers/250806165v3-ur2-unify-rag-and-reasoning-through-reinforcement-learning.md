---
layout: default
title: "UR$^2$: Unify RAG and Reasoning through Reinforcement Learning"
---

# UR$^2$: Unify RAG and Reasoning through Reinforcement Learning

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.06165" class="toolbar-btn" target="_blank">📄 arXiv: 2508.06165v3</a>
  <a href="https://arxiv.org/pdf/2508.06165.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.06165v3" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.06165v3', 'UR$^2$: Unify RAG and Reasoning through Reinforcement Learning')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Weitao Li, Boran Xiang, Xiaolong Wang, Zhinan Gou, Weizhi Ma, Yang Liu

**分类**: cs.CL, cs.AI

**发布日期**: 2025-08-08 (更新: 2025-09-21)

**🔗 代码/项目**: [GITHUB](https://github.com/Tsinghua-dhy/UR2)

---

## 💡 一句话要点

**提出UR$^2$以统一检索增强生成与推理能力**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `检索增强生成` `强化学习` `知识访问` `课程训练` `开放域问答` `医学推理` `数学推理`

## 📋 核心要点

1. 现有的RAG和RL方法通常是孤立发展的，缺乏有效的整合，限制了其在更广泛领域的应用。
2. UR2通过难度感知的课程训练和混合知识访问策略，动态协调检索与推理，提高了模型的适应性。
3. 实验结果显示，UR$^2$在开放域问答、医学和数学推理任务上显著超越现有方法，性能接近最新的GPT模型。

## 📝 摘要（中文）

大型语言模型（LLMs）在检索增强生成（RAG）和基于可验证奖励的强化学习（RLVR）两个互补范式中展现了显著能力。然而，这两种能力通常是孤立发展的，现有的统一努力范围有限，主要集中在开放域问答和特定任务约束下。这种缺乏整合限制了RAG-RL方法的泛化能力和适用性。为此，本文提出UR2（统一检索与推理），一个通过强化学习统一检索与推理的通用框架。UR2引入了两个关键贡献：难度感知的课程训练，仅在挑战性问题上选择性调用检索，以及结合领域特定离线语料库与LLM生成摘要的混合知识访问策略。实验结果表明，UR$^2$在多个基准上显著优于现有的RAG和RL方法，性能与GPT-4o-mini和GPT-4.1-mini相当。

## 🔬 方法详解

**问题定义**：本文旨在解决现有RAG和RL方法在整合上的不足，特别是在开放域问答和特定任务约束下的局限性。

**核心思路**：UR2的核心思路是通过难度感知的课程训练和混合知识访问策略，动态协调检索与推理，从而提升模型在多样化任务中的适应能力。

**技术框架**：UR2框架包括两个主要模块：难度感知课程训练模块和混合知识访问模块。前者根据问题的难度选择性调用检索，后者结合领域特定的离线语料和LLM生成的摘要。

**关键创新**：UR2的关键创新在于其难度感知的课程训练方法和混合知识访问策略，这与现有方法的固定检索设置和任务特定约束形成鲜明对比。

**关键设计**：在设计上，UR2采用了动态调整的检索策略，结合了多种损失函数以优化模型在不同任务上的表现，同时使用了Qwen-2.5-3/7B和LLaMA-3.1-8B作为基础模型。

## 📊 实验亮点

实验结果显示，UR$^2$在开放域问答、MMLU-Pro、医学和数学推理任务上显著优于现有的RAG和RL方法，性能与GPT-4o-mini和GPT-4.1-mini相当，展示了其在多样化任务中的强大适应性。

## 🎯 应用场景

UR2的研究成果在开放域问答、医学推理和数学推理等多个领域具有广泛的应用潜力。通过提升模型的检索与推理能力，该框架能够为智能问答系统、医疗决策支持和教育领域提供更为精准和高效的解决方案，未来可能推动相关技术的进一步发展与应用。

## 📄 摘要（原文）

> Large Language Models (LLMs) have shown remarkable capabilities through two complementary paradigms: Retrieval-Augmented Generation (RAG), which enhances knowledge grounding, and Reinforcement Learning from Verifiable Rewards (RLVR), which optimizes complex reasoning abilities. However, these two capabilities are often developed in isolation, and existing efforts to unify them remain narrow in scope -- typically limited to open-domain QA with fixed retrieval settings and task-specific constraints. This lack of integration constrains generalization and limits the applicability of RAG-RL methods to broader domains. To bridge this gap, we propose UR2 (Unified RAG and Reasoning), a general framework that unifies retrieval and reasoning through reinforcement learning. UR2 introduces two key contributions: a difficulty-aware curriculum training that selectively invokes retrieval only for challenging problems, and a hybrid knowledge access strategy combining domain-specific offline corpora with LLM-generated summaries. These components are designed to enable dynamic coordination between retrieval and reasoning, improving adaptability across a diverse range of tasks. Experiments across open-domain QA, MMLU-Pro, medical, and mathematical reasoning tasks demonstrate that UR$^2$ (built on Qwen-2.5-3/7B and LLaMA-3.1-8B) significantly outperforms existing RAG and RL methods, achieving comparable performance to GPT-4o-mini and GPT-4.1-mini on several benchmarks. We have released all code, models, and data at https://github.com/Tsinghua-dhy/UR2.

