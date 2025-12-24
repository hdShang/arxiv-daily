---
layout: default
title: "WideSearch: Benchmarking Agentic Broad Info-Seeking"
---

# WideSearch: Benchmarking Agentic Broad Info-Seeking

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.07999" class="toolbar-btn" target="_blank">📄 arXiv: 2508.07999v2</a>
  <a href="https://arxiv.org/pdf/2508.07999.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.07999v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.07999v2', 'WideSearch: Benchmarking Agentic Broad Info-Seeking')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Ryan Wong, Jiawei Wang, Junjie Zhao, Li Chen, Yan Gao, Long Zhang, Xuan Zhou, Zuo Wang, Kai Xiang, Ge Zhang, Wenhao Huang, Yang Wang, Ke Wang

**分类**: cs.CL

**发布日期**: 2025-08-11 (更新: 2025-08-28)

---

## 💡 一句话要点

**提出WideSearch基准以评估大规模信息搜索代理的可靠性**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `信息搜索` `大型语言模型` `基准测试` `自动化代理` `数据集` `质量控制` `多领域评估`

## 📋 核心要点

1. 现有的搜索代理在大规模信息收集任务中表现不佳，成功率普遍低于预期，亟需改进。
2. WideSearch基准通过200个真实用户查询的问题，系统评估搜索代理在信息收集任务中的表现。
3. 实验结果显示，当前搜索代理在大规模信息搜索中存在关键缺陷，强调了未来研究的紧迫性。

## 📝 摘要（中文）

在专业研究和日常规划中，广泛的信息搜索任务常常成为瓶颈，且其重复性高于认知复杂性。随着大型语言模型（LLMs）的快速发展，基于LLMs的自动搜索代理为减轻人类的繁琐工作提供了有希望的解决方案。然而，现有代理在执行大规模信息收集任务时的能力尚未得到充分评估。为此，本文提出了WideSearch，一个新的基准，旨在评估代理在这些任务中的可靠性。该基准包含200个手动策划的问题，涵盖15个以上不同领域，基于真实用户查询。通过严格的五阶段质量控制流程，确保数据集的难度、完整性和可验证性。我们对10多个最先进的搜索系统进行了基准测试，结果显示大多数系统的成功率接近0%。

## 🔬 方法详解

**问题定义**：本文旨在解决现有搜索代理在大规模信息收集任务中的可靠性评估问题。现有方法缺乏适当的基准，导致其性能未能得到有效验证。

**核心思路**：WideSearch基准通过设计200个手动策划的问题，涵盖多个领域，提供了一个系统化的评估框架，以测试搜索代理的能力和可靠性。

**技术框架**：该基准包括五个主要阶段的质量控制流程，确保数据集的难度、完整性和可验证性。每个任务要求代理收集大量原子信息，并将其整理成结构化输出。

**关键创新**：WideSearch的创新在于其针对大规模信息收集任务的专门设计，填补了现有评估工具的空白，提供了一个可重复的评估标准。

**关键设计**：数据集包含100个英文和100个中文问题，确保多样性。每个问题的答案都可以逐一验证，增强了评估的客观性。

## 📊 实验亮点

实验结果显示，超过10个最先进的搜索系统在WideSearch基准测试中的整体成功率接近0%，最佳表现者仅达到5%。然而，通过多次人类测试的交叉验证，成功率可接近100%，显示出当前系统在大规模信息搜索中的关键缺陷。

## 🎯 应用场景

WideSearch基准的潜在应用场景包括学术研究、商业智能和日常信息检索等领域。通过提升搜索代理的可靠性，该研究有助于减少人类在信息收集过程中的时间和精力投入，推动智能搜索技术的发展。

## 📄 摘要（原文）

> From professional research to everyday planning, many tasks are bottlenecked by wide-scale information seeking, which is more repetitive than cognitively complex. With the rapid development of Large Language Models (LLMs), automated search agents powered by LLMs offer a promising solution to liberate humans from this tedious work. However, the capability of these agents to perform such "wide-context" collection reliably and completely remains largely unevaluated due to a lack of suitable benchmarks. To bridge this gap, we introduce WideSearch, a new benchmark engineered to evaluate agent reliability on these large-scale collection tasks. The benchmark features 200 manually curated questions (100 in English, 100 in Chinese) from over 15 diverse domains, grounded in real user queries. Each task requires agents to collect large-scale atomic information, which could be verified one by one objectively, and arrange it into a well-organized output. A rigorous five-stage quality control pipeline ensures the difficulty, completeness, and verifiability of the dataset. We benchmark over 10 state-of-the-art agentic search systems, including single-agent, multi-agent frameworks, and end-to-end commercial systems. Most systems achieve overall success rates near 0\%, with the best performer reaching just 5\%. However, given sufficient time, cross-validation by multiple human testers can achieve a near 100\% success rate. These results demonstrate that present search agents have critical deficiencies in large-scale information seeking, underscoring urgent areas for future research and development in agentic search. Our dataset, evaluation pipeline, and benchmark results have been publicly released at https://widesearch-seed.github.io/

