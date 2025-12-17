---
layout: default
title: The Instability of Safety: How Random Seeds and Temperature Expose Inconsistent LLM Refusal Behavior
---

# The Instability of Safety: How Random Seeds and Temperature Expose Inconsistent LLM Refusal Behavior

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.12066" class="toolbar-btn" target="_blank">📄 arXiv: 2512.12066</a>
  <a href="https://arxiv.org/pdf/2512.12066.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.12066" onclick="toggleFavorite(this, '2512.12066', 'The Instability of Safety: How Random Seeds and Temperature Expose Inconsistent LLM Refusal Behavior')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Erik Larsen

**分类**: cs.LG, cs.AI, cs.CL

**发布日期**: 2025-12-18

---

## 💡 一句话要点

**揭示大语言模型安全性评估的不稳定性：随机种子和温度的影响**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大语言模型` `安全性评估` `随机种子` `温度采样` `安全稳定性` `决策翻转` `有害提示词`

## 📋 核心要点

1. 现有LLM安全评估依赖单次测试，忽略了模型输出的随机性，可能导致评估结果不准确。
2. 通过改变随机种子和温度，研究模型在有害提示下的拒绝行为，评估安全决策的稳定性。
3. 实验发现模型在不同配置下拒绝行为不稳定，高温度降低稳定性，并建议使用多样本评估。

## 📝 摘要（中文）

当前对大型语言模型（LLM）的安全评估依赖于单次测试，隐含地假设模型响应是确定性的，并能代表模型的安全对齐状态。本文通过研究随机种子和温度设置对安全拒绝决策的稳定性，挑战了这一假设。在三个模型系列的四个指令调优模型（Llama 3.1 8B、Qwen 2.5 7B、Qwen 3 8B、Gemma 3 12B）上，针对876个有害提示词，在20种不同的采样配置（4种温度 x 5个随机种子）下进行测试，发现18-28%的提示词表现出决策翻转——模型在某些配置下拒绝，而在其他配置下顺从，具体比例取决于模型。安全稳定性指数（SSI）显示，较高的温度显著降低了决策稳定性（Friedman chi-squared = 396.81, p < 0.001），温度从0.0到1.0时，平均温度内SSI从0.977降至0.942。使用Claude 3.5 Haiku作为统一的外部评判器验证了所有模型系列的结果，与主要的Llama 70B评判器达成了89.0%的评判一致性（Cohen's kappa = 0.62）。在每个模型中，顺从率较高的提示词表现出较低的稳定性（Spearman rho = -0.47 to -0.70, all p < 0.001），表明模型在边缘请求上更容易“犹豫”。这些发现表明，单次安全评估不足以进行可靠的安全评估，评估协议必须考虑模型行为的随机变化。结果表明，当跨温度池化时，单次评估仅在92.4%的时间内与多样本真实情况一致（在固定温度下，根据设置，一致性为94.2-97.7%），并建议每个提示词至少使用3个样本进行可靠的安全评估。

## 🔬 方法详解

**问题定义**：当前LLM安全评估方法主要依赖于单次测试，即给定一个有害提示词，观察模型是否拒绝。这种方法忽略了模型输出的随机性，例如随机种子和温度等因素的变化，可能导致评估结果不准确，无法真实反映模型的安全对齐程度。现有方法缺乏对模型安全决策稳定性的系统性评估。

**核心思路**：本文的核心思路是通过系统性地改变随机种子和温度等采样参数，观察模型在同一有害提示下的拒绝行为是否一致。如果模型在不同配置下表现出不一致的拒绝或顺从行为，则表明其安全决策不稳定。通过量化这种不稳定性，可以更全面地评估模型的安全性。

**技术框架**：本文的技术框架主要包括以下几个步骤：1) 选择多个LLM模型（Llama 3.1 8B, Qwen 2.5 7B, Qwen 3 8B, Gemma 3 12B）；2) 构建包含876个有害提示词的测试集；3) 在不同的采样配置下（4种温度 x 5个随机种子）运行模型，记录其拒绝或顺从行为；4) 使用安全稳定性指数（SSI）量化每个提示词的决策稳定性；5) 使用外部评判器（Claude 3.5 Haiku）验证结果的可靠性；6) 分析顺从率与稳定性之间的关系。

**关键创新**：本文最重要的技术创新点在于提出了安全稳定性指数（SSI），用于量化模型在不同采样配置下的安全决策稳定性。SSI能够有效地捕捉模型在边缘情况下的“犹豫”行为，从而更全面地评估模型的安全性。与传统的单次测试相比，SSI能够更好地反映模型的真实安全水平。

**关键设计**：关键设计包括：1) 选择了具有代表性的LLM模型和有害提示词；2) 系统性地改变随机种子和温度，以探索模型行为的随机性；3) 使用外部评判器验证结果的可靠性；4) 通过统计分析，揭示了顺从率与稳定性之间的关系。温度设置范围为0.0到1.0，随机种子数量为5。使用Friedman检验和Spearman相关系数进行统计分析。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.12066/x1.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.12066/x2.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.12066/x3.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

实验结果表明，18-28%的有害提示词会导致模型决策翻转，即在某些配置下拒绝，而在其他配置下顺从。较高的温度显著降低了决策稳定性（Friedman chi-squared = 396.81, p < 0.001）。单次评估仅在92.4%的时间内与多样本真实情况一致。建议每个提示词至少使用3个样本进行可靠的安全评估。

## 🎯 应用场景

该研究成果可应用于LLM安全评估和安全对齐。通过评估模型的安全稳定性，可以更准确地了解模型的安全风险，并指导模型的安全训练和部署。该研究还有助于开发更可靠的安全评估方法和工具，提高LLM的整体安全性。

## 📄 摘要（原文）

> Current safety evaluations of large language models rely on single-shot testing, implicitly assuming that model responses are deterministic and representative of the model's safety alignment. We challenge this assumption by investigating the stability of safety refusal decisions across random seeds and temperature settings. Testing four instruction-tuned models from three families (Llama 3.1 8B, Qwen 2.5 7B, Qwen 3 8B, Gemma 3 12B) on 876 harmful prompts across 20 different sampling configurations (4 temperatures x 5 random seeds), we find that 18-28% of prompts exhibit decision flips--the model refuses in some configurations but complies in others--depending on the model. Our Safety Stability Index (SSI) reveals that higher temperatures significantly reduce decision stability (Friedman chi-squared = 396.81, p < 0.001), with mean within-temperature SSI dropping from 0.977 at temperature 0.0 to 0.942 at temperature 1.0. We validate our findings across all model families using Claude 3.5 Haiku as a unified external judge, achieving 89.0% inter-judge agreement with our primary Llama 70B judge (Cohen's kappa = 0.62). Within each model, prompts with higher compliance rates exhibit lower stability (Spearman rho = -0.47 to -0.70, all p < 0.001), indicating that models "waver" more on borderline requests. These findings demonstrate that single-shot safety evaluations are insufficient for reliable safety assessment and that evaluation protocols must account for stochastic variation in model behavior. We show that single-shot evaluation agrees with multi-sample ground truth only 92.4% of the time when pooling across temperatures (94.2-97.7% at fixed temperature depending on setting), and recommend using at least 3 samples per prompt for reliable safety assessment.

