---
layout: default
title: CSC-SQL: Corrective Self-Consistency in Text-to-SQL via Reinforcement Learning
---

# CSC-SQL: Corrective Self-Consistency in Text-to-SQL via Reinforcement Learning

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.13271" class="toolbar-btn" target="_blank">📄 arXiv: 2505.13271v2</a>
  <a href="https://arxiv.org/pdf/2505.13271.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.13271v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.13271v2', 'CSC-SQL: Corrective Self-Consistency in Text-to-SQL via Reinforcement Learning')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Lei Sheng, Shuai-Shuai Xu

**分类**: cs.CL

**发布日期**: 2025-05-19 (更新: 2025-06-30)

**备注**: 25 pages, 5 figures

**🔗 代码/项目**: [GITHUB](https://github.com/CycloneBoy/csc_sql)

---

## 💡 一句话要点

**提出CSC-SQL以解决文本到SQL转换中的一致性问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `文本到SQL` `自一致性` `自纠正` `强化学习` `SQL生成` `自然语言处理` `模型微调`

## 📋 核心要点

1. 现有的自一致性和自纠正方法在SQL生成中存在选择次优输出和仅解决语法错误的不足。
2. CSC-SQL通过结合自一致性和自纠正，选择最频繁的输出并进行修正，从而提高SQL生成的准确性。
3. 在BIRD私有测试集上，7B模型的执行准确率达到71.72%，而32B模型则达到73.67%，显示出显著的性能提升。

## 📝 摘要（中文）

大型语言模型（LLMs）在将自然语言问题转换为SQL查询方面表现出强大的能力。现有的自一致性和自纠正技术在推理过程中增强了SQL生成的准确性，但存在明显的局限性：自一致性可能选择次优输出，而自纠正通常仅解决语法错误。为此，本文提出了CSC-SQL，一种将自一致性和自纠正相结合的新方法。CSC-SQL从并行采样中选择两个最频繁出现的输出，并将其输入合并修正模型进行纠正。此外，采用群体相对策略优化（GRPO）算法，通过强化学习微调SQL生成和修正模型，显著提升输出质量。实验结果验证了CSC-SQL的有效性和通用性。

## 🔬 方法详解

**问题定义**：本文旨在解决文本到SQL转换中自一致性和自纠正方法的局限性，特别是次优输出选择和语法错误的处理不足。

**核心思路**：CSC-SQL通过结合自一致性和自纠正的优点，选择并修正最频繁的输出，以提高SQL生成的准确性和可靠性。

**技术框架**：整体架构包括并行采样、输出选择、合并修正模型和强化学习微调四个主要模块。首先进行并行采样，然后选择两个最频繁的输出，接着通过合并修正模型进行纠正，最后利用GRPO算法进行微调。

**关键创新**：CSC-SQL的创新在于将自一致性与自纠正相结合，通过选择最频繁的输出并进行修正，克服了现有方法的局限性，提升了SQL生成的质量。

**关键设计**：在模型设计中，采用了GRPO算法进行强化学习微调，确保SQL生成和修正模型的性能优化，同时在损失函数和网络结构上进行了针对性的调整，以适应SQL生成的特定需求。

## 📊 实验亮点

实验结果显示，CSC-SQL在BIRD私有测试集上的表现优异，7B模型的执行准确率为71.72%，32B模型则达到了73.67%。这些结果表明，CSC-SQL在SQL生成任务中显著提升了输出质量，具有良好的通用性和有效性。

## 🎯 应用场景

CSC-SQL的研究成果在数据库查询生成、智能问答系统和数据分析工具等领域具有广泛的应用潜力。通过提高SQL生成的准确性，该方法能够帮助用户更高效地从数据库中提取信息，提升数据驱动决策的质量和速度。未来，该技术有望在更多自然语言处理任务中得到推广和应用。

## 📄 摘要（原文）

> Large language models (LLMs) have demonstrated strong capabilities in translating natural language questions about relational databases into SQL queries. In particular, test-time scaling techniques such as Self-Consistency and Self-Correction can enhance SQL generation accuracy by increasing computational effort during inference. However, these methods have notable limitations: Self-Consistency may select suboptimal outputs despite majority votes, while Self-Correction typically addresses only syntactic errors. To leverage the strengths of both approaches, we propose CSC-SQL, a novel method that integrates Self-Consistency and Self-Correction. CSC-SQL selects the two most frequently occurring outputs from parallel sampling and feeds them into a merge revision model for correction. Additionally, we employ the Group Relative Policy Optimization (GRPO) algorithm to fine-tune both the SQL generation and revision models via reinforcement learning, significantly enhancing output quality. Experimental results confirm the effectiveness and generalizability of CSC-SQL. On the BIRD private test set, our 7B model achieves 71.72\% execution accuracy, while the 32B model achieves 73.67\%. The code has been open sourced at https://github.com/CycloneBoy/csc_sql.

