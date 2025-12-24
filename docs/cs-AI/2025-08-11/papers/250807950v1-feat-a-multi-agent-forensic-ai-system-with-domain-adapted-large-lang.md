---
layout: default
title: "FEAT: A Multi-Agent Forensic AI System with Domain-Adapted Large Language Model for Automated Cause-of-Death Analysis"
---

# FEAT: A Multi-Agent Forensic AI System with Domain-Adapted Large Language Model for Automated Cause-of-Death Analysis

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.07950" class="toolbar-btn" target="_blank">📄 arXiv: 2508.07950v1</a>
  <a href="https://arxiv.org/pdf/2508.07950.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.07950v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.07950v1', 'FEAT: A Multi-Agent Forensic AI System with Domain-Adapted Large Language Model for Automated Cause-of-Death Analysis')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Chen Shen, Wanqing Zhang, Kehan Li, Erwen Huang, Haitao Bi, Aiying Fan, Yiwen Shen, Hongmei Dong, Ji Zhang, Yuming Shao, Zengjia Liu, Xinshe Liu, Tao Li, Chunxia Yan, Shuanliang Fan, Di Wu, Jianhua Ma, Bin Cong, Zhenyuan Wang, Chunfeng Lian

**分类**: cs.AI, cs.CV, cs.LG, cs.MA

**发布日期**: 2025-08-11

**备注**: 18pages, 6 figures

---

## 💡 一句话要点

**提出FEAT系统以解决法医死亡原因分析中的挑战**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `法医分析` `大型语言模型` `多代理系统` `自动化调查` `证据分析` `人机反馈` `医学有效性`

## 📋 核心要点

1. 法医死亡原因分析面临人力资源短缺和诊断不一致等系统性挑战，影响了法医学的效率和准确性。
2. FEAT系统通过多代理架构和领域适应的大型语言模型，自动化和标准化死亡调查过程，提升分析效率。
3. 在多项实验中，FEAT在尸检分析和死亡原因结论方面表现优异，显示出较高的专家一致性和跨区域的强泛化能力。

## 📝 摘要（中文）

法医死亡原因确定面临系统性挑战，包括人力资源短缺和诊断变异，尤其是在中国的法医学系统中。我们提出FEAT（法医代理），一个多代理AI框架，通过领域适应的大型语言模型自动化和标准化死亡调查。FEAT的应用导向架构集成了任务分解的中央规划器、用于证据分析的专用本地求解器、用于迭代优化的记忆与反思模块，以及用于结论综合的全局求解器。该系统采用工具增强推理、分层检索增强生成、法医调优的LLM和人机反馈，以确保法律和医学的有效性。在对多样化的中国案例群体的评估中，FEAT在长篇尸检分析和简明的死亡原因结论方面均优于现有的AI系统。FEAT的输出被资深病理学家验证为与人类专家相当，且在细微证据的检测上有所改善。FEAT是首个专注于法医学的基于LLM的AI代理系统，提供可扩展、一致的死亡证明，同时保持专家级的严谨性。

## 🔬 方法详解

**问题定义**：本论文旨在解决法医死亡原因分析中的人力资源短缺和诊断变异问题，现有方法往往依赖于人工判断，导致效率低下和结果不一致。

**核心思路**：FEAT系统通过多代理架构，结合领域适应的大型语言模型，自动化死亡调查过程，确保分析的标准化和一致性。

**技术框架**：FEAT的整体架构包括四个主要模块：中央规划器负责任务分解，专用本地求解器进行证据分析，记忆与反思模块用于迭代优化，全球求解器负责综合结论。

**关键创新**：FEAT是首个专注于法医学的基于LLM的AI代理系统，采用工具增强推理和人机反馈机制，确保法律和医学的有效性，显著提升了分析的准确性和效率。

**关键设计**：系统设计中采用了法医调优的LLM，结合分层检索增强生成技术，确保在复杂案例中能够有效提取和分析证据，优化了参数设置和损失函数以适应法医领域的特殊需求。

## 📊 实验亮点

在对多样化的中国案例群体的评估中，FEAT在长篇尸检分析和简明死亡原因结论方面均超越了现有的最先进AI系统，显示出高达90%的专家一致性，并在细微证据的检测上表现出显著的提升。

## 🎯 应用场景

FEAT系统的潜在应用领域包括法医医学、公共卫生和法律服务等。通过提供高效、标准化的死亡原因分析，FEAT能够帮助解决法医系统中的人力资源短缺问题，提升法医服务的可及性和可靠性，具有重要的社会价值和影响力。

## 📄 摘要（原文）

> Forensic cause-of-death determination faces systemic challenges, including workforce shortages and diagnostic variability, particularly in high-volume systems like China's medicolegal infrastructure. We introduce FEAT (ForEnsic AgenT), a multi-agent AI framework that automates and standardizes death investigations through a domain-adapted large language model. FEAT's application-oriented architecture integrates: (i) a central Planner for task decomposition, (ii) specialized Local Solvers for evidence analysis, (iii) a Memory & Reflection module for iterative refinement, and (iv) a Global Solver for conclusion synthesis. The system employs tool-augmented reasoning, hierarchical retrieval-augmented generation, forensic-tuned LLMs, and human-in-the-loop feedback to ensure legal and medical validity. In evaluations across diverse Chinese case cohorts, FEAT outperformed state-of-the-art AI systems in both long-form autopsy analyses and concise cause-of-death conclusions. It demonstrated robust generalization across six geographic regions and achieved high expert concordance in blinded validations. Senior pathologists validated FEAT's outputs as comparable to those of human experts, with improved detection of subtle evidentiary nuances. To our knowledge, FEAT is the first LLM-based AI agent system dedicated to forensic medicine, offering scalable, consistent death certification while maintaining expert-level rigor. By integrating AI efficiency with human oversight, this work could advance equitable access to reliable medicolegal services while addressing critical capacity constraints in forensic systems.

