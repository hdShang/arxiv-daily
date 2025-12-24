---
layout: default
title: "ObjexMT: Objective Extraction and Metacognitive Calibration for LLM-as-a-Judge under Multi-Turn Jailbreaks"
---

# ObjexMT: Objective Extraction and Metacognitive Calibration for LLM-as-a-Judge under Multi-Turn Jailbreaks

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.16889" class="toolbar-btn" target="_blank">📄 arXiv: 2508.16889v4</a>
  <a href="https://arxiv.org/pdf/2508.16889.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.16889v4" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.16889v4', 'ObjexMT: Objective Extraction and Metacognitive Calibration for LLM-as-a-Judge under Multi-Turn Jailbreaks')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Hyunjun Kim, Junwoo Ha, Sangyoon Yu, Haon Park

**分类**: cs.CL

**发布日期**: 2025-08-23 (更新: 2025-10-08)

**备注**: NeurIPS 2025 Workshop on MTI-LLM

**🔗 代码/项目**: [GITHUB](https://github.com/hyunjun1121/ObjexMT_dataset)

---

## 💡 一句话要点

**提出ObjexMT以解决多轮对话中的目标提取与元认知校准问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `目标提取` `元认知校准` `多轮对话` `大语言模型` `评判者资格` `语义相似度` `风险评估` `机器学习`

## 📋 核心要点

1. 现有方法在多轮对话中难以准确提取隐含目标，且对话上下文的冗长性影响模型性能。
2. 论文提出ObjexMT基准，要求模型从多轮对话中提取目标并报告置信度，旨在提升目标提取的准确性和可靠性。
3. 实验结果表明，kimi-k2在目标提取准确性上达到0.612，claude-sonnet-4在风险和校准方面表现最佳，展示了方法的有效性。

## 📝 摘要（中文）

LLM作为评判者（LLMaaJ）能够实现可扩展的评估，但缺乏对评判者资格的决定性测试：它能否恢复对话中的隐含目标并判断推断的可靠性？大语言模型在处理无关或冗长的上下文时表现下降，而多轮越狱会将目标分散在多个回合中。我们提出了ObjexMT，一个用于目标提取和元认知的基准。给定多轮对话记录，模型必须输出一句话的基本目标和自我报告的置信度。通过与金标准目标的语义相似度来评分准确性，并在300个校准项目上进行阈值处理。实验结果显示，kimi-k2在目标提取准确性上表现最佳，而claude-sonnet-4在选择性风险和校准方面表现最佳。高置信度错误仍然存在，ObjexMT为LLM评判者提供了可操作的测试。

## 🔬 方法详解

**问题定义**：本论文旨在解决在多轮对话中，如何准确提取隐含目标及评判者的元认知能力不足的问题。现有方法在处理冗长上下文时，容易导致目标推断错误，尤其是在多轮越狱场景中。

**核心思路**：论文提出的ObjexMT基准要求模型从多轮对话中提取出一句话的基本目标，并自我报告置信度。通过这种方式，模型不仅需要理解对话内容，还需评估自身推断的可靠性。

**技术框架**：整体架构包括目标提取模块和元认知校准模块。目标提取模块负责从对话中提取目标，而元认知校准模块则评估模型的置信度和推断的准确性。模型的性能通过与金标准目标的语义相似度进行评估，并在多个校准项目上进行阈值处理。

**关键创新**：最重要的技术创新在于引入了元认知校准的概念，使得模型不仅关注目标提取的准确性，还关注自身推断的可靠性。这与传统方法的单一目标提取有所区别。

**关键设计**：在实验中，使用了300个校准项目进行阈值处理，设定了置信度阈值$τ^	ext{star} = 0.66$，并通过Brier分数和期望校准误差等指标评估模型的元认知能力。

## 📊 实验亮点

实验结果显示，kimi-k2在目标提取准确性上达到0.612，claude-sonnet-4在选择性风险和校准方面表现最佳（AURC 0.242，ECE 0.206，Brier 0.254）。高置信度错误的比例在不同模型间差异显著，表明模型在处理隐含目标时仍面临挑战。

## 🎯 应用场景

该研究的潜在应用领域包括智能客服、对话系统和人机交互等场景。通过提升模型在多轮对话中的目标提取能力和自我评估能力，可以显著改善用户体验和系统的决策质量。未来，该方法有望在更复杂的对话场景中得到应用，推动智能对话系统的发展。

## 📄 摘要（原文）

> LLM-as-a-Judge (LLMaaJ) enables scalable evaluation, yet we lack a decisive test of a judge's qualification: can it recover the hidden objective of a conversation and know when that inference is reliable? Large language models degrade with irrelevant or lengthy context, and multi-turn jailbreaks can scatter goals across turns. We present ObjexMT, a benchmark for objective extraction and metacognition. Given a multi-turn transcript, a model must output a one-sentence base objective and a self-reported confidence. Accuracy is scored by semantic similarity to gold objectives, then thresholded once on 300 calibration items ($τ^\star = 0.66$; $F_1@τ^\star = 0.891$). Metacognition is assessed with expected calibration error, Brier score, Wrong@High-Confidence (0.80 / 0.90 / 0.95), and risk--coverage curves. Across six models (gpt-4.1, claude-sonnet-4, Qwen3-235B-A22B-FP8, kimi-k2, deepseek-v3.1, gemini-2.5-flash) evaluated on SafeMTData\_Attack600, SafeMTData\_1K, and MHJ, kimi-k2 achieves the highest objective-extraction accuracy (0.612; 95\% CI [0.594, 0.630]), while claude-sonnet-4 (0.603) and deepseek-v3.1 (0.599) are statistically tied. claude-sonnet-4 offers the best selective risk and calibration (AURC 0.242; ECE 0.206; Brier 0.254). Performance varies sharply across datasets (16--82\% accuracy), showing that automated obfuscation imposes challenges beyond model choice. High-confidence errors remain: Wrong@0.90 ranges from 14.9\% (claude-sonnet-4) to 47.7\% (Qwen3-235B-A22B-FP8). ObjexMT therefore supplies an actionable test for LLM judges: when objectives are implicit, judges often misinfer them; exposing objectives or gating decisions by confidence is advisable. All experimental data are in the Supplementary Material and at https://github.com/hyunjun1121/ObjexMT_dataset.

