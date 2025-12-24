---
layout: default
title: "Energy Efficiency in Robotics Software: A Systematic Literature Review (2020-2024)"
---

# Energy Efficiency in Robotics Software: A Systematic Literature Review (2020-2024)

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.12170" class="toolbar-btn" target="_blank">📄 arXiv: 2508.12170v1</a>
  <a href="https://arxiv.org/pdf/2508.12170.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.12170v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.12170v1', 'Energy Efficiency in Robotics Software: A Systematic Literature Review (2020-2024)')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Aryan Gupta

**分类**: cs.RO

**发布日期**: 2025-08-16

---

## 💡 一句话要点

**系统评估机器人软件能效以应对能源消耗挑战**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `机器人能效` `文献综述` `能量模型` `自动化审核` `性能评估` `跨层设计` `能耗优化`

## 📋 核心要点

1. 现有机器人软件能效研究缺乏系统性综述，导致能效优化方法的比较和应用受限。
2. 本研究通过系统文献综述，结合自动化与人工审核，分析了79篇相关研究，提出了最小报告清单。
3. 研究发现，电机/执行器是主要能耗来源，模拟评估最为常见，强调了跨层设计的潜在机会。

## 📝 摘要（中文）

本研究对2020至2024年间发表的机器人软件能效相关文献进行了系统性综述，更新并扩展了2020年前的证据。研究采用自动化审核流程，结合Google Scholar检索、前后雪崩法和大型语言模型辅助筛选与数据提取，确保每个自动化步骤都有约10%的人工审核。最终分析了79篇同行评审的研究，涵盖应用领域、评估指标、能量模型等多个维度。研究发现，工业应用占主导地位，电机/执行器是主要能耗来源，而模拟评估仍最为常见。综述提供了最小报告清单，并强调了跨层设计和量化非性能权衡的机会。

## 🔬 方法详解

**问题定义**：本研究旨在解决机器人软件能效研究中缺乏系统性综述的问题，现有方法在能效优化的比较和应用上存在不足，限制了研究的可比性和实用性。

**核心思路**：通过系统文献综述，结合自动化筛选和人工审核，全面分析机器人软件能效的研究现状，提出最小报告清单以提高研究的可比性。

**技术框架**：研究采用自动化审核流程，首先通过Google Scholar进行文献检索，然后应用前后雪崩法进行筛选，最后进行人工审核以确保数据的准确性。

**关键创新**：本研究的创新点在于结合了大型语言模型辅助的文献筛选与人工审核，确保了数据提取的准确性和全面性，同时提出了最小报告清单以促进研究的标准化。

**关键设计**：在数据分析中，研究关注了应用领域、能效评估指标、能量模型等多个维度，特别强调了电机/执行器作为主要能耗来源的发现。

## 📊 实验亮点

研究发现，68.4%的文献指出电机/执行器为主要能耗来源，模拟评估占比51.9%。此外，提出的最小报告清单将有助于提高未来研究的可比性和标准化，促进能效优化技术的进一步发展。

## 🎯 应用场景

该研究的潜在应用领域包括工业机器人、无人机和自动化系统等，能够为这些领域的能效优化提供理论基础和实践指导。通过标准化报告，未来的研究可以更好地比较不同方法的效果，从而推动机器人技术的可持续发展。

## 📄 摘要（原文）

> This study presents a systematic literature review of software-level approaches to energy efficiency in robotics published from 2020 through 2024, updating and extending pre-2020 evidence. An automated-but-audited pipeline combined Google Scholar seeding, backward/forward snowballing, and large-language-model (LLM) assistance for screening and data extraction, with ~10% human audits at each automated step and consensus-with-tie-breaks for full-text decisions. The final corpus comprises 79 peer-reviewed studies analyzed across application domain, metrics, evaluation type, energy models, major energy consumers, software technique families, and energy-quality trade-offs. Industrial settings dominate (31.6%) followed by exploration (25.3%). Motors/actuators are identified as the primary consumer in 68.4% of studies, with computing/controllers a distant second (13.9%). Simulation-only evaluations remain most common (51.9%), though hybrid evaluations are frequent (25.3%). Representational (physics-grounded) energy models predominate (87.3%). Motion and trajectory optimization is the leading technique family (69.6%), often paired with learning/prediction (40.5%) and computation allocation/scheduling (26.6%); power management/idle control (11.4%) and communication/data efficiency (3.8%) are comparatively underexplored. Reporting is heterogeneous: composite objectives that include energy are most common, while task-normalized and performance-per-energy metrics appear less often, limiting cross-paper comparability. The review offers a minimal reporting checklist (e.g., total energy and average power plus a task-normalized metric and clear baselines) and highlights opportunities in cross-layer designs and in quantifying non-performance trade-offs (accuracy, stability). A replication package with code, prompts, and frozen datasets accompanies the review.

