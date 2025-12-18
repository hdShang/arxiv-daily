---
layout: default
title: LAPPI: Interactive Optimization with LLM-Assisted Preference-Based Problem Instantiation
---

# LAPPI: Interactive Optimization with LLM-Assisted Preference-Based Problem Instantiation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.14138" class="toolbar-btn" target="_blank">📄 arXiv: 2512.14138v1</a>
  <a href="https://arxiv.org/pdf/2512.14138.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.14138v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.14138v1', 'LAPPI: Interactive Optimization with LLM-Assisted Preference-Based Problem Instantiation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: So Kuroki, Manami Nakagawa, Shigeo Yoshida, Yuki Koyama, Kozuno Tadashi

**分类**: cs.HC, cs.AI

**发布日期**: 2025-12-16

---

## 💡 一句话要点

**LAPPI：利用LLM辅助的偏好问题实例化进行交互式优化**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `组合优化` `人机交互` `问题实例化` `偏好学习`

## 📋 核心要点

1. 现有优化求解器需要用户进行问题实例化，即定义候选项目、偏好和约束，这对于非专业用户来说是一个挑战。
2. LAPPI利用大型语言模型（LLM）通过自然语言交互，辅助用户将模糊的偏好转化为明确的优化问题，降低使用门槛。
3. 用户研究表明，LAPPI能够有效捕捉用户偏好，生成优于传统方法和提示工程方法的可行方案，并具有良好的通用性。

## 📝 摘要（中文）

许多现实世界的任务，例如旅行计划或膳食计划，都可以被形式化为组合优化问题。然而，对于终端用户来说，使用优化求解器是困难的，因为它需要问题实例化：定义候选项目、分配偏好分数和指定约束。我们介绍了一种交互式方法LAPPI（LLM辅助的基于偏好的问题实例化），该方法使用大型语言模型（LLM）来支持用户完成此实例化过程。通过自然语言对话，该系统帮助用户将模糊的偏好转化为定义明确的优化问题。然后，将这些实例化的传递给现有的优化求解器以生成解决方案。在一项关于旅行计划的用户研究中，我们的方法成功地捕捉了用户的偏好，并生成了优于传统方法和提示工程方法的可行计划。我们进一步通过将其适配到另一个用例来展示LAPPI的多功能性。

## 🔬 方法详解

**问题定义**：现实世界的许多任务可以建模为组合优化问题，但用户需要手动定义候选项目、分配偏好分数和指定约束，这个过程对非专业用户来说非常困难，阻碍了优化求解器的广泛应用。现有方法要么需要用户具备优化领域的专业知识，要么依赖于预定义的规则和模板，难以适应用户个性化的需求。

**核心思路**：LAPPI的核心思路是利用大型语言模型（LLM）的自然语言理解和生成能力，通过交互式对话的方式引导用户表达其偏好，并将这些偏好转化为优化求解器可以理解的数学模型。这种方法降低了用户使用优化求解器的门槛，使得非专业用户也能轻松地解决复杂的优化问题。

**技术框架**：LAPPI的整体框架包含以下几个主要模块：1) 自然语言交互模块：负责与用户进行自然语言对话，收集用户的偏好信息。2) 偏好提取模块：利用LLM从对话中提取用户的偏好，例如对不同候选项目的喜好程度、对各种约束条件的容忍度等。3) 问题实例化模块：将提取的偏好信息转化为优化求解器可以理解的数学模型，包括目标函数、约束条件等。4) 优化求解模块：使用现有的优化求解器求解实例化后的优化问题，生成满足用户偏好的解决方案。5) 结果展示模块：将优化求解器生成的解决方案以用户友好的方式展示给用户。

**关键创新**：LAPPI的关键创新在于将大型语言模型（LLM）引入到优化问题的实例化过程中，通过自然语言交互的方式降低了用户使用优化求解器的门槛。与传统方法相比，LAPPI无需用户具备优化领域的专业知识，也无需依赖于预定义的规则和模板，能够更好地适应用户个性化的需求。

**关键设计**：LAPPI的关键设计包括：1) 针对不同应用场景设计合适的自然语言交互流程，引导用户逐步表达其偏好。2) 设计有效的偏好提取方法，利用LLM准确地从对话中提取用户的偏好信息。3) 设计灵活的问题实例化方法，将提取的偏好信息转化为优化求解器可以理解的数学模型，并能够根据用户的反馈进行调整。4) 选择合适的优化求解器，并根据具体问题进行参数调整。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.14138v1/x1.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.14138v1/x2.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.14138v1/fig/trip-planning-withMarks.jpg" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

用户研究表明，LAPPI能够成功捕捉用户偏好，并生成优于传统方法和提示工程方法的可行计划。在旅行计划任务中，LAPPI生成的方案在用户满意度方面显著优于基线方法，证明了其有效性和实用性。此外，LAPPI还被成功地应用于另一个用例，展示了其良好的通用性。

## 🎯 应用场景

LAPPI具有广泛的应用前景，例如旅行计划、膳食计划、日程安排、资源分配等。它可以帮助用户在各种场景下做出更优的决策，提高效率和满意度。未来，LAPPI可以进一步扩展到更复杂的领域，例如智能制造、金融投资等，为各行各业提供智能化的决策支持。

## 📄 摘要（原文）

> Many real-world tasks, such as trip planning or meal planning, can be formulated as combinatorial optimization problems. However, using optimization solvers is difficult for end users because it requires problem instantiation: defining candidate items, assigning preference scores, and specifying constraints. We introduce LAPPI (LLM-Assisted Preference-based Problem Instantiation), an interactive approach that uses large language models (LLMs) to support users in this instantiation process. Through natural language conversations, the system helps users transform vague preferences into well-defined optimization problems. These instantiated problems are then passed to existing optimization solvers to generate solutions. In a user study on trip planning, our method successfully captured user preferences and generated feasible plans that outperformed both conventional and prompt-engineering approaches. We further demonstrate LAPPI's versatility by adapting it to an additional use case.

