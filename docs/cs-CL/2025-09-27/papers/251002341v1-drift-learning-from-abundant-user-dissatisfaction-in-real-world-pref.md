---
layout: default
title: "DRIFT: Learning from Abundant User Dissatisfaction in Real-World Preference Learning"
---

# DRIFT: Learning from Abundant User Dissatisfaction in Real-World Preference Learning

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2510.02341" class="toolbar-btn" target="_blank">📄 arXiv: 2510.02341v1</a>
  <a href="https://arxiv.org/pdf/2510.02341.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.02341v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2510.02341v1', 'DRIFT: Learning from Abundant User Dissatisfaction in Real-World Preference Learning')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yifan Wang, Bolian Li, Junlin Wu, Zhaoxuan Tan, Zheli Liu, Ruqi Zhang, Ananth Grama, Qingkai Zeng

**分类**: cs.CL, cs.AI

**发布日期**: 2025-09-27

**🔗 代码/项目**: [GITHUB](https://github.com/cacayaya/DRIFT.git)

---

## 💡 一句话要点

**提出DRIFT以解决现实世界偏好学习中的用户不满信号问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `用户不满信号` `偏好学习` `动态抽样` `模型训练` `对话系统` `推荐系统` `代码生成` `用户反馈`

## 📋 核心要点

1. 现有偏好学习方法依赖昂贵的人类标注，难以有效利用用户不满信号，导致模型训练不充分。
2. DRIFT通过利用真实的用户不满信号进行训练，并动态抽样正面反馈，提升了模型的学习效率和效果。
3. 实验结果显示，DRIFT在多个任务上显著提高了模型性能，尤其在大规模模型上表现尤为突出。

## 📝 摘要（中文）

现实世界的大型语言模型部署（如对话AI系统、代码生成助手）自然产生大量隐含的用户不满（DSAT）信号，用户通过迭代改进、纠正和表达偏好来寻求更好的答案，而明确的满意度（SAT）反馈则稀缺。现有的偏好学习方法与这种数据特征不匹配，依赖于昂贵的人类标注或假设大量正面反馈。本文提出了DRIFT（Dissatisfaction-Refined Iterative preference Training），该方法以真实的DSAT信号为基础进行训练，并动态从不断演变的策略中抽样正面反馈。实验证明，基于真实的WildFeedback数据集和合成的UltraFeedback数据集训练的DRIFT模型在WildBench任务得分上提升了6.23%（7B）/ 7.61%（14B），在AlpacaEval2胜率上提升了8.95%（7B）/ 12.29%（14B），超越了强基线方法如迭代DPO和SPIN。

## 🔬 方法详解

**问题定义**：本文旨在解决现实世界偏好学习中用户不满信号的有效利用问题。现有方法往往依赖于昂贵的人类标注，无法充分利用隐含的用户反馈，导致模型性能受限。

**核心思路**：DRIFT的核心思路是将训练锚定在真实的用户不满信号上，并从不断演变的策略中动态抽样正面反馈。这种设计旨在更好地捕捉用户的真实偏好和需求。

**技术框架**：DRIFT的整体框架包括数据收集、信号处理、动态抽样和模型训练四个主要模块。首先收集用户的DSAT信号，然后通过特定算法处理这些信号，接着动态抽样正面反馈，最后进行模型训练。

**关键创新**：DRIFT的最重要技术创新在于其利用用户不满信号进行训练的能力，这与传统方法依赖于正面反馈的方式本质上不同。通过这种方式，DRIFT能够更好地捕捉用户的真实偏好。

**关键设计**：在DRIFT中，关键设计包括损失函数的选择和动态抽样策略的实现。损失函数旨在最大化用户满意度的边际，同时避免梯度退化，确保模型在训练过程中保持探索能力。

## 📊 实验亮点

实验结果表明，DRIFT在WildBench任务得分上提升了6.23%（7B）和7.61%（14B），在AlpacaEval2胜率上提升了8.95%（7B）和12.29%（14B）。在大规模模型中，14B模型训练后的DRIFT超越了GPT-4o-mini，显示出显著的性能提升。

## 🎯 应用场景

DRIFT的研究成果具有广泛的应用潜力，尤其在对话系统、推荐系统和代码生成等领域。通过有效利用用户不满信号，DRIFT能够提升模型的响应质量和用户满意度，进而推动智能系统的实际应用和发展。未来，DRIFT可能会影响更多基于用户反馈的智能应用，提升用户体验和系统性能。

## 📄 摘要（原文）

> Real-world large language model deployments (e.g., conversational AI systems, code generation assistants) naturally generate abundant implicit user dissatisfaction (DSAT) signals, as users iterate toward better answers through refinements, corrections, and expressed preferences, while explicit satisfaction (SAT) feedback is scarce. Existing preference learning approaches are poorly aligned with this data profile, as they rely on costly human annotations or assume plentiful positive responses. In this paper, we introduce \textbf{DRIFT} (\textbf{D}issatisfaction-\textbf{R}efined \textbf{I}terative pre\textbf{F}erence \textbf{T}raining), which anchors training on real-world DSAT signals and samples positives dynamically from the evolving policy. Empirically, DRIFT models trained on real-world \textit{WildFeedback} datasets and synthetic \textit{UltraFeedback} datasets achieve up to +6.23\% (7B) / +7.61\% (14B) on WildBench Task Score and up to +8.95\% (7B) / +12.29\% (14B) on AlpacaEval2 win rate over base models, outperforming strong baseline methods such as iterative DPO and SPIN. At larger scales, the improvements are particularly pronounced: 14B models trained with DRIFT surpass GPT-4o-mini on WildBench. Further analysis shows that DRIFT also preserves exploratory capacity, yielding more diverse high-reward solutions rather than collapsing to narrow subsets. Theoretically, we demonstrate that this design preserves preference margins and avoids the gradient degeneration. These results show that DRIFT is an effective and scalable recipe for real-world post-training that leverages the most abundant and informative signal. The code and data are available at https://github.com/cacayaya/DRIFT.git.

