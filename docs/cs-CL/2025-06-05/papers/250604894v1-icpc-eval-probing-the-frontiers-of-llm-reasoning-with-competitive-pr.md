---
layout: default
title: "ICPC-Eval: Probing the Frontiers of LLM Reasoning with Competitive Programming Contests"
---

# ICPC-Eval: Probing the Frontiers of LLM Reasoning with Competitive Programming Contests

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.04894" class="toolbar-btn" target="_blank">📄 arXiv: 2506.04894v1</a>
  <a href="https://arxiv.org/pdf/2506.04894.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.04894v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.04894v1', 'ICPC-Eval: Probing the Frontiers of LLM Reasoning with Competitive Programming Contests')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Shiyi Xu, Yiwen Hu, Yingqian Min, Zhipeng Chen, Wayne Xin Zhao, Ji-Rong Wen

**分类**: cs.CL

**发布日期**: 2025-06-05

**🔗 代码/项目**: [GITHUB](https://github.com/RUCAIBox/Slow_Thinking_with_LLMs)

---

## 💡 一句话要点

**提出ICPC-Eval以解决LLM在编程竞赛中的评估问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `编程竞赛` `推理能力` `评估基准` `测试用例生成` `Refine@K` `复杂任务`

## 📋 核心要点

1. 现有的编码能力评估基准无法有效反映大型语言模型在真实竞赛环境中的表现，评估指标也未能捕捉推理模型的反思能力。
2. 提出ICPC-Eval基准，包含来自11场ICPC竞赛的118个问题，设计了本地评估工具和Refine@K评估指标，以提升评估的准确性和有效性。
3. 实验结果显示，顶级推理模型在多轮反馈下才能充分发挥其推理能力，且在代码生成方面仍落后于人类团队，凸显了评估的挑战性。

## 📝 摘要（中文）

随着大型推理模型在复杂编码和推理任务中的显著进展，现有基准（如LiveCodeBench和CodeElo）不足以评估大型语言模型（LLMs）在真实竞赛环境中的编码能力。此外，当前评估指标如Pass@K未能捕捉推理模型的反思能力。为了解决这些挑战，我们提出了ICPC-Eval，这是一个顶级的竞争编码基准，旨在探讨LLM推理的前沿。ICPC-Eval包含来自全球11场近期ICPC竞赛的118个精心策划的问题，提供了三个关键贡献：1）具有挑战性的现实ICPC竞赛场景，问题类型和难度分布与实际竞赛一致；2）强大的测试用例生成方法及相应的本地评估工具包，实现高效准确的本地评估；3）有效的测试时间扩展评估指标Refine@K，允许基于执行反馈的迭代修复。结果强调了评估复杂推理能力的重大挑战：顶级推理模型如DeepSeek-R1通常依赖多轮代码反馈来充分释放其上下文推理潜力，与非推理模型相比。此外，尽管代码生成方面取得了近期进展，这些模型仍落后于表现最佳的人类团队。

## 🔬 方法详解

**问题定义**：本论文旨在解决现有评估基准无法有效评估大型语言模型在真实编程竞赛中的表现这一具体问题。现有方法如LiveCodeBench和CodeElo未能充分捕捉模型的推理能力和反思能力。

**核心思路**：论文提出ICPC-Eval基准，通过设计真实的竞赛场景和有效的评估工具，来全面评估LLMs的编码能力和推理能力。这样的设计旨在提供更具挑战性和现实性的测试环境。

**技术框架**：ICPC-Eval的整体架构包括问题集的构建、测试用例生成方法和本地评估工具。问题集由118个问题组成，涵盖多种难度和类型；测试用例生成方法确保了评估的多样性和准确性；本地评估工具则支持高效的评估过程。

**关键创新**：最重要的技术创新点在于提出了Refine@K评估指标，它允许模型在测试过程中根据执行反馈进行迭代修复。这一方法与传统的静态评估指标相比，能够更好地反映模型的推理能力。

**关键设计**：在设计中，采用了多轮反馈机制，确保模型能够在每次反馈中逐步改进其解决方案。此外，测试用例生成方法和评估工具的设计也注重了效率和准确性，以适应实际竞赛的需求。

## 📊 实验亮点

实验结果表明，顶级推理模型如DeepSeek-R1在多轮反馈下的表现显著优于单次评估，充分展现了其推理潜力。此外，尽管在代码生成方面有所进展，这些模型的表现仍落后于人类团队，强调了当前技术的局限性。

## 🎯 应用场景

该研究的潜在应用领域包括教育、编程竞赛和自动化代码生成等。通过提供一个标准化的评估基准，ICPC-Eval可以帮助研究人员和开发者更好地理解和提升大型语言模型在复杂编程任务中的表现，推动相关技术的进步与应用。

## 📄 摘要（原文）

> With the significant progress of large reasoning models in complex coding and reasoning tasks, existing benchmarks, like LiveCodeBench and CodeElo, are insufficient to evaluate the coding capabilities of large language models (LLMs) in real competition environments. Moreover, current evaluation metrics such as Pass@K fail to capture the reflective abilities of reasoning models. To address these challenges, we propose \textbf{ICPC-Eval}, a top-level competitive coding benchmark designed to probing the frontiers of LLM reasoning. ICPC-Eval includes 118 carefully curated problems from 11 recent ICPC contests held in various regions of the world, offering three key contributions: 1) A challenging realistic ICPC competition scenario, featuring a problem type and difficulty distribution consistent with actual contests. 2) A robust test case generation method and a corresponding local evaluation toolkit, enabling efficient and accurate local evaluation. 3) An effective test-time scaling evaluation metric, Refine@K, which allows iterative repair of solutions based on execution feedback. The results underscore the significant challenge in evaluating complex reasoning abilities: top-tier reasoning models like DeepSeek-R1 often rely on multi-turn code feedback to fully unlock their in-context reasoning potential when compared to non-reasoning counterparts. Furthermore, despite recent advancements in code generation, these models still lag behind top-performing human teams. We release the benchmark at: https://github.com/RUCAIBox/Slow_Thinking_with_LLMs

