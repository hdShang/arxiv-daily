---
layout: default
title: Self-Evolving Curriculum for LLM Reasoning
---

# Self-Evolving Curriculum for LLM Reasoning

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.14970" class="toolbar-btn" target="_blank">📄 arXiv: 2505.14970v4</a>
  <a href="https://arxiv.org/pdf/2505.14970.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.14970v4" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.14970v4', 'Self-Evolving Curriculum for LLM Reasoning')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Xiaoyin Chen, Jiarui Lu, Minsu Kim, Dinghuai Zhang, Jian Tang, Alexandre Piché, Nicolas Gontier, Yoshua Bengio, Ehsan Kamalloo

**分类**: cs.AI, cs.LG

**发布日期**: 2025-05-20 (更新: 2025-10-30)

---

## 💡 一句话要点

**提出自演化课程以优化大语言模型推理能力**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `自演化课程` `强化学习` `大语言模型` `推理能力` `自动课程学习` `多臂赌博机` `技能平衡`

## 📋 核心要点

1. 现有的随机课程和手动设计课程在微调大语言模型时效果不佳，缺乏自动化和优化。
2. 提出自演化课程（SEC）方法，通过与RL微调过程并行学习课程策略，优化问题呈现顺序。
3. 实验结果表明，SEC在规划、归纳推理和数学等领域显著提升了模型的推理能力和泛化能力。

## 📝 摘要（中文）

强化学习（RL）在微调大语言模型（LLMs）方面已被证明有效，显著提升了其在数学和代码生成等领域的推理能力。影响RL微调成功的关键因素是训练课程，即训练问题的呈现顺序。随机课程作为常见基线，效果不佳；手动设计的课程往往依赖启发式方法，而在线过滤方法计算开销较大。为解决这些问题，本文提出自演化课程（SEC），一种自动课程学习方法，与RL微调过程同时学习课程策略。我们将课程选择视为非平稳的多臂赌博机问题，将每个问题类别视为单独的臂。通过策略梯度方法的绝对优势作为即时学习增益的代理度量，SEC在三个不同推理领域的实验中显著提升了模型的推理能力，并在多个推理领域的微调中实现了更好的技能平衡。

## 🔬 方法详解

**问题定义**：本文旨在解决大语言模型微调过程中课程设计的不足，现有方法如随机课程和手动设计课程效率低下，缺乏自适应性。

**核心思路**：自演化课程（SEC）通过将课程选择视为非平稳的多臂赌博机问题，自动学习最优的课程策略，以提升模型的学习效率和推理能力。

**技术框架**：SEC方法包括课程选择模块和RL微调模块，课程选择模块根据当前模型状态动态选择问题类别，而RL微调模块则根据选择的课程进行模型训练。

**关键创新**：SEC的核心创新在于将课程选择与RL微调过程结合，通过策略梯度方法的绝对优势来评估学习增益，显著提高了模型的推理能力。

**关键设计**：在实现中，SEC使用TD(0)方法更新课程策略，选择问题类别以最大化即时奖励信号，同时在多个推理领域进行微调以实现技能平衡。

## 📊 实验亮点

实验结果显示，SEC在三个推理领域的模型表现显著优于随机课程和手动设计课程，尤其在处理更难的、超出分布的测试问题时，模型的推理能力得到了显著提升，具体提升幅度未知。

## 🎯 应用场景

该研究的潜在应用领域包括教育、自动化推理系统和智能助手等。通过优化大语言模型的推理能力，SEC可以在复杂问题求解、编程辅助和决策支持等场景中发挥重要作用，未来可能推动智能系统的广泛应用与发展。

## 📄 摘要（原文）

> Reinforcement learning (RL) has proven effective for fine-tuning large language models (LLMs), significantly enhancing their reasoning abilities in domains such as mathematics and code generation. A crucial factor influencing RL fine-tuning success is the training curriculum: the order in which training problems are presented. While random curricula serve as common baselines, they remain suboptimal; manually designed curricula often rely heavily on heuristics, and online filtering methods can be computationally prohibitive. To address these limitations, we propose Self-Evolving Curriculum (SEC), an automatic curriculum learning method that learns a curriculum policy concurrently with the RL fine-tuning process. Our approach formulates curriculum selection as a non-stationary Multi-Armed Bandit problem, treating each problem category (e.g., difficulty level or problem type) as an individual arm. We leverage the absolute advantage from policy gradient methods as a proxy measure for immediate learning gain. At each training step, the curriculum policy selects categories to maximize this reward signal and is updated using the TD(0) method. Across three distinct reasoning domains: planning, inductive reasoning, and mathematics, our experiments demonstrate that SEC significantly improves models' reasoning capabilities, enabling better generalization to harder, out-of-distribution test problems. Additionally, our approach achieves better skill balance when fine-tuning simultaneously on multiple reasoning domains. These findings highlight SEC as a promising strategy for RL fine-tuning of LLMs.

