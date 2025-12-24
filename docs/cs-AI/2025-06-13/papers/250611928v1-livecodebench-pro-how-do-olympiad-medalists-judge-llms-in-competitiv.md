---
layout: default
title: "LiveCodeBench Pro: How Do Olympiad Medalists Judge LLMs in Competitive Programming?"
---

# LiveCodeBench Pro: How Do Olympiad Medalists Judge LLMs in Competitive Programming?

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.11928" class="toolbar-btn" target="_blank">📄 arXiv: 2506.11928v1</a>
  <a href="https://arxiv.org/pdf/2506.11928.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.11928v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.11928v1', 'LiveCodeBench Pro: How Do Olympiad Medalists Judge LLMs in Competitive Programming?')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Zihan Zheng, Zerui Cheng, Zeyu Shen, Shang Zhou, Kaiyuan Liu, Hansen He, Dongruixuan Li, Stanley Wei, Hangyi Hao, Jianzhu Yao, Peiyao Sheng, Zixuan Wang, Wenhao Chai, Aleksandra Korolova, Peter Henderson, Sanjeev Arora, Pramod Viswanath, Jingbo Shang, Saining Xie

**分类**: cs.SE, cs.AI, cs.CL, cs.LG

**发布日期**: 2025-06-13

**备注**: Project Page at https://livecodebenchpro.com/

---

## 💡 一句话要点

**提出LiveCodeBench Pro以评估LLMs在竞赛编程中的表现**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `竞赛编程` `算法推理` `性能评估` `基准测试` `专家注释` `动态更新`

## 📋 核心要点

1. 现有大型语言模型在竞赛编程中的表现被高估，尤其在复杂问题上仍存在显著局限性。
2. 提出LiveCodeBench Pro基准，通过国际竞赛奖牌获得者的注释和分析，评估LLMs的表现。
3. 实验结果显示，最佳模型在中等难度问题上的通过率为53%，在困难问题上为0，显示出与人类专家的差距。

## 📝 摘要（中文）

近期报告称，大型语言模型（LLMs）在竞赛编程中已超越顶尖人类。本文通过国际算法竞赛奖牌获得者的视角，重新审视这一说法，探讨LLMs与人类专家的差异及其局限性。我们引入了LiveCodeBench Pro，一个由Codeforces、ICPC和IOI问题组成的基准，持续更新以减少数据污染的可能性。通过对模型生成的失败提交进行逐行分析，我们发现前沿模型在中等难度问题上的通过率仅为53%，而在困难问题上为0%。LLMs在实现密集型问题上表现良好，但在细致的算法推理和复杂案例分析中存在困难，常常生成自信但错误的解释。LiveCodeBench Pro揭示了与人类大师水平之间的显著差距，并提供了细致的诊断以指导未来的改进。

## 🔬 方法详解

**问题定义**：本文旨在解决大型语言模型在竞赛编程中表现被高估的问题，现有方法未能充分揭示其在复杂算法推理中的局限性。

**核心思路**：通过引入LiveCodeBench Pro基准，结合国际竞赛奖牌获得者的专业知识，对LLMs进行系统评估，揭示其在算法推理和案例分析中的不足。

**技术框架**：整体架构包括问题收集、注释、模型提交分析和性能评估四个主要模块。问题来自多个知名竞赛，确保数据的多样性和代表性。

**关键创新**：LiveCodeBench Pro的最大创新在于其动态更新机制和专家注释，能够有效减少数据污染，并提供细致的失败分析，帮助识别LLMs的具体弱点。

**关键设计**：在实验中，采用了多种难度级别的问题，设置了不同的评估标准，确保模型在实现精度和推理能力上的全面评估。

## 📊 实验亮点

实验结果显示，最佳大型语言模型在中等难度问题上的通过率为53%，而在困难问题上则为0%。这表明，尽管LLMs在实现密集型问题上表现良好，但在复杂算法推理方面仍存在显著不足，强调了与人类专家之间的差距。

## 🎯 应用场景

该研究的潜在应用领域包括教育、编程竞赛培训和自动化代码生成。通过深入理解LLMs的局限性，可以为未来的模型改进提供指导，提升其在复杂编程任务中的表现，进而推动人工智能在编程领域的应用。

## 📄 摘要（原文）

> Recent reports claim that large language models (LLMs) now outperform elite humans in competitive programming. Drawing on knowledge from a group of medalists in international algorithmic contests, we revisit this claim, examining how LLMs differ from human experts and where limitations still remain. We introduce LiveCodeBench Pro, a benchmark composed of problems from Codeforces, ICPC, and IOI that are continuously updated to reduce the likelihood of data contamination. A team of Olympiad medalists annotates every problem for algorithmic categories and conducts a line-by-line analysis of failed model-generated submissions. Using this new data and benchmark, we find that frontier models still have significant limitations: without external tools, the best model achieves only 53% pass@1 on medium-difficulty problems and 0% on hard problems, domains where expert humans still excel. We also find that LLMs succeed at implementation-heavy problems but struggle with nuanced algorithmic reasoning and complex case analysis, often generating confidently incorrect justifications. High performance appears largely driven by implementation precision and tool augmentation, not superior reasoning. LiveCodeBench Pro thus highlights the significant gap to human grandmaster levels, while offering fine-grained diagnostics to steer future improvements in code-centric LLM reasoning.

