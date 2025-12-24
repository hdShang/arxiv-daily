---
layout: default
title: MAS-ZERO: Designing Multi-Agent Systems with Zero Supervision
---

# MAS-ZERO: Designing Multi-Agent Systems with Zero Supervision

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.14996" class="toolbar-btn" target="_blank">📄 arXiv: 2505.14996v3</a>
  <a href="https://arxiv.org/pdf/2505.14996.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.14996v3" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.14996v3', 'MAS-ZERO: Designing Multi-Agent Systems with Zero Supervision')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Zixuan Ke, Austin Xu, Yifei Ming, Xuan-Phi Nguyen, Ryan Chin, Caiming Xiong, Shafiq Joty

**分类**: cs.CL, cs.AI, cs.LG

**发布日期**: 2025-05-21 (更新: 2025-12-01)

**备注**: SEA@NeurIPS (Oral) 2025

---

## 💡 一句话要点

**提出MAS-ZERO以解决多智能体系统设计中的监督依赖问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多智能体系统` `自我演化` `动态设计` `大型语言模型` `元反馈机制` `自动化系统` `复杂任务处理`

## 📋 核心要点

1. 现有的多智能体系统设计依赖于手动配置，缺乏灵活性和适应性，难以应对新任务。
2. MAS-ZERO提出了一种自我演化的框架，通过元级设计在推理时动态优化MAS配置，无需验证集。
3. 实验表明，MAS-ZERO在推理、编码和代理任务上分别提升了16.69%、16.66%和5.45%的准确率，且具备成本效率。

## 📝 摘要（中文）

多智能体系统（MAS）利用大型语言模型（LLMs）的强大能力，具有解决复杂任务的潜力。然而，现有的MAS通常依赖于手动设计的代理角色和通信协议，这些设计往往无法与LLMs的优势相匹配，并且难以适应新任务。MAS-ZERO是首个自我演化的自动MAS设计框架，能够在推理时动态设计、评估和优化MAS配置，而无需验证集。通过元反馈机制，MAS-ZERO实现了动态问题分解和代理组合，实验结果显示其在推理、编码和基于搜索的任务上均优于现有基线，准确率平均提升显著。

## 🔬 方法详解

**问题定义**：本论文旨在解决现有多智能体系统设计中对手动配置的依赖，导致的灵活性不足和适应性差的问题。现有方法通常需要验证集进行调优，且设计静态，无法在推理时动态调整。

**核心思路**：MAS-ZERO的核心思路是通过元级设计在推理时自我演化，动态设计、评估和优化MAS配置。该方法不依赖于验证集，能够根据具体问题实例进行定制。

**技术框架**：MAS-ZERO的整体架构包括多个模块：首先是问题分解模块，接着是代理组合模块，最后是基于元反馈的评估与优化模块。这些模块协同工作，实现动态调整和优化。

**关键创新**：MAS-ZERO的主要创新在于其自我演化能力和动态反馈机制，能够在推理过程中根据问题的可解性和完整性进行实时调整，与传统静态设计方法形成鲜明对比。

**关键设计**：在设计中，MAS-ZERO采用了动态问题分解和代理组合策略，结合元反馈机制，确保系统能够在不同任务中灵活调整。同时，设计中考虑了成本效率，确保在提升性能的同时控制资源消耗。

## 📊 实验亮点

实验结果显示，MAS-ZERO在推理任务上平均提升了16.69%的准确率，在编码任务上提升了16.66%，在基于搜索的代理任务上提升了5.45%。这些结果表明，MAS-ZERO在多智能体系统设计中显著优于现有的手动和自动基线方法，展现了其强大的性能和适应性。

## 🎯 应用场景

MAS-ZERO的研究成果在多个领域具有广泛的应用潜力，包括智能机器人、自动化系统、复杂任务处理等。其自我演化的特性使得系统能够快速适应新环境和任务，提升了多智能体系统的实用性和灵活性，未来可能在智能城市、无人驾驶等领域发挥重要作用。

## 📄 摘要（原文）

> Multi-agent systems (MAS) leveraging the impressive capabilities of Large Language Models (LLMs) hold significant potential for tackling complex tasks. However, most current MAS depend on manually designed agent roles and communication protocols. These manual designs often fail to align with the underlying LLMs' strengths and struggle to adapt to novel tasks. Recent automatic MAS approaches attempt to mitigate these limitations but typically necessitate a validation set for tuning and yield static MAS designs lacking adaptability during inference, while also removing the flexibility to reduce to simpler systems. We introduce MAS-ZERO, the first self-evolved, inference-time framework for automatic MAS design. MAS-ZERO employs meta-level design to iteratively design, critique, and refine MAS configurations tailored to each problem instance, without requiring a validation set. Critically, it enables dynamic problem decomposition and agent composition through meta-feedback on solvability and completeness, and reduction to simpler systems when appropriate. Experiments across reasoning (math and graduate-level QA), coding, and agentic (search-based) benchmarks, using both closed-source and open-source LLM backbones of varying sizes, demonstrate that MAS-ZERO outperforms strong manual and automatic MAS baselines. It achieves substantial average accuracy improvements of up to 16.69% on reasoning, 16.66% on coding, and 5.45% on agentic tasks, while maintaining cost efficiency.

