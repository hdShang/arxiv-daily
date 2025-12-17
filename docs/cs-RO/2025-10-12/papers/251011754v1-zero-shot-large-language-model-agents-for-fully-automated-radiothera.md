---
layout: default
title: Zero-Shot Large Language Model Agents for Fully Automated Radiotherapy Treatment Planning
---

# Zero-Shot Large Language Model Agents for Fully Automated Radiotherapy Treatment Planning

<div class="paper-toolbar">
  <div class="toolbar-left">
    <a href="https://arxiv.org/abs/2510.11754" target="_blank" class="toolbar-btn">arXiv: 2510.11754v1</a>
    <a href="https://arxiv.org/pdf/2510.11754.pdf" target="_blank" class="toolbar-btn">PDF</a>
  </div>
  <div class="toolbar-right">
    <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.11754v1" 
            onclick="toggleFavorite(this, '2510.11754v1', 'Zero-Shot Large Language Model Agents for Fully Automated Radiotherapy Treatment Planning')" title="收藏">
      ☆ 收藏
    </button>
    <button class="toolbar-btn share-btn" onclick="copyLink()" title="复制链接">
      🔗 分享
    </button>
  </div>
</div>


**作者**: Dongrong Yang, Xin Wu, Yibo Xie, Xinyi Li, Qiuwen Wu, Jackie Wu, Yang Sheng

**分类**: physics.med-ph, cs.AI, cs.RO

**发布日期**: 2025-10-12

**备注**: Accepted for poster presentation at the NeurIPS 2025 Workshop on GenAI for Health: Potential, Trust, and Policy Compliance

---

## 💡 一句话要点

**提出基于零样本大语言模型的全自动放射治疗计划方法，提升计划质量。**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `放射治疗计划` `大语言模型` `零样本学习` `自动化` `调强放射治疗` `逆向优化` `头颈癌`

## 📋 核心要点

1. 手动放射治疗计划耗时且依赖专家经验，难以满足日益增长的癌症治疗需求。
2. 利用大语言模型Agent与治疗计划系统交互，实现零样本的自动逆向治疗计划。
3. 实验表明，该方法在危及器官保护方面与临床计划相当，并在热点控制和适形性方面有所提升。

## 📝 摘要（中文）

放射治疗计划是一个迭代且依赖专家经验的过程，日益增长的癌症病例使得依赖手动计划变得难以为继，因此自动化至关重要。本研究提出了一种利用基于大语言模型（LLM）的Agent来指导调强放射治疗（IMRT）逆向计划的流程。该LLM Agent直接与临床治疗计划系统（TPS）交互，迭代地提取中间计划状态并提出新的约束值来指导逆向优化。Agent的决策过程基于当前的观察和之前的优化尝试及评估，从而实现动态的策略改进。该计划过程在零样本推理设置中进行，LLM在没有事先接触手动生成的治疗计划的情况下运行，并且没有经过任何微调或特定于任务的训练。在20个头颈癌病例中，LLM生成的计划与临床手动计划进行了评估，分析并报告了关键的剂量学终点。LLM生成的计划在实现与临床计划相当的危及器官（OAR）保护的同时，表现出改进的热点控制（Dmax：106.5％ vs. 108.8％）和优异的适形性（boost PTV的适形指数：1.18 vs. 1.39；primary PTV的适形指数：1.82 vs. 1.88）。这项研究证明了在商业TPS中，零样本、LLM驱动的自动化IMRT治疗计划工作流程的可行性。所提出的方法提供了一种通用且临床上适用的解决方案，可以减少计划的变异性，并支持更广泛地采用基于AI的计划策略。

## 🔬 方法详解

**问题定义**：放射治疗计划的逆向优化是一个复杂且迭代的过程，需要放射肿瘤学家和物理师的专业知识。手动计划耗时且容易出现人为误差，不同计划者之间也存在差异。现有的自动化方法通常需要大量手动计划数据进行训练，泛化能力有限。

