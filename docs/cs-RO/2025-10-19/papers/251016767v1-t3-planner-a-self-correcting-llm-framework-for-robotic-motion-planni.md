---
layout: default
title: T3 Planner: A Self-Correcting LLM Framework for Robotic Motion Planning with Temporal Logic
---

# T3 Planner: A Self-Correcting LLM Framework for Robotic Motion Planning with Temporal Logic

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2510.16767" class="toolbar-btn" target="_blank">📄 arXiv: 2510.16767v1</a>
  <a href="https://arxiv.org/pdf/2510.16767.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.16767v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2510.16767v1', 'T3 Planner: A Self-Correcting LLM Framework for Robotic Motion Planning with Temporal Logic')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Jia Li, Guoxiang Zhao

**分类**: cs.RO

**发布日期**: 2025-10-19

**🔗 代码/项目**: [GITHUB](https://github.com/leeejia/T3_Planner)

---

## 💡 一句话要点

**提出T3 Planner，利用LLM和形式化方法实现机器人运动规划的自校正。**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `机器人运动规划` `大型语言模型` `形式化方法` `信号时序逻辑` `自校正` `时空约束` `任务分解`

## 📋 核心要点

1. 现有机器人运动规划方法依赖领域知识，难以处理时空约束，导致规划结果不理想。
2. T3 Planner利用LLM生成候选轨迹，并结合信号时序逻辑(STL)验证器进行自校正，确保规划可行性。
3. 实验表明，T3 Planner在不同场景下均优于基线方法，并可提炼到轻量级模型以实现高效部署。

## 📝 摘要（中文）

本文提出了一种基于LLM的机器人运动规划框架T3 Planner，该框架能够通过形式化方法自校正其输出。针对将自然语言指令转化为可执行运动规划这一机器人领域的基础挑战，传统方法通常依赖于领域专家定制规划器，且难以处理时空耦合问题，导致运动不可行或任务规划与运动执行不一致。T3 Planner通过三个级联模块分解时空任务约束，每个模块驱动LLM生成候选轨迹序列，并通过信号时序逻辑(STL)验证器检查其可行性，直到找到满足复杂空间、时间和逻辑约束的轨迹。实验结果表明，T3 Planner显著优于基线方法。所需的推理能力可以提炼到一个轻量级的Qwen3-4B模型中，从而实现高效部署。

## 🔬 方法详解

**问题定义**：论文旨在解决机器人运动规划中，将自然语言指令转化为可执行且满足复杂时空逻辑约束的运动轨迹的问题。现有方法的痛点在于：一是依赖于领域专家知识进行规划器定制，泛化性差；二是难以处理空间、时间和逻辑耦合的约束，容易产生不可行的运动规划，导致任务规划和实际执行之间存在差异。

**核心思路**：论文的核心思路是利用大型语言模型（LLM）强大的语义理解和生成能力，生成候选的运动轨迹序列，并结合形式化方法中的信号时序逻辑（STL）验证器，对LLM生成的轨迹进行可行性验证和自校正。通过迭代生成和验证，最终得到满足所有约束条件的运动规划。这种设计结合了LLM的灵活性和形式化方法的可靠性。

**技术框架**：T3 Planner的整体架构包含三个级联的模块：
1. **任务分解模块**：将自然语言指令分解为一系列时空约束。
2. **轨迹生成模块**：利用LLM根据分解后的约束生成候选的运动轨迹序列。
3. **轨迹验证模块**：使用STL验证器对生成的轨迹进行可行性验证，判断是否满足所有约束条件。如果验证失败，则将验证结果反馈给轨迹生成模块，LLM根据反馈信息调整轨迹，再次进行验证，直到找到满足约束的轨迹。

**关键创新**：T3 Planner的关键创新在于将LLM的生成能力与形式化方法的验证能力相结合，实现了一个自校正的机器人运动规划框架。与传统方法相比，T3 Planner无需人工定制规划器，能够自动处理复杂的时空逻辑约束，并保证运动规划的可行性。

**关键设计**：
*   **LLM的选择与Prompt设计**：论文使用Qwen系列LLM，并精心设计了Prompt，引导LLM生成符合要求的轨迹序列。
*   **STL验证器的使用**：使用STL公式精确描述任务的时空逻辑约束，并利用STL验证器对轨迹进行形式化验证。
*   **反馈机制**：当STL验证失败时，将验证结果（例如，违反了哪些约束）反馈给LLM，LLM根据反馈信息调整轨迹，实现自校正。

## 📊 实验亮点

实验结果表明，T3 Planner在多个机器人运动规划场景中显著优于基线方法。具体而言，T3 Planner能够成功生成满足复杂时空逻辑约束的运动轨迹，并且在规划成功率和执行效率方面均有明显提升。此外，研究表明，可以将所需的推理能力提炼到一个轻量级的Qwen3-4B模型中，从而实现高效部署。

## 🎯 应用场景

T3 Planner可应用于各种需要机器人执行复杂任务的场景，例如：智能家居服务、自动化仓库管理、医疗机器人辅助手术等。该研究的实际价值在于降低了机器人运动规划的开发成本和难度，提高了机器人的自主性和可靠性。未来，该方法有望推广到更复杂的机器人系统和任务中，实现更智能、更安全的机器人应用。

## 📄 摘要（原文）

> Translating natural language instructions into executable motion plans is a fundamental challenge in robotics. Traditional approaches are typically constrained by their reliance on domain-specific expertise to customize planners, and often struggle with spatio-temporal couplings that usually lead to infeasible motions or discrepancies between task planning and motion execution. Despite the proficiency of Large Language Models (LLMs) in high-level semantic reasoning, hallucination could result in infeasible motion plans. In this paper, we introduce the T3 Planner, an LLM-enabled robotic motion planning framework that self-corrects it output with formal methods. The framework decomposes spatio-temporal task constraints via three cascaded modules, each of which stimulates an LLM to generate candidate trajectory sequences and examines their feasibility via a Signal Temporal Logic (STL) verifier until one that satisfies complex spatial, temporal, and logical constraints is found.Experiments across different scenarios show that T3 Planner significantly outperforms the baselines. The required reasoning can be distilled into a lightweight Qwen3-4B model that enables efficient deployment. All supplementary materials are accessible at https://github.com/leeejia/T3_Planner.

