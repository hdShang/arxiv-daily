---
layout: default
title: "SafeLawBench: Towards Safe Alignment of Large Language Models"
---

# SafeLawBench: Towards Safe Alignment of Large Language Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.06636" class="toolbar-btn" target="_blank">📄 arXiv: 2506.06636v1</a>
  <a href="https://arxiv.org/pdf/2506.06636.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.06636v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.06636v1', 'SafeLawBench: Towards Safe Alignment of Large Language Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Chuxue Cao, Han Zhu, Jiaming Ji, Qichao Sun, Zhenghao Zhu, Yinyu Wu, Juntao Dai, Yaodong Yang, Sirui Han, Yike Guo

**分类**: cs.CL

**发布日期**: 2025-06-07

**备注**: Accepted to ACL2025 Findings

---

## 💡 一句话要点

**提出SafeLawBench以解决大型语言模型安全评估问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `安全评估` `法律视角` `多选题` `问答任务` `模型性能` `安全性研究`

## 📋 核心要点

1. 现有的安全评估方法缺乏客观标准，导致大型语言模型的安全性评估面临挑战。
2. 论文提出SafeLawBench基准，从法律角度系统性地评估LLMs的安全性，分类安全风险。
3. 实验结果显示，当前主流模型在多选任务中的准确率未超过80.5%，平均准确率为68.8%。

## 📝 摘要（中文）

随着大型语言模型（LLMs）的普及，其安全性引发了重大关注。然而，由于现有安全基准的主观性，缺乏明确的评估标准。为填补这一空白，我们首次从法律视角探索LLMs的安全评估，提出了SafeLawBench基准。该基准根据法律标准将安全风险分为三个级别，提供了系统全面的评估框架，包含24,860个多选题和1,106个开放领域问答任务。我们的评估涵盖了2个闭源LLMs和18个开源LLMs，突出了每个模型的安全特性，并评估了其安全相关推理的稳定性和拒绝行为。我们发现，多数投票机制可以提升模型性能。值得注意的是，即使是领先的SOTA模型如Claude-3.5-Sonnet和GPT-4o在SafeLawBench的多选任务中准确率也未超过80.5%，而20个LLMs的平均准确率为68.8%。我们呼吁社区优先关注LLMs的安全研究。

## 🔬 方法详解

**问题定义**：本论文旨在解决大型语言模型安全评估缺乏客观标准的问题。现有方法的痛点在于评估标准的主观性，无法有效反映模型的安全性。

**核心思路**：论文提出SafeLawBench基准，通过法律视角对LLMs的安全性进行系统评估，分类安全风险为三个级别，提供全面的评估框架。

**技术框架**：SafeLawBench包含24,860个多选题和1,106个开放领域问答任务，评估包括闭源和开源模型，采用零-shot和few-shot提示方法，分析模型的安全特性和推理稳定性。

**关键创新**：最重要的技术创新在于从法律角度出发，建立了一个系统化的安全评估框架，填补了现有方法的空白。

**关键设计**：在实验中，采用了多数投票机制来提升模型性能，评估了模型在安全相关推理的稳定性和拒绝行为。

## 📊 实验亮点

实验结果显示，尽管使用了先进的模型，如Claude-3.5-Sonnet和GPT-4o，但在SafeLawBench的多选任务中，准确率最高仅为80.5%。而20个LLMs的平均准确率为68.8%，显示出当前模型在安全性评估方面的不足。

## 🎯 应用场景

该研究的潜在应用领域包括法律合规、自动化问答系统和安全性评估工具。通过提供一个系统的评估框架，SafeLawBench可以帮助开发者和研究者更好地理解和提升大型语言模型的安全性，促进其在实际应用中的安全使用。

## 📄 摘要（原文）

> With the growing prevalence of large language models (LLMs), the safety of LLMs has raised significant concerns. However, there is still a lack of definitive standards for evaluating their safety due to the subjective nature of current safety benchmarks. To address this gap, we conducted the first exploration of LLMs' safety evaluation from a legal perspective by proposing the SafeLawBench benchmark. SafeLawBench categorizes safety risks into three levels based on legal standards, providing a systematic and comprehensive framework for evaluation. It comprises 24,860 multi-choice questions and 1,106 open-domain question-answering (QA) tasks. Our evaluation included 2 closed-source LLMs and 18 open-source LLMs using zero-shot and few-shot prompting, highlighting the safety features of each model. We also evaluated the LLMs' safety-related reasoning stability and refusal behavior. Additionally, we found that a majority voting mechanism can enhance model performance. Notably, even leading SOTA models like Claude-3.5-Sonnet and GPT-4o have not exceeded 80.5% accuracy in multi-choice tasks on SafeLawBench, while the average accuracy of 20 LLMs remains at 68.8\%. We urge the community to prioritize research on the safety of LLMs.

