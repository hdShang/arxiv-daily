---
layout: default
title: "AgentGroupChat-V2: Divide-and-Conquer Is What LLM-Based Multi-Agent System Need"
---

# AgentGroupChat-V2: Divide-and-Conquer Is What LLM-Based Multi-Agent System Need

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.15451" class="toolbar-btn" target="_blank">📄 arXiv: 2506.15451v1</a>
  <a href="https://arxiv.org/pdf/2506.15451.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.15451v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.15451v1', 'AgentGroupChat-V2: Divide-and-Conquer Is What LLM-Based Multi-Agent System Need')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Zhouhong Gu, Xiaoxuan Zhu, Yin Cai, Hao Shen, Xingzhou Chen, Qingyi Wang, Jialin Li, Xiaoran Shi, Haoran Guo, Wenxuan Huang, Hongwei Feng, Yanghua Xiao, Zheyu Ye, Yao Hu, Shaosheng Cao

**分类**: cs.CL

**发布日期**: 2025-06-18

**🔗 代码/项目**: [GITHUB](https://github.com/MikeGu721/AgentGroupChat-V2)

---

## 💡 一句话要点

**提出AgentGroupChat-V2以解决多智能体系统的复杂任务挑战**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多智能体系统` `大型语言模型` `复杂任务处理` `分而治之` `自适应协作` `任务分解` `性能优化` `社会模拟`

## 📋 核心要点

1. 现有的多智能体系统在处理复杂任务时面临架构设计、跨域泛化和性能保障等挑战，尤其在任务复杂性和智能体数量增加时问题更加突出。
2. 本文提出的AgentGroupChat-V2框架通过分而治之的并行架构、动态协作引擎和优化的智能体组织策略，旨在高效解决复杂任务。
3. 实验结果显示，AgentGroupChat-V2在GSM8K上达到91.50%的准确率，超越最佳基线5.6个百分点，在AIME和HumanEval上也表现出显著提升，尤其在高难度任务中优势明显。

## 📝 摘要（中文）

基于大型语言模型的多智能体系统在社会模拟和复杂任务解决领域展现出显著潜力。然而，现有框架在系统架构设计、跨域泛化能力和性能保障方面面临重大挑战，尤其是在任务复杂性和智能体数量增加时。本文介绍了AgentGroupChat-V2，一个通过三项核心创新应对这些挑战的新框架：1）一种分而治之的完全并行架构，将用户查询分解为层次任务森林结构，以实现依赖管理和分布式并发处理；2）自适应协作引擎，根据任务特征动态选择异构LLM组合和交互模式；3）结合分而治之方法的智能体组织优化策略，以实现高效问题分解。大量实验表明，AgentGroupChat-V2在多个领域的表现优越，特别是在复杂推理场景中具有显著优势。

## 🔬 方法详解

**问题定义**：本文旨在解决现有多智能体系统在复杂任务处理中的架构设计和性能保障问题，尤其是在任务复杂性和智能体数量增加时的挑战。

**核心思路**：AgentGroupChat-V2通过分而治之的架构设计，将用户查询分解为层次化的任务结构，从而实现依赖管理和并行处理，提升系统的整体效率和准确性。

**技术框架**：该框架包括三个主要模块：分而治之的并行架构、动态协作引擎和智能体组织优化策略。用户查询首先被分解为任务森林，然后通过协作引擎选择合适的LLM组合进行处理，最后通过优化策略提升任务分解的效率。

**关键创新**：最重要的创新在于引入了完全并行的任务处理架构和自适应的协作机制，使得系统能够根据任务特征灵活调整LLM的组合和交互方式，这在现有方法中尚属首次。

**关键设计**：在设计中，采用了层次任务森林结构来管理任务依赖关系，并通过动态选择机制来优化LLM的使用，确保在复杂任务中能够高效协作。

## 📊 实验亮点

实验结果显示，AgentGroupChat-V2在GSM8K数据集上取得91.50%的准确率，超越最佳基线5.6个百分点；在AIME上达到30.4%的准确率，几乎是其他方法的两倍；在HumanEval上实现79.20%的pass@1，尤其在高难度Level 5 MATH问题中，性能提升超过11个百分点，显示出显著的优势。

## 🎯 应用场景

AgentGroupChat-V2的研究成果具有广泛的应用潜力，特别是在需要复杂推理和多智能体协作的领域，如社会模拟、智能客服、教育辅导等。其高效的任务处理能力和自适应协作机制能够显著提升这些应用的智能化水平和用户体验。

## 📄 摘要（原文）

> Large language model based multi-agent systems have demonstrated significant potential in social simulation and complex task resolution domains. However, current frameworks face critical challenges in system architecture design, cross-domain generalizability, and performance guarantees, particularly as task complexity and number of agents increases. We introduces AgentGroupChat-V2, a novel framework addressing these challenges through three core innovations: (1) a divide-and-conquer fully parallel architecture that decomposes user queries into hierarchical task forest structures enabling dependency management and distributed concurrent processing. (2) an adaptive collaboration engine that dynamically selects heterogeneous LLM combinations and interaction modes based on task characteristics. (3) agent organization optimization strategies combining divide-and-conquer approaches for efficient problem decomposition. Extensive experiments demonstrate AgentGroupChat-V2's superior performance across diverse domains, achieving 91.50% accuracy on GSM8K (exceeding the best baseline by 5.6 percentage points), 30.4% accuracy on competition-level AIME (nearly doubling other methods), and 79.20% pass@1 on HumanEval. Performance advantages become increasingly pronounced with higher task difficulty, particularly on Level 5 MATH problems where improvements exceed 11 percentage points compared to state-of-the-art baselines. These results confirm that AgentGroupChat-V2 provides a comprehensive solution for building efficient, general-purpose LLM multi-agent systems with significant advantages in complex reasoning scenarios. Code is available at https://github.com/MikeGu721/AgentGroupChat-V2.

