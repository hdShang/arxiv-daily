---
layout: default
title: LAPPI: Interactive Optimization with LLM-Assisted Preference-Based Problem Instantiation
---

# LAPPI: Interactive Optimization with LLM-Assisted Preference-Based Problem Instantiation

**arXiv**: [2512.14138v1](https://arxiv.org/abs/2512.14138) | [PDF](https://arxiv.org/pdf/2512.14138.pdf)

**作者**: So Kuroki, Manami Nakagawa, Shigeo Yoshida, Yuki Koyama, Kozuno Tadashi

**分类**: cs.HC, cs.AI

**发布日期**: 2025-12-16

---

## 💡 一句话要点

**提出LAPPI方法，利用大语言模型辅助用户将模糊偏好转化为优化问题实例，以解决组合优化问题实例化困难。**

**关键词**: `组合优化` `问题实例化` `大语言模型` `交互式系统` `自然语言处理` `用户偏好建模` `优化求解器` `旅行规划`

## 📋 核心要点

1. 现有方法中，组合优化问题实例化对终端用户困难，需定义候选项、偏好和约束，导致使用门槛高。
2. 论文提出LAPPI，通过LLM驱动的自然语言对话交互，辅助用户将模糊偏好转化为结构化优化问题实例。
3. 在旅行规划用户研究中，LAPPI成功捕捉偏好，生成可行计划，性能优于传统和提示工程方法，并展示通用性。

## 📝 摘要（中文）

许多现实世界任务，如旅行规划或膳食规划，可以表述为组合优化问题。然而，使用优化求解器对终端用户来说很困难，因为它需要问题实例化：定义候选项目、分配偏好分数和指定约束。我们引入了LAPPI（LLM辅助的基于偏好的问题实例化），这是一种交互式方法，利用大语言模型（LLMs）支持用户在此实例化过程中。通过自然语言对话，系统帮助用户将模糊偏好转化为明确定义的优化问题。这些实例化的问题随后传递给现有的优化求解器以生成解决方案。在旅行规划的用户研究中，我们的方法成功捕捉了用户偏好，并生成了可行的计划，优于传统方法和提示工程方法。我们通过将其适应到另一个用例进一步展示了LAPPI的通用性。

## 🔬 方法详解

LAPPI的整体框架基于交互式优化流程，用户通过自然语言对话与LLM交互，系统逐步引导用户澄清偏好、定义候选项目和约束，自动生成优化问题实例。关键技术创新点在于结合LLM的语义理解能力，将非结构化用户输入转化为结构化优化问题参数，如偏好分数和约束条件。与现有方法的主要区别在于，传统方法依赖用户手动实例化，而LAPPI通过对话自动化此过程，降低了技术门槛，提高了易用性和准确性。

## 📊 实验亮点

在旅行规划用户研究中，LAPPI成功捕捉用户偏好，生成可行计划，性能优于传统方法和提示工程方法，具体提升表现为更高的用户满意度和计划可行性，并验证了方法在额外用例中的通用性。

## 🎯 应用场景

该研究适用于需要个性化组合优化的场景，如旅行规划、膳食规划、日程安排和资源分配，潜在价值在于提升终端用户的操作便利性和决策效率，支持更广泛的实际应用部署。

## 📄 摘要（原文）

> Many real-world tasks, such as trip planning or meal planning, can be formulated as combinatorial optimization problems. However, using optimization solvers is difficult for end users because it requires problem instantiation: defining candidate items, assigning preference scores, and specifying constraints. We introduce LAPPI (LLM-Assisted Preference-based Problem Instantiation), an interactive approach that uses large language models (LLMs) to support users in this instantiation process. Through natural language conversations, the system helps users transform vague preferences into well-defined optimization problems. These instantiated problems are then passed to existing optimization solvers to generate solutions. In a user study on trip planning, our method successfully captured user preferences and generated feasible plans that outperformed both conventional and prompt-engineering approaches. We further demonstrate LAPPI's versatility by adapting it to an additional use case.