**核心思路**：利用大语言模型（LLM）的强大推理能力，将其作为一个智能Agent，直接与临床治疗计划系统（TPS）交互。Agent通过观察当前的计划状态，结合之前的优化尝试和评估结果，动态地调整优化策略，从而实现自动化的逆向计划。这种方法无需预先训练或微调，具有良好的泛化能力。

**技术框架**：整体流程包括以下几个主要步骤：1) LLM Agent初始化，设定优化目标和约束条件；2) Agent与TPS交互，提取当前计划状态（如剂量分布、DVH等）；3) Agent基于当前状态和历史经验，提出新的约束值，指导TPS进行逆向优化；4) TPS根据Agent提出的约束值进行优化，生成新的计划；5) Agent评估新计划的质量，并更新优化策略；6) 重复步骤2-5，直到满足优化目标或达到最大迭代次数。

**关键创新**：该方法的核心创新在于利用零样本学习的大语言模型Agent，直接与临床TPS交互，实现全自动的放射治疗计划。与传统的监督学习方法相比，该方法无需大量手动计划数据进行训练，具有更好的泛化能力和适应性。此外，Agent的决策过程是动态的，可以根据当前的计划状态和历史经验进行调整，从而实现更优的优化结果。

**关键设计**：Agent的设计包括以下几个关键方面：1) 状态表示：Agent需要能够准确地理解当前的计划状态，包括剂量分布、DVH、危及器官的剂量等信息。2) 动作空间：Agent需要能够提出有效的约束值，指导TPS进行逆向优化。3) 奖励函数：Agent需要能够评估计划的质量，并根据评估结果调整优化策略。4) 探索策略：Agent需要在探索新的优化策略和利用已有的经验之间进行平衡。

## 📊 实验亮点

在20个头颈癌病例的实验中，LLM生成的计划在危及器官保护方面与临床手动计划相当，并且在热点控制（Dmax：106.5％ vs. 108.8％）和适形性（boost PTV的适形指数：1.18 vs. 1.39；primary PTV的适形指数：1.82 vs. 1.88）方面有所提升。这些结果表明，该方法具有良好的临床应用潜力。

## 🎯 应用场景

该研究成果可应用于临床放射治疗计划的自动化，减少计划时间和人为误差，提高计划质量和一致性。该方法具有良好的泛化能力，可以应用于不同类型的癌症和治疗技术。此外，该方法还可以作为辅助工具，帮助放射肿瘤学家和物理师更好地理解和优化治疗计划。

## 📄 摘要（原文）

> Radiation therapy treatment planning is an iterative, expertise-dependent process, and the growing burden of cancer cases has made reliance on manual planning increasingly unsustainable, underscoring the need for automation. In this study, we propose a workflow that leverages a large language model (LLM)-based agent to navigate inverse treatment planning for intensity-modulated radiation therapy (IMRT). The LLM agent was implemented to directly interact with a clinical treatment planning system (TPS) to iteratively extract intermediate plan states and propose new constraint values to guide inverse optimization. The agent's decision-making process is informed by current observations and previous optimization attempts and evaluations, allowing for dynamic strategy refinement. The planning process was performed in a zero-shot inference setting, where the LLM operated without prior exposure to manually generated treatment plans and was utilized without any fine-tuning or task-specific training. The LLM-generated plans were evaluated on twenty head-and-neck cancer cases against clinical manual plans, with key dosimetric endpoints analyzed and reported. The LLM-generated plans achieved comparable organ-at-risk (OAR) sparing relative to clinical plans while demonstrating improved hot spot control (Dmax: 106.5% vs. 108.8%) and superior conformity (conformity index: 1.18 vs. 1.39 for boost PTV; 1.82 vs. 1.88 for primary PTV). This study demonstrates the feasibility of a zero-shot, LLM-driven workflow for automated IMRT treatment planning in a commercial TPS. The proposed approach provides a generalizable and clinically applicable solution that could reduce planning variability and support broader adoption of AI-based planning strategies.

