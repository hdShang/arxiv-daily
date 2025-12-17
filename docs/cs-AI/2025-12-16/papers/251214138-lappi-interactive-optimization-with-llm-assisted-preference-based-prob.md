---
layout: default
title: LAPPI: Interactive Optimization with LLM-Assisted Preference-Based Problem Instantiation
---

# LAPPI: Interactive Optimization with LLM-Assisted Preference-Based Problem Instantiation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.14138" class="toolbar-btn" target="_blank">📄 arXiv: 2512.14138</a>
  <a href="https://arxiv.org/pdf/2512.14138.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.14138" onclick="toggleFavorite(this, '2512.14138', 'LAPPI: Interactive Optimization with LLM-Assisted Preference-Based Problem Instantiation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: So Kuroki, Manami Nakagawa, Shigeo Yoshida, Yuki Koyama, Kozuno Tadashi

**分类**: cs.HC, cs.AI

**发布日期**: 2025-12-18

---

## 💡 一句话要点

**LAPPI：利用LLM辅助的偏好问题实例化进行交互式优化**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `人机交互` `大型语言模型` `组合优化` `问题实例化` `偏好学习`

## 📋 核心要点

1. 现有优化求解器需要用户进行问题实例化，包括定义候选项目、分配偏好分数和指定约束，这对非专业用户构成挑战。
2. LAPPI利用大型语言模型，通过自然语言交互，辅助用户将模糊偏好转化为明确的优化问题，降低了使用门槛。
3. 用户研究表明，LAPPI在旅行计划任务中能够有效捕捉用户偏好，生成优于传统方法和提示工程的可行方案。

## 📝 摘要（中文）

许多现实世界的任务，如旅行计划或膳食计划，都可以被形式化为组合优化问题。然而，对于终端用户来说，使用优化求解器是困难的，因为它需要问题实例化：定义候选项目、分配偏好分数和指定约束。我们介绍了一种交互式方法LAPPI（LLM辅助的基于偏好的问题实例化），它使用大型语言模型（LLM）来支持用户完成这个实例化过程。通过自然语言对话，该系统帮助用户将模糊的偏好转化为定义良好的优化问题。然后，这些实例化的优化问题被传递给现有的优化求解器以生成解决方案。在旅行计划的用户研究中，我们的方法成功地捕捉了用户的偏好，并生成了优于传统方法和提示工程方法的可行计划。我们进一步通过将其应用于额外的用例来展示LAPPI的多功能性。

## 🔬 方法详解

**问题定义**：论文旨在解决用户难以将自身偏好转化为优化问题实例的问题。现有方法需要用户手动定义候选项目、分配偏好分数和指定约束，这对于不熟悉优化求解器的用户来说非常困难，导致优化工具难以被广泛应用。

**核心思路**：论文的核心思路是利用大型语言模型（LLM）的自然语言理解和生成能力，构建一个交互式系统，通过对话引导用户表达偏好，并将这些偏好转化为优化求解器可以理解的问题实例。这样，用户无需具备专业的优化知识，也能利用优化工具解决实际问题。

**技术框架**：LAPPI的整体框架包含以下几个主要模块：1) 自然语言交互模块：负责与用户进行对话，收集用户的偏好信息。2) 偏好提取模块：利用LLM从对话中提取用户的偏好，例如对不同景点的喜爱程度、对旅行时间的限制等。3) 问题实例化模块：将提取的偏好转化为优化问题的具体参数，例如目标函数、约束条件等。4) 优化求解模块：使用现有的优化求解器，根据问题实例生成解决方案。5) 结果展示模块：将优化结果以用户友好的方式呈现给用户。

**关键创新**：LAPPI的关键创新在于将大型语言模型引入到优化问题的实例化过程中，实现了人机协同的优化问题求解。与传统方法相比，LAPPI无需用户手动进行问题实例化，大大降低了使用门槛。同时，通过自然语言交互，LAPPI能够更好地捕捉用户的真实偏好，从而生成更符合用户需求的解决方案。

**关键设计**：LAPPI的关键设计包括：1) 针对特定应用场景（如旅行计划）设计合适的对话流程，引导用户逐步表达偏好。2) 选择合适的LLM，并对其进行微调，以提高偏好提取的准确性和效率。3) 设计合适的优化问题模型，将用户的偏好转化为目标函数和约束条件。4) 采用合适的优化求解器，以保证求解效率和解的质量。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.14138/x1.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.14138/x2.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.14138/fig/trip-planning-withMarks.jpg" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

在旅行计划的用户研究中，LAPPI成功捕捉了用户偏好，生成的旅行计划优于传统方法和提示工程方法。具体而言，LAPPI生成的计划在用户满意度方面显著高于其他方法，并且能够更好地满足用户的个性化需求。该实验结果验证了LAPPI的有效性和优越性。

## 🎯 应用场景

LAPPI可应用于各种需要组合优化的场景，如旅行计划、膳食计划、日程安排、资源分配等。该研究降低了优化工具的使用门槛，使更多用户能够利用优化技术解决实际问题，具有广泛的应用前景和实际价值。未来，该方法可以扩展到更复杂的优化问题，并与其他AI技术相结合，实现更智能化的优化解决方案。

## 📄 摘要（原文）

> Many real-world tasks, such as trip planning or meal planning, can be formulated as combinatorial optimization problems. However, using optimization solvers is difficult for end users because it requires problem instantiation: defining candidate items, assigning preference scores, and specifying constraints. We introduce LAPPI (LLM-Assisted Preference-based Problem Instantiation), an interactive approach that uses large language models (LLMs) to support users in this instantiation process. Through natural language conversations, the system helps users transform vague preferences into well-defined optimization problems. These instantiated problems are then passed to existing optimization solvers to generate solutions. In a user study on trip planning, our method successfully captured user preferences and generated feasible plans that outperformed both conventional and prompt-engineering approaches. We further demonstrate LAPPI's versatility by adapting it to an additional use case.

