---
layout: default
title: Linear Personality Probing and Steering in LLMs: A Big Five Study
---

# Linear Personality Probing and Steering in LLMs: A Big Five Study

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.17639" class="toolbar-btn" target="_blank">📄 arXiv: 2512.17639v1</a>
  <a href="https://arxiv.org/pdf/2512.17639.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.17639v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.17639v1', 'Linear Personality Probing and Steering in LLMs: A Big Five Study')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Michel Frising, Daniel Balcells

**分类**: cs.CL

**发布日期**: 2025-12-19

**备注**: 29 pages, 6 figures

---

## 💡 一句话要点

**利用线性探针和引导实现LLM性格控制：基于大五人格的研究**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `性格控制` `线性探针` `线性引导` `大五人格` `提示工程` `人机交互`

## 📋 核心要点

1. 现有LLM性格控制方法存在后训练成本高或提示工程脆弱等问题，限制了其应用。
2. 该研究探索利用与大五人格特质对齐的线性方向，实现对LLM性格的探测和引导。
3. 实验表明线性方向可有效探测性格，但引导能力受上下文影响，在特定任务中效果显著。

## 📝 摘要（中文）

大型语言模型（LLMs）表现出独特且一致的性格，这极大地影响了信任和互动。这意味着性格框架将成为表征和控制LLMs行为的非常有价值的工具，但目前的方法要么成本高昂（后训练），要么脆弱（提示工程）。通过线性方向进行探针和引导最近成为一种廉价而有效的替代方案。在本文中，我们研究了与大五人格特质对齐的线性方向是否可以用于探测和引导模型行为。使用Llama 3.3 70B，我们生成了406个虚构角色的描述及其大五人格特质分数。然后，我们使用这些描述和Alpaca问卷中的问题来提示模型，从而能够以已知、可量化的方式对沿人格特质变化的隐藏激活进行采样。使用线性回归，我们学习了一组每层激活空间中的方向，并测试了它们在探测和引导模型行为方面的有效性。我们的结果表明，与特质分数对齐的线性方向是性格检测的有效探针，而它们的引导能力在很大程度上取决于上下文，在强制选择任务中产生可靠的效果，但在开放式生成或提示中存在额外上下文时影响有限。

## 🔬 方法详解

**问题定义**：现有的大型语言模型性格控制方法主要存在两个痛点：一是后训练方法，需要耗费大量的计算资源和时间；二是提示工程方法，其效果往往不稳定，容易受到提示语的细微变化的影响。因此，需要一种更高效、更稳定的方法来控制LLM的性格。

**核心思路**：本文的核心思路是利用线性探针和引导，通过学习与大五人格特质对齐的线性方向，实现在LLM的激活空间中对性格进行探测和引导。这种方法的优势在于其计算成本较低，且相对稳定，能够有效地控制LLM的性格。

**技术框架**：该研究的技术框架主要包括以下几个步骤：1. 生成包含性格描述和对应大五人格分数的虚构角色数据；2. 使用这些数据提示LLM，并提取隐藏层的激活值；3. 利用线性回归学习激活空间中与大五人格特质对齐的线性方向；4. 使用学习到的线性方向进行性格探测和引导，并评估其效果。

**关键创新**：该研究的关键创新在于提出了一种基于线性探针和引导的LLM性格控制方法。与传统的后训练或提示工程方法相比，该方法具有计算成本低、稳定性高等优点。此外，该研究还深入探讨了线性方向在不同上下文下的引导能力，为LLM性格控制提供了新的思路。

**关键设计**：在实验设计方面，作者使用了Llama 3.3 70B模型，并生成了406个虚构角色的描述及其大五人格特质分数。在学习线性方向时，作者使用了线性回归方法。在评估性格探测和引导效果时，作者使用了Alpaca问卷，并设计了强制选择任务和开放式生成任务。此外，作者还分析了不同上下文对引导效果的影响。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.17639v1/media/main_diagram.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.17639v1/x1.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.17639v1/x2.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

实验结果表明，与大五人格特质对齐的线性方向是性格检测的有效探针。在强制选择任务中，该方法能够产生可靠的引导效果。虽然在开放式生成任务中引导效果有限，但该研究为探索LLM性格控制提供了新的方向和思路。

## 🎯 应用场景

该研究成果可应用于个性化对话系统、虚拟角色扮演、心理健康辅助等领域。通过控制LLM的性格，可以提升用户体验，增强用户信任感，并为特定应用场景定制更合适的AI助手。未来，该技术有望在人机交互领域发挥重要作用。

## 📄 摘要（原文）

> Large language models (LLMs) exhibit distinct and consistent personalities that greatly impact trust and engagement. While this means that personality frameworks would be highly valuable tools to characterize and control LLMs' behavior, current approaches remain either costly (post-training) or brittle (prompt engineering). Probing and steering via linear directions has recently emerged as a cheap and efficient alternative. In this paper, we investigate whether linear directions aligned with the Big Five personality traits can be used for probing and steering model behavior. Using Llama 3.3 70B, we generate descriptions of 406 fictional characters and their Big Five trait scores. We then prompt the model with these descriptions and questions from the Alpaca questionnaire, allowing us to sample hidden activations that vary along personality traits in known, quantifiable ways. Using linear regression, we learn a set of per-layer directions in activation space, and test their effectiveness for probing and steering model behavior. Our results suggest that linear directions aligned with trait-scores are effective probes for personality detection, while their steering capabilities strongly depend on context, producing reliable effects in forced-choice tasks but limited influence in open-ended generation or when additional context is present in the prompt.

